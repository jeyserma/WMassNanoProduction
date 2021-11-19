#/bin/bash
set -e
/cvmfs/cms.cern.ch/cmsswet_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cmssw=CMSSW_10_6_19_patch2
scramv1 project $cmssw
cd $cmssw/src
eval `scramv1 runtime -sh`
git cms-init
git remote add WMass git@github.com:WMass/cmssw.git
git fetch WMass WmassNanoProd_106X_genweights
git checkout WMass/WmassNanoProd_106X_genweights
git checkout -b WmassNanoProd_106X_genWeights 
path=Configuration/WMassNanoProduction
git clone git@github.com:WMass/WMassNanoProduction.git $path
cp $path/setup/sparse-checkout .git/info
# A "trick" to link to the newest LHAPDF
scram tool remove lhapdf
cp $path/setup/lhapdf.xml ../config/toolbox/slc7_amd64_gcc700/tools/selected/
scram setup lhapdf
git read-tree -mu HEAD
pwd
scram b -j24

cd $path
