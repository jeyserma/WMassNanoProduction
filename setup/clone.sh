#/bin/bash
set -e
export SCRAM_ARCH=slc7_amd64_gcc700
cmssw=CMSSW_10_6_19_patch2
scramv1 project $cmssw
cd $cmssw/src
scramv1 runtime -sh
git cms-merge-topic WMass:WmassNanoProd_106X
path=Configuration/WMassNanoProduction
git clone git@github.com:kdlong/WMassNanoProduction.git $path
scram b -j8

cd $path
