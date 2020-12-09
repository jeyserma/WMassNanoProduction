#!/bin/usr/python3

import argparse
import os
import subprocess
import string

def fillTemplatedFile(template_file_name, out_file_name, template_dict):
    with open(template_file_name, "r") as templateFile:
        source = string.Template(templateFile.read())
        result = source.substitute(template_dict)
    with open(out_file_name, "w") as outFile:
        outFile.write(result)

parser = argparse.ArgumentParser()
parser.add_argument('--makeConfig', action='store_true', help='run cmsDriver to build config file')
inputType = parser.add_mutually_exclusive_group()
inputType.add_argument('--data', action='store_true', help='run over data')
inputType.add_argument('--mcPreVFP', action='store_true', help='run over data')
inputType.add_argument('--mcPostVFP', action='store_true', help='run over data')
args = parser.parse_args()

era = "NanoV8"
path = os.environ['CMSSW_BASE']+"/src/Configuration/WMassNanoProduction"
datasets = "data.txt"
name = era+"Data"

if args.mcPreVFP:
    name = era+"PreVFP"
    datasets = "preVFPMC.txt"
elif args.mcPostVFP:
    name = era+"PostVFP"
    datasets = "postVFPMC.txt"

input_path = "/".join([path, "inputs", datasets])
inputs = open(input_path).readlines()
if not inputs:
    raise RuntimeError("The input dataset %s is empty" % input_path)

if args.makeConfig:
    subprocess.call([path+"/scripts/make%s.sh" % era, inputs[0], name])
config = "/".join([path, "configs", era+name+"_cfg.py"])

for i in inputs:
    outname = "_".join(i.split("/")[1:(3 if args.data else 2)])
    outfile = "/".join([path, "crab_submit", "submit"+outname+".py"])
    fillTemplatedFile("/".join([path, "Templates", "submitCrab%sTemplate" % era]),
        outfile, 
        {"era" : era, "splitting" : "LumiBased" if args.data else "FileBased",
           "name" : name, "input" : i, "config" : config, "units" : 100 if args.data else 4})
    print("Wrote config file", "/".join(outfile.split("/")[-2:]))
