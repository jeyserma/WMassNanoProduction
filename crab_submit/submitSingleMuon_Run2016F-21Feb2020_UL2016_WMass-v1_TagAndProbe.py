from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SingleMuon_Run2016F-21Feb2020_UL2016_WMass-v1_TagAndProbe'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 8
config.JobType.maxMemoryMB = 8000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/NanoV9DataPostVFP_TagAndProbe_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/SingleMuon/Run2016F-21Feb2020_UL2016_WMass-v1/AOD'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.publication = False
config.Data.outputDatasetTag = 'NanoV9DataPostVFP'

config.Site.storageSite = 'T3_CH_CERNBOX'
