#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Requires at least one command line arguments!"
    echo "ex. "
    echo "    bash makeNanoV8 <das_path> <name>"
    exit 1
fi

das_name=$1
config_name=configs/${2}_cfg.py
outfile=${2}.root
nevents=1000

cmsDriver.py RECO --conditions 106X_mcRun2_asymptotic_v15 --customise Configuration/DataProcessing/Utils.addMonitoring \
    --datatier NANOAOD --era Run2_2016,run2_nanoAOD_106Xv1 --eventcontent NANOAOD \
    --filein dbs:$das_name --fileout file:$outfile --nThreads 4 --no_exec \
    --python_filename $config_name \
    --scenario pp --step NANO --data
