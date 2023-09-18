#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Requires at least one command line arguments!"
    echo "ex. "
    echo "    bash makeNanoV8 <das_path> (<secondary>) <name> <nthreads>"
    exit 1
fi

das_name=$1
nevents=1000
name=${2}
nThreads=${3}

if [[ $# -gt 3 ]]; then
    echo "Secondary files not expected for Nano V9!"
    exit 1
fi

config_name=configs/${name}_cfg.py
outfile=${name}.root

cmsDriver.py RECO --conditions 106X_dataRun2_v36 \
    --customise Configuration/DataProcessing/Utils.addMonitoring \
    --datatier NANOAOD \
    --era Run2_2017,run2_nanoAOD_106Xv2 \
    --eventcontent NANOAOD \
    --filein dbs:$das_name --fileout file:$outfile \
    --nThreads $nThreads \
    --no_exec \
    --number $nevents \
    --python_filename $config_name \
    --scenario pp --step NANO --data
