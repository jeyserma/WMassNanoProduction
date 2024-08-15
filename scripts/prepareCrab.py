#!/usr/bin/env python3

import argparse
import os
import subprocess
import string
import logging
import hashlib
import getpass
import sys
import datetime
import json
import re

def fillTemplatedFile(template_file_name, out_file_name, template_dict):
    with open(template_file_name, "r") as templateFile:
        source = string.Template(templateFile.read())
        result = source.substitute(template_dict)
    with open(out_file_name, "w") as outFile:
        outFile.write(result)

def nameFromInput(das_path, tagAndProbe=False):    
    label = "MC" if "SIM" in das_path[-3:] else "Data"
    if 'UL2017' in das_path or 'UL17' in das_path: #needed since pattern in data and MC names are different
        label += '2017'
    elif 'UL2018' in das_path or 'UL18' in das_path:
        label += '2018'
    if tagAndProbe:
        label += "TagAndProbe"

    if 'Data' in label and 'UL2016' in das_path:
        if 'HIPM' in das_path: 
            label += "PreVFP"
        else: 
            label += "PostVFP"
    elif 'UL16' in das_path:#for MC 2016
        # TODO: This doesn't actually work for data!
        label += "PreVFP" if "APV" in das_path else "PostVFP"

    print(das_path)
    if '5TeV' in das_path or 'Run2017G' in das_path:
        label += "LowPU5TeV"
    elif 'LowPU' in das_path or 'Run2017H':
        label += "LowPU"

    return label

def gitHash(path):
    return subprocess.check_output(['git', 'log', '-1', '--format="%H"'], cwd=path).decode('UTF-8')

def gitDiff(path):
    return subprocess.check_output(['git', 'diff',], cwd=path).decode('UTF-8')

def scriptCall():
    return ' '.join(sys.argv)

# Crab submit doesn't like names over 100 chars long
# Replace last 5 characters with hash in case of duplicates after truncation
def hashedName(name, bits=5):
    if len(name) < 100:
        return name
    
    h = hashlib.sha256(name.encode('utf-8')).hexdigest()
    return name[:(100-bits)] + h[:bits]

def makeConfig(path, name, config_name, das, nThreads):
    print([path+"/scripts/make%s.sh" % name, *das.split(" "), config_name, str(nThreads)])
    subprocess.call(["./scripts/make%s.sh" % name, *das.split(" "), config_name, str(nThreads)], cwd=path)

def makeWhitelist(das):
    out = subprocess.check_output([f'dasgoclient --query="site dataset={das}" -json'], shell=True)
    res = json.loads(out)
    sort = sorted(res, key = lambda x: float(str(x[u'site'][0][u'block_completion']).replace("%", "")), reverse=True)
    whitelist = []
    for r in sort:
        site = r[u'site'][0]
        if (len(whitelist) == 0 or float(str(site[u'block_completion']).strip("%")) > 75) and site[u'kind'] == u'DISK':
            whitelist.append(str(site[u'name']))
    whitelist_text = f"config.Site.whitelist = {whitelist}"
    whitelist_text += "\nconfig.section_('Debug')\nconfig.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']"
    return whitelist_text

def submitCrab(outfile, history_file, dryRun):
    submit_dir = os.chdir("/".join(outfile.split("/")[:-1]))
    command = ["crab", "submit", outfile]
    if dryRun:
        command.insert(0, "echo")
    output = ["\nRunning command: %s" % " ".join(command)]
    try:
        out = subprocess.check_output(command, cwd = submit_dir).decode("UTF-8")
        sys.stdout.write(out)
    except subprocess.CalledProcessError as e:
        out = "--> Failed to submit file %s" % outfile
        logging.warning(out)
    output.append(out)
    with open(history_file, "a") as f:
        f.write("\n".join(output))

def writeHistory(path, history_file, inputFile):
    cmssw_dir = os.environ["CMSSW_BASE"]+"/src"
    with open(history_file, "w") as f:
        f.write("Submit log for inputs: %s\n" % inputFile)
        f.write("Auto-generated with command %s\n" % scriptCall())
        f.write("Script ran at %s\n" % str(datetime.datetime.now()))
        f.write("Git hash of scripts is %s" % gitHash(path))
        f.write("Git hash of CMSSW is %s\n" % gitHash(cmssw_dir))
        f.write("Git diff of scripts is \n%s\n" % gitDiff(path))
        f.write("Git diff of CMSSW is \n%s\n" % gitDiff(cmssw_dir))
        f.write("-"*80+"\n")

