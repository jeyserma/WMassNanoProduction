# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: RECO --conditions 106X_mcRun2_asymptotic_preVFP_v9 --customise Configuration/DataProcessing/Utils.addMonitoring,PhysicsTools/NanoAOD/nano_cff.nanoGenWmassCustomize --datatier NANOAOD --era Run2_2016,run2_nanoAOD_106Xv1 --eventcontent NANOAOD --filein dbs:/WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights-4a2bb86276b1969ddeeb407ab73f93f5/USER --fileout file:NanoV8MCPreVFP_weightFix.root --nThreads 8 --no_exec --python_filename configs/NanoV8MCPreVFP_weightFix_cfg.py --mc --scenario pp --step NANO -n 1000 --secondfilein dbs:/WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v1/MINIAODSIM --customise_commands process.SiteLocalConfigService = cms.Service("SiteLocalConfigService", overrideSourceCacheHintDir = cms.untracked.string("lazy-download"),)
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv1_cff import run2_nanoAOD_106Xv1

process = cms.Process('NANO',Run2_2016,run2_nanoAOD_106Xv1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #"/store/group/cmst3/group/wmass/w-mass-13TeV/edmLHE/WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/LHE_massWeights/210403_063443/0001/SMP-RunIISummer20UL16MiniAOD-massWeights_1573.root"
        "/store/group/cmst3/group/wmass/w-mass-13TeV/edmLHE/WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/LHE_massWeights/201221_071152/0002/SMP-RunIISummer20UL16MiniAOD-massWeights_2750.root"
        ),
    secondaryFileNames = cms.untracked.vstring( (
        #"file:4BC55786-EAAF-2944-930E-1B01801A0CC4.root"
        "file:989C4D3D-6012-3740-A20D-6E74FC7B7CC5.root",
        "file:AD5F0F5D-96D0-DA42-A79F-C440BD88EEF5.root",
     ) )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('RECO nevts:1000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:NanoV8MCPreVFP_weightFix.root'),
    outputCommands = process.NANOAODEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_preVFP_v9', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODoutput_step = cms.EndPath(process.NANOAODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC,nanoGenWmassCustomize 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

#call to customisation function nanoGenWmassCustomize imported from PhysicsTools.NanoAOD.nano_cff
process = nanoGenWmassCustomize(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

process.SiteLocalConfigService = cms.Service("SiteLocalConfigService", overrideSourceCacheHintDir = cms.untracked.string("lazy-download"),)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
