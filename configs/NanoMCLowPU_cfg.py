# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: RECO --conditions 94X_mc2017_realistic_v14 --datatier NANOAODSIM --eventcontent NANOAODSIM --era Run2_2017,run2_nanoAOD_LowPU --customise Configuration/DataProcessing/Utils.addMonitoring,PhysicsTools/NanoAOD/nano_cff.nanoGenWmassCustomize --filein dbs:/DYJetsToMuMu_M-50_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM --fileout file:NanoMCLowPU.root --nThreads 4 --no_exec --python_filename configs/NanoMCLowPU_cfg.py --mc --scenario pp --step NANO -n 1000
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run2_2017_cff import Run2_2017
from Configuration.Eras.Modifier_run2_nanoAOD_LowPU_cff import run2_nanoAOD_LowPU

process = cms.Process('NANO',Run2_2017,run2_nanoAOD_LowPU)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'/store/mc/RunIIFall17MiniAODv2/DYJetsToMuMu_M-50_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/2520000/020949C3-C038-ED11-A55E-D85ED3091D2B.root', 
        'file:/uscms_data/d3/yfeng/WpT/WMass/data/miniaod/020949C3-C038-ED11-A55E-D85ED3091D2B.root'
    )
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

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:NanoMCLowPU.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v14', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
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

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
