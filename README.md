Scripts for keeping track of private nanoaod production. Auto-generates config files from cmsDriver and crab_submit files. Divides the production into X pieces and submits every Y jobs.

# To clone with CMSSW setup

bash <(curl -s https://raw.githubusercontent.com/WMass/WMassNanoProduction/main/setup/clone.sh)

cd CMSSW_10_6_19_patch2/src/Configuration/WMassNanoProduction

# Running

Ex: ```./scripts/prepareCrab.py --makeConfig -j1 inputs/data.txt```

Will make all the crab submit files for the data samples in that text file. ```--makeConfig``` generates the configs from the cmsDriver scripts in the scripts directory, in order to ensure things are up to date.  ```-j1``` forces single core running which is needed for the Geant4e propagator.

Add ```--submit X Y``` to split the submission into X pieces and submit every Y sample. For example, to divide production between 3 people, ./scripts/prepareCrab.py inputs/data.txt --submit 3 i for i = 1,2,3 for the 3 different people.

After you submit, a file named ```history/<dataset>_<date>_<submitArgs>_<username>.txt``` is created. Commit this back to this repo for bookkeeping.