def makeSubmitFiles(inputFile, nThreads, submit, doConfig, dryRun, match_expr, version, storage, site):
    path = os.environ['CMSSW_BASE']+"/src/Configuration/WMassNanoProduction"
    if not os.path.isfile(inputFile):
        raise ValueError("Could not open file %s" % inputFile)
    inputs = filter(lambda x: x[0] != "#", [i.strip() for i in open(inputFile).readlines()])

    if not inputs:
        raise RuntimeError("The input dataset %s is empty" % input_path)
    
    fname = inputFile.split("/")[-1].split(".")[0]
    date =  datetime.datetime.now().strftime("%y_%m_%d")
    history_file = "/".join([path, "history","_".join([fname, date, "submit{0}{1}_{2}.txt".format(*submit, getpass.getuser())])])
    if submit[0] != 0:
        writeHistory(path, history_file, inputFile)

    era = "NanoV9"

    for i, das in enumerate(inputs):
        if match_expr and not re.match(match_expr, das):
            continue

        name = era+nameFromInput(das, args.tagAndProbe)
        isData = "Data" in name
        config_name = name 
        das_split = das.split(" ")
        if len(das_split) > 1:
            config_name += "_weightFix"

        if doConfig and config_name not in configsMade:
            makeConfig(path, name, config_name, das, nThreads)
            configsMade.append(config_name)

        config_name += "_cfg.py"
        config_path = "/".join([path, "configs", config_name])
        if not os.path.isfile(config_path):
            raise RuntimeError("Config file %s does not exist. Rerun with --makeConfig" % config_path)

        outname = "_".join(das.split("/")[1:(3 if isData else 2)])
        if isData:
            if args.tagAndProbe:
                outname += "_TagAndProbe"
        else:
            outname += "_"+nameFromInput(das)
            # check if it is extension samples, where we need to add the extension number to the label
            matched = re.search("_ext(\d+)", das.split('/')[2])
            if matched:
                outname += matched.group(0)
            if len(das_split) > 1:
                name += "WeightFix"
                outname += "WeightFix"
            if args.tagAndProbe:
                outname += "TagAndProbe"

        das = das_split[0]

        run_match = re.search("(Run20\d\d[A-Z])", das)
        if isData and run_match:
            name = name.replace("Data", f"{run_match.group(1)}Data")

        requestName = hashedName("_".join([outname, version]))
        outfile = "/".join([path, "crab_submit", "submit"+outname+".py"])
        
        units = 2 if not isData else 10

        fillTemplatedFile("/".join([path, "Templates", "submitCrab%sTemplate" % era]),
            outfile, 
            {"era" : name, "splitting" : "LumiBased" if isData else "FileBased", 
                "threads" : nThreads, "memory" : nThreads*2000, "name" : requestName, 
                "input" : das, "config" : config_name, "units" : units*args.nThreads,
                "dbs" : "global" if len(das_split) == 1 else "phys03",
                "useParent" : "False" if len(das_split) == 1 else "True",
                "version" : version, "outstorage" : storage, "site" : site
            })
        logging.info("Wrote config file %s" % "/".join(outfile.split("/")[-2:]))
        if submit[0] >= 1 and i % submit[0] == (submit[1]-1):
            submitCrab(outfile, history_file, dryRun)

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', type=str, required=True, help='Version label to append to output tag')
parser.add_argument('--dryRun', action='store_true', help='print submit commands rather than executing them')
parser.add_argument('--makeConfig', action='store_true', help='run cmsDriver to build config file')
parser.add_argument('--tagAndProbe', action='store_true', help='Submit tag and probe nano')
parser.add_argument('-i', '--inputFiles', required=True, type=str, nargs='*', help='inputFiles to process')
parser.add_argument('-m', '--filterExpr', default='', type=str, help='Expression to filter out files from the input list')
parser.add_argument('-s', '--submit', type=int, nargs=2, help='Number of splits to make, which split to submit' \
        ' ex: 1 1 for all, 2 1 for every second file', default=(0,0))
parser.add_argument('-j', '--nThreads', type=int, default=1, 
    help="number of threads (make sure its consistent if you're not regenerating configs)")
parser.add_argument('--storage', default='/store/group/cmst3/group/wmass/w-mass-13TeV/NanoAOD', type=str, help='Storage path of output Ntuples(default CERN storage)')
parser.add_argument('--site', default='T2_CH_CERN', type=str, help='Site of the output storage(default:T2_CH_CERN)')

args = parser.parse_args()
if args.submit[1] > args.submit[0] or (args.submit[1] == 0 and args.submit[1] != args.submit[0]):
    raise ValueError("Second argument of --submit must be non-zero and less than first argument. " \
                        " Instead found %i %i" % args.submit)

logging.basicConfig(level=logging.INFO)

configsMade = []
for i in args.inputFiles:
    makeSubmitFiles(i, args.nThreads, args.submit, args.makeConfig, args.dryRun, args.filterExpr, args.version, args.storage, args.site)

