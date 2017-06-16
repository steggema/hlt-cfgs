from hlt83X_expanded import *

process.hltTauPFJetsRecoTauChargedHadronsWithNeutrals = process.hltTauPFJetsRecoTauChargedHadrons.clone()

process.hltTauPFJetsRecoTauChargedHadronsWithNeutrals.builders = cms.VPSet(
    process.hltTauPFJetsRecoTauChargedHadronsWithNeutrals.builders[0],
    process.hltTauPFJetsRecoTauChargedHadronsWithNeutrals.builders[0].clone(
        name = cms.string("PFNeutralHadrons"),
        plugin = cms.string("PFRecoTauChargedHadronFromPFCandidatePlugin"),
        # process PFNeutralHadrons
        # (numbering scheme defined in DataFormats/ParticleFlowCandidate/interface/PFCandidate.h)
        chargedHadronCandidatesParticleIds = cms.vint32(5),
        minMergeChargedHadronPt = cms.double(0.)
    )
)

process.hltTauPFJetsRecoTauChargedHadronsWithNeutrals.ranking = cms.VPSet(
    cms.PSet(
        name = cms.string('ChargedPFCandidate'),
        plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
        selection = cms.string("algoIs(\'kChargedPFCandidate\')"),
        selectionFailValue = cms.double(1000.0),
        selectionPassFunction = cms.string('-pt')
    ), 
    cms.PSet(
        name = cms.string('ChargedPFCandidate'),
        plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
        selection = cms.string("algoIs(\'kPFNeutralHadron\')"),
        selectionFailValue = cms.double(1000.0),
        selectionPassFunction = cms.string('-pt')
    )
)

# process.hltTauPFJetsRecoTauChargedHadronsWithNeutrals.verbosity = cms.int32(100)

process.hltFixedGridRhoFastjetAllPF = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 4.4 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForPF" )
)

process.hltCombinatoricRecoTausSingleTau = cms.EDProducer("RecoTauProducer",
    # outputSelection=cms.string('pt()>15.'),
    buildNullTaus = cms.bool(False),
    builders = cms.VPSet(cms.PSet(
        decayModes = cms.VPSet(cms.PSet(
            maxPiZeros = cms.uint32(0),
            maxTracks = cms.uint32(6),
            nCharged = cms.uint32(1),
            nPiZeros = cms.uint32(0)
        ), 
            cms.PSet(
                maxPiZeros = cms.uint32(6),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(1)
            ), 
            cms.PSet(
                maxPiZeros = cms.uint32(5),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(2)
            ), 
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(0)
            ), 
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(1)
            ), 
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet( # suggestions made by CV
                # Three prong one pizero mode
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(1),
                maxTracks = cms.uint32(6),
                maxPiZeros = cms.uint32(3),
            )
        ),
        isolationConeSize = cms.double(0.5),
        minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
        minAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
        minRelPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        name = cms.string('combinatoric'),
        pfCandSrc = cms.InputTag("hltParticleFlowForTaus"),
        plugin = cms.string('RecoTauBuilderCombinatoricPlugin'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(3), # DO WE WANT TO TIGHTEN THIS ONLINE?
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("hltPixelVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxTrackChi2 = cms.double(1000.0),
                maxTransverseImpactParameter = cms.double(0.2),
                minGammaEt = cms.double(0.5),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),   
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(1000.0),
                maxTransverseImpactParameter = cms.double(0.2),
                minGammaEt = cms.double(0.5),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        signalConeSize = cms.string('max(min(0.1, 3.0/pt()), 0.05)')
    )),
    chargedHadronSrc = cms.InputTag("hltTauPFJetsRecoTauChargedHadronsWithNeutrals"),
    jetRegionSrc = cms.InputTag("hltTauPFJets08Region"),
    jetSrc = cms.InputTag("hltAK4PFJetsForTaus"),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(14.0),
    modifiers = cms.VPSet(
    #     cms.PSet(
    #     name = cms.string('sipt'),
    #     plugin = cms.string('RecoTauImpactParameterSignificancePlugin'),
    #     qualityCuts = cms.PSet(
    #         isolationQualityCuts = cms.PSet(
    #             maxDeltaZ = cms.double(0.2),
    #             maxTrackChi2 = cms.double(100.0),
    #             maxTransverseImpactParameter = cms.double(0.03),
    #             minGammaEt = cms.double(1.5),
    #             minTrackHits = cms.uint32(8),
    #             minTrackPixelHits = cms.uint32(0),
    #             minTrackPt = cms.double(1.0),
    #             minTrackVertexWeight = cms.double(-1.0)
    #         ),
    #         leadingTrkOrPFCandOption = cms.string('leadPFCand'),
    #         primaryVertexSrc = cms.InputTag("hltPixelVertices"),
    #         pvFindingAlgo = cms.string('closestInDeltaZ'),
    #         recoverLeadingTrk = cms.bool(False),
    #         signalQualityCuts = cms.PSet(
    #             maxDeltaZ = cms.double(0.4),
    #             maxTrackChi2 = cms.double(100.0),
    #             maxTransverseImpactParameter = cms.double(0.1),
    #             minGammaEt = cms.double(0.5),
    #             minNeutralHadronEt = cms.double(30.0),
    #             minTrackHits = cms.uint32(3),
    #             minTrackPixelHits = cms.uint32(0),
    #             minTrackPt = cms.double(0.5),
    #             minTrackVertexWeight = cms.double(-1.0)
    #         ),
    #         vertexTrackFiltering = cms.bool(False),
    #         vxAssocQualityCuts = cms.PSet(
    #             maxTrackChi2 = cms.double(100.0),
    #             maxTransverseImpactParameter = cms.double(0.1),
    #             minGammaEt = cms.double(0.5),
    #             minTrackHits = cms.uint32(3),
    #             minTrackPixelHits = cms.uint32(0),
    #             minTrackPt = cms.double(0.5),
    #             minTrackVertexWeight = cms.double(-1.0)
    #         )
    #     )
    # ), 
        cms.PSet(
            DataType = cms.string('AOD'),
            EcalStripSumE_deltaEta = cms.double(0.03),
            EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
            EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
            EcalStripSumE_minClusEnergy = cms.double(0.1),
            ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
            ElectronPreIDProducer = cms.InputTag("elecpreid"),
            maximumForElectrionPreIDOutput = cms.double(-0.1),
            name = cms.string('elec_rej'),
            plugin = cms.string('RecoTauElectronRejectionPlugin')
        ), 
        # cms.PSet(
        #     dRaddNeutralHadron = cms.double(0.12),
        #     dRaddPhoton = cms.double(-1.0),
        #     minGammaEt = cms.double(10.0),
        #     minNeutralHadronEt = cms.double(50.0),
        #     name = cms.string('tau_en_reconstruction'),
        #     plugin = cms.string('PFRecoTauEnergyAlgorithmPlugin'),
        #     verbosity = cms.int32(0)
        # ), 
        cms.PSet(
            name = cms.string('tau_mass'),
            plugin = cms.string('PFRecoTauMassPlugin'),
            verbosity = cms.int32(0)
        ), 
        # cms.PSet(
        #     name = cms.string('TTIworkaround'),
        #     pfTauTagInfoSrc = cms.InputTag("pfRecoTauTagInfoProducer"),
        #     plugin = cms.string('RecoTauTagInfoWorkaroundModifer')
        # )
    ),
    piZeroSrc = cms.InputTag("hltPFTauPiZeros")
)

