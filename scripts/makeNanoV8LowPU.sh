cmsDriver.py NANO -s NANO --nThreads 2 --mc --era Run2_2017,run2_nanoAOD_LowPU --conditions 94X_mc2017_realistic_v14 --eventcontent NANOAOD --datatier NANOAOD --filein file:pippo.root -n 100 --python_filename=nano_Run2017.py --no_exec --filein file:/eos/cms/store/user/jaeyserm/LowPU/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8.root --fileout testLowPU.root --customise Configuration/DataProcessing/Utils.addMonitoring,PhysicsTools/NanoAOD/nano_cff.nanoGenWmassCustomize --customise_commands process.genWeightsTable.maxGroupsPerType=[1]*5
#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Requires at least one command line arguments!"
    echo "ex. "
    echo "    bash makeNanoV8 <das_path> <name> <nthreads>"
    exit 1
fi

das_name=$1
nevents=1000
name=${2}
nThreads=${3}

# For non-signal samples, don't store all weights
customize=""
if [ $4 -gt 0 ]; then
    customize="--customise_commands process.genWeightsTable.maxGroupsPerType=[1]*5"
fi

config_name=configs/${name}_cfg.py
outfile=${name}.root

cmsDriver.py RECO --conditions 94X_mc2017_realistic_v14 \
    --datatier NANOAOD --era Run2_2016,run2_nanoAOD_LowPU --eventcontent NANOAOD \
    --geometry DB:Extended \
    --customise Configuration/DataProcessing/Utils.addMonitoring,PhysicsTools/NanoAOD/nano_cff.nanoGenWmassCustomize \
    --filein dbs:$das_name --fileout file:$outfile --nThreads $nThreads --no_exec \
    --python_filename $config_name --mc \
    --scenario pp --step NANO -n $nevents $customize
