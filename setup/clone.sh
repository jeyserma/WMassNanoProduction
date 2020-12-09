#/bin/bash
set -e
cmssw=CMSSW_10_6_19_patch2
scramv1 project $cmssw
cd $cmssw/src
scramv1 runtime -sh
git cms-merge-topic WMass:WmassNanoProd_106X
path=Configuration/WMassNanoProduction
git clone git@github.com:kdlong/WMassNanoProduction.git $path
scram b -j8

cd $path
