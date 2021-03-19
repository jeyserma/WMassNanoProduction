from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DYJetsToTauTau_M-50_AtLeastOneEorMuDecay_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPostVFP'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 4
config.JobType.maxMemoryMB = 8000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/NanoV8MCPostVFP_weightFix_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/DYJetsToTauTau_M-50_AtLeastOneEorMuDecay_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights-cc94a1847acdc455d120f750cf354187/USER'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.outLFNDirBase = '/store/group/cmst3/group/wmass/w-mass-13TeV/NanoAOD' 
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoV8MCPostVFP'
config.Data.inputDBS = 'phys03'
config.Data.useParent = True

config.Site.storageSite = 'T2_CH_CERN'
config.Site.whitelist = ['T1_US_FNAL_Disk']
config.section_('Debug')
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
