from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'WplusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPostVFP_14'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 8
config.JobType.maxMemoryMB = 16000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/NanoV8MCPostVFP_weightFix_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/WplusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights-3cd7118e833b46c5beb14479898cf4e4/USER'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 16
config.Data.outLFNDirBase = '/store/group/cmst3/group/wmass/w-mass-13TeV/NanoAOD' 
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoV8MCPostVFP'
config.Data.inputDBS = 'phys03'
config.Data.useParent = True

config.Site.storageSite = 'T2_CH_CERN'
