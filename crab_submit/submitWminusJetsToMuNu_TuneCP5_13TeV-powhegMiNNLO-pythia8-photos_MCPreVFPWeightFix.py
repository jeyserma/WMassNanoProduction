from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPreVFPWeightFix'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 8
config.JobType.maxMemoryMB = 16000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/NanoV8MCPreVFP_weightFix_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights_APVpreVFP-9b9022aedaa4cc92ec8a12485301834e/USER'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 32
config.Data.outLFNDirBase = '/store/group/cmst3/group/wmass/w-mass-13TeV/NanoAOD' 
config.Data.publication = True
config.Data.outputDatasetTag = 'WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPreVFPWeightFix'
config.Data.inputDBS = 'phys03'
config.Data.useParent = True

config.Site.storageSite = 'T2_CH_CERN'
