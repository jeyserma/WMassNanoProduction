# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: RECO --conditions 106X_dataRun2_v35 --customise Configuration/DataProcessing/Utils.addMonitoring --geometry DB:Extended --datatier NANOAOD --era Run2_2016,run2_nanoAOD_106Xv2 --eventcontent NANOAOD --filein dbs:/SingleMuon/Run2016F-21Feb2020_UL2016_WMass-v1/MINIAOD --fileout file:NanoV9DataPostVFP.root --nThreads 1 --no_exec --number 1000 --python_filename configs/NanoV9DataPostVFP_cfg.py --scenario pp --step NANO --data
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2

process = cms.Process('NANO',Run2_2016,run2_nanoAOD_106Xv2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/0DADD84E-DCCB-404F-8FB7-724C0E8CAC02.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/1BEFE7FC-54BB-8B4B-A695-F2CD030769AE.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/20EB970E-12C2-8744-BD85-A8CBECC18807.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/21C606EE-D209-FD42-903C-5E30B5EB9FC0.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/21C750BD-64E3-0243-854C-E0546443D3D1.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/24E22014-41B3-DF40-A741-84906D640ECC.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/267F7BCC-A8DB-364C-993B-FA582406CA5B.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/2A5B4696-E647-F840-97CE-974970973EEA.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/2C4D2576-6D74-674F-A274-854730CD680A.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/2F6834D9-563F-1342-AC05-2137709AB29E.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/35CC6F7F-FA57-5D43-9F1F-2F7B24037F8F.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/36FEDB48-7918-1640-A67E-BBD0D9749663.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/3839A0AD-2992-AC4C-9064-01C57BE519C1.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/3D612873-657B-9C48-9FB2-6BB974EAB59D.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/40A3EC73-A885-B646-B39F-EC0BFCDAF8DF.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/45A20827-3D56-9545-801A-EF71500E59F7.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/466FA75C-3AC9-6349-8760-3BF43F939350.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/4E17775B-93FD-DD43-B0B5-7450E5BDF845.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/4E2F3BD5-354B-D24A-A329-072920BFCF6E.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/4F59C2E7-947B-FA40-8AB0-2A7F0E3399E4.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/4FE01003-11DE-6741-935A-BA820A4C781A.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/50E1A060-F55A-1045-B0ED-8F17336275F5.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/523018D1-97B9-9048-9A94-382B6763BA69.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/53700FC1-27D7-D046-AFB7-97FE5A787963.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/5630DE04-10AD-D14F-8220-334703EFC0E9.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/6403EB67-0487-C849-A631-B8C2AA4A44B1.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/6673F949-B6F4-5049-B13A-D4356B0150A8.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/6A21559A-2D3C-5E44-88C1-1F93692C0767.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/6AE75050-A3D0-2242-B23D-4917E1B701E7.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/6F7EF86F-9917-A349-9160-E23BF30F672B.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/72C8F823-10E9-5F4B-9795-2EBE0D6BE65A.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/72E23101-C2FB-0C4C-A71B-AD0F35F193AA.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/7F110BFA-B532-0640-975C-1AB3386A0906.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/806EA709-4830-B64F-B604-098E45BE5784.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/914FAA16-A413-E040-8D63-856D235A8608.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/963CC376-FCB5-F242-A796-320CCB875F06.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/A2427270-C0B4-CE49-A1BC-CC0147CCECBB.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/A3AC66F3-FF6E-344A-A86C-309A2936A558.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/AD0ABCAD-B9A3-444D-808D-2D79670E26EA.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/AD95AE32-4D7B-C947-A325-CB85336EAEFC.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/ADD0DFA1-0DF9-9645-B314-7CA5A95B3D98.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/B4889926-C959-7F45-9BB6-C7C0D66F724F.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/BD6BBE0B-DFFF-B64D-AEA1-89D3D0F678F4.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/C2971E21-8272-7E48-AD8C-2F6CBA8E56C8.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/C51B0506-3C08-FF42-B539-A2CF470E9657.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/C9A1F32B-DA82-334E-93E8-29021C83A887.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/D2B494BE-0340-E840-9915-BA01F6839777.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/D460C8C7-27A4-6C4F-B36A-36C0BA16E699.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/D6642F66-8E90-7146-8527-C1FF6F695D4E.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/DDEFF951-8D23-F343-ADBC-3C889079A774.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/E06482F0-94F8-194A-BEAF-0433F9E03F5B.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/EB7D7B4C-461B-9B4B-91F2-08026928EE1C.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/EE47A18E-E565-B746-AFA5-5C9F615F00FB.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/EF65D6AE-B68C-7947-810C-3269D05A865F.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/F17B0DFE-23D0-B541-8928-67FC4E37D5CC.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/F54B2ACA-2250-FB4C-906C-470E4D1C6D91.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/F597B53D-49C0-4242-83F9-B065C695B479.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/FB1E1F3A-C8F2-9444-A627-7B99D793AB69.root', 
        '/store/data/Run2016F/SingleMuon/MINIAOD/21Feb2020_UL2016_WMass-v1/2530000/FEE83979-6AF8-6B47-AA12-038008694ED0.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
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
    fileName = cms.untracked.string('file:NanoV9DataPostVFP.root'),
    outputCommands = process.NANOAODEventContent.outputCommands
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_dataRun2_v35', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODoutput_step = cms.EndPath(process.NANOAODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeData 

#call to customisation function nanoAOD_customizeData imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeData(process)

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
