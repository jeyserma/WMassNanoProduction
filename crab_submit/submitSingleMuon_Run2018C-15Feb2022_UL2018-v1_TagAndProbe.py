from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SingleMuon_Run2018C-15Feb2022_UL2018-v1_TagAndProbe_TrackRefit722'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 4
config.JobType.maxMemoryMB = 2000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/NanoV9Data2018TagAndProbe_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/SingleMuon/Run2018C-15Feb2022_UL2018-v1/AOD'

config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1000
config.Data.outLFNDirBase = '/store/user/rbhattac/TNPNano'
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoV9Run2018CData2018TagAndProbe_TrackRefit722'
config.Data.inputDBS = 'global'
config.Data.useParent = False

config.Site.storageSite = 'T2_IT_Pisa'
