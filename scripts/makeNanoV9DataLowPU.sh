#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Requires at least one command line arguments!"
    echo "ex. "
    echo "    bash script/makeNanoLowPUData <das_path> (<secondary>) <name> <nthreads>"
    exit 1
fi

sample_name=$1
if [[ "$sample_name" != file:* ]]; then
    sample_name=dbs:$sample_name
fi

nevents=1000
name=${2}
nThreads=4
if [[ $# -gt 2 ]]; then
    nThreads=${3}
fi
if [[ $# -gt 3 ]]; then
    echo "Secondary files not expected for Nano V9!"
    exit 1
fi

config_name=configs/${name}_cfg.py
outfile=${name}.root

cmsDriver.py RECO --conditions 94X_dataRun2_ReReco_EOY17_v6 \
    --customise Configuration/DataProcessing/Utils.addMonitoring \
    --datatier NANOAOD \
    --era Run2_2017,run2_nanoAOD_LowPU \
    --eventcontent NANOAOD \
    --filein $sample_name --fileout file:$outfile \
    --nThreads $nThreads \
    --no_exec \
    --number $nevents \
    --python_filename $config_name \
    --scenario pp --step NANO --data