process.hltHpsSelectionDiscriminatorSingleTau = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hltCombinatoricRecoTausSingleTau"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            maxMass = cms.string('1.'),
            minMass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1),
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                phi = cms.bool(True),
                mass = cms.bool(True)
            )
        ), 
        cms.PSet(
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.72, min(1.72*sqrt(pt/100.), 4.2))'),
            minMass = cms.double(0.),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1),
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                phi = cms.bool(True),
                mass = cms.bool(True)
            )
        ), 
        cms.PSet(
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.72, min(1.72*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.8), # was 0.2
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.0), # was 0.05
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1),
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                phi = cms.bool(True),
                mass = cms.bool(True)
            )
        ), 
        cms.PSet(
            maxMass = cms.string('1.2'),
            minMass = cms.double(0.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2),
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                phi = cms.bool(True),
                mass = cms.bool(True)
            )
        ), 
        cms.PSet(
            maxMass = cms.string('max(1.6, min(1.6*sqrt(pt/100.), 4.0))'), # was 1.2
            minMass = cms.double(0.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2),
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                phi = cms.bool(True),
                mass = cms.bool(True)
            )
        ), 
        cms.PSet(
            maxMass = cms.string('1.6'),
            minMass = cms.double(0.7),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2),
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                phi = cms.bool(True),
                mass = cms.bool(True)
            )
        ),
        cms.PSet(
            nCharged = cms.uint32(3),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            minMass = cms.double(0.9),
            maxMass = cms.string("1.6"),
            # for XProng0Pi0 decay modes bending corrections are transparent
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                phi = cms.bool(False),
                mass = cms.bool(False)
            )
        ),
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(0),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False)
)

