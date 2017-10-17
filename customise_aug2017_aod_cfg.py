from run_taureco_cleaned_offline import process, cms

from filenames_raw import filenames
from filenames_aod import filenames_aod

process.source.fileNames = cms.untracked.vstring(filenames_aod)
process.source.secondaryFileNames = cms.untracked.vstring(filenames)

process.maxEvents.input = cms.untracked.int32(-1)

# process.patTriggerCustom = cms.EDProducer(
#     'PATTriggerProducer',
#     TriggerResults=cms.InputTag('TriggerResults', '', 'TEST'),
#     hltTriggerSummaryAOD=cms.InputTag('hltTriggerSummaryAOD', '', 'TEST'),
#     l1tAlgBlkInputTag=cms.InputTag('hltgtStage2Digis', '', 'TEST'),
#     l1tExtBlkInputTag=cms.InputTag('hltgtStage2Digis', '', 'TEST'),
#     onlyStandAlone=cms.bool(True),
#     packTriggerPathNames=cms.bool(True),
#     processName=cms.string('TEST')
# )

# process.selectedPatTriggerCustom = cms.EDFilter(
#     'PATTriggerObjectStandAloneSelector',
#     cut=cms.string('!filterLabels.empty()'),
#     src=cms.InputTag('patTriggerCustom')
# )

# if not hasattr(process, 'HLTAnalyzerEndpath'):
#     print 'added needed endpath'
    # process.HLTAnalyzerEndpath = cms.EndPath(process.patTriggerCustom * process.selectedPatTriggerCustom)
    # process.HLTSchedule.append(process.HLTAnalyzerEndpath)
# else:
#     process.HLTAnalyzerEndpath += process.patTriggerCustom
#     process.HLTAnalyzerEndpath += process.selectedPatTriggerCustom

reportInterval = 1
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = reportInterval


process.hltOutputFULL = cms.OutputModule('PoolOutputModule',
                                         fileName=cms.untracked.string('outputFULL.root'),
                                         fastCloning=cms.untracked.bool(False),
                                         dataset=cms.untracked.PSet(
                                             dataTier=cms.untracked.string('RECO'),
                                             filterName=cms.untracked.string('')
                                         ),
                                         outputCommands=cms.untracked.vstring('keep *'),
                                         SelectEvents=cms.untracked.PSet(
                                             SelectEvents=cms.vstring('*',)
                                         )
                                         )

# keep all the MINIAOD content, and the updated trigger collections
process.hltOutputFULL.outputCommands = cms.untracked.vstring(
    'drop *', 
    'keep *_TriggerResults_*_*', 
    'keep *_addPileupInfo_*_*', 
    'keep LHEEventProduct_externalLHEProducer__LHE', 
    'keep GenEventInfoProduct_generator__SIM', 
    'keep *TriggerObjectStandAlone_*_*_*', 
    'keep *_*atTrigger*_*_*', 
    'keep *_hltTriggerSummaryAOD_*_*', 
    'keep double_*ixedGridRho*_*_*', 
    'keep GenEventInfoProduct_generator__SIM', 
    'keep HcalNoiseSummary_hcalnoise__RECO', 
    'keep *BeamSpot_offlineBeamSpot__RECO', 
    'keep *_hltTriggerSummaryAOD_*_*', 
    'keep *_hltHps*_*_*', 
    'keep *_hltCombinatoricRecoTaus*_*_*', 
    'keep recoTracks_hltPixelTracks_*_*', 
    'keep recoTracks_hltLightPFTracks_*_*', 
    'keep *_particleFlow_*_*', 
    'keep *_hpsPFTau*_*_*', 
    'keep *_ak4PFJetsCHS_*_*', 
    'keep *_hpsPFTauProducer_*_*', 
    'keep *_offlinePrimaryVerticesWithBS_*_*', 
    'keep *_genParticles_*_*', 
    'keep recoTracks_generalTracks_*_*', 
    'keep *_hltLightPFTracksReg_*_*', 
    'keep *_hltPFMuonForTauMerging_*_*',
    'keep *_hltPFMuonMerging_*_*', 
    'keep *_hltParticleFlowReg_*_*', 
    'keep *_hltParticleFlowForTaus_*_*', 
    'keep *_hltPixelVertices_*_*',
    'keep *_hltPFTausReg_*_*',
    'keep *_hltPFTaus_*_*',
    'keep *_*_rho_*',
    'keep *_combinatoricRecoTaus*_*_*', 
)

process.hltOutputFULL.fileName = cms.untracked.string(
    'outputFULL_htt.root'
)

process.FULLOutput = cms.EndPath(process.hltOutputFULL)

process.options.numberOfThreads = cms.untracked.uint32(1)

# del process.dqmOutput

# process.remove(process.dqmOutput)
