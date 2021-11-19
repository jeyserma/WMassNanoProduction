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

cmsDriver.py RECO --conditions 106X_dataRun2_v32 --customise Configuration/DataProcessing/Utils.addMonitoring \
    --datatier NANOAOD --era Run2_2016,run2_nanoAOD_106Xv1 --eventcontent NANOAOD \
    --geometry DB:Extended \
    --filein dbs:$das_name --fileout file:$outfile --nThreads $3 --no_exec \
    --python_filename $config_name \
    --scenario pp --step NANO --data \
    --customise_commands \
'process.GlobalTag.toGet = cms.VPSet(cms.PSet(record = cms.string("GeometryFileRcd"),tag = cms.string("XMLFILE_Geometry_2016_81YV1_Extended2016_mc"),label = cms.untracked.string("Extended"),),)'
