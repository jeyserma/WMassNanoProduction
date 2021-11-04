#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Requires at least one command line arguments!"
    echo "ex. "
    echo "    bash makeNanoV8 <das_path> (<secondary>) <name> <nthreads>"
    exit 1
fi

das_name=$1
nevents=1000
secondary=""
name=${2}
nThreads=${3}
if [[ $# -gt 3 ]]; then
    secondary="--secondfilein dbs:$2"
    name=${3}
    nThreads=${4}
fi

config_name=configs/${name}_cfg.py
outfile=${name}.root

cmsDriver.py RECO --conditions 106X_mcRun2_asymptotic_preVFP_v9 \
    --customise Configuration/DataProcessing/Utils.addMonitoring,PhysicsTools/NanoAOD/nano_cff.nanoGenWmassCustomize \
    --datatier NANOAOD --era Run2_2016,run2_nanoAOD_106Xv1 --eventcontent NANOAOD \
    --geometry DB:Extended \
    --filein dbs:$das_name --fileout file:$outfile --nThreads $nThreads --no_exec \
    --python_filename $config_name --mc \
    --scenario pp --step NANO -n $nevents $secondary \
    --customise_commands 'process.SiteLocalConfigService=cms.Service("SiteLocalConfigService",overrideSourceCacheHintDir=cms.untracked.string("lazy-download"),)'
