from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DYJetsToMuMu_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MC2018TagAndProbe_TrackRefit722'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 4
config.JobType.maxMemoryMB = 8000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/NanoV9MC2018TagAndProbe_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/DYJetsToMuMu_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v3/AODSIM'

config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1000
config.Data.outLFNDirBase = '/store/user/rbhattac/TNPNano'
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoV9MC2018TagAndProbe_TrackRefit722'
config.Data.inputDBS = 'global'
config.Data.useParent = False

config.Site.storageSite = 'T2_IT_Pisa'