process.hltHpsPFTauProducerSansRefsSingleTau = cms.EDProducer("RecoTauCleaner",
    # verbosity=cms.int32(100),
    cleaners = cms.VPSet(

        # cms.PSet(
        #     name = cms.string('Charge'),
        #     nprongs = cms.vuint32(1, 3),
        #     passForCharge = cms.int32(1),
        #     plugin = cms.string('RecoTauChargeCleanerPlugin'),
        #     selectionFailValue = cms.double(0)
        # ), 
        cms.PSet(
            name = cms.string('HPS_Select'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin'),
            src = cms.InputTag("hltHpsSelectionDiscriminatorSingleTau")
        ), 
        cms.PSet(
            name = cms.string("killSoftTwoProngTaus"),
            plugin = cms.string("RecoTauSoftTwoProngTausCleanerPlugin"),
            minTrackPt = cms.double(5.)
        ),
        cms.PSet(
            name = cms.string('ChargedHadronMultiplicity'),
            plugin = cms.string('RecoTauChargedHadronMultiplicityCleanerPlugin')
        ), 
        cms.PSet(
            name = cms.string('Pt'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadPFCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt()'),
            tolerance = cms.double(0.01)
        ), 
        cms.PSet(
            name = cms.string('StripMultiplicity'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadPFCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-signalPiZeroCandidates().size()')
        ), 
        cms.PSet(
            name = cms.string('CombinedIsolation'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadPFCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()')
        )),
    src = cms.InputTag("hltCombinatoricRecoTausSingleTau")
)

process.hltHpsPFTauProducerSingleTau = cms.EDProducer("RecoTauPiZeroUnembedder",
    src = cms.InputTag("hltHpsPFTauProducerSansRefsSingleTau")
)

process.hltHpsPFTauDiscriminationByDecayModeFinding = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hltHpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(cms.PSet(
        maxMass = cms.string('1.'),
        minMass = cms.double(-1000.0),
        nCharged = cms.uint32(1),
        nChargedPFCandsMin = cms.uint32(1),
        nPiZeros = cms.uint32(0),
        nTracksMin = cms.uint32(1)
    ), 
        cms.PSet(
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            minMass = cms.double(0.3),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ), 
        cms.PSet(
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ), 
        cms.PSet(
            maxMass = cms.string('1.5'),
            minMass = cms.double(0.8),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(0),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True)
)


process.hltHpsPFTauDiscriminationByDecayModeFindingNewDMs = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hltHpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = process.hltHpsSelectionDiscriminatorSingleTau.decayModes,
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(0),
    minTauPt = cms.double(18.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False)
)

process.hltHpsPFTauDiscriminationByDecayModeFindingNewDMsSingleTau = process.hltHpsPFTauDiscriminationByDecayModeFindingNewDMs.clone(
    PFTauProducer=cms.InputTag('hltHpsPFTauProducerSingleTau')
    )

process.hltHpsPFTauDiscriminationByDecayModeFindingOldDMs = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hltHpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(cms.PSet(
        maxMass = cms.string('1.'),
        minMass = cms.double(-1000.0),
        nCharged = cms.uint32(1),
        nChargedPFCandsMin = cms.uint32(1),
        nPiZeros = cms.uint32(0),
        nTracksMin = cms.uint32(1)
    ), 
        cms.PSet(
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            minMass = cms.double(0.3),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ), 
        cms.PSet(
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ), 
        cms.PSet(
            maxMass = cms.string('1.5'),
            minMass = cms.double(0.8),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(0),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True)
)

process.hltHpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsSingleTau = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hltHpsPFTauProducerSingleTau"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hltHpsPFTauDiscriminationByDecayModeFindingNewDMsSingleTau"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    # applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(False),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(True),
    applySumPtCut = cms.bool(True),
    # deltaBetaFactor = cms.string('0.2000'),
    deltaBetaFactor = cms.string('0.5000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    # isoConeSizeForDeltaBeta = cms.double(0.8),
    isoConeSizeForDeltaBeta = cms.double(0.5),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("hltParticleFlowForTaus"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("hltPixelVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.24),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllPF"),
    rhoUEOffsetCorrection = cms.double(0.0),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("hltPixelVertices")
)


process.HLTLooseIsoPFTauSequenceSingleTau = cms.Sequence( 
    process.hltFixedGridRhoFastjetAllPF +
    process.hltTauPFJets08Region + 
    process.hltTauPFJetsRecoTauChargedHadronsWithNeutrals + 
    process.hltPFTauPiZeros + 
    # Starting from here new stuff
    process.hltCombinatoricRecoTausSingleTau + 
    process.hltHpsSelectionDiscriminatorSingleTau +
    process.hltHpsPFTauProducerSansRefsSingleTau + 
    process.hltHpsPFTauProducerSingleTau +
    process.hltHpsPFTauDiscriminationByDecayModeFindingNewDMsSingleTau +
    process.hltHpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsSingleTau
    )


process.MC_LooseIsoPFTau20_HPS_v5 = cms.Path(process.HLTBeginSequence + process.hltPreMCLooseIsoPFTau20 + process.HLTL2muonrecoSequence + process.HLTL3muonrecoSequence + process.HLTRecoJetSequenceAK4PrePF + process.hltTauJet5 + process.HLTPFTriggerSequenceMuTau + process.HLTLooseIsoPFTauSequenceSingleTau + process.HLTEndSequence )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100000 )
)

# # FIXME DEBUG
# process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/s/steggema/work/trigger/CMSSW_9_1_0_pre3/src/pickevents.root')
# process.hltHpsPFTauProducerSansRefsSingleTau.verbosity=cms.int32(100)
# # process.hltCombinatoricRecoTausSingleTau.builders[0].verbosity = cms.int32(100)
# process.hltHpsSelectionDiscriminatorSingleTau.verbosity = cms.int32(100)
