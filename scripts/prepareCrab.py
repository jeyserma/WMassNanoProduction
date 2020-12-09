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

def makeSubmitFiles(inputFile, nThreads, doConfig):
    path = os.environ['CMSSW_BASE']+"/src/Configuration/WMassNanoProduction"

    if not os.path.isfile(inputFile):
        raise ValueError("Could not open file %s" % inputFile)
    inputs = [i.strip() for i in open(inputFile).readlines()]

    if not inputs:
        raise RuntimeError("The input dataset %s is empty" % input_path)

    era = "NanoV8"

    for i in inputs:
        name = era+nameFromInput(i)
        isData = "Data" in name
        config_name = name+"_cfg.py"
        config = "/".join([path, "configs", config_name])

        if doConfig and name not in configsMade:
            makeConfig(path, name, i, nThreads)
            configsMade.append(name)

        if not os.path.isfile(config):
            raise RuntimeError("Config file %s does not exist. Rerun with --makeConfig" % config)

        outname = "_".join(i.split("/")[1:(3 if isData else 2)])
        if not isData:
            outname += "_"+nameFromInput(i)

        requestName = hashedName(outname)
        outfile = "/".join([path, "crab_submit", "submit"+outname+".py"])
        fillTemplatedFile("/".join([path, "Templates", "submitCrab%sTemplate" % era]),
            outfile, 
            {"era" : name, "splitting" : "LumiBased" if isData else "FileBased", 
                "threads" : nThreads, "memory" : nThreads*2000, "name" : requestName, 
                "input" : i, "config" : config_name, "units" : 100 if isData else 4})
        logging.info("Wrote config file %s" % "/".join(outfile.split("/")[-2:]))

parser = argparse.ArgumentParser()
parser.add_argument('--makeConfig', action='store_true', help='run cmsDriver to build config file')
inputType = parser.add_mutually_exclusive_group()
inputType.add_argument('-i', '--inputFiles', type=str, nargs='*', help='inputFiles to process')
inputType.add_argument('-j', '--nThreads', type=int, default=4, 
    help="number of threads (make sure its consistent if you're not regenerating configs)")
args = parser.parse_args()

logging.basicConfig(level=logging.INFO)

configsMade = []
for i in args.inputFiles:
    makeSubmitFiles(i, 4, args.makeConfig)
