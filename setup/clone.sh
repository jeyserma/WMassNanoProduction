#/bin/bash
set -e
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cmssw=10_6_26
scramv1 project CMSSW_$cmssw
cd CMSSW_$cmssw/src
eval `scramv1 runtime -sh`
git cms-checkout-topic -u WMass:WmassNanoProd_$cmssw
git cms-checkdeps -a
path=Configuration/WMassNanoProduction
git clone git@github.com:WMass/WMassNanoProduction.git $path
# A "trick" to link to the newest LHAPDF
scram tool remove lhapdf
cp $path/setup/lhapdf.xml ../config/toolbox/slc7_amd64_gcc700/tools/selected/
scram setup lhapdf
eval `scramv1 runtime -sh`
pwd
scram b -j24

cd $path
