#/bin/bash
cmssw=10_6_19.patch2
cmsrel $cmssw
cd $cmssw/src
git cms-merge-topic WMass:WMassNanoProd_106X
git clone git@github.com:kdlong/WMassNanoProduction.git Configuration/WMassNanoProduction
cd ..
scram b -j8

cd Configuration/WMassNanoProduction
