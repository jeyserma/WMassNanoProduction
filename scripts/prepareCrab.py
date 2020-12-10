#!/usr/bin/env python3

import argparse
import os
import subprocess
import string
import logging
import hashlib


def fillTemplatedFile(template_file_name, out_file_name, template_dict):
    with open(template_file_name, "r") as templateFile:
        source = string.Template(templateFile.read())
        result = source.substitute(template_dict)
    with open(out_file_name, "w") as outFile:
        outFile.write(result)

def nameFromInput(das_path):
    if not "MINIAODSIM" in das_path:
        return "Data"
    if "APV" in das_path:
        return "MCPreVFP"
    return "MCPostVFP"

# Crab submit doesn't like names over 100 chars long
# Replace last 5 characters with hash in case of duplicates after truncation
def hashedName(name, bits=5):
    if len(name) < 100:
        return name
    
    h = hashlib.sha256(name).hexdigest()
    return name[:(100-bits)] + h[:bits]

def makeConfig(path, name, das, nThreads):
    subprocess.call([path+"/scripts/make%s.sh" % name, das, name, str(nThreads)])

def makeSubmitFiles(inputFile, nThreads, submit, doConfig):
    path = os.environ['CMSSW_BASE']+"/src/Configuration/WMassNanoProduction"

    if not os.path.isfile(inputFile):
        raise ValueError("Could not open file %s" % inputFile)
    inputs = [i.strip() for i in open(inputFile).readlines()]

    if not inputs:
        raise RuntimeError("The input dataset %s is empty" % input_path)

    era = "NanoV8"

    for i, das in enumerate(inputs):
        name = era+nameFromInput(das)
        isData = "Data" in name
        config_name = name+"_cfg.py"
        config = "/".join([path, "configs", config_name])

        if doConfig and name not in configsMade:
            makeConfig(path, name, das, nThreads)
            configsMade.append(name)

        if not os.path.isfile(config):
            raise RuntimeError("Config file %s does not exist. Rerun with --makeConfig" % config)

        outname = "_".join(das.split("/")[1:(3 if isData else 2)])
        if not isData:
            outname += "_"+nameFromInput(das)

        requestName = hashedName(outname)
        outfile = "/".join([path, "crab_submit", "submit"+outname+".py"])
        fillTemplatedFile("/".join([path, "Templates", "submitCrab%sTemplate" % era]),
            outfile, 
            {"era" : name, "splitting" : "LumiBased" if isData else "FileBased", 
                "threads" : nThreads, "memory" : nThreads*2000, "name" : requestName, 
                "input" : das, "config" : config_name, "units" : 100 if isData else 4})
        logging.info("Wrote config file %s" % "/".join(outfile.split("/")[-2:]))
        if submit[0] > 1 and i % submit[0] == submit[1]:
            submit_dir = os.chdir("/".join(outfile.split("/")[:-1]))
            print(submit_dir)
            subprocess.call(["crab", "submit", outfile], cwd = submit_dir)

parser = argparse.ArgumentParser()
parser.add_argument('--makeConfig', action='store_true', help='run cmsDriver to build config file')
parser.add_argument('-i', '--inputFiles', type=str, nargs='*', help='inputFiles to process')
parser.add_argument('-s', '--submit', type=int, nargs=2, help='Number of splits to make, which split to submit' \
        ' ex: 1 1 for all, 2 1 for every second file', default=(0,0))
parser.add_argument('-j', '--nThreads', type=int, default=4, 
    help="number of threads (make sure its consistent if you're not regenerating configs)")
args = parser.parse_args()
if args.submit[1] > args.submit[0] or (args.submit[1] == 0 and args.submit[1] != args.submit[0]):
    raise ValueError("Second argument of --submit must be non-zero and less than first argument. " \
                        " Instead found %i %i" % args.submit)

logging.basicConfig(level=logging.INFO)

configsMade = []
for i in args.inputFiles:
    makeSubmitFiles(i, 4, args.submit, args.makeConfig)

