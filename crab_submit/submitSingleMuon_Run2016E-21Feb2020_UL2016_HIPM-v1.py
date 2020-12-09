from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'NanoV8Data'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 4
config.JobType.maxMemoryMB = 8000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs//home/kelong/work/mWProd/CMSSW_10_6_19_patch2/src/Configuration/WMassNanoProduction/configs/NanoV8NanoV8Data_cfg.py'

config.Data.inputDataset = '/SingleMuon/Run2016E-21Feb2020_UL2016_HIPM-v1/MINIAOD
'

config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
config.Data.outLFNDirBase = '/store/group/cmst3/group/wmass/w-mass-13TeV/NanoAOD' 
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoV8'

config.Site.storageSite = 'T2_CH_CERN'
