import FWCore.ParameterSet.Config as cms

process = cms.Process("MYHLT")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( ('/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/00066AF0-B70D-E711-80F2-0CC47A009148.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/00B28993-C40F-E711-8206-FA163E519C7A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/00F7A8FF-5F0D-E711-9034-E0071B7AE500.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/00FE6CDA-9B0D-E711-8A81-001E67792622.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0207D6D9-A210-E711-9407-549F3525A184.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/022B6D2A-AB10-E711-A676-14187741120B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/024ADB9C-B80D-E711-9EDE-001E67792740.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/026917E1-9B0D-E711-BA9C-001E677926B4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0280289A-AD10-E711-A8D4-782BCB20D86D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0288FFCA-B110-E711-9E27-782BCB20D86D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/02C114B3-AD10-E711-839B-B083FED426E5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/02C69908-300E-E711-AC74-001E67C8050C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/043FBEDD-7A0D-E711-9EAB-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0446E7E1-9B0D-E711-96D5-48D539F3886C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/044B7B10-740E-E711-913F-001E677924DA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/04559C05-820D-E711-9134-848F69FD4667.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0462D74A-540D-E711-A203-4C79BA181187.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0475C026-720D-E711-9FEB-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/047C945C-750D-E711-AA07-001E677925E6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/04B75EAA-E30F-E711-B04F-FA163EA68591.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/04E6F954-C40F-E711-8BC1-02163E013FA9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/04FB1515-7B0D-E711-95A2-842B2B765E01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0618D5F3-A110-E711-8591-24BE05C3FBB1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0625DCA0-A910-E711-B8F6-4C79BA181231.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/063EF2F5-A210-E711-80CE-1866DAEA6E00.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/065BC83F-D00F-E711-A7E3-FA163EBEC193.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0666EF54-AB10-E711-8E6C-782BCB206470.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/066893A4-B80D-E711-B4FD-001E67396A18.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0689C164-AB10-E711-BD7D-24BE05C3DB21.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/068BA427-740E-E711-B5ED-002590200AE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/06990854-540D-E711-BAEE-4C79BA1814CD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/06A62533-5A0D-E711-840D-5065F382B2D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/06BE2688-AC10-E711-B697-E0071B7A8570.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/06D1F87B-810D-E711-B428-001E67792890.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/06D836C8-B80D-E711-9218-001E677927F0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/08182720-790E-E711-BC56-002590FD5A3A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/083290A8-780D-E711-9E3F-48FD8EE73A83.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/085913B1-A910-E711-AEC6-1866DAEEB364.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/08598007-AF10-E711-9105-A4BADB1E6031.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/08733CA2-5A0D-E711-B171-00266CF32AF4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/08D8D820-7B0D-E711-911F-1866DA87A7E7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/08DEA641-630D-E711-8940-848F69FD44E4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/08EA4D03-7B0D-E711-8540-0CC47A7DFF82.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/08F6AB39-AF10-E711-AFD7-D4AE5265ABA5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0A0E6FF7-AA10-E711-99BC-549F3525AE58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0A431600-600D-E711-A236-E0071B7AC750.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0A5772C3-CA0F-E711-84EF-FA163E398D50.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0A73B54D-F20D-E711-B9CE-24BE05CECDD1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0A7793AD-AD10-E711-86EA-D4AE5265ABA5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0A81055E-740E-E711-95D4-001E677924DA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0C0ECFB6-690D-E711-9805-5065F381F291.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0C7D991E-810E-E711-8EA8-002590200934.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0C991163-AB10-E711-A746-5065F3820341.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0CB2437B-AC10-E711-A702-141877411EA2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0CD9DDBF-B010-E711-B88E-4C79BA181327.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0CDFA6BF-510F-E711-947F-70106F4D6874.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0CE028D7-2410-E711-A1B0-00266CFFC7E4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0E0A244C-AB10-E711-AFFB-14187740D279.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0E0F95F8-CA0F-E711-820A-FA163E9D16EF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0E1967B1-AD10-E711-90CF-90B11C0BD910.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0E3369A7-AF10-E711-870D-1866DAEB5230.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0E5587C4-CB0F-E711-979E-FA163E546E50.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0E66AC6C-AB10-E711-B68B-4C79BA1813E1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0E9DDD02-5B0D-E711-8D22-5065F382C231.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0EA644DE-9B0D-E711-8E0D-008CFA000280.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0EE50ED8-7A0D-E711-9BDB-E41D2D08DF20.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/0EF22FE8-9B0D-E711-8D5A-0025902009B8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/10062AB7-510F-E711-87EF-70106F4D2508.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1023F52C-B90D-E711-B903-D4AE5269F656.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1040F9C8-5B0D-E711-B977-0CC47A57CBF8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1058FA06-3F0F-E711-90A2-002590D0AFDC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/106BADA4-820D-E711-B66D-001E677924D8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/109037B2-C30F-E711-931F-FA163E366F7D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/10A047E0-B80D-E711-A50B-A4BF0108B83A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/10A61A9B-A910-E711-8C5E-5065F38122A1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/10BF9685-AC10-E711-B7E0-E0071B741D70.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/10CD13DF-7A0D-E711-BA6A-0CC47A7E00B6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/10DB1F6A-7B0D-E711-B337-E41D2D08E010.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/10DE1747-DD0F-E711-BF90-FA163EC207DB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/121246C0-7A0D-E711-A572-7845C4FC3B69.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1212A91B-AA10-E711-B861-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/121F482B-5B0D-E711-BC29-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/122C3318-AA10-E711-A4A1-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1260BC02-5B0D-E711-A9D0-E0071B7A5540.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/12662841-CB0F-E711-809D-02163E013F01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/12686E76-AC10-E711-B463-B083FED406AD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/12735BE8-B010-E711-83FC-FA163E1E6DF9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/127E5D63-AB10-E711-BB29-24BE05C6E561.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/12B9E93F-820E-E711-839F-0025902008C8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/12CA7656-B210-E711-8D10-842B2B180924.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/12F10785-650D-E711-AA8B-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/14525E48-D70F-E711-8AB9-FA163ED7A589.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/145391BC-B010-E711-B3E2-E0071B7AD7B0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/146202FB-3E0F-E711-BE1E-001E67F674C8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/146DAD77-C50F-E711-A1B0-A0369FC5B4F4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/148C0366-AC10-E711-BE81-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/14E86219-220E-E711-9E99-003048FF2AA6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/160E3CCD-5E0D-E711-A5C2-48FD8E28248F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/161FCDB8-710D-E711-A2A5-0CC47A7E6A66.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1656434C-AB10-E711-89B5-B083FECFEF7D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1670A456-820E-E711-A564-0025902008B8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/16F7C58A-9C0D-E711-8C61-48FD8E282497.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/181E44D9-820E-E711-B670-002590200A00.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/187E3083-6A0D-E711-8F2C-D4AE52E90BA7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/188AF0B1-AD10-E711-9671-001EC94BE9FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/18C866C1-5B0D-E711-AC9C-D4AE52E94750.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/18C94A40-B310-E711-8639-001EC94BE9FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/18E29B6E-AC10-E711-9543-001C23C0B781.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/18E7CFB0-A910-E711-AA9F-B083FED406AD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/18E98CA1-A910-E711-82A7-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1A72BE2E-AB10-E711-B4C8-B083FED18596.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1A733182-AC10-E711-8AFE-782BCB536C90.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1ABFA266-AB10-E711-9612-E0071B73B6C0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1AD55BF7-AA10-E711-A8BA-549F3525AE58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1AED4DC5-650F-E711-9B18-6CC2173BBE60.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1AF0AC48-D00F-E711-8E15-FA163E4BC92C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1C49AD02-5E0D-E711-8FE2-E0071B7A5650.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1C738169-3D0F-E711-858E-C4346BC076D0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1C9B924C-640D-E711-A124-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1CC57DF7-AA10-E711-B555-549F3525AE58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1CDC3D17-C40F-E711-A08D-002590200810.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1CFD9881-760D-E711-B486-D067E5F91BAE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1E07A6C4-820E-E711-A481-001E67E34165.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1E788E76-AC10-E711-872E-141877410512.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1EC14359-740D-E711-8C56-1CC1DE18D026.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1ECDCC14-5B0D-E711-B5A5-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/1EEB4CE7-B70D-E711-BCF8-0CC47A7EEE0E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2021B506-AF10-E711-BF99-90B11C0BDA10.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2025D597-A910-E711-902C-E0071B6C9DF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/204C312C-AB10-E711-B9DB-E0071B73C630.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/20802477-AC10-E711-8306-1866DAEECFD0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/20AD5FF6-A110-E711-8560-E0071B6C9DB0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/20B0C8F0-C30F-E711-B046-48FD8EE73A87.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/20B35FB2-AD10-E711-B115-90B11C0BD910.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/20E85BEA-B210-E711-A752-1866DAEB4100.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/20EDF7EA-9B0D-E711-BCA4-48D539F38546.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/20F2E40F-B410-E711-9823-14187741013C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/20FA55DF-9B0D-E711-B0FB-008CFA000280.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/221EBF4C-AB10-E711-B82A-B083FECFEF7D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2220F45A-AC10-E711-A6C6-24BE05CE2EC1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/22504187-6A0D-E711-BCAE-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/225B756A-D70F-E711-AE14-FA163E7E1AAC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2286DC67-AB10-E711-82EC-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2287F399-820D-E711-AE11-008CFAFC0080.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/22A9A899-AD10-E711-8E39-C81F66DD6743.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/22B4A705-800E-E711-A1FA-001E6779262C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/22BF6BCB-B110-E711-A0B9-842B2B42BCF8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/22C91C9F-AA10-E711-8B84-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2415C853-B90D-E711-B987-0CC47A7EEE32.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/244E22A7-780D-E711-91FB-F02FA78BAFA8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/244F464E-460F-E711-9723-00266CFFBF34.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/245DEB7C-230F-E711-99E6-00266CFEFC5C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/247A681F-B310-E711-B39E-782BCB20D86D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/24A3CAE9-B210-E711-9423-1866DAEB4100.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/24EBD6BF-CA0F-E711-8A60-FA163EEB687E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/24F2F62B-7B0D-E711-B354-1866DA890789.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/24FE3049-AB10-E711-A176-1418774124DE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2603DFC0-CA0F-E711-BBC0-001E6779283A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2619155B-AC10-E711-AE9A-24BE05BD4F81.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2642860B-1710-E711-8E8E-00266CFFC7E4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2647D87D-AC10-E711-AEC3-782BCB539AB1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2698A518-2610-E711-BF75-00266CFFC7E4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/26DBD35E-710D-E711-B6D8-70106F48BCF6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/281757C3-B110-E711-A972-0242AC130006.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/28678F52-750D-E711-93AD-1866DA87F44A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/286E03A0-A910-E711-959B-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/28A03DBE-5E0D-E711-BEBE-48D539F3863E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/28A0D873-800E-E711-976B-0025907DE2A0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/28A47AB1-A910-E711-9C12-B083FECF837B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/28CA77B2-AD10-E711-9323-001EC94BE9FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/28EFFE46-B310-E711-86F7-141877411FED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2A6B35FF-710D-E711-9F20-047D7BD6DF5E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2AD16EB6-A910-E711-BBE2-001C23C0C7AB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2AECA341-540D-E711-B915-5065F37D71E2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2AF2F44F-2F0E-E711-815C-001E67E713B3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2AF77999-A910-E711-A221-E0071B7AE500.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2C04B654-820E-E711-9CAB-001E67792518.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2C154D6D-AB10-E711-A078-4C79BA181391.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2CB1177E-AC10-E711-98A3-842B2B18178A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2CB64EDB-AE10-E711-B815-90B11C0BD910.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2CB742FF-C30F-E711-AB4F-FA163E45439B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2CD851C8-800E-E711-9DD1-001E6779271E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2CF30EC3-B010-E711-BF5D-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2E15A69D-690D-E711-B1C6-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2E616435-AB10-E711-ADD4-001C23C103EB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2E9807B3-AD10-E711-935E-782BCB5300A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2EB228BA-5F0D-E711-8DC8-24BE05C49891.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2EB53429-820D-E711-9BDE-E41D2D08E010.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2EBCE298-AA10-E711-893C-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2EFBE762-AB10-E711-8132-24BE05CECDD1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/2EFE1D68-B310-E711-AC3A-B083FED42A6E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/30080FC3-B010-E711-86F8-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/30257320-AB0F-E711-9E9E-FA163EA85C7C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3070EF7E-640D-E711-8934-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/320F1DAD-AA10-E711-867C-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/324C9177-AC10-E711-B34F-1418774117C7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/329728DC-720D-E711-A110-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/329AC0AD-AD10-E711-8036-D4AE5265ABA5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/329B6DAD-760D-E711-BF4E-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/32A92338-B90D-E711-B087-1866DA890A7A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/32DAD093-370F-E711-9CEB-6CC2173BB810.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3403D2E0-310F-E711-B49D-48FD8E282479.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/341E5FEF-810D-E711-8468-001E67792890.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/34228461-AC10-E711-97E2-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/34291BBA-CA0F-E711-A9AD-001E6779272C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/344257B3-AD10-E711-B9A4-B083FED426E5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/344D9D8B-AC10-E711-BE3C-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/344DA038-AC10-E711-8CD4-001C23C103EB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/346A780A-D70F-E711-9E77-0CC47A4D7650.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/34754CAE-AD10-E711-8642-1866DAEA79C8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/34AA7FA7-630D-E711-96C3-848F69FD28E3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/34B70768-630D-E711-838F-0CC47A7DFD26.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/34CD2560-AC10-E711-8D63-E0071B7AC750.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/34CF327C-230F-E711-9F1A-C4346BC70B58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/360C40C4-B010-E711-93D6-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/368DB409-1710-E711-BA33-00266CFFCC54.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/369579AA-AD10-E711-A2CE-B083FECFF297.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/369857D8-5B0D-E711-B782-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/369BF732-800E-E711-89F3-001E67E6F5AD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/36BCF4D5-D60F-E711-B343-008CFA56D794.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/38651C20-7B0D-E711-95D4-D4AE526A091F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/389CD4BA-690D-E711-AA51-0CC47A57CB62.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/38C74673-7D0D-E711-9BCB-D4AE526A05F2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3A160C63-5E0D-E711-A0EB-48FD8E28246B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3A4329BE-CA0F-E711-92EE-FA163ED14E48.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3AAE5035-580F-E711-B74B-001E67E6F92C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3AC075A3-780D-E711-8484-48FD8E282493.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3AE07704-810E-E711-8ABC-002590200934.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3AF5BB43-BE10-E711-A9EE-FA163EEA700C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3AF79CC2-CB0F-E711-8CF3-FA163E284F54.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3AFF32C6-630D-E711-B15A-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3C355C99-A910-E711-B3CD-24BE05C3FBB1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3C3A3E51-630D-E711-AAC6-0CC47A7FC7B4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3C3A51BB-CA0F-E711-824A-C4346BC76CD8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3C436BEB-820E-E711-9ABC-A4BF0108B872.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3C8616B2-AD10-E711-9E03-90B11C0BD910.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3CDB68AA-C30F-E711-B192-FA163EF84D2A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3CDBC77E-9910-E711-B7E9-48FD8EE739ED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3E0A4E13-9C0D-E711-B2BF-0CC47A0AD6FC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3E2B913C-690D-E711-B6A4-848F69FD3D0D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3E347598-A910-E711-AF0F-E0071B7A5650.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3E423EFC-710D-E711-8ACC-E41D2D08DC90.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3E55CF85-C40F-E711-91D7-A0369FC5E8FC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3E69E409-5B0D-E711-B6B4-0CC47A0AD48A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3E970B79-7D0D-E711-BF9A-0CC47A009E24.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3EE02796-7D0D-E711-B898-0CC47A010854.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/3EECE97C-CB0F-E711-95C5-FA163E9D16EF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/40298D55-800E-E711-9207-001E67E6F5AD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/40401156-AB10-E711-84C7-1866DAEA79D4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/40849C7D-760D-E711-88DF-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/40A6FB02-B310-E711-A42B-549F3525DFE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/40E6D955-630D-E711-9392-047D7B881D0C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4235F3A1-A910-E711-AE1F-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4237D8BE-290F-E711-9917-C4346BC076D0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/425074D8-7A0D-E711-8373-D4AE52E911B3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4289A253-7A0D-E711-9101-001E677923F0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/428A1901-CB0F-E711-A265-FA163E3CBF20.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/42C68C4D-AB10-E711-93C0-1866DAEA8808.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/42F8F376-AC10-E711-A794-782BCB204C40.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/42FC365B-750D-E711-988C-A4BF0108B152.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/442A1A05-5E0D-E711-B406-5065F382C2F1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4439C799-C40F-E711-AD50-FA163E1E7089.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/444C79DD-720D-E711-AD2B-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/446CB44B-540D-E711-B5E4-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4498B9F3-A910-E711-9948-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/44B9CB07-6B0D-E711-9441-D067E5F91BAE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/44BAE6B3-A910-E711-864C-90B11C0BCE26.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/44F9F12B-AB10-E711-A2A7-E0071B7AC7C0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/46019E72-7A0D-E711-B8B4-008CFAF7174A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4617908E-9C0D-E711-AA2E-48D539F3888A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/464BB42F-B410-E711-9347-B083FED3F4E3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4685D8CF-5E0D-E711-9314-5065F3817281.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/46B57C76-B310-E711-9495-14187741013C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/46E093D8-AF10-E711-AA3F-14187741013C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/46F84878-AC10-E711-A058-B083FED42488.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/48099A51-540D-E711-92FB-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/48190703-AF10-E711-BD7F-1866DAEA79C8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4881DD63-AB10-E711-80E7-24BE05C33C71.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/48D08053-540D-E711-A542-4C79BA1814CD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/48E1BE95-6D0D-E711-9A2C-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/48EB85B3-AD10-E711-B6FC-B083FED426E5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4A0B3084-7D0D-E711-AD95-0CC47A7EEC70.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4A0F12D8-7A0D-E711-83C6-E41D2D08DF20.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4A289845-820D-E711-842F-E41D2D08DC90.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4A4C1242-650D-E711-A2FB-003048FF2682.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4A58D74A-540D-E711-AB0E-4C79BA181187.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4A625C9A-A910-E711-AF90-E0071B740D90.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4A66FF69-AB10-E711-A44C-5065F3815241.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4A7488A4-780D-E711-8873-48FD8EE73A01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4A7E2CCE-B110-E711-AC0F-001C23C107AF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4ACAAE4C-AB10-E711-AF0C-842B2B1807B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4AD953C9-B110-E711-87EB-842B2B180924.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4ADDFCC0-790D-E711-A7A3-001E677923F0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4AEC0C7E-B310-E711-91E7-0019B9CABFBB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C1E7862-9C0D-E711-A217-48FD8EE739F1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C4CF89C-B80D-E711-9837-A4BF0108B89A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C63ED5E-630D-E711-81B0-047D7B881D0C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C667606-7B0D-E711-9598-D4AE526A0419.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C76F949-AB10-E711-B25C-1866DAEA8808.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C7A27E3-B210-E711-9115-B083FED4263D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C90394A-540D-E711-900A-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C90464C-AB10-E711-B893-14187740D279.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C9A38BD-CB0F-E711-8191-02163E012F69.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4C9C63EA-B110-E711-BDBC-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4CA4615B-750D-E711-8347-001E677925E6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4CE0AF00-CB0F-E711-9482-FA163EB0FBE4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4E96A1C4-B110-E711-994B-B083FED3F4E3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4EABF9D5-CA0F-E711-B033-FA163E69FB71.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4EC2BA77-AF10-E711-A93C-001C23C0B781.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4EDBE158-1511-E711-8C55-02163E012DD4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4EDDF981-AF10-E711-ABE2-1866DAEA8230.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/4EF91790-9C0D-E711-982D-48D539F383FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/501B90AD-AD10-E711-8B3C-D4AE5265ABA5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/502446F3-B210-E711-85E5-001C23C105CA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/504B9AA6-780D-E711-BB4C-48FD8EE739B5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/507166C4-B010-E711-BBD9-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/50A09E22-AF10-E711-8C69-782BCB5300A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/50BE9728-AB10-E711-83B7-5065F3818291.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/50E35544-D00F-E711-A30C-FA163E4BC92C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/50F0E4F2-B90D-E711-B73D-0CC47A7EEDB0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/522A0A3F-710D-E711-A111-0CC47A7E0104.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/522B21A0-A910-E711-8B53-4C79BA1811DD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/52456CC5-B010-E711-B80B-4C79BA1811A1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/524DD7B3-A910-E711-9A59-001C23C0B781.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5258F96C-7B0D-E711-904A-0CC47A7D9926.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/526FF9A7-830D-E711-ADFC-1866DA87AC15.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/52A5C054-6B0D-E711-A453-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/52B3C35B-710D-E711-8889-D4AE52E911B3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/52C877A2-A910-E711-B67D-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/52D30112-760D-E711-AC14-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/52E01063-AB10-E711-A356-24BE05CEDCF1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5403C116-AA10-E711-A14A-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/541DB6E4-7A0D-E711-9131-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/54396AF0-B70D-E711-9637-0CC47A009148.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/543BF0C5-D00F-E711-9761-A0369FC5DF98.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/543DB9FB-B80D-E711-BF7C-001E67792740.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/545FDA91-C40F-E711-BAAA-FA163EC2865E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5460E8C2-CA0F-E711-9DAE-FA163EB124DF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/546BEF4D-2F0E-E711-8C5D-001E677926FC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/548A0563-AB10-E711-8168-24BE05C38CA1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/548E388C-B410-E711-BA97-141877411FED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5494E5D6-9B0D-E711-B309-7845C4F92EC7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/54D6DAC8-B010-E711-8BEB-4C79BA181041.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/54F5989B-810D-E711-8D95-0CC47A7E6A56.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5649C94A-B210-E711-BE55-02163E01A0A0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/565B88E4-800E-E711-935B-002590200B38.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/56A9962A-7B0D-E711-808B-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/56BA24A7-780D-E711-B8E1-48FD8EE739FB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/56C09D99-A910-E711-A7D2-5065F37D9171.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/56DB9285-6A0D-E711-A840-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/56E13404-710D-E711-B0C6-008CFAF225DC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/56E79DA0-B210-E711-BABA-B083FED3F4E3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5856D7B3-A910-E711-8FAE-001C23C0B781.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/58AA52EC-B80D-E711-AC32-0CC47A01CAFC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/58BA0BB3-AD10-E711-AEA2-782BCB5300A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/58BF8294-C40F-E711-9327-FA163E18AE7C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/58F7A433-D00F-E711-8D55-FA163EA90868.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5A084FEE-820D-E711-8FC6-008CFA001FDC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5A12658D-AC10-E711-89E6-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5A324B4C-540D-E711-9C7D-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5A8A92AA-AD10-E711-AD41-1866DAEA8230.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5A8D967E-760D-E711-99F7-1866DA87F44A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5AA665D8-7A0D-E711-8D55-D4AE52E911B3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5AD6D7C6-AF10-E711-9FB0-90B11C0BD360.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5C185CF0-C30F-E711-A452-A4BF0108B162.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5C19FC61-AB10-E711-BF83-24BE05CE2E91.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5C2D554E-B90D-E711-B43B-0CC47A01035C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5C966163-A910-E711-9D51-549F3525B154.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5CC42E60-AC10-E711-9CC0-B083FED14CE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5CC6AB43-6B0D-E711-A5AA-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5CF13D8A-C40F-E711-8606-FA163E2FDB0E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5CF38157-630D-E711-B2EC-24BE05C46B11.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5E0A9C54-B210-E711-9252-14187741013C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5E1B85F7-800E-E711-B074-001E67792518.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5E49AEB1-A910-E711-9B83-90B11C0BCE26.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5E49AEB1-A910-E711-A2D5-90B11C0BCE26.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5E8BAE49-D00F-E711-974F-FA163E4BC92C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5EC5DB0C-C40F-E711-BE58-70106F48BBC2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/5ECC163F-6B0D-E711-8395-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/60019F25-830E-E711-AA33-A4BF0107E164.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/604AE6C8-AC10-E711-B23A-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6075D2D9-9B0D-E711-8617-48FD8EE739F1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/60A04E3D-C010-E711-A497-FA163E5F7A31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/60B9BC31-6B0D-E711-A520-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/60E4FD80-AC10-E711-AEA3-842B2B172901.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/620342AC-AD10-E711-8D21-1866DAEA8230.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6209F477-AC10-E711-82F7-842B2B17367A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/621E664D-DD0F-E711-BE22-FA163E386709.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/625D6AFE-810D-E711-A388-7845C4FC36E6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6290A3DE-AB0F-E711-B09E-02163E014C3D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/62B44B9B-A910-E711-B050-E0071B741D70.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/62C51581-AC10-E711-9A42-782BCB539ABA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/62C80CBF-630D-E711-A81A-E41D2D08DF60.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/62DF4CA1-A910-E711-9853-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/64300489-9C0D-E711-B910-48D539D33367.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6468F74F-CB0F-E711-A2FD-FA163E69FB71.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/64A4BC34-740D-E711-8985-1866DA87F44A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/64C02EBB-C60F-E711-B4CA-008CFA197D98.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/64CE1B4C-B210-E711-B9F7-B083FED42FC4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/64FAFDD9-9B0D-E711-B5F1-485B39897219.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/64FFF131-640D-E711-8D50-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/66006059-710D-E711-B30F-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/661FCF8C-CB0F-E711-A4A4-FA163EA0F806.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/662034B1-A910-E711-9F7E-1866DAEEB364.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6629569B-820E-E711-87E0-A4BF0107E164.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/662F0DE2-7A0D-E711-A8A8-0CC47A7DFFC8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/66313AA6-780D-E711-8046-48FD8EE73A8F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/66346A5F-AC10-E711-A9EA-D4AE527EDE00.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/66360DEC-B110-E711-98DE-FA163E357839.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/66777B83-820D-E711-BC50-0CC47AA53D6E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/667F0C22-CB0F-E711-82AD-FA163EA26E1F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/668E41A1-780D-E711-90A6-48FD8EE73ACD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/66AE3AB1-810D-E711-A0FF-70106F48BA5E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/66B060FA-A810-E711-BDD5-A0369FC5E49C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/66FB624F-D00F-E711-AC5A-FA163EC03244.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/681F4948-CB0F-E711-87BB-48FD8EE73AC9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/682449E1-B310-E711-85A4-B083FED045ED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6827AB95-370F-E711-9F8E-6CC2173BBE70.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/683F9E6A-AB10-E711-B627-5065F3815241.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/686A5470-810D-E711-9DD2-002590A3C970.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6882B276-AC10-E711-87E6-1866DAEB5D80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/689CBD57-590D-E711-9908-E0071B7A3540.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/68C3E3FD-6A0D-E711-9F58-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/68E3B531-AB10-E711-8120-549F3525A184.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/68E3BE88-760D-E711-B68D-1CC1DE18D026.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/68E5AD5A-AB10-E711-9387-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/68FD44C2-5B0D-E711-B626-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/68FEFECC-CA0F-E711-81B1-FA163E0BFAA9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6A1E454C-540D-E711-A962-4C79BA1814A7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6A3E52D3-720D-E711-B8D1-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6A6379AF-B80D-E711-A36D-0025902009B8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6A8CCDB1-A910-E711-B5AB-1866DAEA8178.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6A996309-B70D-E711-B3BE-0025901ABD1A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6A9F303B-B410-E711-9233-B083FED42A6E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6AA42CD9-800E-E711-85E5-001E6779243C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6AAC88C4-B110-E711-AE88-B083FED3F4E3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6C25CB4B-D70F-E711-8B09-FA163EBE07A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6C49B0A5-6C0D-E711-8DB4-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6C79629B-710D-E711-89D0-0CC47A7E6A12.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6CD1B5A5-A910-E711-B550-4C79BA320415.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6CDFA77F-AC10-E711-93A9-B083FED429D6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6CE8587D-470E-E711-BB89-1866DA87A864.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/6E8BA7EB-680D-E711-908D-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/70061CB2-B210-E711-9A05-141877411FED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/700DE080-B410-E711-A243-549F3525BC38.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/701C638C-790D-E711-8F40-0CC47A57CE00.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/707E7CA3-780D-E711-AA99-48FD8EE73A85.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/70A3959C-D00F-E711-AC48-0CC47A7FC7B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/70A3E981-7B0D-E711-9C00-0CC47A7FC7A8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/70C3CFFD-800D-E711-8691-48FD8E28246B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/70CFE69A-A910-E711-B623-E0071B6C9DB0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/70D55BF9-A210-E711-8BE0-B083FED42FB0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/70E62E5A-750D-E711-934F-001E67792486.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7200B163-AC10-E711-972A-E0071B7A8560.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/725C55B1-A910-E711-955B-B083FED406AD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/72635C8D-B80D-E711-B1B2-001E67792600.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/727265A6-780D-E711-87B4-48FD8EE739BB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/72A6E894-CB0F-E711-BCD7-FA163E125028.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/72ACA04F-C010-E711-853C-FA163E18B86F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/72ADDBB1-A910-E711-B576-90B11C0BCE26.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/72C07D27-AC10-E711-BA63-549F3525BF58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/72E0503E-C010-E711-BE10-FA163E64009C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/72E2BB91-C40F-E711-B47C-FA163E1E7089.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/72F98478-AC10-E711-A727-1866DAEA7D94.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7456FA8A-7D0D-E711-A32C-0CC47A7EEC70.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/74805CC9-760D-E711-A62B-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/74DA1DC9-5B0D-E711-B094-003048FF15D6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7607ACC6-B110-E711-BF1E-0242AC130006.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/760DCCB0-B80D-E711-A009-001E67398E49.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/765600E6-B210-E711-9271-D4AE526DEDB7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/768E5E8D-CB0F-E711-B776-02163E013006.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/76A39207-5B0D-E711-AA33-002590D9D8A4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/76C75452-6B0D-E711-8B23-D4AE52E942FD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/76C82463-A910-E711-80F5-549F3525B154.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/76D89EF0-B70D-E711-8EB9-0CC47A009148.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/76E8367C-750D-E711-9CF0-0CC47A7EEE0E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/781C44B8-690D-E711-9E10-002590785950.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7847C058-590D-E711-835F-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/78621EA4-510F-E711-AE81-00266CF65AC4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/787D0007-AF10-E711-AB88-90B11C0BDA10.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/788EE5B1-A910-E711-8A77-782BCB3B1A5A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7899186B-B210-E711-BB0E-90B11C0BCBD7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/78E1F2F4-A110-E711-BB6B-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/78EE494B-AB10-E711-BFB9-14187733AD89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7A06D5E1-800E-E711-A389-001E67D5D8EF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7A12CA8A-7D0D-E711-B9BD-0CC47A010854.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7A437AC9-710D-E711-B587-008CFAF225DC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7A56EA40-540D-E711-8582-5065F37D71E2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7A5F3AB3-AD10-E711-8986-B083FED426E5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7A8E94A0-510F-E711-BF32-0090FAA58974.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7A9D197E-AC10-E711-9CB8-90B11C0BD48B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7AAE650C-5B0D-E711-9F8C-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7AD153A4-7F0D-E711-BB11-48FD8E28248B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7AE9B49E-A910-E711-ABBB-E0071B7A9810.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7AF11E4F-DD0F-E711-9A51-FA163E87F0C1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7C15E2BE-CA0F-E711-B537-FA163E621732.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7C610FA9-780D-E711-BE40-48FD8E282495.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7C691263-AB10-E711-8428-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7C7D3B78-B310-E711-84AC-B083FED3F4E3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7C7E4CA4-780D-E711-9431-346AC29F11B8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7C931ADD-B310-E711-8E8B-1866DAEB5C94.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7CB64457-6D0D-E711-AD79-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7CF97686-AC10-E711-A220-E0071B7AC7C0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7E152E49-AB10-E711-94DB-1418774124DE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7E31BE6C-B310-E711-A8C0-782BCB539ABA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7E392BB2-AD10-E711-B774-001EC94BE9FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7E7AC17F-750D-E711-9953-1CC1DE18D026.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7E81493A-B80D-E711-BBF4-1866DA890789.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7E9FC274-5F0D-E711-A3F9-24BE05CECBD1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7EB9E5A5-780D-E711-A72A-48FD8EE739F9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/7EE923AC-630D-E711-A91F-002590D9D88C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8002087F-AC10-E711-B62A-90B11C0BCE74.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/80121B97-6A0D-E711-973B-D067E5F91BAE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/802FEC99-AD10-E711-ACB1-C81F66B73923.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8041F553-800E-E711-AF40-001E67E6F5AD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/808B19C5-4A0F-E711-9EB4-A0369F836334.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/808C5386-640D-E711-9D58-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8092CD47-CB0F-E711-8694-48FD8EE73AD7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/80CCFAF4-630D-E711-AD28-047D7BD6DD56.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/80DEC477-AC10-E711-BCEE-B083FED177B1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/80E3E726-740D-E711-A7FD-0CC47A0093B6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/821DE287-820D-E711-B378-002590A3C970.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8227BF99-D70F-E711-B755-FA163EF7BF98.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/822C523B-C60F-E711-95EB-A0369FC5EEF4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/82BBC0A6-780D-E711-9F61-48FD8EE739CB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/82DAEFE8-B210-E711-A50F-842B2B180924.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/82E457C3-B110-E711-A51A-141877411FED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/82F24465-5E0D-E711-A1A1-F02FA768CB76.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/84445CBD-720D-E711-BDBB-001E67792652.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/845DF2B0-A910-E711-8899-1866DAEA8178.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8460A426-B90D-E711-9D5A-1866DA87A5A4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/84A5F6DF-B80D-E711-9922-001E67792600.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/84D701DC-7A0D-E711-90D6-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/86196FF7-AA10-E711-A4D4-549F3525AE58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8626C108-830E-E711-B72F-001E6779243C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/86291702-B110-E711-A9F6-E0071B73C620.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/862D53CB-5F0D-E711-9505-A0369F3102F6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/86D0107C-7B0D-E711-A8CE-0CC47A7E0106.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/86F856A7-B90D-E711-B849-1866DA8908C7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/880B13BF-710D-E711-BBE9-70106F4D69B8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/881E1B03-810D-E711-A8BB-48FD8EE739EB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8829E3B7-DD0F-E711-87AB-0CC47A7E001A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8842581B-AA10-E711-A8C5-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/88438588-C40F-E711-AAE9-008CFA197D98.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/884DB6A3-A910-E711-84C0-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/88543366-1E0F-E711-9BCC-6CC2173BBA30.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/88543C04-5B0D-E711-849B-003048FF2826.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8899F893-AD10-E711-94E5-B083FED04CAB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/88AFB9BC-BD0F-E711-ACF4-02163E00E5CC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8A030D4D-AB10-E711-A55F-14187733AD89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8A0D98A8-810D-E711-B0B7-0CC47A7E6A8E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8A0F679A-7D0D-E711-9544-1866DA890969.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8A0FB798-A910-E711-8805-24BE05CEDC71.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8A1B4759-820D-E711-AC06-001E67792890.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8A623084-B80D-E711-9BEB-A4BF0108B83A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8AAC175C-AC10-E711-8267-24BE05BD4F81.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8ABDDEC5-B010-E711-B0C1-4C79BA1811A1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8AC52472-AC10-E711-ABBD-1866DAEA8808.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8AD2FBDD-9B0D-E711-ADEB-48FD8E2824A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8AF0EB7B-630D-E711-AEB9-0CC47A7E0008.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8C0A9B8B-9C0D-E711-9C2B-48D539F38636.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8C0BEDFD-CA0F-E711-92BD-FA163E7EC49F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8C3ECD3A-AC10-E711-8B9D-001C23C0B673.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8C48135D-820E-E711-8ABE-001E6779243C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8C678861-AB10-E711-94BB-5065F3816201.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8C6C62BF-AF10-E711-B309-782BCB678096.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8CC1D780-630D-E711-B702-002590A2CD68.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8CF05505-640D-E711-ADB3-0CC47AA53D8A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8CF44806-7B0D-E711-A848-842B2B765E01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8E028634-690D-E711-8A77-008CFAFBE6B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8E32BE26-B90D-E711-BD7E-A4BF0108B89A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8E574CFB-CA0F-E711-8237-FA163E125028.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8EA4B8DA-AE10-E711-B4ED-1866DAEA8230.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8EC45378-630D-E711-AD27-0CC47A7E6A54.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8EC46551-B110-E711-84FB-FA163E651269.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8ECC7A0E-B70D-E711-985F-002590D9D8C0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8ECD2DDA-9B0D-E711-AAC5-001E677925E6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/8EE182A1-A910-E711-8434-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/901C4958-750D-E711-B2A1-001E677924C6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/905F0E10-5B0D-E711-8D9F-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/906C8E8C-9C0D-E711-8CB8-0CC47A4128F8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/907E786F-810D-E711-899B-001E677924D8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/909AA553-AB10-E711-A4F9-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/909FD9F8-C30F-E711-AEE0-001E67E6F896.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/90A0B615-AF10-E711-9A05-842B2B180C66.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/90A21AE2-7A0D-E711-90D8-0CC47A7DFFC8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/90AA6830-CA0F-E711-8FDB-1866DA89035E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/90AA71C5-5B0D-E711-A10B-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/92BE6DF1-CA0F-E711-8073-A0369FC5EEF4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/92CD7E66-790D-E711-9011-0CC47A57CD6A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9418E290-C40F-E711-A727-FA163EF7BF98.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/94A9C5CD-5B0D-E711-A988-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/94B19209-B90D-E711-956B-0CC47A7EEDB0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/94BD19C2-CA0F-E711-88A8-FA163E35E470.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/94DD609C-630D-E711-8F45-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/94FD6AA3-820D-E711-9F3A-7845C4FC35E1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/962C3DAB-630D-E711-98E4-002590D9D8C0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9648B147-D00F-E711-885A-FA163E4BC92C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/96639F22-AF10-E711-8A71-782BCB5300A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9665D660-AB10-E711-970E-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9688D790-B90D-E711-B832-1866DA890A68.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/96A3B664-AC10-E711-8C9C-782BCB678096.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/96C2B698-A910-E711-A043-E0071B6C9DF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/96E47C44-640D-E711-B725-D4AE52E94750.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/96EAE63E-540D-E711-AEAB-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/96F71F06-5B0D-E711-AE22-002590D9D966.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9800A580-AC10-E711-ADA4-B083FED04CAB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9842FBCE-B110-E711-8542-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9854A7BC-CA0F-E711-BF1B-FA163E33E238.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9867C637-6B0D-E711-9BB8-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/98839F35-5A0D-E711-A410-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9895A6E0-BC0E-E711-822A-5065F381E271.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/98CC8E02-B90D-E711-A70A-001E6779257C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/98DF754A-AB10-E711-B405-1418774124DE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/98EBF797-CB0F-E711-93CF-02163E013F35.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9A027806-7B0D-E711-BFC5-D4AE526A0419.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9A17C54D-AB10-E711-B31C-B083FED046D9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9A1E0736-D00F-E711-B31C-FA163EDC3DEF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9A20EB27-CB0F-E711-9AD2-FA163EB0FBE4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9A574E6B-AB10-E711-A58C-4C79BA1811F3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9A5A9AC5-B110-E711-A3A4-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9AD43403-720D-E711-8740-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9AF42848-640D-E711-90C9-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9AFB5CCB-B110-E711-BEB2-842B2B42BCF8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9C0320E9-B210-E711-9887-842B2B42BCF8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9CCADAC8-B010-E711-B2F6-4C79BA181041.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9CD82385-AC10-E711-8F3E-24BE05C6E561.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9E2F1064-AB10-E711-A0D7-E0071B749CA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9E7AB2B5-740D-E711-9DAF-0CC47A0093B6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9E7CB3B1-A910-E711-9994-141877410ACD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/9EDF4D5B-B210-E711-81EB-001C23C0B673.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A019873C-5A0D-E711-A409-24BE05CE2EE1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A0465C83-230F-E711-87C2-A0369F8362E8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A04D9465-AB10-E711-B7CF-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A052D306-5B0D-E711-9298-002590D9D8A4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A05C4460-AB10-E711-8764-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A07FA071-7D0D-E711-BB3B-0CC47A009E24.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A0B4C604-AF10-E711-9DDD-1866DAEA79C8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A0F1FF61-7A0D-E711-BD25-002590A37118.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A25D289A-AD10-E711-9F85-782BCB20D86D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A2614231-450F-E711-A4E0-7845C4FC3641.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A2618D4C-AB10-E711-8DFF-842B2B1807B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A26B0151-AB10-E711-97AA-1866DAEA79D4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A27E1EA9-AA10-E711-A109-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A2821494-270E-E711-9FEF-001E677926E6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A2C277A6-630D-E711-89BF-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A2E40B06-760D-E711-8DD1-003048FF263E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A2E6A5A3-780D-E711-A8BD-48FD8E282473.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A2FF444C-540D-E711-B5C7-4C79BA1814A7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A402454C-540D-E711-8D8B-4C79BA1814A7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A4545233-630D-E711-9317-24BE05BD4F81.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A46DF028-B310-E711-B129-B083FED3F4E3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A4A01BD7-CA0F-E711-9856-FA163E69FB71.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A4B23B27-B90D-E711-B19A-1866DA87B3E6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A4BCD6A4-780D-E711-BF81-48FD8E282493.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A4D9B89D-C40F-E711-A1F4-FA163EF7C582.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A4E67163-AB10-E711-976B-001C23C0B781.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A60B7614-3F0F-E711-9A70-00259020081C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A617A733-020E-E711-B997-0CC47A7DFFE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A6215F21-AA10-E711-871A-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A623EE7B-7B0D-E711-BC97-047D7B881D3A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A62727F4-C30F-E711-BBB0-F02FA768CDD0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A62FC44C-B90D-E711-B8D1-0CC47A01035C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A634D9A5-780D-E711-86E4-346AC29F11B0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A688A563-AB10-E711-856C-E0071B7A7870.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A6C0F27D-AC10-E711-82D1-842B2B42BC3A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A6EB28DF-450F-E711-B666-0CC47A7FC706.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A812984E-540D-E711-B34E-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A845828A-AC10-E711-B462-24BE05CEADD1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A846E9C2-A210-E711-A539-141877411D77.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A84D743D-710D-E711-A2E2-0CC47A7E0104.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/A8BE20F6-CA0F-E711-B203-FA163EB0FBE4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AA2C4ECC-1E11-E711-B4E6-FA163EA68EDC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AA33F885-AA10-E711-AC45-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AA36C0C0-7A0D-E711-BD1C-7845C4FC3B0C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AA3B4D94-5B0D-E711-8F94-0CC47A7E0006.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AA5D05B0-AD10-E711-9C1C-1866DAEA6C40.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AA6491B3-AD10-E711-9B6D-B083FED426E5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AA666EE1-AF10-E711-ACE4-1418774120C3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AA6EAFB3-AD10-E711-8BE4-782BCB5300A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AA9B8926-B90D-E711-B84D-1866DA890A7A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AAA98078-DD0F-E711-8A4C-FA163E2DB2A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AAAF46C9-CA0F-E711-AA19-FA163E180EED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AAB812AE-B80D-E711-BF33-001E67398E49.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AAD2F0DD-590D-E711-B8EF-848F69FD457D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AC07F29E-830D-E711-94BA-D4AE526A0455.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AC106EA6-820E-E711-BDAD-A4BF0108B3C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AE12C9A0-A910-E711-8A11-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AE3585A0-C010-E711-8792-FA163E6C1D2A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AE37244A-740D-E711-A5D4-0CC47A7EEE0E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AE451CE9-B210-E711-A1EB-842B2B42BCF8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AE58664D-AB10-E711-9A90-842B2B1807B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AE59A805-800E-E711-945B-001E6779262C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AE7BB147-CB0F-E711-AA71-48FD8EE739BB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AECD4B17-7B0D-E711-97A3-842B2B765E01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/AEE1A894-B90D-E711-B226-1866DA8908C7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B02B270B-1710-E711-9165-00266CFFC7E4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B056039E-A910-E711-A5D7-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B05B4460-AB10-E711-823E-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B064B360-AB10-E711-A30C-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B066E8AA-C010-E711-B058-FA163E18B86F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B09BE983-AC10-E711-B15D-5065F3816291.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B0A3FA0A-5B0D-E711-8615-0025907DE22C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B0BBB460-820E-E711-BE07-001E67792518.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B0E146A2-A910-E711-8B2E-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B0E43EDF-B210-E711-94CA-14187741013C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B215EA2A-CB0F-E711-8BC3-FA163EA0F806.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B223BCAD-AD10-E711-8A6A-D4AE5265ABA5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B24C3971-B210-E711-8C68-B083FED3F4E3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B273D3E9-B70D-E711-AAF0-842B2B765E01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B275DF58-6D0D-E711-AF0C-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B280465A-AB10-E711-ACFE-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B288BF6D-B210-E711-BE74-782BCB20D86D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B2899E22-AF10-E711-8F8C-782BCB5300A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B2A8C3CD-CA0F-E711-A3EB-FA163E9B35CB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B2B79C16-5B0D-E711-9E05-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B2C5EE8D-BD0F-E711-810F-001E6779285C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B2E6E6BC-B010-E711-A92E-E0071B7A4620.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B2FB1CDA-9B0D-E711-850B-1866DA890A7A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B4014EB8-C30F-E711-814D-FA163EB532C3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B4234AA6-780D-E711-927E-346AC29F11B0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B4262DA0-A910-E711-9585-4C79BA4E0055.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B4605A06-7B0D-E711-B95A-842B2B765E01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B48A6961-AC10-E711-BA12-E0071B7AC750.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B4AF0E21-7B0D-E711-96F6-1866DA879B33.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B4FF8CBC-7A0D-E711-A840-008CFAFBF2CA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B671B1A8-780D-E711-8538-48FD8E282471.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B68D8B8E-9C0D-E711-9E46-48D539F383FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B6A35590-9C0D-E711-9EB0-48D539F3888A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B6AD16DA-9B0D-E711-A02F-F04DA274E02A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B6C30477-AC10-E711-81F0-B083FED14CE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B6EEABEC-B70D-E711-AAD9-0CC47A01CAFC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B84DCD5B-710D-E711-8AE9-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B85DCCAA-B80D-E711-BDCA-001E67C8050C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B873BADD-630D-E711-BF26-002590D9D8B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B87B1AA0-A910-E711-9B6B-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B89C544F-7A0D-E711-B0A0-001E67792424.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/B8FE498D-C40F-E711-A51D-FA163EF7C582.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BA38BD03-5B0D-E711-A019-003048FF2826.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BA3C0682-B410-E711-923C-549F3525BC38.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BA51F6BB-CB0F-E711-81EE-FA163E546E50.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BA5ECDBF-B010-E711-8AD4-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BA5F1EB1-A910-E711-BA8F-1866DAEEB364.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BA9C55C8-5D0D-E711-8090-48D539D33361.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BAABCD4F-AB10-E711-86F5-1866DAEB5C74.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BAC2A6B1-A910-E711-852D-C81F66B78625.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BAD98A06-B70D-E711-A5F7-0CC47A0AD3BC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BAF3C8D5-AF10-E711-9CB4-B083FED045ED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BC1D2C4B-AB10-E711-8450-14187733AD89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BC2DAEF1-C30F-E711-AFF6-7845C4FC363E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BC2F2589-9C0D-E711-AE70-48FD8EE73AF7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BC2FFC63-800E-E711-AFC9-001E67E6F5AD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BC3A2BB6-810D-E711-97CB-E41D2D08DCA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BCA7355F-6B0D-E711-976D-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BCBD3E83-AC10-E711-8675-0019B9CABE75.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BCF8FD08-760D-E711-AEAE-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BE0A0554-B210-E711-80E2-FA163EA21BF2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BE28DE97-370F-E711-BAAA-C4346BC70B58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BE525CC0-CA0F-E711-A904-FA163E143844.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BE7CF625-7B0D-E711-BECB-1866DA87967B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BED3AB09-5E0D-E711-B7C5-5065F37DD491.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/BED9B91B-830D-E711-B537-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C01222C6-760D-E711-9927-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C0358119-5B0D-E711-BD24-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C0C68CF3-C30F-E711-98A8-48FD8EE739ED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C244140A-7B0D-E711-B0A6-0CC47A7DFF82.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C2498D61-C20E-E711-A94A-0CC47A7DFE1A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C253E964-AC10-E711-A963-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C26AFD7B-C50F-E711-AE85-A0369FC5E22C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C2DF2484-7D0D-E711-B390-0CC47A7EEC70.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C4007191-9C0D-E711-BE26-48D539F3888A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C43098B1-A910-E711-BABB-C81F66B78625.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C44D364C-D70F-E711-9C6E-FA163EAEFC98.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C44F7235-710D-E711-B000-047D7B881DD4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C45EB08B-B90D-E711-9737-D4AE526A092E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C4725CCB-B110-E711-8023-842B2B42BCF8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C49A2CCE-B110-E711-A877-001C23C107AF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C49B8B99-A910-E711-8202-24BE05CEDCF1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C4AA2729-AB10-E711-944A-24BE05BD0F81.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C4B701D1-D60F-E711-8AA6-0CC47A00A814.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C4C57673-E30F-E711-82DA-FA163E992BDF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C4CE6C7F-7B0D-E711-829F-E41D2D08E0F0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C60FE4C3-CA0F-E711-B339-FA163ED16CDE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C63A6302-C40F-E711-BD1A-FA163E79C325.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C63ADA06-820D-E711-B9DA-008CFA001FDC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C667C64D-AB10-E711-9D59-B083FED046D9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C66F81C4-4A0F-E711-80D8-6CC2173BC990.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C69D47A8-780E-E711-AF09-48FD8E2824AB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C6B0FECA-B110-E711-8DAF-782BCB20D86D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C6C4996D-AB10-E711-9F6D-4C79BA181327.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C6D48053-540D-E711-9202-4C79BA1814CD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C6DF10B2-810E-E711-AB92-001E6779243C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C6F99BB7-690D-E711-AD3D-0CC47A0AD48A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8128949-D70F-E711-B07D-FA163E41B0FC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8258C14-AF10-E711-9A57-842B2B180C66.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8309D2D-B90D-E711-91C8-D4AE5269F656.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8397FED-B80D-E711-8891-1866DA87A96C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8455B8C-AC10-E711-848B-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C85AB7BD-290F-E711-9474-6CC2173BBAA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C85FEABF-5F0D-E711-90A2-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C88F1351-6B0D-E711-9FFA-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8908E38-020E-E711-863F-D4AE5269F5FF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C89EEA4A-AB10-E711-91F4-1866DAEA8808.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8A235BF-B010-E711-8F52-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8C991B1-A910-E711-BCF4-B083FECF837B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8CCD324-B80D-E711-A383-7845C4FC3C02.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8D84F4F-5B0D-E711-9A2E-0CC47A7DFFC6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8F8ECD6-750D-E711-9782-0CC47A7EEDB0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/C8FEECB6-DD0F-E711-A910-0CC47A7E001A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CA075A63-830E-E711-8409-001E67792518.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CA1A37A4-510F-E711-AEB2-C4346BBCD528.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CA561B49-8D0E-E711-99AE-848F69FD454D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CA57C5B5-AF10-E711-859C-141877411FCD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CAAEA4AA-D00F-E711-9949-001E677925E2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CABD0817-7B0D-E711-97D1-0CC47A7EED28.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CAD92CFE-710D-E711-BE75-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CAF5E90C-FD0D-E711-B780-842B2B7680DF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CC0E614C-AB10-E711-9C00-B083FECFEF7D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CC1F889B-B80D-E711-8992-001E6779257C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CC25D00A-5B0D-E711-B8BD-003048FF13E6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CC9C6000-720D-E711-96C4-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CCA2FAD6-9B0D-E711-B376-008CFAF51358.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CCAD62F8-750D-E711-9484-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CE0081B3-AD10-E711-9D9E-782BCB5300A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CE1B954F-AB10-E711-A600-1866DAEB1FC8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CE7F940A-800E-E711-A488-001E6779288E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CEB5853D-630D-E711-992A-047D7B881D0C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CEEEA557-AB10-E711-A733-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/CEEFECB1-A910-E711-8E6A-141877411970.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D00357AD-720D-E711-952B-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D03187F1-C30F-E711-96D3-48FD8E282471.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D052796E-810D-E711-8E54-48FD8E282975.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D07756A0-A910-E711-8693-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D0A4224F-B90D-E711-BFEC-0CC47A01035C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D0CB6AC6-B110-E711-90FC-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D222B49F-A910-E711-833A-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D2895215-180E-E711-9EBF-D4AE5269F611.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D2C47F25-820D-E711-A3FA-001E677924D8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D2CA7820-830D-E711-B278-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D2CC0D68-AB10-E711-A17B-24BE05C48841.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D2F189BC-B80D-E711-8F21-A4BF0108B83A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D2FFFA78-AC10-E711-BB55-141877410340.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D404454C-540D-E711-9DE1-4C79BA1814A7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D43225AA-AD10-E711-81A1-1866DAEA8230.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D46CC57A-790D-E711-A3E9-0CC47A57D066.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D4BE2538-CB0F-E711-88F4-FA163ED596E6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D4F5C19E-A910-E711-B7AA-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D616DDBF-7A0D-E711-A223-7845C4FC3B69.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D639E5BF-B010-E711-A5E9-4C79BA181327.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D6B496B2-AF10-E711-B34D-A4BADB1E6031.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D6C2FEF5-AA10-E711-91A4-141877411D77.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D80CA278-AC10-E711-AB0D-141877410316.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D8269F22-AF10-E711-852E-782BCB5300A3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D87372E1-9B0D-E711-9287-48FD8EE7389D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D8B8E9D9-9B0D-E711-A45D-48FD8E282493.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D8CD3876-D00F-E711-8564-FA163EFFA153.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D8CEF649-AB10-E711-8E11-1866DAEA8808.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/D8E19BDE-7A0D-E711-A7E3-003048FF277E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DA1E98B3-AD10-E711-8F4D-B083FED426E5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DA4599D5-750D-E711-BC36-0CC47A7EEE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DA55EEB1-A910-E711-96A8-1866DAEB31E0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DA5FA2AA-7D0D-E711-9FAC-1866DA87A870.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DA96F1A6-780D-E711-A626-48FD8E282493.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DAD25504-7B0D-E711-A950-1866DA87A96C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DAFDD88E-6A0D-E711-8140-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DAFE71F8-C30F-E711-B7D7-FA163E366F7D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DC022C5A-630D-E711-BDDF-047D7BD6DED2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DC44629B-B80D-E711-B362-001E677924EA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DC4ACEAB-B80D-E711-9258-001E67398E49.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DC7C2C81-B410-E711-B4B5-549F3525BC38.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DC89F201-810E-E711-B224-001E6779243C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DCA41FB2-A910-E711-B82F-549F3525C0BC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DCC5106A-AD10-E711-BDDF-001C23C0B781.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DCC5511C-630D-E711-B27F-E0071B7A7870.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DCE21DBF-B80D-E711-A261-001E677927C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DE1D6427-CB0F-E711-9231-FA163E519C7A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DE28B0D6-5D0D-E711-8C87-48FD8E28248F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DE323E8C-BD0F-E711-B0F2-001E677926B4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DE34CE49-B310-E711-BD6F-001C23C0B673.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DE3AB839-630D-E711-91CE-047D7BD6DD56.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DE994C60-710D-E711-A0B0-0CC47A0AD6FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DEA7D7C0-CA0F-E711-83D0-001E6779283A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/DEF94194-AD10-E711-9F0C-B083FED14CE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E0222677-AC10-E711-A104-141877410340.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E0858033-B80D-E711-8B9F-848F69FD4C94.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E0982E1B-5B0D-E711-A806-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E0C43AA7-780D-E711-BD3E-48FD8E069BA7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E0CE2BBA-450F-E711-9C97-00266CFFC550.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E0E2A8F8-800E-E711-A99F-001E67792518.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E22640A3-630D-E711-99AE-00259075D72C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E280A66A-CA0F-E711-B9DA-0CC47A7DFFCE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E29C4369-B210-E711-AD8E-782BCB20D86D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E29CBDDF-4A0F-E711-AFDE-047D7B881DD4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E2BEE59E-7A0D-E711-9BA4-001E673969D2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E2C9F651-650D-E711-8002-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E445319B-630D-E711-99C5-0CC47AA53D98.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E44A69CD-290F-E711-8D07-002590200B7C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E45559FF-5D0D-E711-B480-E0071B7AC7B0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E46CD698-AF10-E711-B860-90B11C0BD910.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E4A940C7-B90D-E711-BA27-1866DA87A96C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E4AB74FC-710D-E711-9CF3-008CFAFBF0BA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E4B6FDA0-A910-E711-8E6D-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E4BE50F7-A210-E711-8415-14187741212B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E4CA12EE-810D-E711-8356-002590A3C970.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E4CF4175-7B0D-E711-BF40-E41D2D08DDE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E4CF49C6-CA0F-E711-AF31-FA163E8A28E0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E602194C-7A0D-E711-88EB-001E677924B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E61FAED2-810E-E711-B90B-002590200A00.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E63968D8-AF10-E711-9CF4-14187741013C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E657D74A-540D-E711-8401-4C79BA181187.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E65B5A64-AB10-E711-97C5-24BE05CEFB41.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E663FDE4-5A0D-E711-AC01-0CC47A7E0006.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E6693155-5B0D-E711-8D19-00266CF32AF4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E689157F-640D-E711-86DC-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E69620F9-CA0F-E711-AB5B-FA163E3CBF20.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E69B9C0D-9C0D-E711-ADF4-48FD8EE739CB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E6ACD303-5E0D-E711-B6B4-5065F382C2F1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E6ED91E1-AF10-E711-98E3-1418774120C3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E8098A9F-A910-E711-BB96-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E825F5AA-AD10-E711-A208-1866DAEA8230.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E83FA75A-1B0E-E711-8569-0CC47A7EED28.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E853C1E9-B80D-E711-BC45-D4AE526A0A7B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E8845110-720D-E711-B90B-047D7B881DD4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E89CDEF6-A110-E711-A7B1-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E89D6F01-5E0D-E711-B720-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E8ADAE00-A310-E711-9206-782BCB539ABA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E8D906FD-C30F-E711-84F6-FA163E2D0F8B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/E8F5C7ED-750D-E711-B8FB-A4BF0108B152.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EA1F523B-AB10-E711-8557-001C23C0B673.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EA2A4E37-5B0D-E711-85D2-047D7BD6DF5A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EA6317AB-710D-E711-9DBF-FACADE0000BA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EA6414B4-AD10-E711-9698-90B11C0BD910.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EA7271B1-A910-E711-B2AA-1866DAEB31E0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EA7FF169-710D-E711-86A5-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EA9A109D-630D-E711-BFFF-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EAD9F1B0-A910-E711-9090-141877411970.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EADD20A8-780D-E711-ACBD-48FD8E28246B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EC1BBCB1-A910-E711-89D4-141877410ACD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EC4BB74C-CB0F-E711-84E1-F02FA768CFD2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EC776B62-AC10-E711-B0F4-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/ECB3E2A0-B80D-E711-BB7E-001E67E340DE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/ECB4F7BC-B010-E711-BFBE-E0071B7A96B0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/ECD13925-7E0D-E711-A1E9-1866DA87D4B6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/ECD47BA9-780D-E711-A182-48FD8EE73AC5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/ECD9DDCF-5E0D-E711-A507-5065F382C211.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/ECDA6164-AB10-E711-A0E3-E0071B7A18F0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EE1FE27B-750D-E711-988E-002590200B6C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EE2C6F34-690D-E711-8457-008CFAFC02A8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EE45C651-1010-E711-966B-00266CFFCB14.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EEBDE975-7B0D-E711-AE19-70106F4A9994.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/EEE7900B-5B0D-E711-B333-E0071B73C650.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F0065451-720D-E711-B852-008CFAF225DC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F06D45A0-A910-E711-A104-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F0AA787F-B410-E711-B570-C81F66B73923.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F25E7BD6-750D-E711-ACEB-D4AE526A0C89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F2786377-AC10-E711-8C34-1866DAEA8220.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F282CE19-B310-E711-8603-90B11C0BCBD7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F2E24703-7B0D-E711-A39F-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F2ECA716-AA10-E711-A8CC-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F42000AC-7A0D-E711-8A50-001E673969D2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F430F2E8-CA0F-E711-B939-FA163EC93E1F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F435B001-5B0D-E711-A4D4-5065F382C231.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F4651885-B410-E711-B1F5-549F3525DFE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F4A71D02-7B0D-E711-892F-0CC47A7DFF82.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F63CB66C-630D-E711-9892-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F642F338-6D0D-E711-8ADE-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F6691391-B90D-E711-BD31-1866DA890A68.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F6774155-690D-E711-94DC-0CC47A7DFE1A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F682E034-FD0D-E711-BFB2-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F6B6E50E-9210-E711-ABDF-0025905A6070.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F6F2D565-710D-E711-BF14-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F831F550-2F0E-E711-9CC1-001E67E71BFF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F8ACFA78-AC10-E711-AD1F-B083FED42C03.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F8AFF2EC-800E-E711-8D39-001E67792518.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F8B03BD9-9B0D-E711-864E-48FD8EE739ED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F8CCC84A-540D-E711-B800-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/F8EF6C64-AC10-E711-B5F9-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FA33A9C3-B110-E711-8949-14187741013C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FA367AB6-A910-E711-B3D3-001C23C0C7AB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FA4C4FEE-750D-E711-A751-001E67792486.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FA4E8343-630D-E711-AC46-F45214939740.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FA5BF1B1-AD10-E711-9B85-001EC94BE9FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FA92FE87-B90D-E711-9FC7-D4AE526A0A7B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FA9773A2-A910-E711-AD05-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FAA10ADD-AF10-E711-A7C0-1866DAEA7A40.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FAD6A5DE-CA0F-E711-AB56-FA163E69FB71.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FC1E7CB1-A910-E711-8FA8-782BCB3B1A5A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FC305E0A-5B0D-E711-97C2-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FC5443C5-820D-E711-97A2-001E67792890.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FC5FD74A-540D-E711-8DD2-4C79BA181187.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FC86A876-7B0D-E711-A1E7-E41D2D08DFA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FE559D14-800E-E711-B03A-001E6779262C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FE6AD3F2-750D-E711-BDBB-842B2B7680A2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FE78829F-A910-E711-AE7A-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FE85D5E7-5E0D-E711-9784-48D539F385F6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FE876B06-7B0D-E711-AF15-D4AE526A0419.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FE9629B2-A910-E711-8D54-549F3525C0BC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FEE9A905-800E-E711-AAB0-001E6779262C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50000/FEF2B2C9-B110-E711-94F8-90B11C0BCBD7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/0037AD54-B910-E711-AC21-B083FED42A1A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/00519803-BA10-E711-A0A1-1866DAEA8038.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/02134EF1-4711-E711-BCC7-0CC47AB0B828.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/0252D4FA-BF10-E711-A0EB-0025907793F4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/027A6B45-F710-E711-AB07-A0369FC5B504.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/02AC7B05-B910-E711-A4B2-549F3525B154.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/02E7D2E3-4711-E711-865D-001E6779279A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/04372F24-BE10-E711-88EF-FA163E6B9CE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/048AF2A3-B910-E711-8AC0-141877412793.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/049C7F50-DC10-E711-A36A-02163E012DD4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/065681FF-BF10-E711-8913-782BCB517BF6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/06A0FFCF-B810-E711-8EDC-B083FED42FB0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/06AF74DE-E910-E711-9FC9-001E67E6F8EB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/06CB2318-C710-E711-B255-C81F66B73923.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/0854E801-3811-E711-9DA1-FA163EBE7B76.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/08A68ACE-B810-E711-9855-003048FF16DE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/08DD986C-E910-E711-AB89-02163E013BFA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/0AC413D5-C710-E711-85F0-FA163EFAE64D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/0C8491B3-EF10-E711-8B83-B083FED024B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/0C855B6D-C010-E711-9845-FA163E5F7A31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/0CF13A04-C010-E711-9E2D-0025901ABB72.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/0EE52B40-F710-E711-A6BE-02163E00B32B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/101DCFC1-E810-E711-A0DD-141877411FED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/10B790B9-DB10-E711-9DFC-6CC2173BC8B0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/121E2BF5-BF10-E711-840F-B083FED42FB0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/126E77D9-E910-E711-8CBE-001E67E71C95.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/12945207-C010-E711-BA32-1866DAEA8218.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/14595CDE-B310-E711-AD1D-782BCB20E0D5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/14742536-DC10-E711-A553-0CC47A0AD456.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/14D8148B-C010-E711-B824-FA163E6B9CE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/16B810D3-B810-E711-8077-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/18780015-C010-E711-B26B-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/18B22EF0-B810-E711-86C1-FA163EBCACE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/18B4A40E-F010-E711-8D63-90B11C0BCBD7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/1C4CEBF3-B910-E711-B64C-141877410512.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/1C61C799-B910-E711-A2B4-1866DAEECFD0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/1C64E13A-0A11-E711-83A1-B083FED42A6E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/1C8EA3C3-DB10-E711-93DB-90B11C0BD63B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/1CAFEC53-B910-E711-9AB5-B083FED42A1A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/1E0EC82A-BA10-E711-AE0B-14187733AD89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/1E3088D6-B810-E711-B1E7-B083FED42488.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/1EC2638C-9411-E711-918B-FA163EDA7940.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/24FE3059-B910-E711-B246-A4BADB1E6F27.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/282D0D53-BA10-E711-BC0E-0019B9CABD35.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/287430EF-B810-E711-991A-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/28C095E1-E210-E711-B4F8-B083FED42B3B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/2A1DD9CB-BF10-E711-9825-D4AE52651C5F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/2AB93ED3-C010-E711-9652-FA163EA6BC40.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/2AFCEAD7-B810-E711-9604-0CC47A0AD704.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/2C44D4C2-B310-E711-9579-B083FED3F4E3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/2C487B5D-B910-E711-B71B-001C23BEBF16.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/2C5FE7DF-B810-E711-AB8B-782BCB5364D6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/2CC43DDA-E910-E711-BEB2-001E67E6F8EB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/2E87A0CC-E810-E711-966C-842B2B42BCF8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/2EB17705-B910-E711-9D3D-549F3525B154.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/303387FC-BF10-E711-816C-782BCB517BF6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/30EE8FD3-B110-E711-B5AE-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/36406C9C-B910-E711-8508-FA163E0673C3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/36476B3B-BA10-E711-947D-B083FED42FC4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/36D8365D-DC10-E711-AEA8-C4346BC08440.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/384EE4AA-CD10-E711-A7ED-003048FF2826.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/385963AB-C010-E711-AFE7-02163E012FCF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/3872BBAA-CD10-E711-8AD6-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/3C434AB3-C010-E711-B94B-02163E01515C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/3C529DBD-B310-E711-956B-782BCB20D86D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/3CE594C9-B810-E711-809D-1866DAEEB344.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/3E6516E3-B910-E711-893F-B083FED14CE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/3EBD18D0-B810-E711-A91C-0242AC130006.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4064FD1C-C010-E711-B09D-0CC47A4D7650.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/40988D3B-BF10-E711-85AC-02163E01533A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/40E9B054-B910-E711-B8BB-C81F66B7F2C9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4261AF95-B410-E711-B1AA-B083FED045ED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/44357A54-B910-E711-8E50-B083FECFF6AB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/466BA84D-B910-E711-B5CE-1866DAEA8038.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4685915B-2A11-E711-8BA9-782BCB783902.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/46AA6F46-BA10-E711-B47B-90B11C0BE662.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/46AD4B59-B910-E711-95D4-A4BADB1E6F27.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4814D955-D510-E711-928C-AC162DAB0B08.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/48742ECE-B110-E711-ADA0-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/488F8143-BA10-E711-9CF0-90B11C0BCBD7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4A329054-B910-E711-B8C1-C81F66B7F2C9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4A817D54-B910-E711-A645-B083FED42A1A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4A98F906-B510-E711-A171-001EC94BE9FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4AC6F7DB-B810-E711-B356-0242AC130006.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4C053741-BA10-E711-ACAE-B083FECFF6AB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4C3401B6-F610-E711-A172-C81F66B78E01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4C4B3CB5-B910-E711-9332-B083FED426E5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4E231EDC-DB10-E711-B8E2-B083FED179D5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4E58E1C7-E810-E711-AEF2-FA163ED99D83.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/4EDBD4F2-BF10-E711-83FB-5065F3810301.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/5045DD4D-B910-E711-8211-B083FED43141.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/5200AAA4-E210-E711-83C9-0CC47A4D7674.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/52987EE8-B910-E711-8715-549F3525B154.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/5421F8FB-BF10-E711-8F0C-002590D9D84A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/5461CEA5-CD10-E711-AC75-1418774105B6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/5633CF53-B910-E711-A790-14187733AD89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/563EC1AF-4611-E711-B0D1-C4346BC7EDD8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/566AD3DC-B810-E711-9144-0242AC130005.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/566C2BF4-BF10-E711-B55B-1866DAEA6CF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/56C525F6-BF10-E711-99A6-C81F66B7F2C9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/58073548-ED10-E711-9AA0-FA163E1133C1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/5876C1BF-E810-E711-986C-1866DAEA7C48.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/5889DA5D-F110-E711-BEA4-A0369FC5DCBC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/5E381A10-DC10-E711-9320-02163E012DD4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/605028FF-BF10-E711-A2A2-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/6298C8CE-BF10-E711-8D64-549F3525DB98.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/62F702D8-B310-E711-A249-549F3525DFE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/640FC6AC-C010-E711-B257-02163E012E27.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/64E7710D-F010-E711-94E4-B083FED3F2E9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/66584C20-C710-E711-BB1E-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/66EB4B39-4811-E711-A834-24BE05C6E561.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/66FA72D4-B810-E711-9F40-B083FED42FE4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/681A97F5-BF10-E711-8A56-1866DAEA8220.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/6CB2EAD3-BF10-E711-B2AE-842B2B18118F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/6CE2EAC0-D410-E711-89A8-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/6E2C2F56-B910-E711-BDCA-B083FED14CE0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/6EF03A99-E210-E711-AD9E-FA163E4C811E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/6EFD49B3-C010-E711-9CC6-02163E01515C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/70287058-B910-E711-91D8-1866DAEA6D08.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/7048E7C5-CD10-E711-B7A5-002590D9D8C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/70D9FD1A-C710-E711-891B-141877410512.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/726CCDB3-F610-E711-920C-A4BADB1E763D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/72A2648A-C110-E711-B312-FA163EF67F8B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/74ADE014-9411-E711-BF4B-FA163EBC2378.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/74B3C2D3-4711-E711-87F4-FA163ED12ECC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/76767D0A-CE10-E711-B194-FA163E6B4573.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/78295F2E-B910-E711-AAC1-FA163E9DA9B9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/783A0723-C010-E711-96A3-FA163ECA6953.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/78D81ECC-4711-E711-9FD0-1866DAEA6E00.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/7A0810D9-B810-E711-B246-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/7A7BAEC6-F010-E711-B56D-FA163E4D1B47.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/7A8B592D-3D11-E711-AB4F-1866DAEB5C94.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/7E363A71-BA10-E711-94B9-1866DAEECFD0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/7EA4CAD6-A011-E711-8ED3-02163E01314F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/7EE67AF6-1111-E711-B20D-FA163EEBD3A9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/80231715-B910-E711-AED8-FA163E1E2EDC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/80B8E6F9-2311-E711-B817-FA163E2597F9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/80DE1064-BA10-E711-B86C-B083FED42FE4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/827D1176-C010-E711-B3A0-0CC47A0AD74E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/82863400-7311-E711-96B1-FA163E5EE91B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/82FF1B69-B910-E711-954E-90B11C0BE662.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/8435FFA2-CD10-E711-96D8-1418774108DF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/8451476A-8311-E711-A5A1-FA163E3E47D5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/84A037F4-0A11-E711-8FF0-FA163EC559DE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/84A21C69-B910-E711-A2CD-90B11C0BE662.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/86B8A4B2-C010-E711-96DF-FA163E6C1D2A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/86FCA2B8-B910-E711-802B-549F3525B154.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/88EA1AF5-BF10-E711-B71C-1866DAEECFD0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/8A82E205-4811-E711-810E-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/8ABB26F8-BF10-E711-B807-842B2B163FE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/8AD87B29-C710-E711-BE44-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/8CA76DCF-B810-E711-BE62-D4AE52E914C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/8CC706A7-CD10-E711-8ACB-1866DAEA8220.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/8CCFA644-BA10-E711-903E-1418774108DF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/8CE7B938-B410-E711-B247-001C23C105CA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/90B9150C-B410-E711-9665-D4AE526DEDB7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/90E86123-C710-E711-A0D8-0025907D244A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/926E2217-C710-E711-8542-14187741278B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/926FD779-B310-E711-871C-D4AE526DEDB7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/92C942D2-B810-E711-9317-0242AC130006.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/9430EAF3-B810-E711-BC68-00259029E920.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/9656F68F-C010-E711-8BC5-02163E01515C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/96675FC8-DB10-E711-A807-FA163E3C06B1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/96D94403-B310-E711-917F-782BCB20D86D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/983315DB-B810-E711-B4C5-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/986F8546-BA10-E711-AD86-90B11C0BE662.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/9A2837C7-B810-E711-B6B2-24BE05C4D821.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/9A92D01D-B910-E711-88FE-FA163E32BACE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/9C744996-C010-E711-8D81-02163E013C25.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/9CC4E1E0-E210-E711-BE67-D4AE526DF5FB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/9CCE66CE-2911-E711-A9CD-FA163ECC6265.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/9EB096A6-C010-E711-85E2-FA163E87B92F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/A2D2EA8B-C010-E711-AA21-FA163E5F7A31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/A444EDF2-BF10-E711-9B69-141877410512.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/A67532F6-E410-E711-A3FE-001E677926E2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/A698C02D-3D11-E711-981B-1866DAEB5C94.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/A6B9CD20-C710-E711-841A-0CC47A57CCF4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/A83566C5-E810-E711-92F4-842B2B18118F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/A88FA5CA-B810-E711-A2EB-549F3525C0BC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/AA5C660B-C010-E711-9396-0242AC130002.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/AAFBEE53-B910-E711-ACBF-B083FED42A1A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/AC14D9FC-BF10-E711-82B7-0242AC130003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/AC608B59-BA10-E711-A27D-A4BADB1E6F27.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/AE6B760C-CE10-E711-9CEA-B083FED4239C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/AEDDB8D0-B410-E711-B9BE-1866DAEB5C94.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/B23583CE-B810-E711-8E0B-1866DAEECFD0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/B4034D5E-D510-E711-B93B-02163E013A90.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/B6016EE1-B810-E711-8D75-0242AC130004.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/B6E993E0-E210-E711-97E0-141877411D83.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/B8AC4CBD-B010-E711-81A6-E0071B7A96B0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/B8BFCDF1-BF10-E711-8CEE-5065F381A2E1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/B8D9C507-C010-E711-8CFF-1866DAEEB0A8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/B8F772EE-B810-E711-A044-FA163E1E2EDC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/BA1BB553-B910-E711-94AB-C81F66B7F2C9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/BA7B1C52-E910-E711-81AA-00259029ED64.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/BCD533BF-B310-E711-9830-90B11C0BCBD7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/BCDEEBE4-B310-E711-8A03-782BCB536A50.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/BE4052AB-CD10-E711-A2A5-782BCB5094C5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/BE7B365D-B110-E711-9DA0-FA163EF282E9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/BE7E6D11-B910-E711-933F-FA163E1E2EDC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/BED0FA18-B410-E711-8D9C-001EC94BE9FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/BEDDCDB5-B910-E711-8097-B083FED426E5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C04C6AC3-C610-E711-9718-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C06CECD4-B810-E711-BAE3-FA163EBCACE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C09D67EC-B810-E711-87DB-0019B9CAFC2D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C0F5F47B-FD10-E711-A582-A0369FC5E9A4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C2111C4E-B910-E711-B0E5-1418774108DF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C24D4B36-C010-E711-A259-FA163E5F7A31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C2645966-C010-E711-B81A-FA163E18B86F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C2A55FF7-BF10-E711-9EB9-C81F66B78DC1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C44A916E-C010-E711-81D3-FA163E5F7A31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C469166B-C010-E711-AB28-141877410512.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C4709A5D-B110-E711-B160-FA163E651269.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C4CFC9A3-B910-E711-BD6B-B083FED42FE4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C4FFE953-B910-E711-A222-14187733AD89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/C85B3F38-C010-E711-A891-842B2B18118F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/CA5B4654-B910-E711-9707-C81F66B7F2C9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/CA8D2ED1-B810-E711-A02A-141877412793.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/CABA5DC0-DB10-E711-9F6F-FA163ECE2984.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/CAC68B5B-C010-E711-85B7-FA163E5F7A31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/CADAD0CD-B810-E711-9838-A0000420FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/CC64ADE0-E210-E711-A99C-90B11C0BCE26.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/CE36A9F2-BF10-E711-82F0-5065F381A2F1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/CE4286A5-BF10-E711-86D4-549F3525BF58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D06B500A-C010-E711-B768-0CC47A57CD6A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D0F8B800-C010-E711-9128-001C23C0B673.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D22162C7-B110-E711-A32D-D4AE52E90BA7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D2667C37-BA10-E711-8498-B083FED42A1A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D2B1A0E7-B810-E711-889D-FA163EBCACE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D4675B6D-C010-E711-A2DE-FA163E5F7A31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D4715CCE-B810-E711-BAF1-0242AC130006.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D6EFF5BE-B810-E711-A079-0CC47A4C8E20.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D86FE0FA-BF10-E711-95E7-D4AE52E7E8A1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/D88A40E8-C010-E711-B06F-02163E012E27.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/DAA37BCC-B810-E711-8A0F-E0071B740D80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/DAF3FFC2-D410-E711-A63A-549F3525E81C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/DAF777BB-3711-E711-94DE-FA163E40BFD6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/DC1D2C59-B910-E711-A1D9-A4BADB1E6F27.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/DC74E2F4-BF10-E711-B331-B083FED42FB0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/DE361C07-2811-E711-B42E-02163E0176EB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E00F4877-C010-E711-929C-FA163EB435CB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E0671462-1011-E711-B70F-C81F66B782DD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E2358453-D510-E711-8C3E-C4346BBCB6A8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E2FFCCF3-B810-E711-9275-FA163E0673C3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E40FE8EE-B310-E711-89AD-141877411FED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E47EFFC7-B810-E711-B20E-24BE05BD4F81.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E4CA364E-B910-E711-8D40-141877410512.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E6688FF9-BF10-E711-87C7-B083FED42FC4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E832EE0F-F710-E711-9DE4-001E67E713FE.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E8B2AD85-E210-E711-AC32-FA163E66532E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E8BC0DA5-B310-E711-86CA-1866DAEB4100.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/E8E606A7-D410-E711-9E74-141877344134.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EA12D213-BA10-E711-AD3E-0019B9CAFC2D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EA822CF7-F210-E711-B5D8-001E67E71A56.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EA921AB4-F610-E711-8E12-90B11C0BDC70.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EA9B4962-C010-E711-A39D-14187733AD89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EC1D7DDA-B810-E711-80AD-0019B9CB004B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EC39F5A5-C710-E711-A8A5-02163E012D27.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/ECF54D87-B310-E711-A4EC-842B2B42BCF8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EE529BD0-B810-E711-AFC2-E0071B749C40.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EE6D26DB-E910-E711-B91A-001E67E6F8EB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EEB10BBB-DB10-E711-8636-00266CFFC13C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/EEC1E303-BA10-E711-8783-1866DAEA6D08.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F00EAD55-B910-E711-8039-0026B937D37D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F05B8D36-F011-E711-BA3B-002590494C20.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F200F79C-6A11-E711-BF5B-FA163E2B97D0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F2132418-BA10-E711-A3DD-0026B937D37D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F22CCB53-B910-E711-9FEA-14187733AD89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F2FCFD79-1211-E711-8DDD-FA163E69F401.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F44CB8C7-B810-E711-8698-24BE05C6E7E1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F603F27B-FD10-E711-901D-A0369FC5E9A4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F6228224-BA10-E711-AD8B-14187733AD89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F84D3F59-B910-E711-9905-A4BADB1E6F27.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F84FC8D3-B810-E711-977F-90B11C0BCBD7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F8635654-B910-E711-A145-C81F66B7F2C9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/F86A7D5D-B910-E711-9162-001C23BEBF16.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/FA6DBEEA-B810-E711-AA66-FA163E5772D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/FC01FAF8-BF10-E711-9955-549F3525D084.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/FC0684B9-C010-E711-85DB-02163E012E27.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/FC25BB34-1711-E711-8716-FA163E1BA575.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/FC9D7FA2-1711-E711-BD7F-FA163E6EC48D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/50001/FED8222E-C010-E711-A728-D4AE52651C5F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0012E1D2-9614-E711-9A4C-02163E012CF9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/004E5CB0-9D14-E711-B1FA-001E673D2EB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/005E7251-A914-E711-A915-9CB65404EEF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/009FB522-AE14-E711-824B-FA163EEA4485.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/00C062E5-A414-E711-96EC-001E6739C801.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/00D1A21A-9B15-E711-9A56-001E6739C8C1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/025FCA8E-A214-E711-A3B9-FA163E94C2AC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/027B12E0-AB14-E711-B9E8-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0282969F-B114-E711-AF74-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/02C9A2A2-A614-E711-916F-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0400D64E-A714-E711-AB66-001E673D0C31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/04AA8C93-9314-E711-A76A-FA163EC45103.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/04B0CD46-A314-E711-A393-001E673C842D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/04F0CA59-A314-E711-BDD4-FA163EE7F932.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/067094DC-AC14-E711-8F2B-001E673CFFC1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/06743C25-AE14-E711-8A4E-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/06D4EE23-A214-E711-9964-001E6739B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/06F4BD30-A614-E711-B434-FA163EBA4FEC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/08344B88-A214-E711-884C-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/08A2FDD5-A214-E711-BC2F-02163E013BDB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0ADD9574-BB14-E711-9B98-9CB65404ED04.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0C2EA424-AA14-E711-A1C6-FA163E11913F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0C8566BA-B414-E711-A848-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0C86D849-B214-E711-A8C1-001E673CFFC1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0CE689BE-A414-E711-BD4B-FA163E9BB1C9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0E5D4818-B914-E711-B16B-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/0EBA6820-AC14-E711-86CE-001E6739A959.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/10157CE9-9F14-E711-9CEC-FA163ECE5C65.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/102EB4E2-9B14-E711-A4CF-FA163E1DA852.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/10556CDE-A714-E711-B763-9CB65404FBA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/10B52456-9F14-E711-9439-9CB65404FBA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/124D3141-AE14-E711-BA10-FA163E491165.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1259D676-9014-E711-95CF-02163E012D4F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/12DD5CE2-9714-E711-A311-02163E00C1C9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/14318E34-AA14-E711-AB37-FA163E89ADE1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1456A7C9-CC14-E711-8FCD-001E67F8F9F2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/149BD9E3-A414-E711-84B1-9CB65404FBA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/14B72751-A514-E711-8F71-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/14DF94AF-B614-E711-8D7A-FA163E194801.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/160D7A5C-A914-E711-A402-FA163E032721.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/16500D50-A314-E711-9CCF-001E6739B871.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/16ABF09B-AF14-E711-9559-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/16B2F6D2-9D14-E711-B064-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/16CB9753-BD14-E711-834D-FA163E78FE3D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/18C678CB-A314-E711-BB53-001E6739BB01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/18D71D2C-A114-E711-80FF-FA163E94C2AC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/18F6AB90-B214-E711-9829-FA163E35CF48.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/18F87843-9F14-E711-B7F1-FA163E10BB35.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1AAE91B3-9A14-E711-AF2A-FA163E989B5B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1AF9750F-A114-E711-8553-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1C3322A5-AA14-E711-83D1-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1CAF22A7-9A14-E711-B162-001E67FA3812.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1E03776F-AA14-E711-802A-001E6739A411.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1E15E4A8-A614-E711-824B-FA163EEF9401.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1E2FA18F-AC14-E711-AA19-FA163E66742D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/1E32EDF9-B614-E711-BFF4-9CB654AD7670.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/20076D9F-AB14-E711-8438-FA163E44A2C1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/20138CD1-B214-E711-BF3A-001E6739C8B9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2028D83A-A214-E711-8234-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2042A4A5-B514-E711-891F-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/20538F4E-A714-E711-96B6-FA163EEDCF11.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/205770CC-B214-E711-9DF9-FA163EA32CA9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/22193970-B414-E711-84B5-FA163E141358.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/222153F5-C614-E711-B4BB-9CB654AEAC62.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/222F6004-BB14-E711-9925-9CB654AEBE22.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/223B001E-9B14-E711-92C4-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/225D9744-A214-E711-A692-FA163EC64F9E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/22C7C73B-B614-E711-8073-FA163E0D6C45.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/245EAC84-C214-E711-A39B-001E673CFC91.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/24AF6378-BC14-E711-885E-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/24C66A4C-B114-E711-B648-FA163E1A7F54.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2614769E-9F14-E711-B6F8-FA163EA71FB4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/263F9793-9F14-E711-A88D-001E673D2EE9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/26429E96-AB14-E711-82F1-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/26497738-C514-E711-8070-FA163E4383B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2666D9ED-A414-E711-B8AC-FA163EE79003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/26A11909-9B14-E711-A0A2-001E6739B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/283EF3E2-AC14-E711-90E9-001E6739A959.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2896A3D5-AC14-E711-8A25-001E6739C2D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/28B66460-C314-E711-9188-001E673D2261.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/28D726CE-A914-E711-A04A-FA163E4F8C68.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2A085513-A914-E711-A76A-FA163E0369ED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2A2354D2-9D14-E711-8B30-001E673C83E7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2A2E9C5E-AF14-E711-B3EB-001E6739C2D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2AC6FE03-A614-E711-8C85-001E6739B871.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2ADEC1B4-BF14-E711-8972-001E67F8FA4C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2ADECEF6-B114-E711-9C4A-02163E013BDB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2AFDA3E2-A414-E711-88B0-001E6739B871.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2C633075-AA14-E711-A57A-001E6739A3F1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2CA5354F-A714-E711-B3E4-FA163E10BB35.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2CDDF36D-B014-E711-9085-FA163E11913F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2CDE039E-AB14-E711-B2E8-FA163E7141B6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2CF4B7DC-A214-E711-8BF5-FA163EF72FA5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2E17AB6E-9414-E711-A442-FA163E747FF8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2E4278B7-A814-E711-9476-FA163EBCACE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2E623372-9014-E711-8CC2-FA163E09E6DF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2E802CE4-B114-E711-8691-001E6739C8B9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/2E9043CC-C014-E711-9789-9CB654AD7810.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/30009348-BA14-E711-9831-9CB654AD7670.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3091BE48-BC14-E711-89A3-001E67496A6C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/327CE524-A914-E711-B6F2-FA163E4F8C68.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/32856C4D-9614-E711-902F-FA163E09E6DF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/32A107C4-B314-E711-982E-38EAA7A30576.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3433A7B1-B014-E711-AF67-FA163E5362C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3633817B-A114-E711-980D-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/364E3E5E-C314-E711-B7F5-001E6739C2D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/36691734-A914-E711-A155-02163E017660.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3685D442-AD14-E711-86F9-FA163EAAE7B3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/368FCF4C-A314-E711-A447-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/36A3EF6E-BB14-E711-93D5-001E67496A6C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/36AA2848-A214-E711-8521-FA163EB35AAD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/387B3299-AB14-E711-8068-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/387CB42C-9514-E711-B667-FA163EE7768A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/38A577D0-9614-E711-94BE-001E6739D031.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/38CED7E6-9C14-E711-967A-001E673D2EB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3A7C46E2-C314-E711-A5A6-001E6739D281.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3AB5AD21-A814-E711-9FFA-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3AEC1528-AD14-E711-90F4-FA163E5362C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3C06D1D3-9314-E711-BBDF-FA163EC64F9E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3C1D3334-AB14-E711-B7E0-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3CD2D950-B514-E711-BB59-001E6739ABB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3CD5BF28-9514-E711-B714-FA163E78C0FA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3E57FBD8-9D14-E711-93C5-FA163E8FA20F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3E589F17-9C14-E711-A2C2-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/3EDC3424-B714-E711-9F89-001E6739ABB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/409C060D-A914-E711-AFC0-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/40AABF3F-BE14-E711-8EE4-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/40E9DAB5-A714-E711-AC60-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4277B219-B414-E711-92A6-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4285640B-AD14-E711-B991-FA163E78A328.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/428746A1-AB14-E711-B7E7-FA163E63D50D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4292A636-9214-E711-BB5D-FA163E8926DA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/42B2B6A7-AA14-E711-8410-FA163E7C6F41.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/440725E4-BC14-E711-9F32-001E67496A6C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/466BF053-A314-E711-B315-FA163E52A5D8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/469DC0F4-A014-E711-90A2-001E673C842D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/469DF59A-AC14-E711-94A3-38EAA7A6DC58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/46BF51B4-A614-E711-8F10-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/46D6887D-BC14-E711-8CFF-001E67F8F9F2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/485AC9AC-9E14-E711-B01F-FA163EE3B5ED.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/48E4CE4E-A914-E711-9AAC-FA163EBCACE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4A0C1D0C-B014-E711-97F8-001E67FA385D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4A400491-AB14-E711-8F88-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4AA1269F-AB14-E711-B11C-FA163E5362C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4C689C7F-AA14-E711-B945-FA163E4F8C68.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4CABBC52-B514-E711-B6E2-001E673D1B21.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4CFD0599-AB14-E711-AF34-38EAA7A6DC58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/4ECEE760-9D14-E711-A5BE-001E673D2EB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/50452749-A714-E711-93A6-001E67FA4113.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/509B27FD-B014-E711-873C-9CB65404F364.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/50A8EBD9-C614-E711-8EF9-001E67FA3920.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/50B56D6B-9214-E711-B160-9CB654AEBE22.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/50FC4C8F-BB14-E711-82EC-FA163EFE7083.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/52358447-BE14-E711-97F7-001E67F8F9F2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/529DD0D5-BC14-E711-A0DB-9CB654AD7670.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/52D0C0F3-B214-E711-9549-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/52DFF027-C214-E711-9C5B-38EAA7A3137E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/542F2F9C-9F14-E711-947D-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/56348495-9F14-E711-99C5-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/563AF225-A014-E711-988B-FA163E78A328.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/56B258B9-BF14-E711-9AA6-001E67FA4113.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/58006427-C414-E711-BB32-38EAA7A6D65C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/581A9741-B714-E711-8670-001E67F8F7BD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/584E4B50-A714-E711-9AF5-02163E0131D0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/584FBFCF-B214-E711-8798-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/589677FA-B014-E711-BF18-38EAA7A30576.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/589E112D-A514-E711-861B-FA163EF1B5D8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/58C07DEC-A714-E711-91E5-FA163E35CC86.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5A24D2A1-C414-E711-8B8E-001E6739ABB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5ABDC629-AA14-E711-B9AD-02163E013BDB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5C4FFB66-A414-E711-A308-001E673CFFC1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5C66E1D4-9D14-E711-B38F-001E673C842D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5C9937F2-9C14-E711-BD0E-FA163EF3C52F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5CB4B44A-C514-E711-BBDF-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5CD2DDCF-9414-E711-BC42-FA163E78C0FA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5CFDDDF7-9B14-E711-AB2A-FA163E35CF48.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5EBABCF4-9C14-E711-8E9E-001E6739BB01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/5EE42D9A-C514-E711-B1AE-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6014A20F-A514-E711-858D-001E673CFFC1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/60156C42-AC14-E711-9D95-FA163EC45103.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/602772BD-B414-E711-86BE-FA163E194801.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/62354DFE-B014-E711-A66A-FA163E9180FD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6289CB9B-9B14-E711-9FC9-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/62DD1CB9-BF14-E711-971C-001E673C83E7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/64192D1B-C414-E711-ACBD-001E673D21B9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6448F9C5-B914-E711-AE42-9CB654AD7358.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/645D4002-8A15-E711-AF1C-FA163EE98D9B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/646AE21A-B414-E711-8B09-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/647508D6-9514-E711-AF12-001E6739B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6491A520-A114-E711-A9BE-001E6739A3F1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/64C384EB-9C14-E711-BF96-001E67F8F727.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/64FD3E41-A814-E711-B15C-FA163E42BA1E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/660C716A-AF14-E711-B09C-38EAA7A30576.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/661C8847-AB14-E711-BB8E-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/661F176B-B414-E711-BBF6-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/66E96CE9-B614-E711-96D8-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/66EB4297-9F14-E711-B7EB-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/683AAFC4-B414-E711-A511-001E6739ABB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/68B750AD-A814-E711-843A-001E6739B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/68E05A1F-AE14-E711-B179-FA163EDABB13.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6A5E07DA-C114-E711-9D8A-38EAA7A6D65C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6A6CE4DE-9514-E711-AE3D-FA163EE28A6F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6A725CB6-AE14-E711-83C6-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6A726BD0-BC14-E711-BF72-9CB654AEB2C6.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6C04633B-C614-E711-84CC-001E673D2261.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6C216286-AF14-E711-A0C8-001E6739C8B9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6CB1498E-D014-E711-8AFF-001E673CFFC1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6CCA3696-9F14-E711-A814-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6E8ED945-AF14-E711-A397-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6EEA05FB-B714-E711-8510-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/6EFE5DB9-BF14-E711-8B0B-9CB65404F364.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/70134658-9F14-E711-A870-38EAA7A3049A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/701650A6-A814-E711-8978-FA163E5866C0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/70AEBD21-A014-E711-8343-001E6739B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/70F16F86-AF14-E711-B5E9-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/72B6571E-A014-E711-8C90-001E673C842D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/72C298A1-A214-E711-AABA-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/72C529B3-AC14-E711-9150-FA163E78A328.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/72CBBCC3-A814-E711-9653-001E673C808A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/72F7F55A-9314-E711-8AEC-02163E00C1C9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/72F89CF8-CA14-E711-A492-001E67F8F763.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/747D057D-C014-E711-B9DF-001E67F8F6CD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/74C118C4-B814-E711-9B2B-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/7609DC07-9514-E711-9312-FA163E934E90.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/76542ABD-AF14-E711-A420-9CB65404EEF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/769E0AEB-C514-E711-AA64-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/76E22CD1-C414-E711-8204-38EAA7A6DC5C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/76E778A1-A314-E711-8DA8-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/784C045A-A314-E711-A692-FA163E4F8C68.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/785CCB05-AD14-E711-9C7E-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/78A6F8DD-B714-E711-BBBF-38EAA7A6DBC8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/78C2470A-B214-E711-9CDA-001E6739C2D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/7A29AE9F-9D14-E711-BC20-001E673C7FB1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/7AE24B88-C714-E711-88C0-9CB65404FBA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/7AF0459F-A314-E711-86DA-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/7C521E38-9214-E711-8B9C-FA163E1B23B1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/7CB306A8-C414-E711-A7C2-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/7CB4B8E7-A414-E711-A9B9-FA163E4F8C68.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/80414C4E-BA14-E711-B239-9CB654AD7998.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/80BE6E54-B514-E711-B7A6-001E6739BB01.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/80C1982F-A814-E711-B3F6-9CB65404FBA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/827F38BC-A714-E711-A40A-FA163E006E46.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/82AF07AA-CE14-E711-B4AB-001E673C7B3C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/82BBF92B-A414-E711-BF04-FA163E4F8C68.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/82FF375E-A414-E711-877F-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/84325C21-C414-E711-BB52-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/84A91707-C514-E711-8669-001E6739ABB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/866F6A2A-A014-E711-8298-FA163EDAD116.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/86C17DD0-BC14-E711-9148-001E67F8FA06.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/88055DD9-9D14-E711-9BA9-FA163EC87CE2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/88715F0F-A914-E711-BDBA-FA163EE79003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/889A1ADC-A714-E711-8AE0-9CB654AD72EC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/88A49555-A914-E711-9355-38EAA7A6DC58.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/88E5A2B4-A114-E711-8AAD-FA163EF20F4F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/8A6303DF-9B14-E711-9148-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/8A72EBE9-A314-E711-9E6B-FA163E8E3F3A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/8AB4E0D5-9414-E711-B3BC-001E67FA413B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/8C193EDA-AD14-E711-BECB-001E6739A959.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/8C50E7D7-AC14-E711-BD3E-9CB65404F364.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/8CF16982-9D14-E711-AC49-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/8E9EDA7C-A614-E711-AFC1-FA163E1A125C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/8ED942E0-A914-E711-955F-001E6739A411.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/90214710-A914-E711-B0A9-001E673D0C31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/90876152-9B14-E711-B32F-001E673C7FB1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/92BE9DAE-BA14-E711-8224-001E6739ABB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/941E04D6-C014-E711-B687-38EAA7A6DBC8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/94AA82CF-9E14-E711-B111-FA163E0D86FB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/94D0D5A5-B314-E711-BA61-001E6739C8B9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/969FB430-AB14-E711-9C6A-001E673CFC91.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/96A59E39-9414-E711-8B1F-FA163E8F18B2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/96C3D70C-B514-E711-BC62-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/96E9B45F-C314-E711-A897-38EAA7A3049A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/981D535E-C314-E711-873F-9CB654AEAE86.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/9837E7D5-AC14-E711-9DCD-9CB65404FC30.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/98993B64-AE14-E711-96E7-FA163E2C7E9C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/98EB6AA3-B114-E711-A124-FA163E9180FD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/9A4D9668-9E14-E711-B63F-001E673D2261.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/9C73A6FC-C714-E711-B804-001E67F8FA15.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/9CD1C74E-BF14-E711-8CBB-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/9CE45F79-AD14-E711-8C18-9CB65404FBA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/9E07D9F4-9314-E711-840F-001E673C7EF4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/9E8AB224-AD14-E711-B380-001E6739C2D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A01487BD-AE14-E711-AB62-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A03A561D-A014-E711-A25E-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A0483650-C514-E711-B0D0-38EAA7A6D65C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A052B60E-AA14-E711-BD15-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A07E714A-BE14-E711-B3AE-001E6739C8B9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A0CB8527-9E14-E711-9C1E-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A2045C43-9E14-E711-AEF6-FA163EEA7499.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A29AE6EE-C714-E711-9F84-001E6739ABB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A2E1A10F-AA14-E711-93FC-001E6739AC59.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A43E8EC3-AF14-E711-9CDF-FA163E11913F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A4DA5BA9-9714-E711-BB8E-001E673C83E7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A6378C76-AE14-E711-B1B8-001E6739A959.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A657965A-C314-E711-A31C-001E6739D281.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A6CF4FAB-A014-E711-B755-FA163E491165.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A830F731-A614-E711-B73C-02163E01771B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A89BEF2A-C214-E711-87B3-9CB65404EEF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/A8D18FE5-9F14-E711-8A8C-38EAA7A6DBC8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/AA4CADC5-C014-E711-A35B-001E67FA385D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/AA63A853-AD14-E711-AE89-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/AA881AA0-C914-E711-BA73-9CB654AD72F8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/AC43E034-A814-E711-B0A4-FA163EE79003.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/ACB6E80D-A914-E711-8232-9CB65404FBA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/ACE978EB-A314-E711-9E61-001E673D0C31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/AE803D0B-A914-E711-9412-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/AE9B8D37-A814-E711-81E9-FA163EBCACE8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/AECF2F3E-9914-E711-8974-001E6739A411.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/AED09594-9F14-E711-899D-001E673D2261.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/AEFF03A6-AF14-E711-ACFD-FA163E5362C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B06E3D4A-B114-E711-86DF-001E6739C8B9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B0745573-A614-E711-ADCB-001E6739B871.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B0A8EB5A-A914-E711-8B4E-FA163E639162.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B0BE297D-A614-E711-B51B-FA163EA71FB4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B0E01B86-A214-E711-9B9E-001E673C842D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B20B47AA-A814-E711-A2EF-FA163E42BA1E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B229A0AC-C014-E711-8022-001E673C83E7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B4451A26-A014-E711-82E9-FA163E154904.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B4479EE6-A414-E711-97CC-001E6739C801.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B4487117-AA14-E711-A849-FA163E639162.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B45FF0D3-AC14-E711-896C-FA163EE07709.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B6447CD5-A614-E711-B6BB-FA163EEF542F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B6D22125-A614-E711-80AE-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B81D679C-A114-E711-957C-001E673C842D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B84B320D-B014-E711-BC47-001E67F8F6CD.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B8A7DA78-C214-E711-BBB2-001E6739D281.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/B8FFB74F-B114-E711-8B75-FA163E9E7E73.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BA236EF2-9114-E711-87DD-001E6739CFA9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BAE11474-A114-E711-9F70-001E6739B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BC6578C3-A414-E711-BA22-FA163EA2B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BC823F30-AE14-E711-92A5-FA163E01D887.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BCB8FF25-AE14-E711-8E03-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BCC29921-9B14-E711-9261-FA163EE0B622.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BCDE1A14-C514-E711-801A-001E673D2261.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BE6479C9-A114-E711-8DE5-FA163E94C2AC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BEA29345-B414-E711-A31C-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BEA29CA4-AB14-E711-9DBD-FA163EEF542F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/BEA76E74-B414-E711-8F3C-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C0471F7B-AB14-E711-B1CE-001E6739A959.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C050CF2B-9C14-E711-B89A-02163E00B514.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C052FDDA-C114-E711-B920-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C0999053-AB14-E711-A0BD-FA163E086F03.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C0A66328-A614-E711-B497-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C21C9BD6-9D14-E711-AB9E-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C23E142C-9914-E711-BA0E-FA163E234EB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C40B8DFC-A314-E711-9CE2-FA163E93AE87.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C480BAE6-C114-E711-906A-9CB65404ED04.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C491099E-AA14-E711-9A2E-001E6739AC59.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C4F136BE-AC14-E711-815F-FA163EEF542F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C4F1E644-AD14-E711-B29D-001E6739C2D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C607255E-9814-E711-93F1-001E673CFA89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C61E5BF8-B014-E711-9692-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C653C3B6-9614-E711-8956-FA163E09E6DF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C68BFF9F-A214-E711-900C-001E6739B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C6EEC002-B714-E711-B947-9CB654AEBE22.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C6F0B33B-AC14-E711-BC83-FA163E78A328.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/C82EFDC7-B914-E711-B634-9CB654AD7358.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CA27AA31-A814-E711-8F10-9CB65404FC30.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CA4009EF-9F14-E711-8212-001E67F8FA42.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CA56A13F-9214-E711-894D-FA163EEC1B84.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CAAC49ED-A414-E711-8C3E-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CAF159C6-B214-E711-8179-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CE2809A3-A014-E711-94DC-9CB65404FBA0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CE6386AD-A614-E711-8A6F-001E6739B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CEC25AE0-BD14-E711-BF3F-001E673C7EF4.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CEC6ACD2-9D14-E711-896A-001E673D2261.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/CEEC4100-A614-E711-8B16-FA163E006E46.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D2502601-CC14-E711-AE79-38EAA7A30576.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D26EDA76-9D14-E711-A575-02163E012E0C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D2962160-A414-E711-9116-38EAA7A30576.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D2E1F649-AE14-E711-8C8F-FA163E5E63FF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D41F5CCC-AE14-E711-91E0-02163E017632.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D635A553-AD14-E711-B5E6-FA163EE07709.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D648A859-AF14-E711-94C3-FA163E772A9F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D65A89C8-9814-E711-B052-001E67F8F763.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D6B25C15-A314-E711-A16C-02163E014C12.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D81D17C4-B314-E711-A2F7-FA163ECCE898.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/D83F3029-9114-E711-8C3D-FA163E772A9F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DA4D810E-AA14-E711-A3F4-001E6739A3F1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DAA07DE6-A514-E711-9659-FA163EF1B5D8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DAA1DF20-BD14-E711-AA74-FA163E4D17B5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DAD5C666-BB14-E711-BF4D-001E67F8FA15.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DAE998BD-9714-E711-92DE-001E673C7FB1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DAEBD45B-9D14-E711-B11C-FA163E3F4CDA.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DAF470D6-9B14-E711-B0EA-FA163E1DA852.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DC016926-9A14-E711-BB27-001E6739A411.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DC15CBDC-BD14-E711-96DB-001E673CFA89.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DC314179-AD14-E711-AEDE-38EAA7A6D65C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DC8D7A24-9F14-E711-8695-02163E00B514.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DC998F5C-C314-E711-93B2-001E6739C801.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DCD307F8-9814-E711-AA8B-FA163EEA4485.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DCF93ADA-B714-E711-9E71-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/DE021934-A714-E711-87F6-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E0311205-B614-E711-B3A9-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E0828EC3-A714-E711-96F8-FA163E04BE23.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E0E3BF23-A614-E711-8B5B-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E0EF30CB-B814-E711-BB8E-001E67FA3939.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E2248416-A214-E711-A5B8-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E2BED3E0-A714-E711-AEE2-FA163EE98D9B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E2CDF615-AA14-E711-A4F8-9CB654AEAC62.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E44467F6-9E14-E711-8E89-FA163EE0B622.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E44AC769-BB14-E711-920F-001E6739B871.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E465323E-AC14-E711-999C-FA163EEF542F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E47BBA19-C414-E711-B571-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E4E39776-BD14-E711-9480-001E67FA394D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E4F15891-C914-E711-90FE-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E4FEFB59-B014-E711-B190-FA163E5362C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E612D542-C914-E711-80B1-001E6739C2D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E61CEA1A-A014-E711-8CCC-001E6739AD61.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E629CDFF-9814-E711-A937-38EAA7A6D65C.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E64B372C-AE14-E711-B26E-FA163E01D887.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E671735B-A914-E711-B98E-FA163E8E3F3A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E6D6EF80-C014-E711-998F-9CB654AD7670.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E6FC32E3-9F14-E711-B320-9CB654AEBD56.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E856D75A-C314-E711-97F5-001E6739ABB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/E87EAB76-A614-E711-BBE7-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EA41EC25-A614-E711-BD92-001E6739B019.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EA953B28-A114-E711-9768-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EC06E4DD-A714-E711-9CEF-001E673C808A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EC1CD172-9214-E711-BFC7-FA163EF626F3.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EC8EB4E5-9714-E711-B057-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EC9256AF-AA14-E711-93BC-FA163E141358.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/ECD76751-BC14-E711-BB28-001E673D2EB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EE029A13-AA14-E711-A971-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EE0A5BE5-C314-E711-BA7C-001E6739C2D1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EE4B81A5-AB14-E711-A9D6-FA163E06ECEF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EE5F5049-A714-E711-BC79-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EE84D083-9014-E711-950A-FA163E09E6DF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EEA6E62C-B914-E711-8326-001E673D2EB9.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/EEC1009A-C614-E711-9582-9CB654AD72F8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F01D0EA5-AA14-E711-99B9-001E673CFC91.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F070B7BC-AA14-E711-8E92-FA163E5E63FF.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F0CAADDF-9B14-E711-8E84-001E673D0C31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F24F26A4-AA14-E711-A691-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F2AEFBCC-9814-E711-931C-FA163E92A9F5.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F2D12E35-A814-E711-AFE9-001E673D0C31.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F2DBBFFA-B014-E711-AA1E-FA163E5362C2.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F2F5FDE8-9214-E711-987F-FA163E3EDE47.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F40A71E4-B714-E711-AD4B-9CB654AEBE22.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F41ACF19-A114-E711-89B9-FA163E4468F1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F452C4E4-A314-E711-A7BC-001E67FA385D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F4AF2FD2-A714-E711-9690-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F65DC3C5-BB14-E711-8405-001E67FA394D.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F67BA055-A914-E711-8C01-001E6739A411.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F6DB2058-C614-E711-A975-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F83B4D57-9D14-E711-85FC-FA163E0D86FB.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F83BB016-A314-E711-B1F1-FA163EFB9DCC.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F89949D2-C714-E711-B29F-001E67FA38A8.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F8DFB929-A614-E711-BCF0-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/F8F6AA3A-B514-E711-A583-FA163E9B471F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/FA40BE1E-AE14-E711-9CF5-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/FC6DDBB6-A114-E711-A032-FA163E8E3F3A.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/FCA8A796-A114-E711-8C97-A0000220FE80.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/FCDA5B43-BE14-E711-A730-001E673C7FB1.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/FE029919-AE14-E711-A90D-001E673C8537.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/FE472E59-AD14-E711-827B-FA163E78A328.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/FEA1780F-AD14-E711-B664-FA163EE050D7.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/FEAE6BDE-BA14-E711-8D73-38EAA7A6DCF0.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/90000/FEBAC85D-C314-E711-B841-001E6739C159.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/18857EA5-7314-E711-9211-FA163E83C06F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/1E7C6524-7514-E711-9D90-FA163E6B8B99.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/28C2AF9F-7314-E711-BD2D-FA163E6B8B99.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/3E61CCC6-7514-E711-8A57-02163E01311F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/487DB19F-7314-E711-A614-FA163E6B8B99.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/5253715D-7514-E711-8E62-D4AE526A048B.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/62471F34-7414-E711-9AD0-02163E012F6E.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/88C9B19F-7314-E711-A83A-FA163E6B8B99.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/8A733B23-7414-E711-B6BA-FA163E83C06F.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/9EF0CDA5-7314-E711-AFF7-FA163E6B8B99.root', 
        '/store/mc/PhaseIFall16DR/GluGluHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/910000/D852DA9D-7314-E711-863D-FA163E83C06F.root' ) ),
    inputCommands = cms.untracked.vstring('keep *')
)
process.HLTConfigVersion = cms.PSet(
    tableName = cms.string('/dev/CMSSW_9_1_0/HLT/V8')
)

process.HLTIter0GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useHitsSplitting = cms.bool(False),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(4),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter1GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter1ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter1ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useHitsSplitting = cms.bool(False),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter2HighPtTkMuESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter2ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter3PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter3ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter3PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter3PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter4ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    minNrOfHitsForRebuild = cms.untracked.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter4PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkf3HitTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedCkfTrajectoryBuilderForHI = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHI')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(0.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHI')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(0.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedCkfTrajectoryFilterForHI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(0.701),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(0.701),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(8.0),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedStepTrajectoryFilterBase')
    ))
)

process.HLTPSetDetachedStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(2),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialCkfTrajectoryBuilderForHI = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialCkfTrajectoryFilterForHI')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetInitialCkfTrajectoryFilterForHI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBase')
    ))
)

process.HLTPSetInitialStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(2),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetJetCoreStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(1),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.05),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiEffTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(9),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(8),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(10.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryBuilderSeedHit = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(True)
)

process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonTrackingRegionBuilder8356 = cms.PSet(
    DeltaEta = cms.double(0.2),
    DeltaPhi = cms.double(0.2),
    DeltaR = cms.double(0.2),
    DeltaZ = cms.double(15.9),
    EtaR_UpperLimit_Par1 = cms.double(0.25),
    EtaR_UpperLimit_Par2 = cms.double(0.15),
    Eta_fixed = cms.bool(False),
    Eta_min = cms.double(0.1),
    MeasurementTrackerName = cms.InputTag("hltESPMeasurementTracker"),
    OnDemand = cms.int32(-1),
    PhiR_UpperLimit_Par1 = cms.double(0.6),
    PhiR_UpperLimit_Par2 = cms.double(0.2),
    Phi_fixed = cms.bool(False),
    Phi_min = cms.double(0.1),
    Pt_fixed = cms.bool(False),
    Pt_min = cms.double(1.5),
    Rescale_Dz = cms.double(3.0),
    Rescale_eta = cms.double(3.0),
    Rescale_phi = cms.double(3.0),
    UseVertex = cms.bool(False),
    Z_fixed = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    input = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    maxRegions = cms.int32(2),
    precise = cms.bool(True),
    vertexCollection = cms.InputTag("pixelVertices")
)

process.HLTPSetPixelLessStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelLessStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.05),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairCkfTrajectoryBuilderForHI = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHI')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHI')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelPairCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelPairCkfTrajectoryFilterForHI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(100),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(100),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(8.0),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelPairStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterBase')
    ))
)

process.HLTPSetPixelPairStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(2),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPvClusterComparer = cms.PSet(
    track_chi2_max = cms.double(9999999.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(10.0),
    track_pt_min = cms.double(2.5)
)

process.HLTPSetPvClusterComparerForBTag = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(0.1)
)

process.HLTPSetPvClusterComparerForIT = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(1.0)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilterBase')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilterBase')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryBuilderForElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryBuilderForGsfElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryFilterForElectrons = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(-1),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryFilterL3 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(1000000000),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.5),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(8),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTSeedFromConsecutiveHitsCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    propagator = cms.string('PropagatorWithMaterial')
)

process.HLTSeedFromConsecutiveHitsCreatorIT = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSeedFromProtoTracks = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSiStripClusterChargeCutForHI = cms.PSet(
    value = cms.double(2069.0)
)

process.HLTSiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.HLTSiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.HLTSiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.HLTSiStripClusterChargeCutTiny = cms.PSet(
    value = cms.double(800.0)
)

process.datasets = cms.PSet(
    AlCaElectron = cms.vstring('AlCa_DoubleEle_CaloIdL_TrackIdL_IsoVL_DZ_v6', 
        'AlCa_DoubleEle_CaloIdL_TrackIdL_IsoVL_v6', 
        'AlCa_SingleEle_WPVeryLoose_Gsf_v7'),
    AlCaLumiPixels = cms.vstring('AlCa_LumiPixels_Random_v2', 
        'AlCa_LumiPixels_ZeroBias_v5'),
    AlCaP0 = cms.vstring('AlCa_EcalEtaEBonly_v8', 
        'AlCa_EcalEtaEEonly_v8', 
        'AlCa_EcalPi0EBonly_v8', 
        'AlCa_EcalPi0EEonly_v8'),
    AlCaPhiSym = cms.vstring('AlCa_EcalPhiSym_v6'),
    BTagCSV = cms.vstring('HLT_AK4PFBJetBCSV60_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFBJetBCSV80_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFBJetBSSV60_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFBJetBSSV80_Eta2p1ForPPRef_v5', 
        'HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v5', 
        'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v5', 
        'HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v5', 
        'HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v5', 
        'HLT_DoubleJetsC100_SingleBTagCSV_p014_SinglePFJetC350_v5', 
        'HLT_DoubleJetsC100_SingleBTagCSV_p014_v3', 
        'HLT_DoubleJetsC100_SingleBTagCSV_p026_SinglePFJetC350_v5', 
        'HLT_DoubleJetsC100_SingleBTagCSV_p026_v3', 
        'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v5', 
        'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v5', 
        'HLT_QuadJet45_DoubleBTagCSV_p087_v6', 
        'HLT_QuadJet45_TripleBTagCSV_p087_v6', 
        'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v5', 
        'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v5', 
        'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v5', 
        'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v5', 
        'HLT_Rsq0p02_MR400_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200_v3', 
        'HLT_Rsq0p02_MR450_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200_v3', 
        'HLT_Rsq0p02_MR500_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200_v2', 
        'HLT_Rsq0p02_MR550_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200_v2'),
    BTagMu = cms.vstring('HLT_BTagMu_AK8Jet300_Mu5_v4', 
        'HLT_BTagMu_DiJet110_Mu5_v5', 
        'HLT_BTagMu_DiJet170_Mu5_v4', 
        'HLT_BTagMu_DiJet20_Mu5_v5', 
        'HLT_BTagMu_DiJet40_Mu5_v5', 
        'HLT_BTagMu_DiJet70_Mu5_v5', 
        'HLT_BTagMu_Jet300_Mu5_v5'),
    Charmonium = cms.vstring('HLT_Dimuon0_Jpsi_Muon_v5', 
        'HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v4', 
        'HLT_Dimuon13_PsiPrime_v6', 
        'HLT_Dimuon16_Jpsi_v6', 
        'HLT_Dimuon20_Jpsi_v6', 
        'HLT_Dimuon6_Jpsi_NoVertexing_v4', 
        'HLT_Dimuon8_PsiPrime_Barrel_v6', 
        'HLT_DoubleMu4_3_Bs_v7', 
        'HLT_DoubleMu4_3_Jpsi_Displaced_v7', 
        'HLT_DoubleMu4_JpsiTrk_Displaced_v7', 
        'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v7', 
        'HLT_Mu7p5_L2Mu2_Jpsi_v4', 
        'HLT_Mu7p5_Track2_Jpsi_v4', 
        'HLT_Mu7p5_Track3p5_Jpsi_v4', 
        'HLT_Mu7p5_Track7_Jpsi_v4', 
        'HLT_QuadMuon0_Dimuon0_Jpsi_v4'),
    Commissioning = cms.vstring('HLT_DiSC30_18_EIso_AND_HE_Mass70_v6', 
        'HLT_HcalIsolatedbunch_v2', 
        'HLT_IsoTrackHB_v3', 
        'HLT_IsoTrackHE_v3'),
    DisplacedJet = cms.vstring('HLT_HT200_v4', 
        'HLT_HT250_DisplacedDijet40_DisplacedTrack_v5', 
        'HLT_HT275_v4', 
        'HLT_HT325_v4', 
        'HLT_HT350_DisplacedDijet40_DisplacedTrack_v5', 
        'HLT_HT350_DisplacedDijet40_Inclusive_v4', 
        'HLT_HT350_DisplacedDijet80_DisplacedTrack_v5', 
        'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v5', 
        'HLT_HT425_v4', 
        'HLT_HT550_DisplacedDijet80_Inclusive_v2', 
        'HLT_HT575_v4', 
        'HLT_HT650_DisplacedDijet80_Inclusive_v5', 
        'HLT_HT750_DisplacedDijet80_Inclusive_v5', 
        'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v5', 
        'HLT_VBF_DisplacedJet40_DisplacedTrack_v5', 
        'HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v5', 
        'HLT_VBF_DisplacedJet40_TightID_Hadronic_v5', 
        'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v5', 
        'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v5', 
        'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v5', 
        'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v5'),
    DoubleEG = cms.vstring('HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v7', 
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v7', 
        'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70_v7', 
        'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v7', 
        'HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55_v7', 
        'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v8', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v10', 
        'HLT_DoubleEle33_CaloIdL_MW_v8', 
        'HLT_DoubleEle33_CaloIdL_v7', 
        'HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL_v7', 
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v10', 
        'HLT_DoublePhoton60_v7', 
        'HLT_DoublePhoton85_v8', 
        'HLT_ECALHT800_v6', 
        'HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV_p13_v7', 
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v9', 
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v8', 
        'HLT_Ele12_CaloIdM_TrackIdM_PFJet30_v9', 
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v8', 
        'HLT_Ele17_CaloIdL_GsfTrkIdVL_v6', 
        'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30_v7', 
        'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v7', 
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v7', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v9', 
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v8', 
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v9', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_L1JetTauSeeded_v3', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Ele27_HighEta_Ele20_Mass55_v8', 
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v7', 
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v9', 
        'HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60_v9', 
        'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15_v9', 
        'HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15_v9'),
    DoubleMuon = cms.vstring('HLT_DoubleMu0_v2', 
        'HLT_DoubleMu18NoFiltersNoVtx_v5', 
        'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v5', 
        'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v5', 
        'HLT_DoubleMu33NoFiltersNoVtx_v5', 
        'HLT_DoubleMu38NoFiltersNoVtx_v5', 
        'HLT_DoubleMu8_Mass8_PFHT300_v9', 
        'HLT_HIL1DoubleMu0ForPPRef_v2', 
        'HLT_HIL1DoubleMu10ForPPRef_v2', 
        'HLT_HIL2DoubleMu0_NHitQForPPRef_v3', 
        'HLT_HIL3DoubleMu0_OS_m2p5to4p5ForPPRef_v3', 
        'HLT_HIL3DoubleMu0_OS_m7to14ForPPRef_v3', 
        'HLT_L2DoubleMu23_NoVertex_v6', 
        'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v6', 
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v6', 
        'HLT_Mu10_CentralPFJet30_BTagCSV_p13_v5', 
        'HLT_Mu17_Mu8_DZ_v7', 
        'HLT_Mu17_Mu8_SameSign_DZ_v6', 
        'HLT_Mu17_Mu8_SameSign_v5', 
        'HLT_Mu17_Mu8_v5', 
        'HLT_Mu17_TkMu8_DZ_v6', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v7', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v6', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v6', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v5', 
        'HLT_Mu17_TrkIsoVVL_v4', 
        'HLT_Mu17_v4', 
        'HLT_Mu20_Mu10_DZ_v6', 
        'HLT_Mu20_Mu10_SameSign_DZ_v6', 
        'HLT_Mu20_Mu10_SameSign_v4', 
        'HLT_Mu20_Mu10_v5', 
        'HLT_Mu27_TkMu8_v5', 
        'HLT_Mu30_TkMu11_v5', 
        'HLT_Mu3_PFJet40_v6', 
        'HLT_Mu40_TkMu11_v5', 
        'HLT_Mu8_TrkIsoVVL_v5', 
        'HLT_Mu8_v5', 
        'HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v3', 
        'HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v3', 
        'HLT_TripleMu_12_10_5_v4', 
        'HLT_TripleMu_5_3_3_DZ_Mass3p8_v1', 
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v6', 
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v6'),
    DoubleMuonLowMass = cms.vstring('HLT_DoubleMu3_Trk_Tau3mu_v4', 
        'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v7'),
    EcalLaser = cms.vstring('HLT_EcalCalibration_v3'),
    EmptyBX = cms.vstring('HLT_L1BptxMinus_v2', 
        'HLT_L1BptxPlus_v2', 
        'HLT_L1NotBptxOR_v2'),
    EventDisplay = cms.vstring('HLT_AK4PFJet100_v7', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v10', 
        'HLT_DoublePhoton85_v8', 
        'HLT_HISinglePhoton60_v4', 
        'HLT_Mu40_TkMu11_v5', 
        'HLT_PFJet500_v9', 
        'HLT_PFMET170_HBHECleaned_v9'),
    ExpressPhysics = cms.vstring('HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9', 
        'HLT_Ele250_CaloIdVT_GsfTrkIdT_v6', 
        'HLT_Ele300_CaloIdVT_GsfTrkIdT_v6', 
        'HLT_HIL1DoubleMu0ForPPRef_v2', 
        'HLT_HT2000_v5', 
        'HLT_HT2500_v5', 
        'HLT_IsoMu20_v6', 
        'HLT_IsoMu24_v4', 
        'HLT_L1FatEvents_v2', 
        'HLT_L1MinimumBiasHF1AND_v2', 
        'HLT_MET600_v5', 
        'HLT_MET700_v5', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v7', 
        'HLT_Mu300_v3', 
        'HLT_Mu350_v3', 
        'HLT_PFMET500_v7', 
        'HLT_PFMET600_v7', 
        'HLT_Photon500_v6', 
        'HLT_Photon600_v6', 
        'HLT_Physics_v5', 
        'HLT_Random_v2', 
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_copy_v1', 
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v3', 
        'HLT_ZeroBias_IsolatedBunches_v3', 
        'HLT_ZeroBias_v4'),
    FSQJets = cms.vstring('HLT_DiPFJet15_FBEta3_NoCaloMatched_v6', 
        'HLT_DiPFJet15_NoCaloMatched_v5', 
        'HLT_DiPFJet25_FBEta3_NoCaloMatched_v6', 
        'HLT_DiPFJet25_NoCaloMatched_v5', 
        'HLT_DiPFJetAve15_HFJEC_v6', 
        'HLT_DiPFJetAve25_HFJEC_v6', 
        'HLT_DiPFJetAve35_HFJEC_v6', 
        'HLT_PFJet15_NoCaloMatched_v7', 
        'HLT_PFJet25_NoCaloMatched_v5'),
    FullTrack = cms.vstring('HLT_FullTrack18ForPPRef_v4', 
        'HLT_FullTrack24ForPPRef_v4', 
        'HLT_FullTrack34ForPPRef_v4', 
        'HLT_FullTrack45ForPPRef_v4', 
        'HLT_FullTrack53ForPPRef_v4'),
    HINCaloJets = cms.vstring('HLT_AK4CaloJet100_v4', 
        'HLT_AK4CaloJet30_v5', 
        'HLT_AK4CaloJet40_v4', 
        'HLT_AK4CaloJet50_v4', 
        'HLT_AK4CaloJet80_v4'),
    HINPFJets = cms.vstring('HLT_AK4PFJet100_v7', 
        'HLT_AK4PFJet30_v7', 
        'HLT_AK4PFJet50_v7', 
        'HLT_AK4PFJet80_v7'),
    HINPhoton = cms.vstring('HLT_HISinglePhoton10_v4', 
        'HLT_HISinglePhoton15_v4', 
        'HLT_HISinglePhoton20_v4', 
        'HLT_HISinglePhoton40_v4', 
        'HLT_HISinglePhoton60_v4'),
    HLTMonitor = cms.vstring('HLT_DiPFJetAve40_v8', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9', 
        'HLT_Ele27_WPTight_Gsf_v7', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v8', 
        'HLT_PFHT350_v8', 
        'HLT_PFMET120_PFMHT120_IDTight_v8', 
        'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v5', 
        'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v5', 
        'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v5', 
        'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v5', 
        'HLT_QuadPFJet_VBF_v8'),
    HLTPhysics = cms.vstring('HLT_L1FatEvents_v2', 
        'HLT_Physics_v5'),
    HLTPhysics0 = cms.vstring('HLT_L1FatEvents_part0_v1'),
    HLTPhysics1 = cms.vstring('HLT_L1FatEvents_part1_v1'),
    HLTPhysics2 = cms.vstring('HLT_L1FatEvents_part2_v1'),
    HLTPhysics3 = cms.vstring('HLT_L1FatEvents_part3_v1'),
    HTMHT = cms.vstring('HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v6', 
        'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80_v5', 
        'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v8', 
        'HLT_PFHT200_PFAlphaT0p51_v8', 
        'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v8', 
        'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v8', 
        'HLT_PFHT300_PFMET110_v6', 
        'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v8', 
        'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v8', 
        'HLT_Rsq0p25_v6', 
        'HLT_Rsq0p30_v6', 
        'HLT_RsqMR270_Rsq0p09_MR200_4jet_v6', 
        'HLT_RsqMR270_Rsq0p09_MR200_v6'),
    HcalHPDNoise = cms.vstring('HLT_GlobalRunHPDNoise_v4'),
    HcalNZS = cms.vstring('HLT_HcalNZS_v10', 
        'HLT_HcalPhiSym_v11'),
    HeavyFlavor = cms.vstring('HLT_DmesonPPTrackingGlobal_Dpt15ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt20ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt30ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt40ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt50ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt60ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt8ForPPRef_v4'),
    HighMultiplicity = cms.vstring('HLT_PixelTracks_Multiplicity110ForPPRef_v2', 
        'HLT_PixelTracks_Multiplicity135ForPPRef_v2', 
        'HLT_PixelTracks_Multiplicity160ForPPRef_v2', 
        'HLT_PixelTracks_Multiplicity60ForPPRef_v2', 
        'HLT_PixelTracks_Multiplicity85ForPPRef_v2'),
    HighMultiplicityEOF = cms.vstring('HLT_FullTracks_Multiplicity100_v5', 
        'HLT_FullTracks_Multiplicity130_v5', 
        'HLT_FullTracks_Multiplicity150_v5', 
        'HLT_FullTracks_Multiplicity80_v4'),
    HighPtJet80 = cms.vstring('HLT_AK4CaloJet100_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet100_Jet35_Eta0p7ForPPRef_v3', 
        'HLT_AK4CaloJet100_Jet35_Eta1p1ForPPRef_v3', 
        'HLT_AK4CaloJet110_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet120_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet150ForPPRef_v3', 
        'HLT_AK4CaloJet80_45_45_Eta2p1ForPPRef_v3', 
        'HLT_AK4CaloJet80_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet80_Jet35_Eta0p7ForPPRef_v3', 
        'HLT_AK4CaloJet80_Jet35_Eta1p1ForPPRef_v3', 
        'HLT_AK4PFJet100_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet110_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet120_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet80_Eta5p1ForPPRef_v5'),
    HighPtLowerJets = cms.vstring('HLT_AK4CaloJet40_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet60_Eta5p1ForPPRef_v3', 
        'HLT_AK4PFJet40_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet60_Eta5p1ForPPRef_v5'),
    HighPtLowerPhotons = cms.vstring('HLT_HISinglePhoton10_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton10_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton15_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton15_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton20_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton20_Eta3p1ForPPRef_v3'),
    HighPtPhoton30AndZ = cms.vstring('HLT_HIDoublePhoton15_Eta1p5_Mass50_1000ForPPRef_v3', 
        'HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_R9HECutForPPRef_v3', 
        'HLT_HIDoublePhoton15_Eta2p1_Mass50_1000_R9CutForPPRef_v3', 
        'HLT_HIDoublePhoton15_Eta2p5_Mass50_1000_R9SigmaHECutForPPRef_v3', 
        'HLT_HISinglePhoton30_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton30_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton40_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton40_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton50_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton50_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton60_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton60_Eta3p1ForPPRef_v3'),
    JetHT = cms.vstring('HLT_AK4PFDJet60_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFDJet80_Eta2p1ForPPRef_v5', 
        'HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v5', 
        'HLT_AK8DiPFJet250_200_TrimMass30_v5', 
        'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p087_v1', 
        'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v5', 
        'HLT_AK8DiPFJet280_200_TrimMass30_v5', 
        'HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p087_v1', 
        'HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p20_v1', 
        'HLT_AK8DiPFJet300_200_TrimMass30_v1', 
        'HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v6', 
        'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v7', 
        'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v8', 
        'HLT_AK8PFHT750_TrimMass50_v1', 
        'HLT_AK8PFHT800_TrimMass50_v1', 
        'HLT_AK8PFJet140_v4', 
        'HLT_AK8PFJet200_v4', 
        'HLT_AK8PFJet260_v5', 
        'HLT_AK8PFJet320_v5', 
        'HLT_AK8PFJet360_TrimMass30_v7', 
        'HLT_AK8PFJet400_TrimMass30_v1', 
        'HLT_AK8PFJet400_v5', 
        'HLT_AK8PFJet40_v5', 
        'HLT_AK8PFJet450_v5', 
        'HLT_AK8PFJet500_v5', 
        'HLT_AK8PFJet60_v4', 
        'HLT_AK8PFJet80_v4', 
        'HLT_CaloJet500_NoJetID_v5', 
        'HLT_DiCentralPFJet170_CFMax0p1_v5', 
        'HLT_DiCentralPFJet170_v5', 
        'HLT_DiCentralPFJet330_CFMax0p5_v5', 
        'HLT_DiCentralPFJet430_v5', 
        'HLT_DiJetVBFMu_PassThrough_v1', 
        'HLT_DiJetVBF_PassThrough_v1', 
        'HLT_DiPFJetAve100_HFJEC_v8', 
        'HLT_DiPFJetAve140_v7', 
        'HLT_DiPFJetAve160_HFJEC_v8', 
        'HLT_DiPFJetAve200_v7', 
        'HLT_DiPFJetAve220_HFJEC_v9', 
        'HLT_DiPFJetAve260_v8', 
        'HLT_DiPFJetAve300_HFJEC_v9', 
        'HLT_DiPFJetAve320_v8', 
        'HLT_DiPFJetAve400_v8', 
        'HLT_DiPFJetAve40_v8', 
        'HLT_DiPFJetAve500_v8', 
        'HLT_DiPFJetAve60_HFJEC_v8', 
        'HLT_DiPFJetAve60_v8', 
        'HLT_DiPFJetAve80_HFJEC_v8', 
        'HLT_DiPFJetAve80_v7', 
        'HLT_HT2000_v5', 
        'HLT_HT2500_v5', 
        'HLT_L1_TripleJet_VBF_v5', 
        'HLT_PFHT125_v5', 
        'HLT_PFHT200_v6', 
        'HLT_PFHT250_v6', 
        'HLT_PFHT300_v7', 
        'HLT_PFHT350_v8', 
        'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v6', 
        'HLT_PFHT400_SixJet30_v8', 
        'HLT_PFHT400_v7', 
        'HLT_PFHT450_SixJet40_BTagCSV_p056_v6', 
        'HLT_PFHT450_SixJet40_v8', 
        'HLT_PFHT475_v7', 
        'HLT_PFHT550_4JetPt50_v6', 
        'HLT_PFHT600_v8', 
        'HLT_PFHT650_4JetPt50_v6', 
        'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v8', 
        'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v8', 
        'HLT_PFHT650_v8', 
        'HLT_PFHT750_4JetPt70_v2', 
        'HLT_PFHT750_4JetPt80_v2', 
        'HLT_PFHT800_4JetPt50_v2', 
        'HLT_PFHT850_4JetPt50_v2', 
        'HLT_PFHT900_v6', 
        'HLT_PFJet140_v8', 
        'HLT_PFJet200_v8', 
        'HLT_PFJet260_v9', 
        'HLT_PFJet320_v9', 
        'HLT_PFJet400_v9', 
        'HLT_PFJet40_v9', 
        'HLT_PFJet450_v9', 
        'HLT_PFJet500_v9', 
        'HLT_PFJet60_v9', 
        'HLT_PFJet80_v8', 
        'HLT_QuadPFJet_VBF_v8', 
        'HLT_SingleCentralPFJet170_CFMax0p1_v5'),
    L1Accept = cms.vstring('DST_Physics_v5'),
    L1MinimumBias = cms.vstring('HLT_L1MinimumBiasHF1AND_v2', 
        'HLT_L1MinimumBiasHF1OR_v2', 
        'HLT_L1MinimumBiasHF2AND_v2', 
        'HLT_L1MinimumBiasHF2ORNoBptxGating_v3', 
        'HLT_L1MinimumBiasHF2OR_v2', 
        'HLT_L1MinimumBiasHF_AND_v2'),
    L1MinimumBias0 = cms.vstring('HLT_L1MinimumBiasHF_OR_part0_v2'),
    L1MinimumBias1 = cms.vstring('HLT_L1MinimumBiasHF_OR_part1_v2'),
    L1MinimumBias2 = cms.vstring('HLT_L1MinimumBiasHF_OR_part2_v2'),
    L1MinimumBias3 = cms.vstring('HLT_L1MinimumBiasHF_OR_part3_v2'),
    L1MinimumBias4 = cms.vstring('HLT_L1MinimumBiasHF_OR_part4_v2'),
    L1MinimumBias5 = cms.vstring('HLT_L1MinimumBiasHF_OR_part5_v2'),
    L1MinimumBias6 = cms.vstring('HLT_L1MinimumBiasHF_OR_part6_v2'),
    L1MinimumBias7 = cms.vstring('HLT_L1MinimumBiasHF_OR_part7_v2'),
    L1MinimumBias8 = cms.vstring('HLT_L1MinimumBiasHF_OR_part8_v2'),
    L1MinimumBias9 = cms.vstring('HLT_L1MinimumBiasHF_OR_part9_v2'),
    MET = cms.vstring('HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v7', 
        'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v8', 
        'HLT_DoubleMu3_PFMET50_v6', 
        'HLT_MET200_v5', 
        'HLT_MET250_v5', 
        'HLT_MET300_v5', 
        'HLT_MET600_v5', 
        'HLT_MET60_IsoTrk35_Loose_v3', 
        'HLT_MET700_v5', 
        'HLT_MET75_IsoTrk50_v6', 
        'HLT_MET90_IsoTrk50_v6', 
        'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v8', 
        'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v8', 
        'HLT_Mu6_PFHT200_PFMET100_v5', 
        'HLT_PFMET110_PFMHT110_IDTight_v8', 
        'HLT_PFMET120_PFMHT120_IDTight_v8', 
        'HLT_PFMET170_BeamHaloCleaned_v7', 
        'HLT_PFMET170_HBHECleaned_v9', 
        'HLT_PFMET170_HBHE_BeamHaloCleaned_v5', 
        'HLT_PFMET170_NotCleaned_v8', 
        'HLT_PFMET300_v7', 
        'HLT_PFMET400_v7', 
        'HLT_PFMET500_v7', 
        'HLT_PFMET600_v7', 
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v8', 
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v8', 
        'HLT_PFMETTypeOne190_HBHE_BeamHaloCleaned_v5'),
    MonteCarlo = cms.vstring('MC_AK4CaloJetsFromPV_v1', 
        'MC_AK4CaloJets_v3', 
        'MC_AK4PFJets_v6', 
        'MC_AK8CaloHT_v3', 
        'MC_AK8PFHT_v6', 
        'MC_AK8PFJets_v6', 
        'MC_AK8TrimPFJets_v6', 
        'MC_CaloBTagCSV_v1', 
        'MC_CaloHT_v3', 
        'MC_CaloMET_JetIdCleaned_v3', 
        'MC_CaloMET_v3', 
        'MC_CaloMHT_v3', 
        'MC_Diphoton10_10_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass10_v6', 
        'MC_DoubleEle5_CaloIdL_GsfTrkIdVL_MW_v6', 
        'MC_DoubleGlbTrkMu_TrkIsoVVL_DZ_v4', 
        'MC_DoubleL1Tau_MediumIsoPFTau32_Trk1_eta2p1_Reg_v6', 
        'MC_DoubleMuNoFiltersNoVtx_v3', 
        'MC_DoubleMu_TrkIsoVVL_DZ_v4', 
        'MC_Ele15_Ele10_CaloIdL_TrackIdL_IsoVL_DZ_v7', 
        'MC_Ele5_WPLoose_Gsf_v8', 
        'MC_IsoMu_v7', 
        'MC_IsoTkMu15_v6', 
        'MC_LooseIsoPFTau20_v5', 
        'MC_LooseIsoPFTau50_Trk30_eta2p1_v4', 
        'MC_PFBTagCSV_v1', 
        'MC_PFHT_v6', 
        'MC_PFMET_v6', 
        'MC_PFMHT_v6', 
        'MC_ReducedIterativeTracking_v3'),
    MuOnia = cms.vstring('HLT_Dimuon0_Phi_Barrel_v6', 
        'HLT_Dimuon0_Upsilon_Muon_v5', 
        'HLT_Dimuon13_Upsilon_v6', 
        'HLT_Dimuon8_Upsilon_Barrel_v6', 
        'HLT_Mu25_TkMu0_dEta18_Onia_v6', 
        'HLT_Mu7p5_L2Mu2_Upsilon_v4', 
        'HLT_Mu7p5_Track2_Upsilon_v4', 
        'HLT_Mu7p5_Track3p5_Upsilon_v4', 
        'HLT_Mu7p5_Track7_Upsilon_v4', 
        'HLT_QuadMuon0_Dimuon0_Upsilon_v4'),
    MuPlusX = cms.vstring('HLT_HIL2Mu3Eta2p5_AK4CaloJet100Eta2p1ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet40Eta2p1ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet60Eta2p1ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet80Eta2p1ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton30Eta1p5ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton40Eta1p5ForPPRef_v4'),
    MuonEG = cms.vstring('HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v8', 
        'HLT_Mu12_Photon25_CaloIdL_L1ISO_v8', 
        'HLT_Mu12_Photon25_CaloIdL_L1OR_v8', 
        'HLT_Mu12_Photon25_CaloIdL_v8', 
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v4', 
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v3', 
        'HLT_Mu17_Photon30_CaloIdL_L1ISO_v9', 
        'HLT_Mu17_Photon35_CaloIdL_L1ISO_v9', 
        'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL_v7', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v4', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v3', 
        'HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL_v6', 
        'HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v7', 
        'HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL_v7', 
        'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL_v3', 
        'HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL_v6', 
        'HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v7', 
        'HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL_v7', 
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v9', 
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v10', 
        'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v4'),
    NoBPTX = cms.vstring('HLT_JetE30_NoBPTX3BX_v4', 
        'HLT_JetE30_NoBPTX_v4', 
        'HLT_JetE50_NoBPTX3BX_v4', 
        'HLT_JetE70_NoBPTX3BX_v4', 
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v2', 
        'HLT_L2Mu10_NoVertex_NoBPTX_v3', 
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v2', 
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v1'),
    OnlineMonitor = cms.vstring( ('DST_CaloJet40_BTagScouting_v7', 
        'DST_CaloJet40_CaloBTagScouting_v6', 
        'DST_CaloJet40_CaloScouting_PFScouting_v7', 
        'DST_DoubleMu3_Mass10_BTagScouting_v8', 
        'DST_DoubleMu3_Mass10_CaloScouting_PFScouting_v7', 
        'DST_HT250_CaloBTagScouting_v3', 
        'DST_HT250_CaloScouting_v5', 
        'DST_HT410_BTagScouting_v7', 
        'DST_HT410_PFScouting_v7', 
        'DST_HT450_BTagScouting_v7', 
        'DST_HT450_PFScouting_v7', 
        'DST_L1DoubleMu_BTagScouting_v8', 
        'DST_L1DoubleMu_CaloScouting_PFScouting_v7', 
        'DST_L1HTT_BTagScouting_v7', 
        'DST_L1HTT_CaloBTagScouting_v6', 
        'DST_L1HTT_CaloScouting_PFScouting_v7', 
        'DST_ZeroBias_BTagScouting_v7', 
        'DST_ZeroBias_CaloScouting_PFScouting_v6', 
        'HLT_AK4CaloJet100_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet100_Jet35_Eta0p7ForPPRef_v3', 
        'HLT_AK4CaloJet100_Jet35_Eta1p1ForPPRef_v3', 
        'HLT_AK4CaloJet100_v4', 
        'HLT_AK4CaloJet110_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet120_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet150ForPPRef_v3', 
        'HLT_AK4CaloJet30_v5', 
        'HLT_AK4CaloJet40_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet40_v4', 
        'HLT_AK4CaloJet50_v4', 
        'HLT_AK4CaloJet60_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet80_45_45_Eta2p1ForPPRef_v3', 
        'HLT_AK4CaloJet80_Eta5p1ForPPRef_v3', 
        'HLT_AK4CaloJet80_Jet35_Eta0p7ForPPRef_v3', 
        'HLT_AK4CaloJet80_Jet35_Eta1p1ForPPRef_v3', 
        'HLT_AK4CaloJet80_v4', 
        'HLT_AK4PFBJetBCSV60_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFBJetBCSV80_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFBJetBSSV60_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFBJetBSSV80_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFDJet60_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFDJet80_Eta2p1ForPPRef_v5', 
        'HLT_AK4PFJet100_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet100_v7', 
        'HLT_AK4PFJet110_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet120_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet30_v7', 
        'HLT_AK4PFJet40_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet50_v7', 
        'HLT_AK4PFJet60_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet80_Eta5p1ForPPRef_v5', 
        'HLT_AK4PFJet80_v7', 
        'HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v5', 
        'HLT_AK8DiPFJet250_200_TrimMass30_v5', 
        'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p087_v1', 
        'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v5', 
        'HLT_AK8DiPFJet280_200_TrimMass30_v5', 
        'HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p087_v1', 
        'HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p20_v1', 
        'HLT_AK8DiPFJet300_200_TrimMass30_v1', 
        'HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v6', 
        'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v7', 
        'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v8', 
        'HLT_AK8PFHT750_TrimMass50_v1', 
        'HLT_AK8PFHT800_TrimMass50_v1', 
        'HLT_AK8PFJet140_v4', 
        'HLT_AK8PFJet200_v4', 
        'HLT_AK8PFJet260_v5', 
        'HLT_AK8PFJet320_v5', 
        'HLT_AK8PFJet360_TrimMass30_v7', 
        'HLT_AK8PFJet400_TrimMass30_v1', 
        'HLT_AK8PFJet400_v5', 
        'HLT_AK8PFJet40_v5', 
        'HLT_AK8PFJet450_v5', 
        'HLT_AK8PFJet500_v5', 
        'HLT_AK8PFJet60_v4', 
        'HLT_AK8PFJet80_v4', 
        'HLT_BTagMu_AK8Jet300_Mu5_v4', 
        'HLT_BTagMu_DiJet110_Mu5_v5', 
        'HLT_BTagMu_DiJet170_Mu5_v4', 
        'HLT_BTagMu_DiJet20_Mu5_v5', 
        'HLT_BTagMu_DiJet40_Mu5_v5', 
        'HLT_BTagMu_DiJet70_Mu5_v5', 
        'HLT_BTagMu_Jet300_Mu5_v5', 
        'HLT_CaloJet500_NoJetID_v5', 
        'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v7', 
        'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v8', 
        'HLT_DiCentralPFJet170_CFMax0p1_v5', 
        'HLT_DiCentralPFJet170_v5', 
        'HLT_DiCentralPFJet330_CFMax0p5_v5', 
        'HLT_DiCentralPFJet430_v5', 
        'HLT_DiJetVBFMu_PassThrough_v1', 
        'HLT_DiJetVBF_PassThrough_v1', 
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v8', 
        'HLT_DiPFJet15_FBEta3_NoCaloMatched_v6', 
        'HLT_DiPFJet15_NoCaloMatched_v5', 
        'HLT_DiPFJet25_FBEta3_NoCaloMatched_v6', 
        'HLT_DiPFJet25_NoCaloMatched_v5', 
        'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v6', 
        'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80_v5', 
        'HLT_DiPFJetAve100_HFJEC_v8', 
        'HLT_DiPFJetAve140_v7', 
        'HLT_DiPFJetAve15_HFJEC_v6', 
        'HLT_DiPFJetAve160_HFJEC_v8', 
        'HLT_DiPFJetAve200_v7', 
        'HLT_DiPFJetAve220_HFJEC_v9', 
        'HLT_DiPFJetAve25_HFJEC_v6', 
        'HLT_DiPFJetAve260_v8', 
        'HLT_DiPFJetAve300_HFJEC_v9', 
        'HLT_DiPFJetAve320_v8', 
        'HLT_DiPFJetAve35_HFJEC_v6', 
        'HLT_DiPFJetAve400_v8', 
        'HLT_DiPFJetAve40_v8', 
        'HLT_DiPFJetAve500_v8', 
        'HLT_DiPFJetAve60_HFJEC_v8', 
        'HLT_DiPFJetAve60_v8', 
        'HLT_DiPFJetAve80_HFJEC_v8', 
        'HLT_DiPFJetAve80_v7', 
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v6', 
        'HLT_Dimuon0_Jpsi_Muon_v5', 
        'HLT_Dimuon0_Phi_Barrel_v6', 
        'HLT_Dimuon0_Upsilon_Muon_v5', 
        'HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v4', 
        'HLT_Dimuon13_PsiPrime_v6', 
        'HLT_Dimuon13_Upsilon_v6', 
        'HLT_Dimuon16_Jpsi_v6', 
        'HLT_Dimuon20_Jpsi_v6', 
        'HLT_Dimuon6_Jpsi_NoVertexing_v4', 
        'HLT_Dimuon8_PsiPrime_Barrel_v6', 
        'HLT_Dimuon8_Upsilon_Barrel_v6', 
        'HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v7', 
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v7', 
        'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70_v7', 
        'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v7', 
        'HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55_v7', 
        'HLT_DmesonPPTrackingGlobal_Dpt15ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt20ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt30ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt40ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt50ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt60ForPPRef_v4', 
        'HLT_DmesonPPTrackingGlobal_Dpt8ForPPRef_v4', 
        'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v8', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v10', 
        'HLT_DoubleEle33_CaloIdL_MW_v8', 
        'HLT_DoubleEle33_CaloIdL_v7', 
        'HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL_v7', 
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v10', 
        'HLT_DoubleIsoMu17_eta2p1_noDzCut_v5', 
        'HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v5', 
        'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v5', 
        'HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v5', 
        'HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v5', 
        'HLT_DoubleJetsC100_SingleBTagCSV_p014_SinglePFJetC350_v5', 
        'HLT_DoubleJetsC100_SingleBTagCSV_p014_v3', 
        'HLT_DoubleJetsC100_SingleBTagCSV_p026_SinglePFJetC350_v5', 
        'HLT_DoubleJetsC100_SingleBTagCSV_p026_v3', 
        'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v5', 
        'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v5', 
        'HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v3', 
        'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg_v2', 
        'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_v2', 
        'HLT_DoubleMu0_v2', 
        'HLT_DoubleMu18NoFiltersNoVtx_v5', 
        'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v5', 
        'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v5', 
        'HLT_DoubleMu33NoFiltersNoVtx_v5', 
        'HLT_DoubleMu38NoFiltersNoVtx_v5', 
        'HLT_DoubleMu3_PFMET50_v6', 
        'HLT_DoubleMu3_Trk_Tau3mu_v4', 
        'HLT_DoubleMu4_3_Bs_v7', 
        'HLT_DoubleMu4_3_Jpsi_Displaced_v7', 
        'HLT_DoubleMu4_JpsiTrk_Displaced_v7', 
        'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v7', 
        'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v7', 
        'HLT_DoubleMu8_Mass8_PFHT300_v9', 
        'HLT_DoublePhoton60_v7', 
        'HLT_DoublePhoton85_v8', 
        'HLT_DoubleTightCombinedIsoPFTau35_Trk1_eta2p1_Reg_v3', 
        'HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1_Reg_v2', 
        'HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1_v2', 
        'HLT_ECALHT800_v6', 
        'HLT_Ele105_CaloIdVT_GsfTrkIdT_v8', 
        'HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV_p13_v7', 
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v7', 
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v9', 
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v8', 
        'HLT_Ele12_CaloIdM_TrackIdM_PFJet30_v9', 
        'HLT_Ele145_CaloIdVT_GsfTrkIdT_v1', 
        'HLT_Ele15_IsoVVVL_BTagCSV_p067_PFHT400_v7', 
        'HLT_Ele15_IsoVVVL_PFHT400_PFMET50_v6', 
        'HLT_Ele15_IsoVVVL_PFHT400_v6', 
        'HLT_Ele15_IsoVVVL_PFHT600_v9', 
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v8', 
        'HLT_Ele17_CaloIdL_GsfTrkIdVL_v6', 
        'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30_v7', 
        'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v7', 
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v7', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Ele200_CaloIdVT_GsfTrkIdT_v1', 
        'HLT_Ele20_eta2p1_WPLoose_Gsf_LooseIsoPFTau28_v3', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau29_v3', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_v9', 
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v9', 
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v8', 
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v9', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_L1JetTauSeeded_v3', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v4', 
        'HLT_Ele250_CaloIdVT_GsfTrkIdT_v6', 
        'HLT_Ele25_WPTight_Gsf_v7', 
        'HLT_Ele25_eta2p1_WPTight_Gsf_v7', 
        'HLT_Ele27_HighEta_Ele20_Mass55_v8', 
        'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v9', 
        'HLT_Ele27_WPTight_Gsf_L1JetTauSeeded_v4', 
        'HLT_Ele27_WPTight_Gsf_v7', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v10', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v8', 
        'HLT_Ele27_eta2p1_WPTight_Gsf_v8', 
        'HLT_Ele300_CaloIdVT_GsfTrkIdT_v6', 
        'HLT_Ele30_WPTight_Gsf_v1', 
        'HLT_Ele30_eta2p1_WPTight_Gsf_v1', 
        'HLT_Ele32_WPTight_Gsf_v1', 
        'HLT_Ele32_eta2p1_WPTight_Gsf_v8', 
        'HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v3', 
        'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v9', 
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v7', 
        'HLT_Ele50_IsoVVVL_PFHT400_v6', 
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v7', 
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v9', 
        'HLT_FullTrack18ForPPRef_v4', 
        'HLT_FullTrack24ForPPRef_v4', 
        'HLT_FullTrack34ForPPRef_v4', 
        'HLT_FullTrack45ForPPRef_v4', 
        'HLT_FullTrack53ForPPRef_v4', 
        'HLT_FullTracks_Multiplicity100_v5', 
        'HLT_FullTracks_Multiplicity130_v5', 
        'HLT_FullTracks_Multiplicity150_v5', 
        'HLT_FullTracks_Multiplicity80_v4', 
        'HLT_GlobalRunHPDNoise_v4', 
        'HLT_HICastorMediumJetPixel_SingleTrackForPPRef_v2', 
        'HLT_HIDoublePhoton15_Eta1p5_Mass50_1000ForPPRef_v3', 
        'HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_R9HECutForPPRef_v3', 
        'HLT_HIDoublePhoton15_Eta2p1_Mass50_1000_R9CutForPPRef_v3', 
        'HLT_HIDoublePhoton15_Eta2p5_Mass50_1000_R9SigmaHECutForPPRef_v3', 
        'HLT_HIL1CastorMediumJetForPPRef_v2', 
        'HLT_HIL1DoubleMu0ForPPRef_v2', 
        'HLT_HIL1DoubleMu10ForPPRef_v2', 
        'HLT_HIL2DoubleMu0_NHitQForPPRef_v3', 
        'HLT_HIL2Mu15ForPPRef_v3', 
        'HLT_HIL2Mu20ForPPRef_v3', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet100Eta2p1ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet40Eta2p1ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet60Eta2p1ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet80Eta2p1ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5ForPPRef_v4', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5ForPPRef_v4', 
        'HLT_HIL2Mu3_NHitQ10ForPPRef_v3', 
        'HLT_HIL2Mu5_NHitQ10ForPPRef_v3', 
        'HLT_HIL2Mu7_NHitQ10ForPPRef_v3', 
        'HLT_HIL3DoubleMu0_OS_m2p5to4p5ForPPRef_v3', 
        'HLT_HIL3DoubleMu0_OS_m7to14ForPPRef_v3', 
        'HLT_HIL3Mu15ForPPRef_v3', 
        'HLT_HIL3Mu20ForPPRef_v3', 
        'HLT_HIL3Mu3_NHitQ15ForPPRef_v3', 
        'HLT_HIL3Mu5_NHitQ15ForPPRef_v3', 
        'HLT_HIL3Mu7_NHitQ15ForPPRef_v3', 
        'HLT_HISinglePhoton10_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton10_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton10_v4', 
        'HLT_HISinglePhoton15_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton15_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton15_v4', 
        'HLT_HISinglePhoton20_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton20_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton20_v4', 
        'HLT_HISinglePhoton30_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton30_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton40_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton40_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton40_v4', 
        'HLT_HISinglePhoton50_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton50_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton60_Eta1p5ForPPRef_v3', 
        'HLT_HISinglePhoton60_Eta3p1ForPPRef_v3', 
        'HLT_HISinglePhoton60_v4', 
        'HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrackForPPRef_v3', 
        'HLT_HIUPCL1DoubleMuOpenNotHF2ForPPRef_v3', 
        'HLT_HIUPCL1MuOpen_NotMinimumBiasHF2_ANDForPPRef_v3', 
        'HLT_HIUPCL1NotMinimumBiasHF2_ANDForPPRef_v3', 
        'HLT_HIUPCL1NotZdcOR_BptxANDForPPRef_v2', 
        'HLT_HIUPCL1ZdcOR_BptxANDForPPRef_v2', 
        'HLT_HIUPCL1ZdcXOR_BptxANDForPPRef_v2', 
        'HLT_HIUPCMuOpen_NotMinimumBiasHF2_ANDPixel_SingleTrackForPPRef_v3', 
        'HLT_HIUPCNotMinimumBiasHF2_ANDPixel_SingleTrackForPPRef_v3', 
        'HLT_HIUPCNotZdcOR_BptxANDPixel_SingleTrackForPPRef_v2', 
        'HLT_HIUPCZdcOR_BptxANDPixel_SingleTrackForPPRef_v2', 
        'HLT_HIUPCZdcXOR_BptxANDPixel_SingleTrackForPPRef_v2', 
        'HLT_HT2000_v5', 
        'HLT_HT200_v4', 
        'HLT_HT2500_v5', 
        'HLT_HT250_DisplacedDijet40_DisplacedTrack_v5', 
        'HLT_HT275_v4', 
        'HLT_HT325_v4', 
        'HLT_HT350_DisplacedDijet40_DisplacedTrack_v5', 
        'HLT_HT350_DisplacedDijet40_Inclusive_v4', 
        'HLT_HT350_DisplacedDijet80_DisplacedTrack_v5', 
        'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v5', 
        'HLT_HT425_v4', 
        'HLT_HT430to450_v4', 
        'HLT_HT450to470_v4', 
        'HLT_HT470to500_v4', 
        'HLT_HT500to550_v4', 
        'HLT_HT550_DisplacedDijet80_Inclusive_v2', 
        'HLT_HT550to650_v4', 
        'HLT_HT575_v4', 
        'HLT_HT650_DisplacedDijet80_Inclusive_v5', 
        'HLT_HT650_v5', 
        'HLT_HT750_DisplacedDijet80_Inclusive_v5', 
        'HLT_HcalIsolatedbunch_v2', 
        'HLT_HcalNZS_v10', 
        'HLT_HcalPhiSym_v11', 
        'HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1_v5', 
        'HLT_IsoMu16_eta2p1_MET30_v4', 
        'HLT_IsoMu19_eta2p1_LooseCombinedIsoPFTau20_v1', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v5', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v5', 
        'HLT_IsoMu19_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu19_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg_v5', 
        'HLT_IsoMu19_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu20_v6', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v5', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau50_Trk30_eta2p1_SingleL1_v4', 
        'HLT_IsoMu21_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu21_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg_v5', 
        'HLT_IsoMu21_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu22_eta2p1_v4', 
        'HLT_IsoMu22_v5', 
        'HLT_IsoMu24_eta2p1_v3', 
        'HLT_IsoMu24_v4', 
        'HLT_IsoMu27_v7', 
        'HLT_IsoTkMu20_v7', 
        'HLT_IsoTkMu22_eta2p1_v4', 
        'HLT_IsoTkMu22_v5', 
        'HLT_IsoTkMu24_eta2p1_v3', 
        'HLT_IsoTkMu24_v4', 
        'HLT_IsoTkMu27_v7', 
        'HLT_IsoTrackHB_v3', 
        'HLT_IsoTrackHE_v3', 
        'HLT_JetE30_NoBPTX3BX_v4', 
        'HLT_JetE30_NoBPTX_v4', 
        'HLT_JetE50_NoBPTX3BX_v4', 
        'HLT_JetE70_NoBPTX3BX_v4', 
        'HLT_L1BptxMinus_v2', 
        'HLT_L1BptxPlus_v2', 
        'HLT_L1FatEvents_v2', 
        'HLT_L1MinimumBiasHF1AND_v2', 
        'HLT_L1MinimumBiasHF1OR_v2', 
        'HLT_L1MinimumBiasHF2AND_v2', 
        'HLT_L1MinimumBiasHF2ORNoBptxGating_v3', 
        'HLT_L1MinimumBiasHF2OR_v2', 
        'HLT_L1MinimumBiasHF_AND_v2', 
        'HLT_L1MinimumBiasHF_OR_part0_v2', 
        'HLT_L1MinimumBiasHF_OR_part1_v2', 
        'HLT_L1MinimumBiasHF_OR_part2_v2', 
        'HLT_L1MinimumBiasHF_OR_part3_v2', 
        'HLT_L1MinimumBiasHF_OR_part4_v2', 
        'HLT_L1MinimumBiasHF_OR_part5_v2', 
        'HLT_L1MinimumBiasHF_OR_part6_v2', 
        'HLT_L1MinimumBiasHF_OR_part7_v2', 
        'HLT_L1MinimumBiasHF_OR_part8_v2', 
        'HLT_L1MinimumBiasHF_OR_part9_v2', 
        'HLT_L1NotBptxOR_v2', 
        'HLT_L1SingleMu18_v1', 
        'HLT_L1TOTEM1_MinBias_v2', 
        'HLT_L1TOTEM2_ZeroBias_v2', 
        'HLT_L1_TripleJet_VBF_v5', 
        'HLT_L2DoubleMu23_NoVertex_v6', 
        'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v6', 
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v6', 
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v2', 
        'HLT_L2Mu10_NoVertex_NoBPTX_v3', 
        'HLT_L2Mu10_v3', 
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v2', 
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v1', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110_v6', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v6', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v6', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_v7', 
        'HLT_MET200_v5', 
        'HLT_MET250_v5', 
        'HLT_MET300_v5', 
        'HLT_MET600_v5', 
        'HLT_MET60_IsoTrk35_Loose_v3', 
        'HLT_MET700_v5', 
        'HLT_MET75_IsoTrk50_v6', 
        'HLT_MET90_IsoTrk50_v6', 
        'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v8', 
        'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v8', 
        'HLT_Mu10_CentralPFJet30_BTagCSV_p13_v5', 
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v5', 
        'HLT_Mu12_Photon25_CaloIdL_L1ISO_v8', 
        'HLT_Mu12_Photon25_CaloIdL_L1OR_v8', 
        'HLT_Mu12_Photon25_CaloIdL_v8', 
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v4', 
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v3', 
        'HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400_v6', 
        'HLT_Mu15_IsoVVVL_PFHT400_PFMET50_v5', 
        'HLT_Mu15_IsoVVVL_PFHT400_v5', 
        'HLT_Mu15_IsoVVVL_PFHT600_v8', 
        'HLT_Mu17_Mu8_DZ_v7', 
        'HLT_Mu17_Mu8_SameSign_DZ_v6', 
        'HLT_Mu17_Mu8_SameSign_v5', 
        'HLT_Mu17_Mu8_v5', 
        'HLT_Mu17_Photon30_CaloIdL_L1ISO_v9', 
        'HLT_Mu17_Photon35_CaloIdL_L1ISO_v9', 
        'HLT_Mu17_TkMu8_DZ_v6', 
        'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v7', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v6', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v6', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v5', 
        'HLT_Mu17_TrkIsoVVL_v4', 
        'HLT_Mu17_v4', 
        'HLT_Mu20_Mu10_DZ_v6', 
        'HLT_Mu20_Mu10_SameSign_DZ_v6', 
        'HLT_Mu20_Mu10_SameSign_v4', 
        'HLT_Mu20_Mu10_v5', 
        'HLT_Mu20_v4', 
        'HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL_v7', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v4', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v3', 
        'HLT_Mu24_eta2p1_v5', 
        'HLT_Mu25_TkMu0_dEta18_Onia_v6', 
        'HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL_v6', 
        'HLT_Mu27_TkMu8_v5', 
        'HLT_Mu27_v5', 
        'HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v7', 
        'HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v5', 
        'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v5', 
        'HLT_Mu300_v3', 
        'HLT_Mu30_TkMu11_v5', 
        'HLT_Mu30_eta2p1_PFJet150_PFJet50_v5', 
        'HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL_v7', 
        'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL_v3', 
        'HLT_Mu350_v3', 
        'HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL_v6', 
        'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v5', 
        'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v5', 
        'HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v5', 
        'HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v7', 
        'HLT_Mu3_PFJet40_v6', 
        'HLT_Mu40_TkMu11_v5', 
        'HLT_Mu40_eta2p1_PFJet200_PFJet50_v7', 
        'HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL_v7', 
        'HLT_Mu45_eta2p1_v5', 
        'HLT_Mu50_IsoVVVL_PFHT400_v5', 
        'HLT_Mu50_v5', 
        'HLT_Mu55_v4', 
        'HLT_Mu6_PFHT200_PFMET100_v5', 
        'HLT_Mu7p5_L2Mu2_Jpsi_v4', 
        'HLT_Mu7p5_L2Mu2_Upsilon_v4', 
        'HLT_Mu7p5_Track2_Jpsi_v4', 
        'HLT_Mu7p5_Track2_Upsilon_v4', 
        'HLT_Mu7p5_Track3p5_Jpsi_v4', 
        'HLT_Mu7p5_Track3p5_Upsilon_v4', 
        'HLT_Mu7p5_Track7_Jpsi_v4', 
        'HLT_Mu7p5_Track7_Upsilon_v4', 
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v9', 
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v10', 
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v4', 
        'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v9', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v4', 
        'HLT_Mu8_TrkIsoVVL_v5', 
        'HLT_Mu8_v5', 
        'HLT_PFHT125_v5', 
        'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v8', 
        'HLT_PFHT200_PFAlphaT0p51_v8', 
        'HLT_PFHT200_v6', 
        'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v8', 
        'HLT_PFHT250_v6', 
        'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v8', 
        'HLT_PFHT300_PFMET110_v6', 
        'HLT_PFHT300_v7', 
        'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v8', 
        'HLT_PFHT350_v8', 
        'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v8', 
        'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v6', 
        'HLT_PFHT400_SixJet30_v8', 
        'HLT_PFHT400_v7', 
        'HLT_PFHT450_SixJet40_BTagCSV_p056_v6', 
        'HLT_PFHT450_SixJet40_v8', 
        'HLT_PFHT475_v7', 
        'HLT_PFHT550_4JetPt50_v6', 
        'HLT_PFHT600_v8', 
        'HLT_PFHT650_4JetPt50_v6', 
        'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v8', 
        'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v8', 
        'HLT_PFHT650_v8', 
        'HLT_PFHT750_4JetPt70_v2', 
        'HLT_PFHT750_4JetPt80_v2', 
        'HLT_PFHT800_4JetPt50_v2', 
        'HLT_PFHT850_4JetPt50_v2', 
        'HLT_PFHT900_v6', 
        'HLT_PFJet140_v8', 
        'HLT_PFJet15_NoCaloMatched_v7', 
        'HLT_PFJet200_v8', 
        'HLT_PFJet25_NoCaloMatched_v5', 
        'HLT_PFJet260_v9', 
        'HLT_PFJet320_v9', 
        'HLT_PFJet400_v9', 
        'HLT_PFJet40_v9', 
        'HLT_PFJet450_v9', 
        'HLT_PFJet500_v9', 
        'HLT_PFJet60_v9', 
        'HLT_PFJet80_v8', 
        'HLT_PFMET110_PFMHT110_IDTight_v8', 
        'HLT_PFMET120_PFMHT120_IDTight_v8', 
        'HLT_PFMET170_BeamHaloCleaned_v7', 
        'HLT_PFMET170_HBHECleaned_v9', 
        'HLT_PFMET170_HBHE_BeamHaloCleaned_v5', 
        'HLT_PFMET170_NotCleaned_v8', 
        'HLT_PFMET300_v7', 
        'HLT_PFMET400_v7', 
        'HLT_PFMET500_v7', 
        'HLT_PFMET600_v7', 
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v8', 
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v8', 
        'HLT_PFMETTypeOne190_HBHE_BeamHaloCleaned_v5', 
        'HLT_PFTau120_eta2p1_v5', 
        'HLT_PFTau140_eta2p1_v5', 
        'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon120_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon120_v7', 
        'HLT_Photon135_PFMET100_v8', 
        'HLT_Photon165_HE10_v8', 
        'HLT_Photon165_R9Id90_HE10_IsoM_v9', 
        'HLT_Photon175_v8', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon22_R9Id90_HE10_IsoM_v7', 
        'HLT_Photon22_v6', 
        'HLT_Photon250_NoHE_v7', 
        'HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60_v9', 
        'HLT_Photon300_NoHE_v7', 
        'HLT_Photon30_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon30_v7', 
        'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15_v9', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v8', 
        'HLT_Photon36_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon36_v7', 
        'HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15_v9', 
        'HLT_Photon500_v6', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon50_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon50_v7', 
        'HLT_Photon600_v6', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon75_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon75_v7', 
        'HLT_Photon90_CaloIdL_PFHT600_v8', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon90_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon90_v7', 
        'HLT_Physics_v5', 
        'HLT_PixelTracks_Multiplicity110ForPPRef_v2', 
        'HLT_PixelTracks_Multiplicity135ForPPRef_v2', 
        'HLT_PixelTracks_Multiplicity160ForPPRef_v2', 
        'HLT_PixelTracks_Multiplicity60ForPPRef_v2', 
        'HLT_PixelTracks_Multiplicity85ForPPRef_v2', 
        'HLT_QuadJet45_DoubleBTagCSV_p087_v6', 
        'HLT_QuadJet45_TripleBTagCSV_p087_v6', 
        'HLT_QuadMuon0_Dimuon0_Jpsi_v4', 
        'HLT_QuadMuon0_Dimuon0_Upsilon_v4', 
        'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v5', 
        'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v5', 
        'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v5', 
        'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v5', 
        'HLT_QuadPFJet_VBF_v8', 
        'HLT_Random_v2', 
        'HLT_Rsq0p02_MR400_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200_v3', 
        'HLT_Rsq0p02_MR450_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200_v3', 
        'HLT_Rsq0p02_MR500_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200_v2', 
        'HLT_Rsq0p02_MR550_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200_v2', 
        'HLT_Rsq0p25_v6', 
        'HLT_Rsq0p30_v6', 
        'HLT_RsqMR270_Rsq0p09_MR200_4jet_v6', 
        'HLT_RsqMR270_Rsq0p09_MR200_v6', 
        'HLT_SingleCentralPFJet170_CFMax0p1_v5', 
        'HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v3', 
        'HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v3', 
        'HLT_TkMu17_v1', 
        'HLT_TkMu20_v4', 
        'HLT_TkMu24_eta2p1_v5', 
        'HLT_TkMu27_v5', 
        'HLT_TkMu50_v3', 
        'HLT_TripleMu_12_10_5_v4', 
        'HLT_TripleMu_5_3_3_DZ_Mass3p8_v1', 
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v6', 
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v6', 
        'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v5', 
        'HLT_VBF_DisplacedJet40_DisplacedTrack_v5', 
        'HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v5', 
        'HLT_VBF_DisplacedJet40_TightID_Hadronic_v5', 
        'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v5', 
        'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v5', 
        'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v5', 
        'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v5', 
        'HLT_VLooseIsoPFTau120_Trk50_eta2p1_v5', 
        'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v5', 
        'HLT_ZeroBias_FirstBXAfterTrain_v1', 
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_copy_v1', 
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v3', 
        'HLT_ZeroBias_FirstCollisionInTrain_v1', 
        'HLT_ZeroBias_IsolatedBunches_v3', 
        'HLT_ZeroBias_v4' ) ),
    ParkingHT430to450 = cms.vstring('HLT_HT430to450_v4'),
    ParkingHT450to470 = cms.vstring('HLT_HT450to470_v4'),
    ParkingHT470to500 = cms.vstring('HLT_HT470to500_v4'),
    ParkingHT500to550 = cms.vstring('HLT_HT500to550_v4'),
    ParkingHT550to650 = cms.vstring('HLT_HT550to650_v4'),
    ParkingHT650 = cms.vstring('HLT_HT650_v5'),
    ParkingScoutingMonitor = cms.vstring('DST_CaloJet40_BTagScouting_v7', 
        'DST_CaloJet40_CaloBTagScouting_v6', 
        'DST_CaloJet40_CaloScouting_PFScouting_v7', 
        'DST_DoubleMu3_Mass10_BTagScouting_v8', 
        'DST_DoubleMu3_Mass10_CaloScouting_PFScouting_v7', 
        'DST_HT250_CaloBTagScouting_v3', 
        'DST_HT250_CaloScouting_v5', 
        'DST_HT410_BTagScouting_v7', 
        'DST_HT410_PFScouting_v7', 
        'DST_HT450_BTagScouting_v7', 
        'DST_HT450_PFScouting_v7', 
        'DST_L1DoubleMu_BTagScouting_v8', 
        'DST_L1DoubleMu_CaloScouting_PFScouting_v7', 
        'DST_L1HTT_BTagScouting_v7', 
        'DST_L1HTT_CaloBTagScouting_v6', 
        'DST_L1HTT_CaloScouting_PFScouting_v7', 
        'DST_ZeroBias_BTagScouting_v7', 
        'DST_ZeroBias_CaloScouting_PFScouting_v6', 
        'HLT_HT430to450_v4', 
        'HLT_HT450to470_v4', 
        'HLT_HT470to500_v4', 
        'HLT_HT500to550_v4', 
        'HLT_HT550to650_v4', 
        'HLT_HT650_v5'),
    RPCMonitor = cms.vstring('AlCa_RPCMuonNoHits_v10', 
        'AlCa_RPCMuonNoTriggers_v10', 
        'AlCa_RPCMuonNormalisation_v10'),
    ScoutingCaloCommissioning = cms.vstring('DST_CaloJet40_CaloBTagScouting_v6', 
        'DST_CaloJet40_CaloScouting_PFScouting_v7', 
        'DST_L1HTT_CaloBTagScouting_v6', 
        'DST_L1HTT_CaloScouting_PFScouting_v7'),
    ScoutingCaloHT = cms.vstring('DST_HT250_CaloBTagScouting_v3', 
        'DST_HT250_CaloScouting_v5'),
    ScoutingPFCommissioning = cms.vstring('DST_CaloJet40_BTagScouting_v7', 
        'DST_CaloJet40_CaloScouting_PFScouting_v7', 
        'DST_L1DoubleMu_BTagScouting_v8', 
        'DST_L1DoubleMu_CaloScouting_PFScouting_v7', 
        'DST_L1HTT_BTagScouting_v7', 
        'DST_L1HTT_CaloScouting_PFScouting_v7', 
        'DST_ZeroBias_BTagScouting_v7', 
        'DST_ZeroBias_CaloScouting_PFScouting_v6'),
    ScoutingPFHT = cms.vstring('DST_HT410_BTagScouting_v7', 
        'DST_HT410_PFScouting_v7', 
        'DST_HT450_BTagScouting_v7', 
        'DST_HT450_PFScouting_v7'),
    ScoutingPFMuons = cms.vstring('DST_DoubleMu3_Mass10_BTagScouting_v8', 
        'DST_DoubleMu3_Mass10_CaloScouting_PFScouting_v7'),
    SingleElectron = cms.vstring('HLT_Ele105_CaloIdVT_GsfTrkIdT_v8', 
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v7', 
        'HLT_Ele145_CaloIdVT_GsfTrkIdT_v1', 
        'HLT_Ele15_IsoVVVL_BTagCSV_p067_PFHT400_v7', 
        'HLT_Ele15_IsoVVVL_PFHT400_PFMET50_v6', 
        'HLT_Ele15_IsoVVVL_PFHT400_v6', 
        'HLT_Ele15_IsoVVVL_PFHT600_v9', 
        'HLT_Ele200_CaloIdVT_GsfTrkIdT_v1', 
        'HLT_Ele20_eta2p1_WPLoose_Gsf_LooseIsoPFTau28_v3', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau29_v3', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_v9', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v4', 
        'HLT_Ele250_CaloIdVT_GsfTrkIdT_v6', 
        'HLT_Ele25_WPTight_Gsf_v7', 
        'HLT_Ele25_eta2p1_WPTight_Gsf_v7', 
        'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v9', 
        'HLT_Ele27_WPTight_Gsf_L1JetTauSeeded_v4', 
        'HLT_Ele27_WPTight_Gsf_v7', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v10', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v8', 
        'HLT_Ele27_eta2p1_WPTight_Gsf_v8', 
        'HLT_Ele300_CaloIdVT_GsfTrkIdT_v6', 
        'HLT_Ele30_WPTight_Gsf_v1', 
        'HLT_Ele30_eta2p1_WPTight_Gsf_v1', 
        'HLT_Ele32_WPTight_Gsf_v1', 
        'HLT_Ele32_eta2p1_WPTight_Gsf_v8', 
        'HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v3', 
        'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v9', 
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v7', 
        'HLT_Ele50_IsoVVVL_PFHT400_v6'),
    SingleMuHighPt = cms.vstring('HLT_HIL2Mu15ForPPRef_v3', 
        'HLT_HIL2Mu20ForPPRef_v3', 
        'HLT_HIL2Mu5_NHitQ10ForPPRef_v3', 
        'HLT_HIL2Mu7_NHitQ10ForPPRef_v3', 
        'HLT_HIL3Mu15ForPPRef_v3', 
        'HLT_HIL3Mu20ForPPRef_v3', 
        'HLT_HIL3Mu5_NHitQ15ForPPRef_v3', 
        'HLT_HIL3Mu7_NHitQ15ForPPRef_v3'),
    SingleMuLowPt = cms.vstring('HLT_HIL2Mu3_NHitQ10ForPPRef_v3', 
        'HLT_HIL3Mu3_NHitQ15ForPPRef_v3'),
    SingleMuon = cms.vstring('HLT_DoubleIsoMu17_eta2p1_noDzCut_v5', 
        'HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1_v5', 
        'HLT_IsoMu16_eta2p1_MET30_v4', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v5', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v5', 
        'HLT_IsoMu19_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg_v5', 
        'HLT_IsoMu20_v6', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v5', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau50_Trk30_eta2p1_SingleL1_v4', 
        'HLT_IsoMu21_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg_v5', 
        'HLT_IsoMu22_eta2p1_v4', 
        'HLT_IsoMu22_v5', 
        'HLT_IsoMu24_eta2p1_v3', 
        'HLT_IsoMu24_v4', 
        'HLT_IsoMu27_v7', 
        'HLT_IsoTkMu20_v7', 
        'HLT_IsoTkMu22_eta2p1_v4', 
        'HLT_IsoTkMu22_v5', 
        'HLT_IsoTkMu24_eta2p1_v3', 
        'HLT_IsoTkMu24_v4', 
        'HLT_IsoTkMu27_v7', 
        'HLT_L1SingleMu18_v1', 
        'HLT_L2Mu10_v3', 
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v5', 
        'HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400_v6', 
        'HLT_Mu15_IsoVVVL_PFHT400_PFMET50_v5', 
        'HLT_Mu15_IsoVVVL_PFHT400_v5', 
        'HLT_Mu15_IsoVVVL_PFHT600_v8', 
        'HLT_Mu20_v4', 
        'HLT_Mu24_eta2p1_v5', 
        'HLT_Mu27_v5', 
        'HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v5', 
        'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v5', 
        'HLT_Mu300_v3', 
        'HLT_Mu30_eta2p1_PFJet150_PFJet50_v5', 
        'HLT_Mu350_v3', 
        'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v5', 
        'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v5', 
        'HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v5', 
        'HLT_Mu40_eta2p1_PFJet200_PFJet50_v7', 
        'HLT_Mu45_eta2p1_v5', 
        'HLT_Mu50_IsoVVVL_PFHT400_v5', 
        'HLT_Mu50_v5', 
        'HLT_Mu55_v4', 
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v4', 
        'HLT_TkMu17_v1', 
        'HLT_TkMu20_v4', 
        'HLT_TkMu24_eta2p1_v5', 
        'HLT_TkMu27_v5', 
        'HLT_TkMu50_v3'),
    SinglePhoton = cms.vstring('HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon120_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon120_v7', 
        'HLT_Photon135_PFMET100_v8', 
        'HLT_Photon165_HE10_v8', 
        'HLT_Photon165_R9Id90_HE10_IsoM_v9', 
        'HLT_Photon175_v8', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon22_R9Id90_HE10_IsoM_v7', 
        'HLT_Photon22_v6', 
        'HLT_Photon250_NoHE_v7', 
        'HLT_Photon300_NoHE_v7', 
        'HLT_Photon30_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon30_v7', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v8', 
        'HLT_Photon36_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon36_v7', 
        'HLT_Photon500_v6', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon50_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon50_v7', 
        'HLT_Photon600_v6', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon75_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon75_v7', 
        'HLT_Photon90_CaloIdL_PFHT600_v8', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v9', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v7', 
        'HLT_Photon90_R9Id90_HE10_IsoM_v8', 
        'HLT_Photon90_v7'),
    TOTEM_minBias = cms.vstring('HLT_L1TOTEM1_MinBias_v2'),
    TOTEM_zeroBias = cms.vstring('HLT_L1TOTEM2_ZeroBias_v2'),
    Tau = cms.vstring('HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v3', 
        'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg_v2', 
        'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_v2', 
        'HLT_DoubleTightCombinedIsoPFTau35_Trk1_eta2p1_Reg_v3', 
        'HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1_Reg_v2', 
        'HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1_v2', 
        'HLT_IsoMu19_eta2p1_LooseCombinedIsoPFTau20_v1', 
        'HLT_IsoMu19_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu19_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu21_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu21_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg_v1', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110_v6', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v6', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v6', 
        'HLT_LooseIsoPFTau50_Trk30_eta2p1_v7', 
        'HLT_PFTau120_eta2p1_v5', 
        'HLT_PFTau140_eta2p1_v5', 
        'HLT_VLooseIsoPFTau120_Trk50_eta2p1_v5', 
        'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v5'),
    TestEnablesEcalHcal = cms.vstring('HLT_EcalCalibration_v3', 
        'HLT_HcalCalibration_v4'),
    TestEnablesEcalHcalDQM = cms.vstring('HLT_EcalCalibration_v3', 
        'HLT_HcalCalibration_v4'),
    ZeroBias = cms.vstring('HLT_Random_v2', 
        'HLT_ZeroBias_FirstBXAfterTrain_v1', 
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_copy_v1', 
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v3', 
        'HLT_ZeroBias_FirstCollisionInTrain_v1', 
        'HLT_ZeroBias_IsolatedBunches_v3', 
        'HLT_ZeroBias_v4'),
    ppForward = cms.vstring('HLT_HICastorMediumJetPixel_SingleTrackForPPRef_v2', 
        'HLT_HIL1CastorMediumJetForPPRef_v2', 
        'HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrackForPPRef_v3', 
        'HLT_HIUPCL1DoubleMuOpenNotHF2ForPPRef_v3', 
        'HLT_HIUPCL1MuOpen_NotMinimumBiasHF2_ANDForPPRef_v3', 
        'HLT_HIUPCL1NotMinimumBiasHF2_ANDForPPRef_v3', 
        'HLT_HIUPCL1NotZdcOR_BptxANDForPPRef_v2', 
        'HLT_HIUPCL1ZdcOR_BptxANDForPPRef_v2', 
        'HLT_HIUPCL1ZdcXOR_BptxANDForPPRef_v2', 
        'HLT_HIUPCMuOpen_NotMinimumBiasHF2_ANDPixel_SingleTrackForPPRef_v3', 
        'HLT_HIUPCNotMinimumBiasHF2_ANDPixel_SingleTrackForPPRef_v3', 
        'HLT_HIUPCNotZdcOR_BptxANDPixel_SingleTrackForPPRef_v2', 
        'HLT_HIUPCZdcOR_BptxANDPixel_SingleTrackForPPRef_v2', 
        'HLT_HIUPCZdcXOR_BptxANDPixel_SingleTrackForPPRef_v2')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.options = cms.untracked.PSet(
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(4),
    sizeOfStackForThreadsInKB = cms.untracked.uint32(10240),
    wantSummary = cms.untracked.bool(True)
)

process.streams = cms.PSet(
    ALCAELECTRON = cms.vstring('AlCaElectron'),
    ALCALUMIPIXELS = cms.vstring('AlCaLumiPixels'),
    ALCAP0 = cms.vstring('AlCaP0'),
    ALCAPHISYM = cms.vstring('AlCaPhiSym'),
    Calibration = cms.vstring('TestEnablesEcalHcal'),
    DQM = cms.vstring('OnlineMonitor'),
    DQMCalibration = cms.vstring('TestEnablesEcalHcalDQM'),
    DQMEventDisplay = cms.vstring('EventDisplay'),
    EcalCalibration = cms.vstring('EcalLaser'),
    Express = cms.vstring('ExpressPhysics'),
    HLTMonitor = cms.vstring('HLTMonitor'),
    NanoDST = cms.vstring('L1Accept'),
    Parking = cms.vstring('ParkingHT430to450', 
        'ParkingHT450to470', 
        'ParkingHT470to500', 
        'ParkingHT500to550', 
        'ParkingHT550to650', 
        'ParkingHT650'),
    ParkingHLTPhysics = cms.vstring('HLTPhysics0', 
        'HLTPhysics1', 
        'HLTPhysics2', 
        'HLTPhysics3'),
    PhysicsCommissioning = cms.vstring('Commissioning', 
        'HLTPhysics', 
        'HcalHPDNoise', 
        'HcalNZS', 
        'HighPtLowerPhotons', 
        'HighPtPhoton30AndZ', 
        'MonteCarlo', 
        'NoBPTX', 
        'TOTEM_minBias', 
        'TOTEM_zeroBias', 
        'ZeroBias'),
    PhysicsEGamma = cms.vstring('DoubleEG', 
        'SingleElectron', 
        'SinglePhoton'),
    PhysicsEndOfFill = cms.vstring('EmptyBX', 
        'FSQJets', 
        'HINCaloJets', 
        'HINPFJets', 
        'HINPhoton', 
        'HighMultiplicityEOF', 
        'L1MinimumBias'),
    PhysicsForward = cms.vstring('ppForward'),
    PhysicsHadronsTaus = cms.vstring('BTagCSV', 
        'BTagMu', 
        'DisplacedJet', 
        'HTMHT', 
        'HeavyFlavor', 
        'HighPtJet80', 
        'HighPtLowerJets', 
        'JetHT', 
        'MET', 
        'Tau'),
    PhysicsMinimumBias0 = cms.vstring('L1MinimumBias0', 
        'L1MinimumBias1', 
        'L1MinimumBias2'),
    PhysicsMinimumBias1 = cms.vstring('L1MinimumBias3', 
        'L1MinimumBias4', 
        'L1MinimumBias5'),
    PhysicsMinimumBias2 = cms.vstring('L1MinimumBias6', 
        'L1MinimumBias7', 
        'L1MinimumBias8', 
        'L1MinimumBias9'),
    PhysicsMuons = cms.vstring('Charmonium', 
        'DoubleMuon', 
        'DoubleMuonLowMass', 
        'MuOnia', 
        'MuPlusX', 
        'MuonEG', 
        'SingleMuHighPt', 
        'SingleMuLowPt', 
        'SingleMuon'),
    PhysicsParkingScoutingMonitor = cms.vstring('ParkingScoutingMonitor'),
    PhysicsTracks = cms.vstring('FullTrack', 
        'HighMultiplicity'),
    RPCMON = cms.vstring('RPCMonitor'),
    ReleaseValidation = cms.vstring(),
    ScoutingCalo = cms.vstring('ScoutingCaloCommissioning', 
        'ScoutingCaloHT'),
    ScoutingPF = cms.vstring('ScoutingPFCommissioning', 
        'ScoutingPFHT', 
        'ScoutingPFMuons')
)

process.transferSystem = cms.PSet(
    default = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        streamLookArea = cms.PSet(

        ),
        test = cms.vstring('Lustre')
    ),
    destinations = cms.vstring('Tier0', 
        'DQM', 
        'ECAL', 
        'EventDisplay', 
        'Lustre', 
        'None'),
    streamA = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        test = cms.vstring('Lustre')
    ),
    streamCalibration = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamDQM = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring('DQM', 
            'Lustre')
    ),
    streamDQMCalibration = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring('DQM', 
            'Lustre')
    ),
    streamEcalCalibration = cms.PSet(
        default = cms.vstring('ECAL'),
        emulator = cms.vstring('None'),
        test = cms.vstring('ECAL')
    ),
    streamEventDisplay = cms.PSet(
        default = cms.vstring('EventDisplay', 
            'Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('EventDisplay', 
            'Lustre')
    ),
    streamExpressCosmics = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        test = cms.vstring('Lustre')
    ),
    streamLookArea = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring('DQM', 
            'Lustre')
    ),
    streamNanoDST = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamRPCMON = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamTrackerCalibration = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    transferModes = cms.vstring('default', 
        'test', 
        'emulator')
)

process.hltAK4CaloJetsPF = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltTowerMakerForPF"),
    srcPVs = cms.InputTag("NotUsed"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(-9.0),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4Iter0TrackJets4Iter1 = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.2),
    DzTrVtxMax = cms.double(0.5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(30.0),
    MinVtxNdof = cms.int32(0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(True),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.1),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('TrackJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltTrackIter0RefsForJets4Iter1"),
    srcPVs = cms.InputTag("hltTrimmedPixelVertices"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(0.9),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4Iter1TrackJets4Iter2 = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.2),
    DzTrVtxMax = cms.double(0.5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(30.0),
    MinVtxNdof = cms.int32(0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(True),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.1),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(7.5),
    jetType = cms.string('TrackJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltIter1TrackRefsForJets4Iter2"),
    srcPVs = cms.InputTag("hltTrimmedPixelVertices"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(0.9),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltAK4PFJetsForTaus = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(True),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10.0),
    rFilt = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    src = cms.InputTag("hltParticleFlowForTaus"),
    srcPVs = cms.InputTag("hltTrimmedPixelVertices"),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useFiltering = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useTrimming = cms.bool(False),
    voronoiRfact = cms.double(-9.0),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltCsc2DRecHits = cms.EDProducer("CSCRecHitDProducer",
    CSCDebug = cms.untracked.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripClusterSize = cms.untracked.int32(3),
    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripxtalksOffset = cms.double(0.03),
    CSCUseCalibrations = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(False),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCUseStaticPedestals = cms.bool(False),
    CSCUseTimingCorrections = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCstripWireDeltaTime = cms.int32(8),
    ConstSyst_ME12 = cms.double(0.0),
    ConstSyst_ME13 = cms.double(0.0),
    ConstSyst_ME1a = cms.double(0.022),
    ConstSyst_ME1b = cms.double(0.007),
    ConstSyst_ME21 = cms.double(0.0),
    ConstSyst_ME22 = cms.double(0.0),
    ConstSyst_ME31 = cms.double(0.0),
    ConstSyst_ME32 = cms.double(0.0),
    ConstSyst_ME41 = cms.double(0.0),
    NoiseLevel_ME12 = cms.double(9.0),
    NoiseLevel_ME13 = cms.double(8.0),
    NoiseLevel_ME1a = cms.double(7.0),
    NoiseLevel_ME1b = cms.double(8.0),
    NoiseLevel_ME21 = cms.double(9.0),
    NoiseLevel_ME22 = cms.double(9.0),
    NoiseLevel_ME31 = cms.double(9.0),
    NoiseLevel_ME32 = cms.double(9.0),
    NoiseLevel_ME41 = cms.double(9.0),
    UseAverageTime = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    UseParabolaFit = cms.bool(False),
    XTasymmetry_ME12 = cms.double(0.0),
    XTasymmetry_ME13 = cms.double(0.0),
    XTasymmetry_ME1a = cms.double(0.0),
    XTasymmetry_ME1b = cms.double(0.0),
    XTasymmetry_ME21 = cms.double(0.0),
    XTasymmetry_ME22 = cms.double(0.0),
    XTasymmetry_ME31 = cms.double(0.0),
    XTasymmetry_ME32 = cms.double(0.0),
    XTasymmetry_ME41 = cms.double(0.0),
    readBadChambers = cms.bool(True),
    readBadChannels = cms.bool(False),
    stripDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCStripDigi"),
    wireDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCWireDigi")
)


process.hltCscSegments = cms.EDProducer("CSCSegmentProducer",
    algo_psets = cms.VPSet(cms.PSet(
        algo_name = cms.string('CSCSegAlgoST'),
        algo_psets = cms.VPSet(cms.PSet(
            BPMinImprovement = cms.double(10000.0),
            BrutePruning = cms.bool(True),
            CSCDebug = cms.untracked.bool(False),
            CorrectTheErrors = cms.bool(True),
            Covariance = cms.double(0.0),
            ForceCovariance = cms.bool(False),
            ForceCovarianceAll = cms.bool(False),
            NormChi2Cut2D = cms.double(20.0),
            NormChi2Cut3D = cms.double(10.0),
            Pruning = cms.bool(True),
            SeedBig = cms.double(0.0015),
            SeedSmall = cms.double(0.0002),
            curvePenalty = cms.double(2.0),
            curvePenaltyThreshold = cms.double(0.85),
            dPhiFineMax = cms.double(0.025),
            dRPhiFineMax = cms.double(8.0),
            dXclusBoxMax = cms.double(4.0),
            dYclusBoxMax = cms.double(8.0),
            hitDropLimit4Hits = cms.double(0.6),
            hitDropLimit5Hits = cms.double(0.8),
            hitDropLimit6Hits = cms.double(0.3333),
            maxDPhi = cms.double(999.0),
            maxDTheta = cms.double(999.0),
            maxRatioResidualPrune = cms.double(3.0),
            maxRecHitsInCluster = cms.int32(20),
            minHitsPerSegment = cms.int32(3),
            onlyBestSegment = cms.bool(False),
            preClustering = cms.bool(True),
            preClusteringUseChaining = cms.bool(True),
            prePrun = cms.bool(True),
            prePrunLimit = cms.double(3.17),
            tanPhiMax = cms.double(0.5),
            tanThetaMax = cms.double(1.2),
            useShowering = cms.bool(False),
            yweightPenalty = cms.double(1.5),
            yweightPenaltyThreshold = cms.double(1.0)
        ), 
            cms.PSet(
                BPMinImprovement = cms.double(10000.0),
                BrutePruning = cms.bool(True),
                CSCDebug = cms.untracked.bool(False),
                CorrectTheErrors = cms.bool(True),
                Covariance = cms.double(0.0),
                ForceCovariance = cms.bool(False),
                ForceCovarianceAll = cms.bool(False),
                NormChi2Cut2D = cms.double(20.0),
                NormChi2Cut3D = cms.double(10.0),
                Pruning = cms.bool(True),
                SeedBig = cms.double(0.0015),
                SeedSmall = cms.double(0.0002),
                curvePenalty = cms.double(2.0),
                curvePenaltyThreshold = cms.double(0.85),
                dPhiFineMax = cms.double(0.025),
                dRPhiFineMax = cms.double(8.0),
                dXclusBoxMax = cms.double(4.0),
                dYclusBoxMax = cms.double(8.0),
                hitDropLimit4Hits = cms.double(0.6),
                hitDropLimit5Hits = cms.double(0.8),
                hitDropLimit6Hits = cms.double(0.3333),
                maxDPhi = cms.double(999.0),
                maxDTheta = cms.double(999.0),
                maxRatioResidualPrune = cms.double(3.0),
                maxRecHitsInCluster = cms.int32(24),
                minHitsPerSegment = cms.int32(3),
                onlyBestSegment = cms.bool(False),
                preClustering = cms.bool(True),
                preClusteringUseChaining = cms.bool(True),
                prePrun = cms.bool(True),
                prePrunLimit = cms.double(3.17),
                tanPhiMax = cms.double(0.5),
                tanThetaMax = cms.double(1.2),
                useShowering = cms.bool(False),
                yweightPenalty = cms.double(1.5),
                yweightPenaltyThreshold = cms.double(1.0)
            )),
        chamber_types = cms.vstring('ME1/a', 
            'ME1/b', 
            'ME1/2', 
            'ME1/3', 
            'ME2/1', 
            'ME2/2', 
            'ME3/1', 
            'ME3/2', 
            'ME4/1', 
            'ME4/2'),
        parameters_per_chamber_type = cms.vint32(2, 1, 1, 1, 1, 
            1, 1, 1, 1, 1)
    )),
    algo_type = cms.int32(1),
    inputObjects = cms.InputTag("hltCsc2DRecHits")
)


process.hltDt1DRecHits = cms.EDProducer("DTRecHitProducer",
    debug = cms.untracked.bool(False),
    dtDigiLabel = cms.InputTag("hltMuonDTDigis"),
    recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
    recAlgoConfig = cms.PSet(
        debug = cms.untracked.bool(False),
        doVdriftCorr = cms.bool(True),
        maxTime = cms.double(420.0),
        minTime = cms.double(-3.0),
        stepTwoFromDigi = cms.bool(False),
        tTrigMode = cms.string('DTTTrigSyncFromDB'),
        tTrigModeConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doT0Correction = cms.bool(True),
            doTOFCorrection = cms.bool(True),
            doWirePropCorrection = cms.bool(True),
            tTrigLabel = cms.string(''),
            tofCorrType = cms.int32(0),
            vPropWire = cms.double(24.4),
            wirePropCorrType = cms.int32(0)
        ),
        useUncertDB = cms.bool(True)
    )
)


process.hltDt4DSegments = cms.EDProducer("DTRecSegment4DProducer",
    Reco4DAlgoConfig = cms.PSet(
        AllDTRecHits = cms.bool(True),
        Reco2DAlgoConfig = cms.PSet(
            AlphaMaxPhi = cms.double(1.0),
            AlphaMaxTheta = cms.double(0.9),
            MaxAllowedHits = cms.uint32(50),
            debug = cms.untracked.bool(False),
            hit_afterT0_resolution = cms.double(0.03),
            nSharedHitsMax = cms.int32(2),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False),
            performT0_vdriftSegCorrection = cms.bool(False),
            perform_delta_rejecting = cms.bool(False),
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doVdriftCorr = cms.bool(True),
                maxTime = cms.double(420.0),
                minTime = cms.double(-3.0),
                stepTwoFromDigi = cms.bool(False),
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                tTrigModeConfig = cms.PSet(
                    debug = cms.untracked.bool(False),
                    doT0Correction = cms.bool(True),
                    doTOFCorrection = cms.bool(True),
                    doWirePropCorrection = cms.bool(True),
                    tTrigLabel = cms.string(''),
                    tofCorrType = cms.int32(0),
                    vPropWire = cms.double(24.4),
                    wirePropCorrType = cms.int32(0)
                ),
                useUncertDB = cms.bool(True)
            ),
            segmCleanerMode = cms.int32(2)
        ),
        Reco2DAlgoName = cms.string('DTCombinatorialPatternReco'),
        debug = cms.untracked.bool(False),
        hit_afterT0_resolution = cms.double(0.03),
        nSharedHitsMax = cms.int32(2),
        nUnSharedHitsMin = cms.int32(2),
        performT0SegCorrection = cms.bool(False),
        performT0_vdriftSegCorrection = cms.bool(False),
        perform_delta_rejecting = cms.bool(False),
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        recAlgoConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doVdriftCorr = cms.bool(True),
            maxTime = cms.double(420.0),
            minTime = cms.double(-3.0),
            stepTwoFromDigi = cms.bool(False),
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            tTrigModeConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doT0Correction = cms.bool(True),
                doTOFCorrection = cms.bool(True),
                doWirePropCorrection = cms.bool(True),
                tTrigLabel = cms.string(''),
                tofCorrType = cms.int32(0),
                vPropWire = cms.double(24.4),
                wirePropCorrType = cms.int32(0)
            ),
            useUncertDB = cms.bool(True)
        ),
        segmCleanerMode = cms.int32(2)
    ),
    Reco4DAlgoName = cms.string('DTCombinatorialPatternReco4D'),
    debug = cms.untracked.bool(False),
    recHits1DLabel = cms.InputTag("hltDt1DRecHits"),
    recHits2DLabel = cms.InputTag("dt2DSegments")
)


process.hltEcalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("hltEcalDigis"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = cms.InputTag("hltEcalDigis"),
    integrityBlockSizeErrors = cms.InputTag("hltEcalDigis","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityTTIdErrors")
)


process.hltEcalDigis = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 
        16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 
        26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 
        36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 
        46, 47, 48, 49, 50, 
        51, 52, 53, 54),
    orderedFedList = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.hltEcalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    ESdigiCollection = cms.string(''),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    debugMode = cms.untracked.bool(False),
    sourceTag = cms.InputTag("rawDataCollector")
)


process.hltEcalPreshowerRecHit = cms.EDProducer("ESRecHitProducer",
    ESRecoAlgo = cms.int32(0),
    ESdigiCollection = cms.InputTag("hltEcalPreshowerDigis"),
    ESrechitCollection = cms.string('EcalRecHitsES'),
    algo = cms.string('ESRecHitWorker')
)


process.hltEcalRecHit = cms.EDProducer("EcalRecHitProducer",
    ChannelStatusToBeExcluded = cms.vstring(),
    EBLaserMAX = cms.double(3.0),
    EBLaserMIN = cms.double(0.5),
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    EBuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEB"),
    EELaserMAX = cms.double(8.0),
    EELaserMIN = cms.double(0.5),
    EErechitCollection = cms.string('EcalRecHitsEE'),
    EEuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEE"),
    algo = cms.string('EcalRecHitWorkerSimple'),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    cleaningConfig = cms.PSet(
        cThreshold_barrel = cms.double(4.0),
        cThreshold_double = cms.double(10.0),
        cThreshold_endcap = cms.double(15.0),
        e4e1Threshold_barrel = cms.double(0.08),
        e4e1Threshold_endcap = cms.double(0.3),
        e4e1_a_barrel = cms.double(0.04),
        e4e1_a_endcap = cms.double(0.02),
        e4e1_b_barrel = cms.double(-0.024),
        e4e1_b_endcap = cms.double(-0.0125),
        e6e2thresh = cms.double(0.04),
        ignoreOutOfTimeThresh = cms.double(1000000000.0),
        tightenCrack_e1_double = cms.double(2.0),
        tightenCrack_e1_single = cms.double(2.0),
        tightenCrack_e4e1_single = cms.double(3.0),
        tightenCrack_e6e2_double = cms.double(3.0)
    ),
    dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
    dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
    ebDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebDetId"),
    ebFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebFE"),
    eeDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeDetId"),
    eeFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeFE"),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring('kOk', 
            'kDAC', 
            'kNoLaser', 
            'kNoisy'),
        kNeighboursRecovered = cms.vstring('kFixedG0', 
            'kNonRespondingIsolated', 
            'kDeadVFE'),
        kNoisy = cms.vstring('kNNoisy', 
            'kFixedG6', 
            'kFixedG1'),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    killDeadChannels = cms.bool(True),
    laserCorrection = cms.bool(True),
    logWarningEtThreshold_EB_FE = cms.double(50.0),
    logWarningEtThreshold_EE_FE = cms.double(50.0),
    recoverEBFE = cms.bool(True),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    recoverEEFE = cms.bool(True),
    recoverEEIsolatedChannels = cms.bool(False),
    recoverEEVFE = cms.bool(False),
    singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
    singleChannelRecoveryThreshold = cms.double(8.0),
    skipTimeCalib = cms.bool(True),
    triggerPrimitiveDigiCollection = cms.InputTag("hltEcalDigis","EcalTriggerPrimitives")
)


process.hltEcalUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("hltEcalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = cms.InputTag("hltEcalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
    algoPSet = cms.PSet(
        EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
        EBtimeConstantTerm = cms.double(0.6),
        EBtimeFitLimits_Lower = cms.double(0.2),
        EBtimeFitLimits_Upper = cms.double(1.4),
        EBtimeFitParameters = cms.vdouble(-2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 
            91.01147, -50.35761, 11.05621),
        EBtimeNconst = cms.double(28.5),
        EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
        EEtimeConstantTerm = cms.double(1.0),
        EEtimeFitLimits_Lower = cms.double(0.2),
        EEtimeFitLimits_Upper = cms.double(1.4),
        EEtimeFitParameters = cms.vdouble(-2.390548, 3.553628, -17.62341, 67.67538, -133.213, 
            140.7432, -75.41106, 16.20277),
        EEtimeNconst = cms.double(31.8),
        activeBXs = cms.vint32(-5, -4, -3, -2, -1, 
            0, 1, 2),
        ampErrorCalculation = cms.bool(False),
        amplitudeThresholdEB = cms.double(10.0),
        amplitudeThresholdEE = cms.double(10.0),
        chi2ThreshEB_ = cms.double(65.0),
        chi2ThreshEE_ = cms.double(50.0),
        doPrefitEB = cms.bool(True),
        doPrefitEE = cms.bool(True),
        ebSpikeThreshold = cms.double(1.042),
        kPoorRecoFlagEB = cms.bool(True),
        kPoorRecoFlagEE = cms.bool(False),
        outOfTimeThresholdGain12mEB = cms.double(5.0),
        outOfTimeThresholdGain12mEE = cms.double(1000.0),
        outOfTimeThresholdGain12pEB = cms.double(5.0),
        outOfTimeThresholdGain12pEE = cms.double(1000.0),
        outOfTimeThresholdGain61mEB = cms.double(5.0),
        outOfTimeThresholdGain61mEE = cms.double(1000.0),
        outOfTimeThresholdGain61pEB = cms.double(5.0),
        outOfTimeThresholdGain61pEE = cms.double(1000.0),
        prefitMaxChiSqEB = cms.double(15.0),
        prefitMaxChiSqEE = cms.double(10.0),
        timealgo = cms.string('None'),
        useLumiInfoRunHeader = cms.bool(False)
    )
)


process.hltFEDSelector = cms.EDProducer("EvFFEDSelector",
    fedList = cms.vuint32(1023, 1024),
    inputTag = cms.InputTag("rawDataCollector")
)


process.hltGtStage2Digis = cms.EDProducer("L1TRawToDigi",
    CTP7 = cms.untracked.bool(False),
    FWId = cms.uint32(0),
    FWOverride = cms.bool(False),
    FedIds = cms.vint32(1404),
    InputLabel = cms.InputTag("rawDataCollector"),
    MTF7 = cms.untracked.bool(False),
    MinFeds = cms.uint32(0),
    Setup = cms.string('stage2::GTSetup'),
    debug = cms.untracked.bool(False),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.hltGtStage2ObjectMap = cms.EDProducer("L1TGlobalProducer",
    AlgorithmTriggersUnmasked = cms.bool(True),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    AlternativeNrBxBoardDaq = cms.uint32(0),
    BstLengthBytes = cms.int32(-1),
    EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    EmulateBxInEvent = cms.int32(1),
    EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    ExtInputTag = cms.InputTag("hltGtStage2Digis"),
    JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1DataBxInEvent = cms.int32(5),
    MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    PrescaleCSVFile = cms.string('prescale_L1TGlobal.csv'),
    PrescaleSet = cms.uint32(1),
    PrintL1Menu = cms.untracked.bool(False),
    ProduceL1GtDaqRecord = cms.bool(True),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    TriggerMenuLuminosity = cms.string('startup'),
    Verbosity = cms.untracked.int32(0)
)


process.hltHbhePhase1Reco = cms.EDProducer("HBHEPhase1Reconstructor",
    algoConfigClass = cms.string(''),
    algorithm = cms.PSet(
        Class = cms.string('SimpleHBHEPhase1Algo'),
        applyPedConstraint = cms.bool(True),
        applyPulseJitter = cms.bool(False),
        applyTimeConstraint = cms.bool(True),
        applyTimeSlew = cms.bool(True),
        applyTimeSlewM3 = cms.bool(True),
        correctForPhaseContainment = cms.bool(True),
        correctionPhaseNS = cms.double(6.0),
        firstSampleShift = cms.int32(0),
        fitTimes = cms.int32(1),
        meanPed = cms.double(0.0),
        meanTime = cms.double(0.0),
        noiseHPD = cms.double(1.0),
        noiseSiPM = cms.double(1.0),
        pedSigmaHPD = cms.double(0.5),
        pedSigmaSiPM = cms.double(0.00065),
        pedestalUpperLimit = cms.double(2.7),
        pulseJitter = cms.double(1.0),
        respCorrM3 = cms.double(1.0),
        samplesToAdd = cms.int32(2),
        tdcTimeShift = cms.double(0.0),
        timeMax = cms.double(12.5),
        timeMin = cms.double(-12.5),
        timeSigmaHPD = cms.double(5.0),
        timeSigmaSiPM = cms.double(2.5),
        timeSlewPars = cms.vdouble(12.2999, -2.19142, 0.0, 12.2999, -2.19142, 
            0.0, 12.2999, -2.19142, 0.0),
        timeSlewParsType = cms.int32(3),
        ts4Max = cms.vdouble(100.0, 45000.0),
        ts4Min = cms.double(0.0),
        ts4chi2 = cms.vdouble(15.0, 15.0),
        useM2 = cms.bool(False),
        useM3 = cms.bool(True)
    ),
    digiLabelQIE11 = cms.InputTag("hltHcalDigis"),
    digiLabelQIE8 = cms.InputTag("hltHcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    flagParametersQIE11 = cms.PSet(

    ),
    flagParametersQIE8 = cms.PSet(
        hitEnergyMinimum = cms.double(1.0),
        hitMultiplicityThreshold = cms.int32(17),
        nominalPedestal = cms.double(3.0),
        pulseShapeParameterSets = cms.VPSet(cms.PSet(
            pulseShapeParameters = cms.vdouble(0.0, 100.0, -50.0, 0.0, -15.0, 
                0.15)
        ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(100.0, 2000.0, -50.0, 0.0, -5.0, 
                    0.05)
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(2000.0, 1000000.0, -50.0, 0.0, 95.0, 
                    0.0)
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(-1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 
                    0.0)
            ))
    ),
    makeRecHits = cms.bool(True),
    processQIE11 = cms.bool(True),
    processQIE8 = cms.bool(True),
    pulseShapeParametersQIE11 = cms.PSet(

    ),
    pulseShapeParametersQIE8 = cms.PSet(
        LeftSlopeCut = cms.vdouble(5.0, 2.55, 2.55),
        LeftSlopeThreshold = cms.vdouble(250.0, 500.0, 100000.0),
        LinearCut = cms.vdouble(-3.0, -0.054, -0.054),
        LinearThreshold = cms.vdouble(20.0, 100.0, 100000.0),
        MinimumChargeThreshold = cms.double(20.0),
        MinimumTS4TS5Threshold = cms.double(100.0),
        R45MinusOneRange = cms.double(0.2),
        R45PlusOneRange = cms.double(0.2),
        RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
        RMS8MaxThreshold = cms.vdouble(20.0, 100.0, 100000.0),
        RightSlopeCut = cms.vdouble(5.0, 4.15, 4.15),
        RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
        RightSlopeSmallThreshold = cms.vdouble(150.0, 200.0, 100000.0),
        RightSlopeThreshold = cms.vdouble(250.0, 400.0, 100000.0),
        TS3TS4ChargeThreshold = cms.double(70.0),
        TS3TS4UpperChargeThreshold = cms.double(20.0),
        TS4TS5ChargeThreshold = cms.double(70.0),
        TS4TS5LowerCut = cms.vdouble(-1.0, -0.7, -0.5, -0.4, -0.3, 
            0.1),
        TS4TS5LowerThreshold = cms.vdouble(100.0, 120.0, 160.0, 200.0, 300.0, 
            500.0),
        TS4TS5UpperCut = cms.vdouble(1.0, 0.8, 0.75, 0.72),
        TS4TS5UpperThreshold = cms.vdouble(70.0, 90.0, 100.0, 400.0),
        TS5TS6ChargeThreshold = cms.double(70.0),
        TS5TS6UpperChargeThreshold = cms.double(20.0),
        TriangleIgnoreSlow = cms.bool(False),
        TrianglePeakTS = cms.uint32(10000),
        UseDualFit = cms.bool(True)
    ),
    recoParamsFromDB = cms.bool(True),
    saveDroppedInfos = cms.bool(False),
    saveEffectivePedestal = cms.bool(False),
    saveInfos = cms.bool(False),
    setLegacyFlagsQIE11 = cms.bool(False),
    setLegacyFlagsQIE8 = cms.bool(True),
    setNegativeFlagsQIE11 = cms.bool(False),
    setNegativeFlagsQIE8 = cms.bool(False),
    setNoiseFlagsQIE11 = cms.bool(False),
    setNoiseFlagsQIE8 = cms.bool(True),
    setPulseShapeFlagsQIE11 = cms.bool(False),
    setPulseShapeFlagsQIE8 = cms.bool(True),
    tsFromDB = cms.bool(False)
)


process.hltHbhereco = cms.EDProducer("HBHEPlan1Combiner",
    algorithm = cms.PSet(
        Class = cms.string('SimplePlan1RechitCombiner')
    ),
    hbheInput = cms.InputTag("hltHbhePhase1Reco"),
    ignorePlan1Topology = cms.bool(False),
    usePlan1Mode = cms.bool(True)
)


process.hltHcalDigis = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(False),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    silent = cms.untracked.bool(True)
)


process.hltHfprereco = cms.EDProducer("HFPreReconstructor",
    digiLabel = cms.InputTag("hltHcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    sumAllTimeSlices = cms.bool(False),
    tsFromDB = cms.bool(False)
)


process.hltHfreco = cms.EDProducer("HFPhase1Reconstructor",
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        longETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        longEnergyParams = cms.vdouble(43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        shortEnergyParams = cms.vdouble(35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        longEnergyParams = cms.vdouble(40.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0),
        long_optimumSlope = cms.vdouble(0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1),
        shortETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        shortEnergyParams = cms.vdouble(40.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0, 100.0, 100.0, 
            100.0, 100.0, 100.0),
        short_optimumSlope = cms.vdouble(0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1)
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        longEnergyParams = cms.vdouble(43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62),
        long_optimumSlope = cms.vdouble(-99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927),
        shortETParams = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 0.0),
        shortEnergyParams = cms.vdouble(35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093),
        short_optimumSlope = cms.vdouble(-99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927)
    ),
    algoConfigClass = cms.string('HFPhase1PMTParams'),
    algorithm = cms.PSet(
        Class = cms.string('HFFlexibleTimeCheck'),
        energyWeights = cms.vdouble(1.0, 1.0, 1.0, 0.0, 1.0, 
            0.0, 2.0, 0.0, 2.0, 0.0, 
            2.0, 0.0, 1.0, 0.0, 0.0, 
            1.0, 0.0, 1.0, 0.0, 2.0, 
            0.0, 2.0, 0.0, 2.0, 0.0, 
            1.0),
        rejectAllFailures = cms.bool(True),
        soiPhase = cms.uint32(1),
        tfallIfNoTDC = cms.double(-101.0),
        timeShift = cms.double(0.0),
        tlimits = cms.vdouble(-1000.0, 1000.0, -1000.0, 1000.0),
        triseIfNoTDC = cms.double(-100.0)
    ),
    checkChannelQualityForDepth3and4 = cms.bool(False),
    inputLabel = cms.InputTag("hltHfprereco"),
    setNoiseFlags = cms.bool(False),
    useChannelQualityFromDB = cms.bool(False)
)


process.hltHoreco = cms.EDProducer("HcalHitReconstructor",
    HFInWindowStat = cms.PSet(

    ),
    PETstat = cms.PSet(

    ),
    S8S1stat = cms.PSet(

    ),
    S9S1stat = cms.PSet(

    ),
    Subdetector = cms.string('HO'),
    applyPedConstraint = cms.bool(True),
    applyPulseJitter = cms.bool(False),
    applyTimeConstraint = cms.bool(True),
    applyTimeSlew = cms.bool(True),
    applyTimeSlewM3 = cms.bool(True),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(False),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hltHcalDigis"),
    digiTimeFromDB = cms.bool(True),
    digistat = cms.PSet(

    ),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    fitTimes = cms.int32(1),
    flagParameters = cms.PSet(

    ),
    hfTimingTrustParameters = cms.PSet(

    ),
    hscpParameters = cms.PSet(

    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    meanPed = cms.double(0.0),
    meanTime = cms.double(-2.5),
    noiseHPD = cms.double(1.0),
    noiseSiPM = cms.double(1.0),
    pedSigmaHPD = cms.double(0.5),
    pedSigmaSiPM = cms.double(0.00065),
    pedestalUpperLimit = cms.double(2.7),
    puCorrMethod = cms.int32(0),
    pulseJitter = cms.double(1.0),
    pulseShapeParameters = cms.PSet(

    ),
    recoParamsFromDB = cms.bool(True),
    respCorrM3 = cms.double(1.0),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(False),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(False),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(False),
    setTimingShapedCutsFlags = cms.bool(False),
    setTimingTrustFlags = cms.bool(False),
    timeMax = cms.double(10.0),
    timeMin = cms.double(-15.0),
    timeSigmaHPD = cms.double(5.0),
    timeSigmaSiPM = cms.double(2.5),
    timeSlewPars = cms.vdouble(12.2999, -2.19142, 0.0, 12.2999, -2.19142, 
        0.0, 12.2999, -2.19142, 0.0),
    timeSlewParsType = cms.int32(3),
    timingshapedcutsParameters = cms.PSet(

    ),
    ts4Max = cms.vdouble(100.0, 45000.0),
    ts4Min = cms.double(5.0),
    ts4chi2 = cms.vdouble(15.0, 15.0),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag("hltPixelTracks"),
    InputVertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(False),
    useProtoTrackKinematics = cms.bool(False)
)


process.hltIter0PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter0GroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    produceSeedStopReasons = cms.bool(False),
    src = cms.InputTag("hltIter0PFLowPixelSeedsFromPixelTracks"),
    useHitsSplitting = cms.bool(False)
)


process.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter0'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter0PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter0PFlowTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    GBRForestFileName = cms.string(''),
    GBRForestLabel = cms.string(''),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            dr_exp = cms.vint32(4, 4, 4),
            dr_par1 = cms.vdouble(0.4, 0.4, 0.4),
            dr_par2 = cms.vdouble(0.3, 0.3, 0.3)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 4),
            dz_par1 = cms.vdouble(0.4, 0.4, 0.4),
            dz_par2 = cms.vdouble(0.35, 0.35, 0.35)
        ),
        maxChi2 = cms.vdouble(9999.0, 25.0, 16.0),
        maxChi2n = cms.vdouble(1.2, 1.0, 0.7),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 3, 4),
        minLayers = cms.vint32(3, 3, 4),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 3, 4)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltIter0PFlowTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks")
)


process.hltIter0TrackAndTauJets4Iter1 = cms.EDProducer("TauJetSelectorForHLTTrackSeeding",
    etaMaxCaloJet = cms.double(2.7),
    etaMinCaloJet = cms.double(-2.7),
    fractionMaxChargedPUInCaloCone = cms.double(0.3),
    fractionMinCaloInTauCone = cms.double(0.7),
    inputCaloJetTag = cms.InputTag("hltAK4CaloJetsPFEt5"),
    inputTrackJetTag = cms.InputTag("hltAK4Iter0TrackJets4Iter1"),
    inputTrackTag = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity"),
    isolationConeSize = cms.double(0.5),
    nTrkMaxInCaloCone = cms.int32(0),
    ptMinCaloJet = cms.double(5.0),
    ptTrkMaxInCaloCone = cms.double(1.0),
    tauConeSize = cms.double(0.2)
)


process.hltIter1ClustersRefRemoval = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("hltSiPixelClusters"),
    stripClusters = cms.InputTag("hltSiStripRawToClustersFacility"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity")
)


process.hltIter1MaskedMeasurementTrackerEvent = cms.EDProducer("MaskedMeasurementTrackerEventProducer",
    OnDemand = cms.bool(False),
    clustersToSkip = cms.InputTag("hltIter1ClustersRefRemoval"),
    src = cms.InputTag("hltSiStripClusters")
)


process.hltIter1Merged = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltIter0PFlowTrackSelectionHighPurity", "hltIter1PFlowTrackSelectionHighPurity"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltIter0PFlowTrackSelectionHighPurity", "hltIter1PFlowTrackSelectionHighPurity"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltIter1PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltIter1MaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter1GroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    produceSeedStopReasons = cms.bool(False),
    src = cms.InputTag("hltIter1PFlowPixelSeeds"),
    useHitsSplitting = cms.bool(False)
)


process.hltIter1PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter1'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltIter1MaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter1PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter1PFlowPixelClusterCheck = cms.EDProducer("ClusterCheckerEDProducer",
    ClusterCollectionLabel = cms.InputTag("hltSiStripClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(800000),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag("hltSiPixelClusters"),
    cut = cms.string(''),
    doClusterCheck = cms.bool(False),
    silentClusterCheck = cms.untracked.bool(False)
)


process.hltIter1PFlowPixelHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("hltIter1PFlowPixelClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("hltIter1PixelLayerQuadruplets"),
    trackingRegions = cms.InputTag("hltIter1PFlowPixelTrackingRegions")
)


process.hltIter1PFlowPixelHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0.0),
    CAOnlyOneLastHitPerLayerFilter = cms.bool(False),
    CAPhiCut = cms.double(0.3),
    CAThetaCut = cms.double(0.004),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none'),
        clusterShapeCacheSrc = cms.InputTag("hltSiPixelClustersCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("hltIter1PFlowPixelHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2.0),
        value1 = cms.double(2000.0),
        value2 = cms.double(150.0)
    ),
    useBendingCorrection = cms.bool(True)
)


process.hltIter1PFlowPixelSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltIter1PFlowPixelHitQuadruplets")
)


process.hltIter1PFlowPixelTrackingRegions = cms.EDProducer("CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        deltaEta = cms.double(1.0),
        deltaPhi = cms.double(1.0),
        input = cms.InputTag("hltIter0TrackAndTauJets4Iter1"),
        maxNRegions = cms.int32(100),
        maxNVertices = cms.int32(10),
        measurementTrackerName = cms.InputTag("hltIter1MaskedMeasurementTrackerEvent"),
        mode = cms.string('VerticesFixed'),
        nSigmaZBeamSpot = cms.double(4.0),
        nSigmaZVertex = cms.double(4.0),
        originRadius = cms.double(0.05),
        precise = cms.bool(True),
        ptMin = cms.double(0.3),
        searchOpt = cms.bool(True),
        vertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
        whereToUseMeasurementTracker = cms.string('ForSiStrips'),
        zErrorBeamSpot = cms.double(15.0),
        zErrorVetex = cms.double(0.1)
    )
)


process.hltIter1PFlowTrackCutClassifierDetached = cms.EDProducer("TrackCutClassifier",
    GBRForestFileName = cms.string(''),
    GBRForestLabel = cms.string(''),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            dr_exp = cms.vint32(4, 4, 4),
            dr_par1 = cms.vdouble(1.0, 1.0, 1.0),
            dr_par2 = cms.vdouble(1.0, 1.0, 1.0)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 4),
            dz_par1 = cms.vdouble(1.0, 1.0, 1.0),
            dz_par2 = cms.vdouble(1.0, 1.0, 1.0)
        ),
        maxChi2 = cms.vdouble(9999.0, 25.0, 16.0),
        maxChi2n = cms.vdouble(1.0, 0.7, 0.4),
        maxDr = cms.vdouble(3.40282346639e+38, 1.0, 3.40282346639e+38),
        maxDz = cms.vdouble(3.40282346639e+38, 1.0, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
        maxLostLayers = cms.vint32(99, 3, 3),
        min3DLayers = cms.vint32(1, 2, 3),
        minLayers = cms.vint32(5, 5, 5),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1.0, -1.0, -1.0),
        minPixelHits = cms.vint32(0, 0, 1)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter1PFlowCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltIter1PFlowTrackCutClassifierMerged = cms.EDProducer("ClassifierMerger",
    inputClassifiers = cms.vstring('hltIter1PFlowTrackCutClassifierPrompt', 
        'hltIter1PFlowTrackCutClassifierDetached')
)


process.hltIter1PFlowTrackCutClassifierPrompt = cms.EDProducer("TrackCutClassifier",
    GBRForestFileName = cms.string(''),
    GBRForestLabel = cms.string(''),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            dr_exp = cms.vint32(3, 3, 3),
            dr_par1 = cms.vdouble(3.40282346639e+38, 1.0, 0.9),
            dr_par2 = cms.vdouble(3.40282346639e+38, 1.0, 0.85)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(3, 3, 3),
            dz_par1 = cms.vdouble(3.40282346639e+38, 1.0, 0.9),
            dz_par2 = cms.vdouble(3.40282346639e+38, 1.0, 0.8)
        ),
        maxChi2 = cms.vdouble(9999.0, 25.0, 16.0),
        maxChi2n = cms.vdouble(1.2, 1.0, 0.7),
        maxDr = cms.vdouble(3.40282346639e+38, 1.0, 3.40282346639e+38),
        maxDz = cms.vdouble(3.40282346639e+38, 1.0, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 0, 0),
        minLayers = cms.vint32(3, 3, 3),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 2)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter1PFlowCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltIter1PFlowTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter1PFlowTrackCutClassifierMerged","MVAValues"),
    originalQualVals = cms.InputTag("hltIter1PFlowTrackCutClassifierMerged","QualityMasks"),
    originalSource = cms.InputTag("hltIter1PFlowCtfWithMaterialTracks")
)


process.hltIter1PixelLayerQuadruplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3+BPix4', 
        'BPix1+BPix2+BPix3+FPix1_pos', 
        'BPix1+BPix2+BPix3+FPix1_neg', 
        'BPix1+BPix2+FPix1_pos+FPix2_pos', 
        'BPix1+BPix2+FPix1_neg+FPix2_neg', 
        'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
        'BPix1+FPix1_neg+FPix2_neg+FPix3_neg')
)


process.hltIter1TrackAndTauJets4Iter2 = cms.EDProducer("TauJetSelectorForHLTTrackSeeding",
    etaMaxCaloJet = cms.double(2.7),
    etaMinCaloJet = cms.double(-2.7),
    fractionMaxChargedPUInCaloCone = cms.double(0.3),
    fractionMinCaloInTauCone = cms.double(0.7),
    inputCaloJetTag = cms.InputTag("hltAK4CaloJetsPFEt5"),
    inputTrackJetTag = cms.InputTag("hltAK4Iter1TrackJets4Iter2"),
    inputTrackTag = cms.InputTag("hltIter1Merged"),
    isolationConeSize = cms.double(0.5),
    nTrkMaxInCaloCone = cms.int32(0),
    ptMinCaloJet = cms.double(5.0),
    ptTrkMaxInCaloCone = cms.double(1.4),
    tauConeSize = cms.double(0.2)
)


process.hltIter1TrackRefsForJets4Iter2 = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltIter1Merged")
)


process.hltIter2ClustersRefRemoval = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(16.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("hltIter1ClustersRefRemoval"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("hltSiPixelClusters"),
    stripClusters = cms.InputTag("hltSiStripRawToClustersFacility"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("hltIter1PFlowTrackSelectionHighPurity")
)


process.hltIter2MaskedMeasurementTrackerEvent = cms.EDProducer("MaskedMeasurementTrackerEventProducer",
    OnDemand = cms.bool(False),
    clustersToSkip = cms.InputTag("hltIter2ClustersRefRemoval"),
    src = cms.InputTag("hltSiStripClusters")
)


process.hltIter2Merged = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltIter1Merged", "hltIter2PFlowTrackSelectionHighPurity"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltIter1Merged", "hltIter2PFlowTrackSelectionHighPurity"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltIter2PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltIter2MaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter2GroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    produceSeedStopReasons = cms.bool(False),
    src = cms.InputTag("hltIter2PFlowPixelSeeds"),
    useHitsSplitting = cms.bool(False)
)


process.hltIter2PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter2'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltIter2MaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter2PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter2PFlowPixelClusterCheck = cms.EDProducer("ClusterCheckerEDProducer",
    ClusterCollectionLabel = cms.InputTag("hltSiStripClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(800000),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag("hltSiPixelClusters"),
    cut = cms.string(''),
    doClusterCheck = cms.bool(False),
    silentClusterCheck = cms.untracked.bool(False)
)


process.hltIter2PFlowPixelHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("hltIter2PFlowPixelClusterCheck"),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("hltIter2PixelLayerTriplets"),
    trackingRegions = cms.InputTag("hltIter2PFlowPixelTrackingRegions")
)


process.hltIter2PFlowPixelHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.3),
    CAPhiCut = cms.double(0.1),
    CAThetaCut = cms.double(0.004),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("hltIter2PFlowPixelHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8.0),
        value1 = cms.double(100.0),
        value2 = cms.double(6.0)
    ),
    useBendingCorrection = cms.bool(True)
)


process.hltIter2PFlowPixelSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltIter2PFlowPixelHitTriplets")
)


process.hltIter2PFlowPixelTrackingRegions = cms.EDProducer("CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        deltaEta = cms.double(0.8),
        deltaPhi = cms.double(0.8),
        input = cms.InputTag("hltIter1TrackAndTauJets4Iter2"),
        maxNRegions = cms.int32(100),
        maxNVertices = cms.int32(10),
        measurementTrackerName = cms.InputTag("hltIter2MaskedMeasurementTrackerEvent"),
        mode = cms.string('VerticesFixed'),
        nSigmaZBeamSpot = cms.double(3.0),
        nSigmaZVertex = cms.double(4.0),
        originRadius = cms.double(0.025),
        precise = cms.bool(True),
        ptMin = cms.double(0.8),
        searchOpt = cms.bool(True),
        vertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
        whereToUseMeasurementTracker = cms.string('ForSiStrips'),
        zErrorBeamSpot = cms.double(15.0),
        zErrorVetex = cms.double(0.05)
    )
)


process.hltIter2PFlowTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    GBRForestFileName = cms.string(''),
    GBRForestLabel = cms.string(''),
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            dr_exp = cms.vint32(4, 4, 4),
            dr_par1 = cms.vdouble(3.40282346639e+38, 0.4, 0.4),
            dr_par2 = cms.vdouble(3.40282346639e+38, 0.3, 0.3)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 4),
            dz_par1 = cms.vdouble(3.40282346639e+38, 0.4, 0.4),
            dz_par2 = cms.vdouble(3.40282346639e+38, 0.35, 0.35)
        ),
        maxChi2 = cms.vdouble(9999.0, 25.0, 16.0),
        maxChi2n = cms.vdouble(1.2, 1.0, 0.7),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 0, 0),
        minLayers = cms.vint32(3, 3, 3),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter2PFlowCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltIter2PFlowTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter2PFlowTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter2PFlowTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter2PFlowCtfWithMaterialTracks")
)


process.hltIter2PixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix2+BPix3+BPix4', 
        'BPix1+BPix3+BPix4', 
        'BPix1+BPix2+BPix4', 
        'BPix2+BPix3+FPix1_pos', 
        'BPix2+BPix3+FPix1_neg', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix2_pos+FPix3_pos', 
        'FPix1_neg+FPix2_neg+FPix3_neg')
)


process.hltL2MuonCandidates = cms.EDProducer("L2MuonCandidateProducer",
    InputObjects = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL2MuonSeeds = cms.EDProducer("L2MuonSeedGeneratorFromL1T",
    CentralBxOnly = cms.bool(True),
    EtaMatchingBins = cms.vdouble(0.0, 2.5),
    GMTReadoutCollection = cms.InputTag(""),
    InputObjects = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MaxEta = cms.double(2.5),
    L1MinPt = cms.double(0.0),
    L1MinQuality = cms.uint32(7),
    MatchDR = cms.vdouble(0.3),
    OfflineSeedLabel = cms.untracked.InputTag("hltL2OfflineMuonSeeds"),
    Propagator = cms.string('SteppingHelixPropagatorAny'),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    UseOfflineSeed = cms.untracked.bool(True),
    UseUnassociatedL1 = cms.bool(False)
)


process.hltL2Muons = cms.EDProducer("L2MuonProducer",
    DoSeedRefit = cms.bool(False),
    InputObjects = cms.InputTag("hltL2MuonSeeds"),
    L2TrajBuilderParameters = cms.PSet(
        BWFilterParameters = cms.PSet(
            BWSeedType = cms.string('fromGenerator'),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('outsideIn'),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits")
        ),
        DoBackwardFilter = cms.bool(True),
        DoRefit = cms.bool(False),
        DoSeedRefit = cms.bool(False),
        FilterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            EnableCSCMeasurement = cms.bool(True),
            EnableDTMeasurement = cms.bool(True),
            EnableRPCMeasurement = cms.bool(True),
            FitDirection = cms.string('insideOut'),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                ExcludeRPCFromFit = cms.bool(False),
                Granularity = cms.int32(0),
                MaxChi2 = cms.double(25.0),
                RescaleError = cms.bool(False),
                RescaleErrorFactor = cms.double(100.0),
                UseInvalidHits = cms.bool(True)
            ),
            NumberOfSigma = cms.double(3.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits")
        ),
        NavigationType = cms.string('Standard'),
        SeedPosition = cms.string('in'),
        SeedPropagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            NMinRecHits = cms.uint32(2),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RescaleError = cms.double(100.0),
            UseSubRecHits = cms.bool(False)
        )
    ),
    MuonTrajectoryBuilder = cms.string('Exhaustive'),
    SeedTransformerParameters = cms.PSet(
        Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        NMinRecHits = cms.uint32(2),
        Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        RescaleError = cms.double(100.0),
        UseSubRecHits = cms.bool(False)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny', 
            'hltESPFastSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(False),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPosition = cms.vdouble(0.0, 0.0, 0.0),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(True),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL2OfflineMuonSeeds = cms.EDProducer("MuonSeedGenerator",
    CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
    CSC_01 = cms.vdouble(0.166, 0.0, 0.0, 0.031, 0.0, 
        0.0),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    CSC_02 = cms.vdouble(0.612, -0.207, 0.0, 0.067, -0.001, 
        0.0),
    CSC_03 = cms.vdouble(0.787, -0.338, 0.029, 0.101, -0.008, 
        0.0),
    CSC_12 = cms.vdouble(-0.161, 0.254, -0.047, 0.042, -0.007, 
        0.0),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    CSC_13 = cms.vdouble(0.901, -1.302, 0.533, 0.045, 0.005, 
        0.0),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    CSC_14 = cms.vdouble(0.606, -0.181, -0.002, 0.111, -0.003, 
        0.0),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    CSC_23 = cms.vdouble(-0.081, 0.113, -0.029, 0.015, 0.008, 
        0.0),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    CSC_24 = cms.vdouble(0.004, 0.021, -0.002, 0.053, 0.0, 
        0.0),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_34 = cms.vdouble(0.062, -0.067, 0.019, 0.021, 0.003, 
        0.0),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
    DT_12 = cms.vdouble(0.183, 0.054, -0.087, 0.028, 0.002, 
        0.0),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    DT_13 = cms.vdouble(0.315, 0.068, -0.127, 0.051, -0.002, 
        0.0),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    DT_14 = cms.vdouble(0.359, 0.052, -0.107, 0.072, -0.004, 
        0.0),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    DT_23 = cms.vdouble(0.13, 0.023, -0.057, 0.028, 0.004, 
        0.0),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    DT_24 = cms.vdouble(0.176, 0.014, -0.051, 0.051, 0.003, 
        0.0),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    DT_34 = cms.vdouble(0.044, 0.004, -0.013, 0.029, 0.003, 
        0.0),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    EnableCSCMeasurement = cms.bool(True),
    EnableDTMeasurement = cms.bool(True),
    OL_1213 = cms.vdouble(0.96, -0.737, 0.0, 0.052, 0.0, 
        0.0),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    OL_1222 = cms.vdouble(0.848, -0.591, 0.0, 0.062, 0.0, 
        0.0),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    OL_1232 = cms.vdouble(0.184, 0.0, 0.0, 0.066, 0.0, 
        0.0),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    OL_2213 = cms.vdouble(0.117, 0.0, 0.0, 0.044, 0.0, 
        0.0),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    OL_2222 = cms.vdouble(0.107, 0.0, 0.0, 0.04, 0.0, 
        0.0),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    SMB_10 = cms.vdouble(1.387, -0.038, 0.0, 0.19, 0.0, 
        0.0),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    SMB_11 = cms.vdouble(1.247, 0.72, -0.802, 0.229, -0.075, 
        0.0),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    SMB_12 = cms.vdouble(2.128, -0.956, 0.0, 0.199, 0.0, 
        0.0),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    SMB_20 = cms.vdouble(1.011, -0.052, 0.0, 0.188, 0.0, 
        0.0),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    SMB_21 = cms.vdouble(1.043, -0.124, 0.0, 0.183, 0.0, 
        0.0),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    SMB_22 = cms.vdouble(1.474, -0.758, 0.0, 0.185, 0.0, 
        0.0),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    SMB_30 = cms.vdouble(0.505, -0.022, 0.0, 0.215, 0.0, 
        0.0),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    SMB_31 = cms.vdouble(0.549, -0.145, 0.0, 0.207, 0.0, 
        0.0),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    SMB_32 = cms.vdouble(0.67, -0.327, 0.0, 0.22, 0.0, 
        0.0),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    SME_11 = cms.vdouble(3.295, -1.527, 0.112, 0.378, 0.02, 
        0.0),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SME_12 = cms.vdouble(0.102, 0.599, 0.0, 0.38, 0.0, 
        0.0),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    SME_13 = cms.vdouble(-1.286, 1.711, 0.0, 0.356, 0.0, 
        0.0),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SME_21 = cms.vdouble(-0.529, 1.194, -0.358, 0.472, 0.086, 
        0.0),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    SME_22 = cms.vdouble(-1.207, 1.491, -0.251, 0.189, 0.243, 
        0.0),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    SME_31 = cms.vdouble(-1.594, 1.482, -0.317, 0.487, 0.097, 
        0.0),
    SME_32 = cms.vdouble(-0.901, 1.333, -0.47, 0.41, 0.073, 
        0.0),
    SME_41 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    SME_42 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    beamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    crackEtas = cms.vdouble(0.2, 1.6, 1.7),
    crackWindow = cms.double(0.04),
    deltaEtaCrackSearchWindow = cms.double(0.25),
    deltaEtaSearchWindow = cms.double(0.2),
    deltaPhiSearchWindow = cms.double(0.25),
    scaleDT = cms.bool(True)
)


process.hltL3MuonCandidates = cms.EDProducer("L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag("hltL3MuonsLinksCombination"),
    InputObjects = cms.InputTag("hltL3Muons"),
    MuonPtOption = cms.string('Tracker')
)


process.hltL3Muons = cms.EDProducer("L3TrackCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit")
)


process.hltL3MuonsIOHit = cms.EDProducer("L3MuonProducer",
    L3TrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutRPC = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            DYTthrs = cms.vint32(30, 15),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(0.001),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            refToPSet_ = cms.string('HLTPSetMuonTrackingRegionBuilder8356')
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2IOHit"),
        tkTrajMaxChi2 = cms.double(9999.0),
        tkTrajMaxDXYBeamSpot = cms.double(0.2),
        tkTrajUseVertex = cms.bool(False),
        tkTrajVertex = cms.InputTag("pixelVertices")
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL3MuonsLinksCombination = cms.EDProducer("L3TrackLinksCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit")
)


process.hltL3MuonsOIHit = cms.EDProducer("L3MuonProducer",
    L3TrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutRPC = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            DYTthrs = cms.vint32(30, 15),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(0.001),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            refToPSet_ = cms.string('HLTPSetMuonTrackingRegionBuilder8356')
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2OIHit"),
        tkTrajMaxChi2 = cms.double(9999.0),
        tkTrajMaxDXYBeamSpot = cms.double(0.2),
        tkTrajUseVertex = cms.bool(False),
        tkTrajVertex = cms.InputTag("pixelVertices")
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL3MuonsOIState = cms.EDProducer("L3MuonProducer",
    L3TrajBuilderParameters = cms.PSet(
        GlbRefitterParameters = cms.PSet(
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            Chi2CutCSC = cms.double(150.0),
            Chi2CutDT = cms.double(10.0),
            Chi2CutRPC = cms.double(1.0),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            DYTthrs = cms.vint32(30, 15),
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = cms.bool(False),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            TrackerSkipSection = cms.int32(-1),
            TrackerSkipSystem = cms.int32(-1)
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Chi2Cut_1 = cms.double(50.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaDCut_3 = cms.double(15.0),
            DeltaRCut_1 = cms.double(0.1),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            Eta_threshold = cms.double(1.2),
            LocChi2Cut = cms.double(0.001),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = cms.double(0.0),
            Pt_threshold2 = cms.double(999999999.0),
            Quality_1 = cms.double(20.0),
            Quality_2 = cms.double(15.0),
            Quality_3 = cms.double(7.0)
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            refToPSet_ = cms.string('HLTPSetMuonTrackingRegionBuilder8356')
        ),
        PCut = cms.double(2.5),
        PtCut = cms.double(1.0),
        RefitRPCHits = cms.bool(True),
        ScaleTECxFactor = cms.double(-1.0),
        ScaleTECyFactor = cms.double(-1.0),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        tkTrajBeamSpot = cms.InputTag("hltOnlineBeamSpot"),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2OIState"),
        tkTrajMaxChi2 = cms.double(9999.0),
        tkTrajMaxDXYBeamSpot = cms.double(0.2),
        tkTrajUseVertex = cms.bool(False),
        tkTrajVertex = cms.InputTag("pixelVertices")
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = cms.PSet(
        DoSmoothing = cms.bool(True),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3),
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        VertexConstraint = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot")
    )
)


process.hltL3TkFromL2OICombination = cms.EDProducer("L3TrackCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit")
)


process.hltL3TkTracksFromL2 = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(100.0),
    LostHitPenalty = cms.double(0.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltL3TkTracksMergeStep1", "hltL3TkTracksFromL2IOHit"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltL3TkTracksMergeStep1", "hltL3TkTracksFromL2IOHit"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltL3TkTracksFromL2IOHit = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIterX'),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('PropagatorWithMaterial'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string(''),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltL3TrackCandidateFromL2IOHit"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.hltL3TkTracksFromL2OIHit = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIterX'),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('PropagatorWithMaterial'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string(''),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltL3TrackCandidateFromL2OIHit"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.hltL3TkTracksFromL2OIState = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIterX'),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('PropagatorWithMaterial'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string(''),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltL3TrackCandidateFromL2OIState"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.hltL3TkTracksMergeStep1 = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(100.0),
    LostHitPenalty = cms.double(0.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltL3TkTracksFromL2OIState", "hltL3TkTracksFromL2OIHit"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltL3TkTracksFromL2OIState", "hltL3TkTracksFromL2OIHit"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltL3TrackCandidateFromL2 = cms.EDProducer("L3TrackCandCombiner",
    labels = cms.VInputTag("hltL3TrackCandidateFromL2IOHit", "hltL3TrackCandidateFromL2OIHit", "hltL3TrackCandidateFromL2OIState")
)


process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer("CkfTrajectoryMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltL3TrajSeedIOHit"),
    trackCandidateAlso = cms.bool(True),
    useHitsSplitting = cms.bool(False)
)


process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer("CkfTrajectoryMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    reverseTrajectories = cms.bool(True),
    src = cms.InputTag("hltL3TrajSeedOIHit"),
    trackCandidateAlso = cms.bool(True),
    useHitsSplitting = cms.bool(False)
)


process.hltL3TrackCandidateFromL2OIState = cms.EDProducer("CkfTrajectoryMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    reverseTrajectories = cms.bool(True),
    src = cms.InputTag("hltL3TrajSeedOIState"),
    trackCandidateAlso = cms.bool(True),
    useHitsSplitting = cms.bool(False)
)


process.hltL3TrajSeedIOHit = cms.EDProducer("TSGFromL2Muon",
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonTrackingRegionBuilder8356')
    ),
    PCut = cms.double(2.5),
    PtCut = cms.double(1.0),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('PropagatorWithMaterial'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('DualByL2TSG'),
        L3TkCollectionA = cms.InputTag("hltL3TkFromL2OICombination"),
        PSetNames = cms.vstring('skipTSG', 
            'iterativeTSG'),
        iterativeTSG = cms.PSet(
            ComponentName = cms.string('CombinedTSG'),
            PSetNames = cms.vstring('firstTSG', 
                'secondTSG'),
            firstTSG = cms.PSet(
                ComponentName = cms.string('TSGFromOrderedHits'),
                OrderedHitsFactoryPSet = cms.PSet(
                    ComponentName = cms.string('StandardHitTripletGenerator'),
                    GeneratorPSet = cms.PSet(
                        ComponentName = cms.string('PixelTripletHLTGenerator'),
                        SeedComparitorPSet = cms.PSet(
                            ComponentName = cms.string('none')
                        ),
                        extraHitRPhitolerance = cms.double(0.06),
                        extraHitRZtolerance = cms.double(0.06),
                        maxElement = cms.uint32(0),
                        phiPreFiltering = cms.double(0.3),
                        useBending = cms.bool(True),
                        useFixedPreFiltering = cms.bool(False),
                        useMultScattering = cms.bool(True)
                    ),
                    SeedingLayers = cms.InputTag("hltPixelLayerTriplets")
                ),
                SeedCreatorPSet = cms.PSet(
                    refToPSet_ = cms.string('HLTSeedFromConsecutiveHitsCreator')
                ),
                TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
            ),
            secondTSG = cms.PSet(
                ComponentName = cms.string('TSGFromOrderedHits'),
                OrderedHitsFactoryPSet = cms.PSet(
                    ComponentName = cms.string('StandardHitPairGenerator'),
                    SeedingLayers = cms.InputTag("hltPixelLayerPairs"),
                    maxElement = cms.uint32(0),
                    useOnDemandTracker = cms.untracked.int32(0)
                ),
                SeedCreatorPSet = cms.PSet(
                    refToPSet_ = cms.string('HLTSeedFromConsecutiveHitsCreator')
                ),
                TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
            ),
            thirdTSG = cms.PSet(
                ComponentName = cms.string('DualByEtaTSG'),
                PSetNames = cms.vstring('endcapTSG', 
                    'barrelTSG'),
                SeedCreatorPSet = cms.PSet(
                    refToPSet_ = cms.string('HLTSeedFromConsecutiveHitsCreator')
                ),
                barrelTSG = cms.PSet(

                ),
                endcapTSG = cms.PSet(
                    ComponentName = cms.string('TSGFromOrderedHits'),
                    OrderedHitsFactoryPSet = cms.PSet(
                        ComponentName = cms.string('StandardHitPairGenerator'),
                        SeedingLayers = cms.InputTag("hltMixedLayerPairs"),
                        maxElement = cms.uint32(0),
                        useOnDemandTracker = cms.untracked.int32(0)
                    ),
                    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
                ),
                etaSeparation = cms.double(2.0)
            )
        ),
        skipTSG = cms.PSet(

        )
    ),
    TrackerSeedCleaner = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        cleanerFromSharedHits = cms.bool(True),
        directionCleaner = cms.bool(True),
        ptCleaner = cms.bool(True)
    )
)


process.hltL3TrajSeedOIHit = cms.EDProducer("TSGFromL2Muon",
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(

    ),
    PCut = cms.double(2.5),
    PtCut = cms.double(1.0),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('PropagatorWithMaterial', 
            'hltESPSmartPropagatorAnyOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('DualByL2TSG'),
        L3TkCollectionA = cms.InputTag("hltL3MuonsOIState"),
        PSetNames = cms.vstring('skipTSG', 
            'iterativeTSG'),
        iterativeTSG = cms.PSet(
            ComponentName = cms.string('TSGFromPropagation'),
            ErrorRescaling = cms.double(3.0),
            MaxChi2 = cms.double(40.0),
            MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
            ResetMethod = cms.string('matrix'),
            SelectState = cms.bool(False),
            SigmaZ = cms.double(25.0),
            UpdateState = cms.bool(True),
            UseVertexState = cms.bool(True),
            beamSpot = cms.InputTag("unused"),
            errorMatrixPset = cms.PSet(
                action = cms.string('use'),
                atIP = cms.bool(True),
                errorMatrixValuesPSet = cms.PSet(
                    pf3_V11 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V12 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V13 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V14 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V15 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V22 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V23 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V24 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V25 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V33 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V34 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V35 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V44 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V45 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V55 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    xAxis = cms.vdouble(0.0, 13.0, 30.0, 70.0, 1000.0),
                    yAxis = cms.vdouble(0.0, 1.0, 1.4, 10.0),
                    zAxis = cms.vdouble(-3.14159, 3.14159)
                )
            )
        ),
        skipTSG = cms.PSet(

        )
    ),
    TrackerSeedCleaner = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        cleanerFromSharedHits = cms.bool(True),
        directionCleaner = cms.bool(True),
        ptCleaner = cms.bool(True)
    )
)


process.hltL3TrajSeedOIState = cms.EDProducer("TSGFromL2Muon",
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(

    ),
    PCut = cms.double(2.5),
    PtCut = cms.double(1.0),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSteppingHelixPropagatorOpposite', 
            'hltESPSteppingHelixPropagatorAlong'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('TSGForRoadSearch'),
        MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
        copyMuonRecHit = cms.bool(False),
        errorMatrixPset = cms.PSet(
            action = cms.string('use'),
            atIP = cms.bool(True),
            errorMatrixValuesPSet = cms.PSet(
                pf3_V11 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V12 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V13 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V14 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V15 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V22 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V23 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V24 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V25 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V33 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V34 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V35 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V44 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V45 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V55 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                xAxis = cms.vdouble(0.0, 13.0, 30.0, 70.0, 1000.0),
                yAxis = cms.vdouble(0.0, 1.0, 1.4, 10.0),
                zAxis = cms.vdouble(-3.14159, 3.14159)
            )
        ),
        manySeeds = cms.bool(False),
        maxChi2 = cms.double(40.0),
        option = cms.uint32(3),
        propagatorCompatibleName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
        propagatorName = cms.string('hltESPSteppingHelixPropagatorAlong')
    ),
    TrackerSeedCleaner = cms.PSet(

    )
)


process.hltL3TrajectorySeed = cms.EDProducer("L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag("hltL3TrajSeedIOHit", "hltL3TrajSeedOIState", "hltL3TrajSeedOIHit")
)


process.hltLightPFTracks = cms.EDProducer("LightPFTrackProducer",
    TkColList = cms.VInputTag("hltPFMuonMerging"),
    TrackQuality = cms.string('none'),
    UseQuality = cms.bool(False)
)


process.hltMixedLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
        ),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix2_pos+TEC1_pos', 
        'FPix2_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC1_neg', 
        'FPix2_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg')
)


process.hltMuonCSCDigis = cms.EDProducer("CSCDCCUnpacker",
    Debug = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535557110),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    runDQM = cms.untracked.bool(False)
)


process.hltMuonDTDigis = cms.EDProducer("DTUnpackingModule",
    dataType = cms.string('DDU'),
    dqmOnly = cms.bool(False),
    inputLabel = cms.InputTag("rawDataCollector"),
    maxFEDid = cms.untracked.int32(779),
    minFEDid = cms.untracked.int32(770),
    readOutParameters = cms.PSet(
        debug = cms.untracked.bool(False),
        localDAQ = cms.untracked.bool(False),
        performDataIntegrityMonitor = cms.untracked.bool(False),
        rosParameters = cms.PSet(
            debug = cms.untracked.bool(False),
            localDAQ = cms.untracked.bool(False),
            performDataIntegrityMonitor = cms.untracked.bool(False),
            readDDUIDfromDDU = cms.untracked.bool(True),
            readingDDU = cms.untracked.bool(True),
            writeSC = cms.untracked.bool(True)
        )
    ),
    useStandardFEDid = cms.bool(True)
)


process.hltMuonLinks = cms.EDProducer("MuonLinksProducerForHLT",
    InclusiveTrackerTrackCollection = cms.InputTag("hltPFMuonMerging"),
    LinkCollection = cms.InputTag("hltL3MuonsLinksCombination"),
    pMin = cms.double(2.5),
    ptMin = cms.double(2.5),
    shareHitFraction = cms.double(0.8)
)


process.hltMuonRPCDigis = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    doSynchro = cms.bool(False)
)


process.hltMuons = cms.EDProducer("MuonIdProducer",
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(1.0),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring('ecal', 
            'hcal', 
            'ho'),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForPF"),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
            HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
            HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("hltAK4CaloJetsPFEt5"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForPF"),
            DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
            HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
            HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            CSCsegments = cms.InputTag("hltCscSegments"),
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                DTsegments = cms.InputTag("hltDt4DSegments"),
                TightMatchCSC = cms.bool(True),
                TightMatchDT = cms.bool(False)
            ),
            PruneCut = cms.double(100.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(2.7),
            DTsegments = cms.InputTag("hltDt4DSegments"),
            DoWireCorr = cms.bool(False),
            DropTheta = cms.bool(True),
            HitError = cms.double(6.0),
            HitsMin = cms.int32(5),
            MatchParameters = cms.PSet(
                CSCsegments = cms.InputTag("hltCscSegments"),
                DTradius = cms.double(0.01),
                DTsegments = cms.InputTag("hltDt4DSegments"),
                TightMatchCSC = cms.bool(True),
                TightMatchDT = cms.bool(False)
            ),
            PruneCut = cms.double(10000.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny'),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorCSC = cms.double(7.4),
        ErrorDT = cms.double(6.0),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(True)
    ),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("hltTowerMakerForPF"),
        DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        HBHERecHitCollectionLabel = cms.InputTag("hltHbhereco"),
        HORecHitCollectionLabel = cms.InputTag("hltHoreco"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("hltOnlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("hltPFMuonMerging")
    ),
    TrackerKinkFinderParameters = cms.PSet(
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(False)
    ),
    addExtraSoftMuons = cms.bool(False),
    arbitrateTrackerMuons = cms.bool(False),
    arbitrationCleanerOptions = cms.PSet(
        ClusterDPhi = cms.double(0.6),
        ClusterDTheta = cms.double(0.02),
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        OverlapDTheta = cms.double(0.02)
    ),
    debugWithTruthMatching = cms.bool(False),
    ecalDepositName = cms.string('ecal'),
    fillCaloCompatibility = cms.bool(True),
    fillEnergy = cms.bool(True),
    fillGlobalTrackQuality = cms.bool(False),
    fillGlobalTrackRefits = cms.bool(False),
    fillIsolation = cms.bool(True),
    fillMatching = cms.bool(True),
    fillTrackerKink = cms.bool(False),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    inputCollectionLabels = cms.VInputTag("hltPFMuonMerging", "hltMuonLinks", "hltL2Muons"),
    inputCollectionTypes = cms.vstring('inner tracks', 
        'links', 
        'outer tracks'),
    jetDepositName = cms.string('jets'),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    maxAbsEta = cms.double(3.0),
    maxAbsPullX = cms.double(4.0),
    maxAbsPullY = cms.double(9999.0),
    minCaloCompatibility = cms.double(0.6),
    minNumberOfMatches = cms.int32(1),
    minP = cms.double(10.0),
    minPCaloMuon = cms.double(1000000000.0),
    minPt = cms.double(10.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    runArbitrationCleaner = cms.bool(False),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    trackDepositName = cms.string('tracker'),
    writeIsoDeposits = cms.bool(False)
)


process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotOnlineProducer",
    changeToCMSCoordinates = cms.bool(False),
    gtEvmLabel = cms.InputTag(""),
    maxRadius = cms.double(2.0),
    maxZ = cms.double(40.0),
    setSigmaZ = cms.double(0.0),
    src = cms.InputTag("hltScalersRawToDigi")
)


process.hltPFMuonMerging = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltL3TkTracksFromL2", "hltIter2Merged"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltL3TkTracksFromL2", "hltIter2Merged"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltPFTauAgainstMuonDiscriminator = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon2",
    HoPMin = cms.double(-1.0),
    PFTauProducer = cms.InputTag("hltPFTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    discriminatorOption = cms.string('custom'),
    doCaloMuonVeto = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    maxNumberOfHitsLast2Stations = cms.int32(-1),
    maxNumberOfMatches = cms.int32(1),
    minPtMatchedMuon = cms.double(5.0),
    srcMuons = cms.InputTag(""),
    verbosity = cms.int32(0)
)


process.hltPFTauLooseAbsOrRelIsolationDiscriminator = cms.EDProducer("PFTauDiscriminatorLogicalAndProducer",
    FailValue = cms.double(0.0),
    PFTauProducer = cms.InputTag("hltPFTaus"),
    PassValue = cms.double(1.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('or'),
        discr1 = cms.PSet(
            Producer = cms.InputTag("hltPFTauLooseAbsoluteIsolationDiscriminator"),
            cut = cms.double(0.5)
        ),
        discr2 = cms.PSet(
            Producer = cms.InputTag("hltPFTauLooseRelativeIsolationDiscriminator"),
            cut = cms.double(0.5)
        )
    )
)


process.hltPFTauLooseAbsoluteIsolationDiscriminator = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hltPFTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(False),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(True),
    customOuterCone = cms.double(-1.0),
    deltaBetaFactor = cms.string('0.38'),
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
    isoConeSizeForDeltaBeta = cms.double(0.3),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(3.0),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("hltParticleFlowForTaus"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.05),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(5),
            minTrackPixelHits = cms.uint32(2),
            minTrackPt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False)
        ),
        primaryVertexSrc = cms.InputTag("hltPixelVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(1000.0),
            maxTransverseImpactParameter = cms.double(0.2),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.0),
            useTracksInsteadOfPFHadrons = cms.bool(False)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(1000.0),
            maxTransverseImpactParameter = cms.double(0.2),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.0),
            useTracksInsteadOfPFHadrons = cms.bool(False)
        )
    ),
    relativeSumPtCut = cms.double(0.06),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawFootprintCorrection = cms.bool(False),
    storeRawPUsumPt = cms.bool(False),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool(False),
    storeRawSumPt = cms.bool(False),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("NotUsed")
)


process.hltPFTauLooseRelativeIsolationDiscriminator = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hltPFTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    WeightECALIsolation = cms.double(1.0),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(False),
    applyRelativeSumPtCut = cms.bool(True),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(-1.0),
    deltaBetaFactor = cms.string('0.38'),
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
    isoConeSizeForDeltaBeta = cms.double(0.3),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(3.0),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("hltParticleFlowForTaus"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.05),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(5),
            minTrackPixelHits = cms.uint32(2),
            minTrackPt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False)
        ),
        primaryVertexSrc = cms.InputTag("hltPixelVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(1000.0),
            maxTransverseImpactParameter = cms.double(0.2),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.0),
            useTracksInsteadOfPFHadrons = cms.bool(False)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(1000.0),
            maxTransverseImpactParameter = cms.double(0.2),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.0),
            useTracksInsteadOfPFHadrons = cms.bool(False)
        )
    ),
    relativeSumPtCut = cms.double(0.1),
    relativeSumPtOffset = cms.double(20.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawFootprintCorrection = cms.bool(False),
    storeRawPUsumPt = cms.bool(False),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool(False),
    storeRawSumPt = cms.bool(False),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("NotUsed")
)


process.hltPFTauPiZeros = cms.EDProducer("RecoTauPiZeroProducer",
    builders = cms.VPSet(cms.PSet(
        applyElecTrackQcuts = cms.bool(False),
        makeCombinatoricStrips = cms.bool(False),
        maxStripBuildIterations = cms.int32(-1),
        minGammaEtStripAdd = cms.double(0.0),
        minGammaEtStripSeed = cms.double(0.5),
        minStripEt = cms.double(1.0),
        name = cms.string('s'),
        plugin = cms.string('RecoTauPiZeroStripPlugin2'),
        qualityCuts = cms.PSet(
            primaryVertexSrc = cms.InputTag("hltPixelVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxTrackChi2 = cms.double(1000.0),
                maxTransverseImpactParameter = cms.double(0.2),
                minGammaEt = cms.double(0.5),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.0),
                useTracksInsteadOfPFHadrons = cms.bool(False)
            ),
            vertexTrackFiltering = cms.bool(False)
        ),
        stripCandidatesParticleIds = cms.vint32(2, 4),
        stripEtaAssociationDistance = cms.double(0.05),
        stripPhiAssociationDistance = cms.double(0.2),
        updateStripAfterEachDaughter = cms.bool(False)
    )),
    jetSrc = cms.InputTag("hltAK4PFJetsForTaus"),
    massHypothesis = cms.double(0.136),
    maxJetAbsEta = cms.double(99.0),
    minJetPt = cms.double(-1.0),
    outputSelection = cms.string('pt > 0'),
    ranking = cms.VPSet(cms.PSet(
        name = cms.string('InStrip'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selection = cms.string("algoIs(\'kStrips\')"),
        selectionFailValue = cms.double(1000.0),
        selectionPassFunction = cms.string('abs(mass() - 0.13579)')
    ))
)


process.hltPFTauTrackFindingDiscriminator = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    PFTauProducer = cms.InputTag("hltPFTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.hltPFTaus = cms.EDProducer("RecoTauPiZeroUnembedder",
    src = cms.InputTag("hltPFTausSansRef")
)


process.hltPFTausSansRef = cms.EDProducer("RecoTauProducer",
    buildNullTaus = cms.bool(True),
    builders = cms.VPSet(cms.PSet(
        isoConeChargedHadrons = cms.string('0.4'),
        isoConeNeutralHadrons = cms.string('0.4'),
        isoConePiZeros = cms.string('0.4'),
        leadObjectPt = cms.double(0.5),
        matchingCone = cms.string('0.4'),
        maxSignalConeChargedHadrons = cms.int32(3),
        name = cms.string('fixedConeTau'),
        pfCandSrc = cms.InputTag("hltParticleFlowForTaus"),
        plugin = cms.string('RecoTauBuilderConePlugin'),
        qualityCuts = cms.PSet(
            primaryVertexSrc = cms.InputTag("hltPixelVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxTrackChi2 = cms.double(1000.0),
                maxTransverseImpactParameter = cms.double(0.2),
                minGammaEt = cms.double(0.5),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.0),
                useTracksInsteadOfPFHadrons = cms.bool(False)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(1000.0),
                maxTransverseImpactParameter = cms.double(0.2),
                minGammaEt = cms.double(0.5),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.0),
                useTracksInsteadOfPFHadrons = cms.bool(False)
            )
        ),
        signalConeChargedHadrons = cms.string('min(max(3.6/pt(),0.08),0.12)'),
        signalConeNeutralHadrons = cms.string('0.1'),
        signalConePiZeros = cms.string('min(max(3.6/pt(),0.08),0.12)'),
        usePFLeptons = cms.bool(True)
    )),
    chargedHadronSrc = cms.InputTag("hltTauPFJetsRecoTauChargedHadrons"),
    jetRegionSrc = cms.InputTag("hltTauPFJets08Region"),
    jetSrc = cms.InputTag("hltAK4PFJetsForTaus"),
    maxJetAbsEta = cms.double(99.0),
    minJetPt = cms.double(-1.0),
    modifiers = cms.VPSet(cms.PSet(
        DataType = cms.string('AOD'),
        EcalStripSumE_deltaEta = cms.double(0.03),
        EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
        EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
        EcalStripSumE_minClusEnergy = cms.double(0.1),
        ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
        ElectronPreIDProducer = cms.InputTag("elecpreid"),
        maximumForElectrionPreIDOutput = cms.double(-0.1),
        name = cms.string('shrinkingConeElectronRej'),
        plugin = cms.string('RecoTauElectronRejectionPlugin')
    )),
    outputSelection = cms.string(''),
    piZeroSrc = cms.InputTag("hltPFTauPiZeros")
)


process.hltParticleFlowBlockForTaus = cms.EDProducer("PFBlockProducer",
    debug = cms.untracked.bool(False),
    elementImporters = cms.VPSet(cms.PSet(
        DPtOverPtCuts_byTrackAlgo = cms.vdouble(20.0, 20.0, 20.0, 20.0, 20.0, 
            20.0),
        NHitCuts_byTrackAlgo = cms.vuint32(3, 3, 3, 3, 3, 
            3),
        importerName = cms.string('GeneralTracksImporter'),
        muonSrc = cms.InputTag("hltMuons"),
        source = cms.InputTag("hltLightPFTracks"),
        useIterativeTracking = cms.bool(False)
    ), 
        cms.PSet(
            BCtoPFCMap = cms.InputTag(""),
            importerName = cms.string('ECALClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterECALUnseeded")
        ), 
        cms.PSet(
            importerName = cms.string('GenericClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterHCAL")
        ), 
        cms.PSet(
            importerName = cms.string('GenericClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterHF")
        ), 
        cms.PSet(
            importerName = cms.string('GenericClusterImporter'),
            source = cms.InputTag("hltParticleFlowClusterPSUnseeded")
        )),
    linkDefinitions = cms.VPSet(cms.PSet(
        linkType = cms.string('PS1:ECAL'),
        linkerName = cms.string('PreshowerAndECALLinker'),
        useKDTree = cms.bool(True)
    ), 
        cms.PSet(
            linkType = cms.string('PS2:ECAL'),
            linkerName = cms.string('PreshowerAndECALLinker'),
            useKDTree = cms.bool(True)
        ), 
        cms.PSet(
            linkType = cms.string('TRACK:ECAL'),
            linkerName = cms.string('TrackAndECALLinker'),
            useKDTree = cms.bool(True)
        ), 
        cms.PSet(
            linkType = cms.string('TRACK:HCAL'),
            linkerName = cms.string('TrackAndHCALLinker'),
            useKDTree = cms.bool(True)
        ), 
        cms.PSet(
            linkType = cms.string('ECAL:HCAL'),
            linkerName = cms.string('ECALAndHCALLinker'),
            useKDTree = cms.bool(False)
        ), 
        cms.PSet(
            linkType = cms.string('HFEM:HFHAD'),
            linkerName = cms.string('HFEMAndHFHADLinker'),
            useKDTree = cms.bool(False)
        )),
    verbose = cms.untracked.bool(False)
)


process.hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            gatheringThreshold = cms.double(0.08),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            recHitEnergyNorm = cms.double(0.08)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            doubleSpikeS6S2 = cms.double(0.04),
            doubleSpikeThresh = cms.double(10.0),
            energyThresholdModifier = cms.double(2.0),
            fractionThresholdModifier = cms.double(3.0),
            minS4S1_a = cms.double(0.04),
            minS4S1_b = cms.double(-0.024),
            singleSpikeThresh = cms.double(4.0)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                doubleSpikeS6S2 = cms.double(-1.0),
                doubleSpikeThresh = cms.double(1000000000.0),
                energyThresholdModifier = cms.double(2.0),
                fractionThresholdModifier = cms.double(3.0),
                minS4S1_a = cms.double(0.02),
                minS4S1_b = cms.double(-0.0125),
                singleSpikeThresh = cms.double(15.0)
            ))
    )),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECALUnseeded"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_ENDCAP'),
            seedingThreshold = cms.double(0.6),
            seedingThresholdPt = cms.double(0.15)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.hltParticleFlowClusterECALUnseeded = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        algoName = cms.string('PFClusterEMEnergyCorrector'),
        applyCrackCorrections = cms.bool(False)
    ),
    inputECAL = cms.InputTag("hltParticleFlowClusterECALUncorrectedUnseeded"),
    inputPS = cms.InputTag("hltParticleFlowClusterPSUnseeded"),
    minimumPSEnergy = cms.double(0.0)
)


process.hltParticleFlowClusterHBHE = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            gatheringThreshold = cms.double(0.8),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThreshold = cms.double(0.8),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        clusterTimeResFromSeed = cms.bool(False),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        maxNSigmaTime = cms.double(10.0),
        minChi2Prob = cms.double(0.0),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            recHitEnergyNorm = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.8)
            )),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08),
        timeResolutionCalcBarrel = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeResolutionCalcEndcap = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeSigmaEB = cms.double(10.0),
        timeSigmaEE = cms.double(10.0)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHBHE"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            seedingThreshold = cms.double(1.0),
            seedingThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                seedingThreshold = cms.double(1.1),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.hltParticleFlowClusterHCAL = cms.EDProducer("PFMultiDepthClusterProducer",
    clustersSource = cms.InputTag("hltParticleFlowClusterHBHE"),
    energyCorrector = cms.PSet(

    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('PFMultiDepthClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        minFractionToKeep = cms.double(1e-07),
        nSigmaEta = cms.double(2.0),
        nSigmaPhi = cms.double(2.0)
    ),
    positionReCalc = cms.PSet(

    )
)


process.hltParticleFlowClusterHF = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            gatheringThreshold = cms.double(0.8),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                gatheringThreshold = cms.double(0.8),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            recHitEnergyNorm = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                recHitEnergyNorm = cms.double(0.8)
            )),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            doubleSpikeS6S2 = cms.double(-1.0),
            doubleSpikeThresh = cms.double(1000000000.0),
            energyThresholdModifier = cms.double(1.0),
            fractionThresholdModifier = cms.double(1.0),
            minS4S1_a = cms.double(0.11),
            minS4S1_b = cms.double(-0.19),
            singleSpikeThresh = cms.double(80.0)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                doubleSpikeS6S2 = cms.double(-1.0),
                doubleSpikeThresh = cms.double(1000000000.0),
                energyThresholdModifier = cms.double(1.0),
                fractionThresholdModifier = cms.double(1.0),
                minS4S1_a = cms.double(0.045),
                minS4S1_b = cms.double(-0.08),
                singleSpikeThresh = cms.double(120.0)
            ))
    )),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHF"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(0),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            seedingThreshold = cms.double(1.4),
            seedingThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                seedingThreshold = cms.double(1.4),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.hltParticleFlowClusterPSUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            gatheringThreshold = cms.double(6e-05),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            recHitEnergyNorm = cms.double(6e-05)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitPSUnseeded"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            seedingThreshold = cms.double(0.00012),
            seedingThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.hltParticleFlowForTaus = cms.EDProducer("PFProducer",
    GedElectronValueMap = cms.InputTag("gedGsfElectronsTmp"),
    GedPhotonValueMap = cms.InputTag("tmpGedPhotons","valMapPFEgammaCandToPhoton"),
    PFEGammaCandidates = cms.InputTag("particleFlowEGamma"),
    X0_Map = cms.string('RecoParticleFlow/PFProducer/data/allX0histos.root'),
    algoType = cms.uint32(0),
    blocks = cms.InputTag("hltParticleFlowBlockForTaus"),
    calibHF_a_EMHAD = cms.vdouble(1.42215, 1.00496, 0.68961, 0.81656, 0.98504, 
        0.98504, 1.00802, 1.0593, 1.4576, 1.4576),
    calibHF_a_EMonly = cms.vdouble(0.96945, 0.96701, 0.76309, 0.82268, 0.87583, 
        0.89718, 0.98674, 1.4681, 1.458, 1.458),
    calibHF_b_EMHAD = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    calibHF_b_HADonly = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    calibHF_eta_step = cms.vdouble(0.0, 2.9, 3.0, 3.2, 4.2, 
        4.4, 4.6, 4.8, 5.2, 5.4),
    calibHF_use = cms.bool(False),
    calibPFSCEle_Fbrem_barrel = cms.vdouble(0.6, 6.0, -0.0255975, 0.0576727, 0.975442, 
        -0.000546394, 1.26147, 25.0, -0.02025, 0.04537, 
        0.9728, -0.0008962, 1.172),
    calibPFSCEle_Fbrem_endcap = cms.vdouble(0.9, 6.5, -0.0692932, 0.101776, 0.995338, 
        -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 
        0.923165, 0.000474665, 1.10782),
    calibPFSCEle_barrel = cms.vdouble(1.004, -1.536, 22.88, -1.467, 0.3555, 
        0.6227, 14.65, 2051.0, 25.0, 0.9932, 
        -0.5444, 0.0, 0.5438, 0.7109, 7.645, 
        0.2904, 0.0),
    calibPFSCEle_endcap = cms.vdouble(1.153, -16.5975, 5.668, -0.1772, 16.22, 
        7.326, 0.0483, -4.068, 9.406),
    calibrationsLabel = cms.string('HLT'),
    cleanedHF = cms.VInputTag("hltParticleFlowRecHitHF:Cleaned", "hltParticleFlowClusterHF:Cleaned"),
    coneEcalIsoForEgammaSC = cms.double(0.3),
    coneTrackIsoForEgammaSC = cms.double(0.3),
    cosmicRejectionDistance = cms.double(1.0),
    debug = cms.untracked.bool(False),
    dptRel_DispVtx = cms.double(10.0),
    dzPV = cms.double(0.2),
    egammaElectrons = cms.InputTag(""),
    electron_iso_combIso_barrel = cms.double(10.0),
    electron_iso_combIso_endcap = cms.double(10.0),
    electron_iso_mva_barrel = cms.double(-0.1875),
    electron_iso_mva_endcap = cms.double(-0.1075),
    electron_iso_pt = cms.double(10.0),
    electron_missinghits = cms.uint32(1),
    electron_noniso_mvaCut = cms.double(-0.1),
    electron_protectionsForJetMET = cms.PSet(
        maxDPhiIN = cms.double(0.1),
        maxE = cms.double(50.0),
        maxEcalEOverPRes = cms.double(0.2),
        maxEcalEOverP_1 = cms.double(0.5),
        maxEcalEOverP_2 = cms.double(0.2),
        maxEeleOverPout = cms.double(0.2),
        maxEeleOverPoutRes = cms.double(0.5),
        maxEleHcalEOverEcalE = cms.double(0.1),
        maxHcalE = cms.double(10.0),
        maxHcalEOverEcalE = cms.double(0.1),
        maxHcalEOverP = cms.double(1.0),
        maxNtracks = cms.double(3.0),
        maxTrackPOverEele = cms.double(1.0)
    ),
    eventFactorForCosmics = cms.double(10.0),
    eventFractionForCleaning = cms.double(0.5),
    eventFractionForRejection = cms.double(0.8),
    factors_45 = cms.vdouble(10.0, 100.0),
    iCfgCandConnector = cms.PSet(
        bCalibPrimary = cms.bool(False),
        bCalibSecondary = cms.bool(False),
        bCorrect = cms.bool(False),
        nuclCalibFactors = cms.vdouble(0.8, 0.15, 0.5, 0.5, 0.05)
    ),
    isolatedElectronID_mvaWeightFile = cms.string('RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml'),
    maxDPtOPt = cms.double(1.0),
    maxDeltaPhiPt = cms.double(7.0),
    maxSignificance = cms.double(2.5),
    metFactorForCleaning = cms.double(4.0),
    metFactorForFakes = cms.double(4.0),
    metFactorForHighEta = cms.double(25.0),
    metFactorForRejection = cms.double(4.0),
    metSignificanceForCleaning = cms.double(3.0),
    metSignificanceForRejection = cms.double(4.0),
    minDeltaMet = cms.double(0.4),
    minEnergyForPunchThrough = cms.double(100.0),
    minHFCleaningPt = cms.double(5.0),
    minMomentumForPunchThrough = cms.double(100.0),
    minPixelHits = cms.int32(1),
    minPtForPostCleaning = cms.double(20.0),
    minSignificance = cms.double(2.5),
    minSignificanceReduction = cms.double(1.4),
    minTrackerHits = cms.int32(8),
    muon_ECAL = cms.vdouble(0.5, 0.5),
    muon_HCAL = cms.vdouble(3.0, 3.0),
    muon_HO = cms.vdouble(0.9, 0.9),
    muons = cms.InputTag("hltMuons"),
    nTrackIsoForEgammaSC = cms.uint32(2),
    nsigma_TRACK = cms.double(1.0),
    pf_GlobC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFGlobalCorr_14Dec2011.root'),
    pf_Res_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFRes_14Dec2011.root'),
    pf_convID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt'),
    pf_conv_mvaCut = cms.double(0.0),
    pf_electronID_crackCorrection = cms.bool(False),
    pf_electronID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt'),
    pf_electron_mvaCut = cms.double(-0.1),
    pf_electron_output_col = cms.string('electrons'),
    pf_locC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFClusterLCorr_14Dec2011.root'),
    pf_nsigma_ECAL = cms.double(0.0),
    pf_nsigma_HCAL = cms.double(1.0),
    photon_HoE = cms.double(0.05),
    photon_MinEt = cms.double(10.0),
    photon_SigmaiEtaiEta_barrel = cms.double(0.0125),
    photon_SigmaiEtaiEta_endcap = cms.double(0.034),
    photon_combIso = cms.double(10.0),
    photon_protectionsForJetMET = cms.PSet(
        sumPtTrackIso = cms.double(2.0),
        sumPtTrackIsoSlope = cms.double(0.001)
    ),
    postHFCleaning = cms.bool(False),
    postMuonCleaning = cms.bool(True),
    ptErrorScale = cms.double(8.0),
    ptFactorForHighEta = cms.double(2.0),
    pt_Error = cms.double(1.0),
    punchThroughFactor = cms.double(3.0),
    punchThroughMETFactor = cms.double(4.0),
    rejectTracks_Bad = cms.bool(False),
    rejectTracks_Step45 = cms.bool(False),
    sumEtEcalIsoForEgammaSC_barrel = cms.double(1.0),
    sumEtEcalIsoForEgammaSC_endcap = cms.double(2.0),
    sumPtTrackIsoForEgammaSC_barrel = cms.double(4.0),
    sumPtTrackIsoForEgammaSC_endcap = cms.double(4.0),
    sumPtTrackIsoForPhoton = cms.double(-1.0),
    sumPtTrackIsoSlopeForPhoton = cms.double(-1.0),
    trackQuality = cms.string('highPurity'),
    useCalibrationsFromDB = cms.bool(True),
    useEGammaElectrons = cms.bool(False),
    useEGammaFilters = cms.bool(False),
    useEGammaSupercluster = cms.bool(False),
    useHO = cms.bool(False),
    usePFConversions = cms.bool(False),
    usePFDecays = cms.bool(False),
    usePFElectrons = cms.bool(False),
    usePFNuclearInteractions = cms.bool(False),
    usePFPhotons = cms.bool(False),
    usePFSCEleCalib = cms.bool(True),
    usePhotonReg = cms.bool(False),
    useProtectionsForJetMET = cms.bool(True),
    useRegressionFromDB = cms.bool(False),
    useVerticesForNeutral = cms.bool(True),
    verbose = cms.untracked.bool(False),
    vertexCollection = cms.InputTag("hltPixelVertices")
)


process.hltParticleFlowRecHitECALUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFEBRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(0.08)
        ), 
            cms.PSet(
                cleaningThreshold = cms.double(2.0),
                name = cms.string('PFRecHitQTestECAL'),
                skipTTRecoveredHits = cms.bool(True),
                timingCleaning = cms.bool(True),
                topologicalCleaning = cms.bool(True)
            )),
        srFlags = cms.InputTag("hltEcalDigis"),
        src = cms.InputTag("hltEcalRecHit","EcalRecHitsEB")
    ), 
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                name = cms.string('PFRecHitQTestThreshold'),
                threshold = cms.double(0.3)
            ), 
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )),
            srFlags = cms.InputTag("hltEcalDigis"),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEE")
        ))
)


process.hltParticleFlowRecHitHBHE = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitHCALNavigator'),
        sigmaCut = cms.double(4.0),
        timeResolutionCalc = cms.PSet(
            constantTerm = cms.double(1.92),
            constantTermLowE = cms.double(6.0),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(8.64),
            noiseTermLowE = cms.double(0.0),
            threshHighE = cms.double(8.0),
            threshLowE = cms.double(2.0)
        )
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFHBHERecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(0.8)
        ), 
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                maxSeverities = cms.vint32(11),
                name = cms.string('PFRecHitQTestHCALChannel')
            )),
        src = cms.InputTag("hltHbhereco")
    ))
)


process.hltParticleFlowRecHitHCAL = cms.EDProducer("PFCTRecHitProducer",
    ApplyLongShortDPG = cms.bool(True),
    ApplyPulseDPG = cms.bool(False),
    ApplyTimeDPG = cms.bool(False),
    ECAL_Compensate = cms.bool(False),
    ECAL_Compensation = cms.double(0.5),
    ECAL_Dead_Code = cms.uint32(10),
    ECAL_Threshold = cms.double(10.0),
    EM_Depth = cms.double(22.0),
    HAD_Depth = cms.double(47.0),
    HCAL_Calib = cms.bool(True),
    HCAL_Calib_29 = cms.double(1.35),
    HF_Calib = cms.bool(True),
    HF_Calib_29 = cms.double(1.07),
    HcalMaxAllowedChannelStatusSev = cms.int32(9),
    HcalMaxAllowedHFDigiTimeSev = cms.int32(9),
    HcalMaxAllowedHFInTimeWindowSev = cms.int32(9),
    HcalMaxAllowedHFLongShortSev = cms.int32(9),
    LongFibre_Cut = cms.double(120.0),
    LongFibre_Fraction = cms.double(0.1),
    LongShortFibre_Cut = cms.double(1000000000.0),
    MaxLongTiming_Cut = cms.double(5.0),
    MaxShortTiming_Cut = cms.double(5.0),
    MinLongTiming_Cut = cms.double(-5.0),
    MinShortTiming_Cut = cms.double(-5.0),
    ShortFibre_Cut = cms.double(60.0),
    ShortFibre_Fraction = cms.double(0.01),
    caloTowers = cms.InputTag("hltTowerMakerForPF"),
    hcalRecHitsHBHE = cms.InputTag("hltHbhereco"),
    hcalRecHitsHF = cms.InputTag("hltHfreco"),
    navigation_HF = cms.bool(True),
    navigator = cms.PSet(
        name = cms.string('PFRecHitCaloTowerNavigator')
    ),
    thresh_Barrel = cms.double(0.4),
    thresh_Endcap = cms.double(0.4),
    thresh_HF = cms.double(0.4),
    weight_HFem = cms.double(1.0),
    weight_HFhad = cms.double(1.0)
)


process.hltParticleFlowRecHitHF = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitHCALNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        EMDepthCorrection = cms.double(22.0),
        HADDepthCorrection = cms.double(25.0),
        HFCalib29 = cms.double(1.07),
        LongFibre_Cut = cms.double(120.0),
        LongFibre_Fraction = cms.double(0.1),
        ShortFibre_Cut = cms.double(60.0),
        ShortFibre_Fraction = cms.double(0.01),
        name = cms.string('PFHFRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            cleaningThresholds = cms.vdouble(0.0, 120.0, 60.0),
            flags = cms.vstring('Standard', 
                'HFLong', 
                'HFShort'),
            maxSeverities = cms.vint32(11, 9, 9),
            name = cms.string('PFRecHitQTestHCALChannel')
        ), 
            cms.PSet(
                cuts = cms.VPSet(cms.PSet(
                    depth = cms.int32(1),
                    threshold = cms.double(1.2)
                ), 
                    cms.PSet(
                        depth = cms.int32(2),
                        threshold = cms.double(1.8)
                    )),
                name = cms.string('PFRecHitQTestHCALThresholdVsDepth')
            )),
        src = cms.InputTag("hltHfreco"),
        thresh_HF = cms.double(0.4)
    ))
)


process.hltParticleFlowRecHitPSUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(7e-06)
        )),
        src = cms.InputTag("hltEcalPreshowerRecHit","EcalRecHitsES")
    ))
)


process.hltPixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg')
)


process.hltPixelLayerQuadruplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3+BPix4', 
        'BPix1+BPix2+BPix3+FPix1_pos', 
        'BPix1+BPix2+BPix3+FPix1_neg', 
        'BPix1+BPix2+FPix1_pos+FPix2_pos', 
        'BPix1+BPix2+FPix1_neg+FPix2_neg', 
        'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
        'BPix1+FPix1_neg+FPix2_neg+FPix3_neg')
)


process.hltPixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix2+BPix3+BPix4', 
        'BPix1+BPix3+BPix4', 
        'BPix1+BPix2+BPix4', 
        'BPix2+BPix3+FPix1_pos', 
        'BPix2+BPix3+FPix1_neg', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix2_pos+FPix3_pos', 
        'FPix1_neg+FPix2_neg+FPix3_neg')
)


process.hltPixelTracks = cms.EDProducer("PixelTrackProducer",
    Cleaner = cms.string('hltPixelTracksCleanerBySharedHits'),
    Filter = cms.InputTag("hltPixelTracksFilter"),
    Fitter = cms.InputTag("hltPixelTracksFitter"),
    SeedingHitSets = cms.InputTag("hltPixelTracksHitQuadruplets"),
    passLabel = cms.string('')
)


process.hltPixelTracksFilter = cms.EDProducer("PixelTrackFilterByKinematicsProducer",
    chi2 = cms.double(1000.0),
    nSigmaInvPtTolerance = cms.double(0.0),
    nSigmaTipMaxTolerance = cms.double(0.0),
    ptMin = cms.double(0.1),
    tipMax = cms.double(1.0)
)


process.hltPixelTracksFitter = cms.EDProducer("PixelFitterByHelixProjectionsProducer")


process.hltPixelTracksHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("hltPixelLayerQuadruplets"),
    trackingRegions = cms.InputTag("hltPixelTracksTrackingRegions")
)


process.hltPixelTracksHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0.0),
    CAOnlyOneLastHitPerLayerFilter = cms.bool(False),
    CAPhiCut = cms.double(0.2),
    CAThetaCut = cms.double(0.002),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("hltSiPixelClustersCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("hltPixelTracksHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2.0),
        value1 = cms.double(200.0),
        value2 = cms.double(50.0)
    ),
    useBendingCorrection = cms.bool(True)
)


process.hltPixelTracksTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        nSigmaZ = cms.double(4.0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.8)
    )
)


process.hltPixelVertices = cms.EDProducer("PixelVertexProducer",
    Finder = cms.string('DivisiveVertexFinder'),
    Method2 = cms.bool(True),
    NTrkMin = cms.int32(2),
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    ),
    PtMin = cms.double(1.0),
    TrackCollection = cms.InputTag("hltPixelTracks"),
    UseError = cms.bool(True),
    Verbosity = cms.int32(0),
    WtAverage = cms.bool(True),
    ZOffset = cms.double(5.0),
    ZSeparation = cms.double(0.05),
    beamSpot = cms.InputTag("hltOnlineBeamSpot")
)


process.hltRpcRecHits = cms.EDProducer("RPCRecHitProducer",
    deadSource = cms.string('File'),
    deadvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat'),
    maskSource = cms.string('File'),
    maskvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat'),
    recAlgo = cms.string('RPCRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    ),
    rpcDigiLabel = cms.InputTag("hltMuonRPCDigis")
)


process.hltScalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    scalersInputTag = cms.InputTag("rawDataCollector")
)


process.hltSiPixelClusters = cms.EDProducer("SiPixelClusterProducer",
    ChannelThreshold = cms.int32(1000),
    ClusterThreshold = cms.double(4000.0),
    MissCalibrate = cms.untracked.bool(True),
    SeedThreshold = cms.int32(1000),
    SplitClusters = cms.bool(False),
    VCaltoElectronGain = cms.int32(65),
    VCaltoElectronOffset = cms.int32(-414),
    maxNumberOfClusters = cms.int32(40000),
    payloadType = cms.string('HLT'),
    src = cms.InputTag("hltSiPixelDigis")
)


process.hltSiPixelClustersCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelDigis = cms.EDProducer("SiPixelRawToDigi",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(),
    IncludeErrors = cms.bool(False),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    Timing = cms.untracked.bool(False),
    UsePhase1 = cms.bool(True),
    UsePilotBlade = cms.bool(False),
    UseQualityInfo = cms.bool(False),
    UserErrorList = cms.vint32()
)


process.hltSiPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('hltESPPixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiStripClusters = cms.EDProducer("MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    measurementTracker = cms.string('hltESPMeasurementTracker'),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string('hltSiStripRawToClustersFacility'),
    switchOffPixelsIfEmpty = cms.bool(True)
)


process.hltSiStripExcludedFEDListProducer = cms.EDProducer("SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag("rawDataCollector")
)


process.hltSiStripRawToClustersFacility = cms.EDProducer("SiStripClusterizerFromRaw",
    Algorithms = cms.PSet(
        CommonModeNoiseSubtractionMode = cms.string('Median'),
        PedestalSubtractionFedMode = cms.bool(True),
        SiStripFedZeroSuppressionMode = cms.uint32(4),
        TruncateInSuppressor = cms.bool(True),
        doAPVRestore = cms.bool(False),
        useCMMeanMap = cms.bool(False)
    ),
    Clusterizer = cms.PSet(
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        ChannelThreshold = cms.double(2.0),
        ClusterThreshold = cms.double(5.0),
        MaxAdjacentBad = cms.uint32(0),
        MaxSequentialBad = cms.uint32(1),
        MaxSequentialHoles = cms.uint32(0),
        QualityLabel = cms.string(''),
        RemoveApvShots = cms.bool(True),
        SeedThreshold = cms.double(3.0),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
        ),
        setDetId = cms.bool(True)
    ),
    DoAPVEmulatorCheck = cms.bool(False),
    ProductLabel = cms.InputTag("rawDataCollector"),
    onDemand = cms.bool(True)
)


process.hltTauPFJets08Region = cms.EDProducer("RecoTauJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(99.0),
    minJetPt = cms.double(-1.0),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("hltParticleFlowForTaus"),
    src = cms.InputTag("hltAK4PFJetsForTaus")
)


process.hltTauPFJetsRecoTauChargedHadrons = cms.EDProducer("PFRecoTauChargedHadronProducer",
    builders = cms.VPSet(cms.PSet(
        chargedHadronCandidatesParticleIds = cms.vint32(1, 2, 3),
        dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
        dRmergeNeutralHadronWrtElectron = cms.double(0.05),
        dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
        dRmergeNeutralHadronWrtOther = cms.double(0.005),
        dRmergePhotonWrtChargedHadron = cms.double(0.005),
        dRmergePhotonWrtElectron = cms.double(0.005),
        dRmergePhotonWrtNeutralHadron = cms.double(0.01),
        dRmergePhotonWrtOther = cms.double(0.005),
        maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
        maxUnmatchedBlockElementsPhoton = cms.int32(1),
        minBlockElementMatchesNeutralHadron = cms.int32(2),
        minBlockElementMatchesPhoton = cms.int32(2),
        minMergeChargedHadronPt = cms.double(100.0),
        minMergeGammaEt = cms.double(0.0),
        minMergeNeutralHadronEt = cms.double(0.0),
        name = cms.string('chargedPFCandidates'),
        plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
        qualityCuts = cms.PSet(
            primaryVertexSrc = cms.InputTag("hltPixelVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxTrackChi2 = cms.double(1000.0),
                maxTransverseImpactParameter = cms.double(0.2),
                minGammaEt = cms.double(0.5),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.0),
                useTracksInsteadOfPFHadrons = cms.bool(False)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(1000.0),
                maxTransverseImpactParameter = cms.double(0.2),
                minGammaEt = cms.double(0.5),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.0),
                useTracksInsteadOfPFHadrons = cms.bool(False)
            )
        )
    )),
    jetSrc = cms.InputTag("hltAK4PFJetsForTaus"),
    maxJetAbsEta = cms.double(99.0),
    minJetPt = cms.double(-1.0),
    outputSelection = cms.string('pt > 0.5'),
    ranking = cms.VPSet(cms.PSet(
        name = cms.string('ChargedPFCandidate'),
        plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
        selection = cms.string("algoIs(\'kChargedPFCandidate\')"),
        selectionFailValue = cms.double(1000.0),
        selectionPassFunction = cms.string('-pt')
    ))
)


process.hltTowerMakerForPF = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(),
    EEGrid = cms.vdouble(),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring('kTime', 
        'kWeird', 
        'kBad'),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(),
    HBThreshold = cms.double(0.4),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(),
    HEDGrid = cms.vdouble(),
    HEDThreshold = cms.double(0.4),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(),
    HESGrid = cms.vdouble(),
    HESThreshold = cms.double(0.4),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(),
    HF1Grid = cms.vdouble(),
    HF1Threshold = cms.double(1.2),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(),
    HF2Grid = cms.vdouble(),
    HF2Threshold = cms.double(1.8),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(),
    HOGrid = cms.vdouble(),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(1.1),
    HOThresholdMinus2 = cms.double(1.1),
    HOThresholdPlus1 = cms.double(1.1),
    HOThresholdPlus2 = cms.double(1.1),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(),
    HcalAcceptSeverityLevel = cms.uint32(11),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalPhase = cms.int32(0),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(False),
    UseSymEBTreshold = cms.bool(False),
    UseSymEETreshold = cms.bool(False),
    ecalInputs = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE"),
    hbheInput = cms.InputTag("hltHbhereco"),
    hfInput = cms.InputTag("hltHfreco"),
    hoInput = cms.InputTag("hltHoreco")
)


process.hltTrackIter0RefsForJets4Iter1 = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity")
)


process.hltTriggerSummaryAOD = cms.EDProducer("TriggerSummaryProducerAOD",
    moduleLabelPatternsToMatch = cms.vstring('hlt*'),
    moduleLabelPatternsToSkip = cms.vstring(),
    processName = cms.string('@')
)


process.hltTriggerSummaryRAW = cms.EDProducer("TriggerSummaryProducerRAW",
    processName = cms.string('@')
)


process.hltTrimmedPixelVertices = cms.EDProducer("PixelVertexCollectionTrimmer",
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    ),
    fractionSumPt2 = cms.double(0.3),
    maxVtx = cms.uint32(100),
    minSumPt2 = cms.double(0.0),
    src = cms.InputTag("hltPixelVertices")
)


process.packCaloStage2 = cms.EDProducer("L1TDigiToRaw",
    FWId = cms.uint32(1),
    FedId = cms.int32(1366),
    InputLabel = cms.InputTag("simCaloStage2Digis"),
    Setup = cms.string('stage2::CaloSetup'),
    TowerInputLabel = cms.InputTag("simCaloStage2Layer1Digis"),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.packGmtStage2 = cms.EDProducer("L1TDigiToRaw",
    BMTFInputLabel = cms.InputTag("simBmtfDigis","BMTF"),
    EMTFInputLabel = cms.InputTag("simEmtfDigis","EMTF"),
    FWId = cms.uint32(67174400),
    FedId = cms.int32(1402),
    ImdInputLabelBMTF = cms.InputTag("simGmtStage2Digis","imdMuonsBMTF"),
    ImdInputLabelEMTFNeg = cms.InputTag("simGmtStage2Digis","imdMuonsEMTFNeg"),
    ImdInputLabelEMTFPos = cms.InputTag("simGmtStage2Digis","imdMuonsEMTFPos"),
    ImdInputLabelOMTFNeg = cms.InputTag("simGmtStage2Digis","imdMuonsOMTFNeg"),
    ImdInputLabelOMTFPos = cms.InputTag("simGmtStage2Digis","imdMuonsOMTFPos"),
    InputLabel = cms.InputTag("simGmtStage2Digis"),
    OMTFInputLabel = cms.InputTag("simOmtfDigis","OMTF"),
    Setup = cms.string('stage2::GMTSetup'),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.packGtStage2 = cms.EDProducer("L1TDigiToRaw",
    EGammaInputTag = cms.InputTag("simCaloStage2Digis"),
    EtSumInputTag = cms.InputTag("simCaloStage2Digis"),
    ExtInputTag = cms.InputTag("simGtExtFakeStage2Digis"),
    FWId = cms.uint32(4262),
    FedId = cms.int32(1404),
    GtInputTag = cms.InputTag("simGtStage2Digis"),
    JetInputTag = cms.InputTag("simCaloStage2Digis"),
    MuonInputTag = cms.InputTag("simGmtStage2Digis"),
    Setup = cms.string('stage2::GTSetup'),
    TauInputTag = cms.InputTag("simCaloStage2Digis"),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.rawDataCollector = cms.EDProducer("RawDataCollectorByLabel",
    RawCollectionList = cms.VInputTag(cms.InputTag("packCaloStage2"), cms.InputTag("packGmtStage2"), cms.InputTag("packGtStage2"), cms.InputTag("rawDataCollector","","@skipCurrentProcess")),
    verbose = cms.untracked.int32(0)
)


process.simBmtfDigis = cms.EDProducer("L1TMuonBarrelTrackProducer",
    DTDigi_Source = cms.InputTag("simTwinMuxDigis"),
    DTDigi_Theta_Source = cms.InputTag("simDtTriggerPrimitiveDigis"),
    Debug = cms.untracked.int32(0)
)


process.simCaloStage2Digis = cms.EDProducer("L1TStage2Layer2Producer",
    firmware = cms.int32(1),
    towerToken = cms.InputTag("simCaloStage2Layer1Digis")
)


process.simCaloStage2Layer1Digis = cms.EDProducer("L1TCaloLayer1",
    ecalToken = cms.InputTag("unpackEcal","EcalTriggerPrimitives"),
    firmwareVersion = cms.int32(1),
    hcalToken = cms.InputTag("simHcalTriggerPrimitiveDigis"),
    unpackEcalMask = cms.bool(False),
    unpackHcalMask = cms.bool(False),
    useCalib = cms.bool(True),
    useECALLUT = cms.bool(True),
    useHCALLUT = cms.bool(True),
    useHFLUT = cms.bool(True),
    useLSB = cms.bool(True),
    verbose = cms.bool(False)
)


process.simCscTriggerPrimitiveDigis = cms.EDProducer("CSCTriggerPrimitivesProducer",
    CSCComparatorDigiProducer = cms.InputTag("unpackCSC","MuonCSCComparatorDigi"),
    CSCWireDigiProducer = cms.InputTag("unpackCSC","MuonCSCWireDigi"),
    MaxBX = cms.int32(9),
    MinBX = cms.int32(3),
    alctParam07 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(4),
        alctGhostCancellationSideQuality = cms.bool(False),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(False),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(4),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    alctParamMTCC = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(3),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctL1aWindowWidth = cms.uint32(3),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(2),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(2),
        alctTrigMode = cms.uint32(2),
        verbosity = cms.int32(0)
    ),
    alctParamOldMC = cms.PSet(
        alctAccelMode = cms.uint32(1),
        alctDriftDelay = cms.uint32(3),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctL1aWindowWidth = cms.uint32(5),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(2),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(2),
        alctTrigMode = cms.uint32(3),
        verbosity = cms.int32(0)
    ),
    alctSLHC = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    checkBadChambers = cms.bool(False),
    clctParam07 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(10),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctStartBxShift = cms.int32(0),
        verbosity = cms.int32(0)
    ),
    clctParamMTCC = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(6),
        clctMinSeparation = cms.uint32(10),
        clctNplanesHitPattern = cms.uint32(1),
        clctNplanesHitPretrig = cms.uint32(4),
        clctPidThreshPretrig = cms.uint32(2),
        verbosity = cms.int32(0)
    ),
    clctParamOldMC = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(6),
        clctMinSeparation = cms.uint32(10),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(2),
        clctPidThreshPretrig = cms.uint32(2),
        verbosity = cms.int32(0)
    ),
    clctSLHC = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(4),
        clctPretriggerTriggerZone = cms.uint32(5),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(8),
        clctUseCorrectedBx = cms.bool(True),
        useDeadTimeZoning = cms.bool(True),
        useDynamicStateMachineZone = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    commonParam = cms.PSet(
        disableME1a = cms.bool(False),
        disableME42 = cms.bool(False),
        gangedME1a = cms.bool(False),
        isMTCC = cms.bool(False),
        isSLHC = cms.bool(False),
        isTMB07 = cms.bool(True),
        smartME1aME1b = cms.bool(False)
    ),
    debugParameters = cms.bool(True),
    mpcRun2 = cms.PSet(
        dropInvalidStubs = cms.bool(False),
        dropLowQualityStubs = cms.bool(False),
        sortStubs = cms.bool(False)
    ),
    mpcSLHC = cms.PSet(
        dropInvalidStubs = cms.bool(False),
        dropLowQualityStubs = cms.bool(False),
        mpcMaxStubs = cms.uint32(18),
        sortStubs = cms.bool(False)
    ),
    tmbParam = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctTrigEnable = cms.uint32(0),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        mpcBlockMe1a = cms.uint32(0),
        tmbDropUsedAlcts = cms.bool(True),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    tmbSLHC = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctToAlct = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        matchEarliestAlctME11Only = cms.bool(False),
        matchEarliestClctME11Only = cms.bool(False),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(3),
        maxME11LCTs = cms.uint32(2),
        mpcBlockMe1a = cms.uint32(0),
        tmbCrossBxAlgorithm = cms.uint32(1),
        tmbDropUsedAlcts = cms.bool(False),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(False),
        verbosity = cms.int32(0)
    )
)


process.simDtTriggerPrimitiveDigis = cms.EDProducer("DTTrigProd",
    DTTFSectorNumbering = cms.bool(True),
    debug = cms.untracked.bool(False),
    digiTag = cms.InputTag("unpackDT"),
    lutBtic = cms.untracked.int32(31),
    lutDumpFlag = cms.untracked.bool(False)
)


process.simEmtfDigis = cms.EDProducer("L1TMuonEndCapTrackProducer",
    CSCInput = cms.InputTag("unpackEmtf"),
    CSCInputBxShift = cms.untracked.int32(0),
    RPCInput = cms.InputTag("unpackRPC")
)


process.simGmtCaloSumDigis = cms.EDProducer("L1TMuonCaloSumProducer",
    caloStage2Layer2Label = cms.InputTag("simCaloStage2Layer1Digis")
)


process.simGmtStage2Digis = cms.EDProducer("L1TMuonProducer",
    autoBxRange = cms.bool(True),
    barrelTFInput = cms.InputTag("simBmtfDigis","BMTF"),
    bxMax = cms.int32(2),
    bxMin = cms.int32(-2),
    forwardTFInput = cms.InputTag("simEmtfDigis","EMTF"),
    overlapTFInput = cms.InputTag("simOmtfDigis","OMTF"),
    triggerTowerInput = cms.InputTag("simGmtCaloSumDigis","TriggerTowerSums")
)


process.simGtExtFakeStage2Digis = cms.EDProducer("L1TExtCondProducer",
    bxFirst = cms.int32(-2),
    bxLast = cms.int32(2),
    setBptxAND = cms.bool(True),
    setBptxMinus = cms.bool(True),
    setBptxOR = cms.bool(True),
    setBptxPlus = cms.bool(True)
)


process.simGtStage2Digis = cms.EDProducer("L1TGlobalProducer",
    AlgorithmTriggersUnmasked = cms.bool(True),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    EGammaInputTag = cms.InputTag("simCaloStage2Digis"),
    EtSumInputTag = cms.InputTag("simCaloStage2Digis"),
    ExtInputTag = cms.InputTag("simGtExtFakeStage2Digis"),
    JetInputTag = cms.InputTag("simCaloStage2Digis"),
    MuonInputTag = cms.InputTag("simGmtStage2Digis"),
    TauInputTag = cms.InputTag("simCaloStage2Digis")
)


process.simHcalTriggerPrimitiveDigis = cms.EDProducer("HcalTrigPrimDigiProducer",
    FG_HF_threshold = cms.uint32(17),
    FG_threshold = cms.uint32(12),
    FrontEndFormatError = cms.bool(False),
    HFTPScaleShift = cms.PSet(
        NCT = cms.int32(1),
        RCT = cms.int32(3)
    ),
    InputTagFEDRaw = cms.InputTag("rawDataCollector"),
    LSConfig = cms.untracked.PSet(
        HcalFeatureHFEMBit = cms.bool(False),
        Long_Short_Offset = cms.double(10.1),
        Long_vrs_Short_Slope = cms.double(100.2),
        Min_Long_Energy = cms.double(10),
        Min_Short_Energy = cms.double(10)
    ),
    MinSignalThreshold = cms.uint32(0),
    PMTNoiseThreshold = cms.uint32(0),
    PeakFinderAlgorithm = cms.int32(2),
    RunZS = cms.bool(False),
    ZS_threshold = cms.uint32(1),
    inputLabel = cms.VInputTag(cms.InputTag("simHcalUnsuppressedDigis"), cms.InputTag("simHcalUnsuppressedDigis")),
    inputUpgradeLabel = cms.VInputTag(cms.InputTag("simHcalUnsuppressedDigis","HBHEQIE11DigiCollection"), cms.InputTag("simHcalUnsuppressedDigis","HFQIE10DigiCollection")),
    latency = cms.int32(1),
    numberOfPresamples = cms.int32(2),
    numberOfPresamplesHF = cms.int32(1),
    numberOfSamples = cms.int32(4),
    numberOfSamplesHF = cms.int32(2),
    peakFilter = cms.bool(True),
    upgradeHB = cms.bool(False),
    upgradeHE = cms.bool(True),
    upgradeHF = cms.bool(True),
    weights = cms.vdouble(1.0, 1.0)
)


process.simOmtfDigis = cms.EDProducer("L1TMuonOverlapTrackProducer",
    XMLDumpFileName = cms.string('TestEvents.xml'),
    dropCSCPrimitives = cms.bool(False),
    dropDTPrimitives = cms.bool(False),
    dropRPCPrimitives = cms.bool(False),
    dumpDetailedResultToXML = cms.bool(False),
    dumpGPToXML = cms.bool(False),
    dumpResultToXML = cms.bool(False),
    eventsXMLFiles = cms.vstring('TestEvents.xml'),
    readEventsFromXML = cms.bool(False),
    srcCSC = cms.InputTag("unpackCsctf"),
    srcDTPh = cms.InputTag("simDtTriggerPrimitiveDigis"),
    srcDTTh = cms.InputTag("simDtTriggerPrimitiveDigis"),
    srcRPC = cms.InputTag("unpackRPC")
)


process.simTwinMuxDigis = cms.EDProducer("L1TTwinMuxProducer",
    DTDigi_Source = cms.InputTag("simDtTriggerPrimitiveDigis"),
    DTThetaDigi_Source = cms.InputTag("simDtTriggerPrimitiveDigis"),
    RPC_Source = cms.InputTag("unpackRPC")
)


process.unpackBmtf = cms.EDProducer("L1TRawToDigi",
    FWId = cms.uint32(1),
    FedIds = cms.vint32(1376, 1377),
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    Setup = cms.string('stage2::BMTFSetup'),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.unpackCSC = cms.EDProducer("CSCDCCUnpacker",
    Debug = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535557110),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    runDQM = cms.untracked.bool(False)
)


process.unpackCsctf = cms.EDProducer("CSCTFUnpacker",
    MaxBX = cms.int32(9),
    MinBX = cms.int32(3),
    mappingFile = cms.string(''),
    producer = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    slot2sector = cms.vint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0),
    swapME1strips = cms.bool(False)
)


process.unpackDT = cms.EDProducer("DTUnpackingModule",
    dataType = cms.string('DDU'),
    dqmOnly = cms.bool(False),
    inputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    maxFEDid = cms.untracked.int32(779),
    minFEDid = cms.untracked.int32(770),
    readOutParameters = cms.PSet(
        debug = cms.untracked.bool(False),
        localDAQ = cms.untracked.bool(False),
        performDataIntegrityMonitor = cms.untracked.bool(False),
        rosParameters = cms.PSet(
            debug = cms.untracked.bool(False),
            localDAQ = cms.untracked.bool(False),
            performDataIntegrityMonitor = cms.untracked.bool(False),
            readDDUIDfromDDU = cms.untracked.bool(True),
            readingDDU = cms.untracked.bool(True),
            writeSC = cms.untracked.bool(True)
        )
    ),
    useStandardFEDid = cms.bool(True)
)


process.unpackEcal = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 
        16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 
        26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 
        36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 
        46, 47, 48, 49, 50, 
        51, 52, 53, 54),
    orderedFedList = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.unpackEmtf = cms.EDProducer("L1TRawToDigi",
    FWId = cms.uint32(0),
    FedIds = cms.vint32(1384, 1385),
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    MTF7 = cms.untracked.bool(True),
    Setup = cms.string('stage2::EMTFSetup'),
    debug = cms.untracked.bool(False)
)


process.unpackRPC = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    doSynchro = cms.bool(True)
)


process.hltAK4CaloJetsPFEt5 = cms.EDFilter("EtMinCaloJetSelector",
    etMin = cms.double(5.0),
    filter = cms.bool(False),
    src = cms.InputTag("hltAK4CaloJetsPF")
)


process.hltBoolEnd = cms.EDFilter("HLTBool",
    result = cms.bool(True)
)


process.hltBoolFalse = cms.EDFilter("HLTBool",
    result = cms.bool(False)
)


process.hltPFTau20 = cms.EDFilter("HLT1PFTau",
    MaxEta = cms.double(2.5),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(20.0),
    inputTag = cms.InputTag("hltPFTaus"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(84)
)


process.hltPFTau20Track = cms.EDFilter("HLT1PFTau",
    MaxEta = cms.double(2.5),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(20.0),
    inputTag = cms.InputTag("hltSelectedPFTausTrackFinding"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(84)
)


process.hltPFTau20TrackLooseIso = cms.EDFilter("HLT1PFTau",
    MaxEta = cms.double(2.5),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(20.0),
    inputTag = cms.InputTag("hltSelectedPFTausTrackFindingLooseIsolation"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(84)
)


process.hltPFTau20TrackLooseIsoAgainstMuon = cms.EDFilter("HLT1PFTau",
    MaxEta = cms.double(2.5),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(20.0),
    inputTag = cms.InputTag("hltSelectedPFTausTrackFindingLooseIsolationAgainstMuon"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(84)
)


process.hltPreHLTAnalyzerEndpath = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreMCLooseIsoPFTau20 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltSelectedPFTausTrackFinding = cms.EDFilter("PFTauSelector",
    cut = cms.string('pt > 0'),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hltPFTauTrackFindingDiscriminator"),
        selectionCut = cms.double(0.5)
    )),
    src = cms.InputTag("hltPFTaus")
)


process.hltSelectedPFTausTrackFindingLooseIsolation = cms.EDFilter("PFTauSelector",
    cut = cms.string('pt > 0'),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hltPFTauTrackFindingDiscriminator"),
        selectionCut = cms.double(0.5)
    ), 
        cms.PSet(
            discriminator = cms.InputTag("hltPFTauLooseAbsOrRelIsolationDiscriminator"),
            selectionCut = cms.double(0.5)
        )),
    src = cms.InputTag("hltPFTaus")
)


process.hltSelectedPFTausTrackFindingLooseIsolationAgainstMuon = cms.EDFilter("PFTauSelector",
    cut = cms.string('pt > 0'),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hltPFTauTrackFindingDiscriminator"),
        selectionCut = cms.double(0.5)
    ), 
        cms.PSet(
            discriminator = cms.InputTag("hltPFTauLooseAbsOrRelIsolationDiscriminator"),
            selectionCut = cms.double(0.5)
        ), 
        cms.PSet(
            discriminator = cms.InputTag("hltPFTauAgainstMuonDiscriminator"),
            selectionCut = cms.double(0.5)
        )),
    src = cms.InputTag("hltPFTaus")
)


process.hltTauJet5 = cms.EDFilter("HLT1CaloJet",
    MaxEta = cms.double(2.5),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(5.0),
    inputTag = cms.InputTag("hltAK4CaloJetsPFEt5"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(84)
)


process.hltTriggerType = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)


process.hltGetConditions = cms.EDAnalyzer("EventSetupRecordDataGetter",
    toGet = cms.VPSet(),
    verbose = cms.untracked.bool(False)
)


process.hltGetRaw = cms.EDAnalyzer("HLTGetRaw",
    RawDataCollection = cms.InputTag("rawDataCollector")
)


process.hltL1TGlobalSummary = cms.EDAnalyzer("L1TGlobalSummary",
    AlgInputTag = cms.InputTag("hltGtStage2Digis"),
    DumpRecord = cms.bool(False),
    DumpTrigResults = cms.bool(False),
    DumpTrigSummary = cms.bool(True),
    ExtInputTag = cms.InputTag("hltGtStage2Digis"),
    MaxBx = cms.int32(0),
    MinBx = cms.int32(0),
    ReadPrescalesFromFile = cms.bool(False),
    psColumn = cms.int32(0),
    psFileName = cms.string('prescale_L1TGlobal.csv')
)


process.hltTrigReport = cms.EDAnalyzer("HLTrigReport",
    HLTriggerResults = cms.InputTag("TriggerResults","","MYHLT"),
    ReferencePath = cms.untracked.string('HLTriggerFinalPath'),
    ReferenceRate = cms.untracked.double(100.0),
    reportBy = cms.untracked.string('job'),
    resetBy = cms.untracked.string('never'),
    serviceBy = cms.untracked.string('never')
)


# process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
#     fileName = cms.untracked.string('DQMIO.root')
# )


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(True),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.FastTimerService = cms.Service("FastTimerService",
    dqmLumiSectionsRange = cms.untracked.uint32(2500),
    dqmModuleTimeRange = cms.untracked.double(40.0),
    dqmModuleTimeResolution = cms.untracked.double(0.2),
    dqmPath = cms.untracked.string('HLT/TimerService'),
    dqmPathTimeRange = cms.untracked.double(100.0),
    dqmPathTimeResolution = cms.untracked.double(0.5),
    dqmTimeRange = cms.untracked.double(2000.0),
    dqmTimeResolution = cms.untracked.double(5.0),
    enableDQM = cms.untracked.bool(True),
    enableDQMbyLumiSection = cms.untracked.bool(True),
    enableDQMbyModule = cms.untracked.bool(False),
    enableDQMbyProcesses = cms.untracked.bool(True),
    printEventSummary = cms.untracked.bool(False),
    printJobSummary = cms.untracked.bool(True),
    printRunSummary = cms.untracked.bool(True)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary', 
        'TriggerSummaryProducerAOD', 
        'L1GtTrigReport', 
        'L1TGlobalSummary', 
        'HLTrigReport', 
        'FastReport'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        placeholder = cms.untracked.bool(True),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    ),
    statistics = cms.untracked.vstring('cerr'),
    suppressDebug = cms.untracked.vstring(),
    suppressError = cms.untracked.vstring('hltOnlineBeamSpot', 
        'hltL3MuonCandidates', 
        'hltL3TkTracksFromL2OIState', 
        'hltPFJetCtfWithMaterialTracks', 
        'hltL3TkTracksFromL2IOHit', 
        'hltL3TkTracksFromL2OIHit'),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring('hltOnlineBeamSpot', 
        'hltCtf3HitL1SeededWithMaterialTracks', 
        'hltL3MuonsOIState', 
        'hltPixelTracksForHighMult', 
        'hltHITPixelTracksHE', 
        'hltHITPixelTracksHB', 
        'hltCtfL1SeededWithMaterialTracks', 
        'hltRegionalTracksForL3MuonIsolation', 
        'hltSiPixelClusters', 
        'hltActivityStartUpElectronPixelSeeds', 
        'hltLightPFTracks', 
        'hltPixelVertices3DbbPhi', 
        'hltL3MuonsIOHit', 
        'hltPixelTracks', 
        'hltSiPixelDigis', 
        'hltL3MuonsOIHit', 
        'hltL1SeededElectronGsfTracks', 
        'hltL1SeededStartUpElectronPixelSeeds', 
        'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV', 
        'hltCtfActivityWithMaterialTracks'),
    threshold = cms.untracked.string('INFO'),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO')
    )
)


process.ThroughputService = cms.Service("ThroughputService",
    dqmPath = cms.untracked.string('HLT/Throughput'),
    timeRange = cms.untracked.double(60000.0),
    timeResolution = cms.untracked.double(5.828)
)


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection')
)


process.CSCChannelMapperESProducer = cms.ESProducer("CSCChannelMapperESProducer",
    AlgoName = cms.string('CSCChannelMapperPostls1')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CSCIndexerESProducer = cms.ESProducer("CSCIndexerESProducer",
    AlgoName = cms.string('CSCIndexerPostls1')
)


process.CSCObjectMapESProducer = cms.ESProducer("CSCObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTPGTranscoder = cms.ESProducer("CaloTPGTranscoderULUTs",
    HFTPScaleShift = cms.PSet(
        NCT = cms.int32(1),
        RCT = cms.int32(3)
    ),
    LUTfactor = cms.vint32(1, 2, 5, 0),
    RCTLSB = cms.double(0.25),
    ZS = cms.vint32(4, 2, 1, 0),
    hcalLUT1 = cms.FileInPath('CalibCalorimetry/CaloTPG/data/outputLUTtranscoder_physics.dat'),
    hcalLUT2 = cms.FileInPath('CalibCalorimetry/CaloTPG/data/TPGcalcDecompress2.txt'),
    ietaLowerBound = cms.vint32(1, 18, 27, 29),
    ietaUpperBound = cms.vint32(17, 26, 28, 32),
    nominal_gain = cms.double(0.177),
    read_Ascii_Compression_LUTs = cms.bool(False),
    read_Ascii_RCT_LUTs = cms.bool(False)
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapAuto = cms.untracked.bool(False),
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz'),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape_Phase1TkNewFPix.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    )
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.DTObjectMapESProducer = cms.ESProducer("DTObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.HcalTPGCoderULUT = cms.ESProducer("HcalTPGCoderULUT",
    FGLUTs = cms.FileInPath('CalibCalorimetry/HcalTPGAlgos/data/HBHE_FG_LUT.dat'),
    LUTGenerationMode = cms.bool(True),
    MaskBit = cms.int32(32768),
    RCalibFile = cms.FileInPath('CalibCalorimetry/HcalTPGAlgos/data/RecHit-TPG-calib.dat'),
    inputLUTs = cms.FileInPath('CalibCalorimetry/HcalTPGAlgos/data/inputLUTcoder_physics.dat'),
    read_Ascii_LUTs = cms.bool(False),
    read_FG_LUTs = cms.bool(False),
    read_XML_LUTs = cms.bool(False)
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
)


process.HcalTrigTowerGeometryESProducer = cms.ESProducer("HcalTrigTowerGeometryESProducer")


process.L1DTConfigFromDB = cms.ESProducer("DTConfigDBProducer",
    DTTPGMap = cms.untracked.PSet(
    **dict(
        [
            ("wh0st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh0st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh0st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh0st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh0st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh0st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh0st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh0st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh1st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se4" , cms.untracked.vint32(50, 48, 50, 13) ),
            ("wh1st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se4" , cms.untracked.vint32(60, 48, 60, 15) ),
            ("wh1st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se4" , cms.untracked.vint32(72, 48, 72, 18) ),
            ("wh1st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh1st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh1st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh1st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh1st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh1st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh1st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh1st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh2st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh2st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh2st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh2st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh2st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh2st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh2st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh2st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("whm1st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se3" , cms.untracked.vint32(50, 48, 50, 13) ),
            ("whm1st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se3" , cms.untracked.vint32(60, 48, 60, 15) ),
            ("whm1st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se3" , cms.untracked.vint32(72, 48, 72, 18) ),
            ("whm1st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm1st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("whm1st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm1st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm1st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm1st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm1st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm1st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
        ] +
        [
            ("whm2st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm2st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("whm2st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm2st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm2st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm2st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm2st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm2st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ]
        )
    ),
    DTTPGParameters = cms.PSet(
        Debug = cms.untracked.bool(False),
        SectCollParameters = cms.PSet(
            Debug = cms.untracked.bool(False),
            SCCSP1 = cms.int32(0),
            SCCSP2 = cms.int32(0),
            SCCSP3 = cms.int32(0),
            SCCSP4 = cms.int32(0),
            SCCSP5 = cms.int32(0),
            SCECF1 = cms.bool(False),
            SCECF2 = cms.bool(False),
            SCECF3 = cms.bool(False),
            SCECF4 = cms.bool(False)
        ),
        TUParameters = cms.PSet(
            BtiParameters = cms.PSet(
                AC1 = cms.int32(0),
                AC2 = cms.int32(3),
                ACH = cms.int32(1),
                ACL = cms.int32(2),
                CH = cms.int32(41),
                CL = cms.int32(22),
                DEAD = cms.int32(31),
                Debug = cms.untracked.int32(0),
                KACCTHETA = cms.int32(1),
                KMAX = cms.int32(64),
                LH = cms.int32(21),
                LL = cms.int32(2),
                LTS = cms.int32(3),
                PTMS0 = cms.int32(0),
                PTMS1 = cms.int32(0),
                PTMS10 = cms.int32(1),
                PTMS11 = cms.int32(1),
                PTMS12 = cms.int32(1),
                PTMS13 = cms.int32(1),
                PTMS14 = cms.int32(1),
                PTMS15 = cms.int32(1),
                PTMS16 = cms.int32(1),
                PTMS17 = cms.int32(1),
                PTMS18 = cms.int32(1),
                PTMS19 = cms.int32(1),
                PTMS2 = cms.int32(0),
                PTMS20 = cms.int32(1),
                PTMS21 = cms.int32(1),
                PTMS22 = cms.int32(1),
                PTMS23 = cms.int32(1),
                PTMS24 = cms.int32(1),
                PTMS25 = cms.int32(1),
                PTMS26 = cms.int32(1),
                PTMS27 = cms.int32(1),
                PTMS28 = cms.int32(1),
                PTMS29 = cms.int32(1),
                PTMS3 = cms.int32(0),
                PTMS30 = cms.int32(0),
                PTMS31 = cms.int32(0),
                PTMS4 = cms.int32(1),
                PTMS5 = cms.int32(1),
                PTMS6 = cms.int32(1),
                PTMS7 = cms.int32(1),
                PTMS8 = cms.int32(1),
                PTMS9 = cms.int32(1),
                RE43 = cms.int32(2),
                RH = cms.int32(61),
                RL = cms.int32(42),
                RON = cms.bool(True),
                SET = cms.int32(7),
                ST43 = cms.int32(42),
                WEN0 = cms.int32(1),
                WEN1 = cms.int32(1),
                WEN2 = cms.int32(1),
                WEN3 = cms.int32(1),
                WEN4 = cms.int32(1),
                WEN5 = cms.int32(1),
                WEN6 = cms.int32(1),
                WEN7 = cms.int32(1),
                WEN8 = cms.int32(1),
                XON = cms.bool(False)
            ),
            Debug = cms.untracked.bool(False),
            LutParameters = cms.PSet(
                BTIC = cms.untracked.int32(0),
                D = cms.untracked.double(0),
                Debug = cms.untracked.bool(False),
                WHEEL = cms.untracked.int32(-1),
                XCN = cms.untracked.double(0)
            ),
            TSPhiParameters = cms.PSet(
                Debug = cms.untracked.bool(False),
                TSMCCE1 = cms.bool(True),
                TSMCCE2 = cms.bool(False),
                TSMCCEC = cms.bool(False),
                TSMCGS1 = cms.bool(True),
                TSMCGS2 = cms.bool(True),
                TSMGS1 = cms.int32(1),
                TSMGS2 = cms.int32(1),
                TSMHSP = cms.int32(1),
                TSMHTE1 = cms.bool(True),
                TSMHTE2 = cms.bool(False),
                TSMHTEC = cms.bool(False),
                TSMMSK1 = cms.int32(312),
                TSMMSK2 = cms.int32(312),
                TSMNOE1 = cms.bool(True),
                TSMNOE2 = cms.bool(False),
                TSMNOEC = cms.bool(False),
                TSMWORD = cms.int32(255),
                TSSCCE1 = cms.bool(True),
                TSSCCE2 = cms.bool(False),
                TSSCCEC = cms.bool(False),
                TSSCGS1 = cms.bool(True),
                TSSCGS2 = cms.bool(True),
                TSSGS1 = cms.int32(1),
                TSSGS2 = cms.int32(1),
                TSSHTE1 = cms.bool(True),
                TSSHTE2 = cms.bool(False),
                TSSHTEC = cms.bool(False),
                TSSMSK1 = cms.int32(312),
                TSSMSK2 = cms.int32(312),
                TSSNOE1 = cms.bool(True),
                TSSNOE2 = cms.bool(False),
                TSSNOEC = cms.bool(False),
                TSTREN0 = cms.bool(True),
                TSTREN1 = cms.bool(True),
                TSTREN10 = cms.bool(True),
                TSTREN11 = cms.bool(True),
                TSTREN12 = cms.bool(True),
                TSTREN13 = cms.bool(True),
                TSTREN14 = cms.bool(True),
                TSTREN15 = cms.bool(True),
                TSTREN16 = cms.bool(True),
                TSTREN17 = cms.bool(True),
                TSTREN18 = cms.bool(True),
                TSTREN19 = cms.bool(True),
                TSTREN2 = cms.bool(True),
                TSTREN20 = cms.bool(True),
                TSTREN21 = cms.bool(True),
                TSTREN22 = cms.bool(True),
                TSTREN23 = cms.bool(True),
                TSTREN3 = cms.bool(True),
                TSTREN4 = cms.bool(True),
                TSTREN5 = cms.bool(True),
                TSTREN6 = cms.bool(True),
                TSTREN7 = cms.bool(True),
                TSTREN8 = cms.bool(True),
                TSTREN9 = cms.bool(True)
            ),
            TSThetaParameters = cms.PSet(
                Debug = cms.untracked.bool(False)
            ),
            TracoParameters = cms.PSet(
                BTIC = cms.int32(32),
                DD = cms.int32(18),
                Debug = cms.untracked.int32(0),
                FHISM = cms.int32(0),
                FHTMSK = cms.int32(0),
                FHTPRF = cms.int32(1),
                FLTMSK = cms.int32(1),
                FPRGCOMP = cms.int32(2),
                FSLMSK = cms.int32(0),
                IBTIOFF = cms.int32(0),
                KPRGCOM = cms.int32(255),
                KRAD = cms.int32(0),
                LTF = cms.int32(0),
                LTS = cms.int32(0),
                LVALIDIFH = cms.int32(0),
                REUSEI = cms.int32(1),
                REUSEO = cms.int32(1),
                SHISM = cms.int32(0),
                SHTMSK = cms.int32(0),
                SHTPRF = cms.int32(1),
                SLTMSK = cms.int32(1),
                SPRGCOMP = cms.int32(2),
                SSLMSK = cms.int32(0),
                TRGENB0 = cms.int32(1),
                TRGENB1 = cms.int32(1),
                TRGENB10 = cms.int32(1),
                TRGENB11 = cms.int32(1),
                TRGENB12 = cms.int32(1),
                TRGENB13 = cms.int32(1),
                TRGENB14 = cms.int32(1),
                TRGENB15 = cms.int32(1),
                TRGENB2 = cms.int32(1),
                TRGENB3 = cms.int32(1),
                TRGENB4 = cms.int32(1),
                TRGENB5 = cms.int32(1),
                TRGENB6 = cms.int32(1),
                TRGENB7 = cms.int32(1),
                TRGENB8 = cms.int32(1),
                TRGENB9 = cms.int32(1)
            )
        )
    ),
    TracoLutsFromDB = cms.bool(True),
    UseBtiAcceptParam = cms.bool(True),
    UseT0 = cms.bool(False),
    bxOffset = cms.int32(19),
    cfgConfig = cms.bool(False),
    debug = cms.bool(False),
    debugBti = cms.int32(0),
    debugDB = cms.bool(False),
    debugLUTs = cms.bool(False),
    debugPed = cms.bool(False),
    debugSC = cms.bool(False),
    debugTSP = cms.bool(False),
    debugTST = cms.bool(False),
    debugTU = cms.bool(False),
    debugTraco = cms.int32(0),
    finePhase = cms.double(25.0)
)


process.L1TGlobalPrescalesVetos = cms.ESProducer("L1TGlobalPrescalesVetosESProducer",
    AlgoBxMaskDefault = cms.int32(1),
    AlgoBxMaskXMLFile = cms.string('UGT_BASE_RS_ALGOBX_MASK_V1.xml'),
    FinOrMaskXMLFile = cms.string('UGT_BASE_RS_FINOR_MASK_v17.xml'),
    PrescaleXMLFile = cms.string('UGT_BASE_RS_PRESCALES_v11.xml'),
    TriggerMenuLuminosity = cms.string('startup'),
    Verbosity = cms.int32(0),
    VetoMaskXMLFile = cms.string('UGT_BASE_RS_VETO_MASK_v1.xml')
)


process.L1TriggerMenu = cms.ESProducer("L1TUtmTriggerMenuESProducer",
    L1TriggerMenuFile = cms.string('L1Menu_20170412.xml')
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOppositeForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositePropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.ParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.PropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStep'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.SiStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SiStripRegionConnectivity = cms.ESProducer("SiStripRegionConnectivity",
    EtaDivisions = cms.untracked.uint32(20),
    EtaMax = cms.untracked.double(2.5),
    PhiDivisions = cms.untracked.uint32(20)
)


process.SimpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    minVertices = cms.uint32(1),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.StableParameters = cms.ESProducer("StableParametersTrivialProducer",
    IfCaloEtaNumberBits = cms.uint32(4),
    IfMuEtaNumberBits = cms.uint32(6),
    NumberChips = cms.uint32(5),
    NumberConditionChips = cms.uint32(1),
    NumberL1CenJet = cms.uint32(4),
    NumberL1EGamma = cms.uint32(12),
    NumberL1ForJet = cms.uint32(4),
    NumberL1IsoEG = cms.uint32(4),
    NumberL1Jet = cms.uint32(12),
    NumberL1JetCounts = cms.uint32(12),
    NumberL1Mu = cms.uint32(4),
    NumberL1Muon = cms.uint32(12),
    NumberL1NoIsoEG = cms.uint32(4),
    NumberL1Tau = cms.uint32(8),
    NumberL1TauJet = cms.uint32(4),
    NumberPhysTriggers = cms.uint32(512),
    NumberPhysTriggersExtended = cms.uint32(64),
    NumberPsbBoards = cms.int32(7),
    NumberTechnicalTriggers = cms.uint32(64),
    OrderConditionChip = cms.vint32(1),
    OrderOfChip = cms.vint32(1),
    PinsOnChip = cms.uint32(512),
    PinsOnConditionChip = cms.uint32(512),
    TotalBxInEvent = cms.int32(5),
    UnitLength = cms.int32(8),
    WordLength = cms.int32(64),
    appendToDataLabel = cms.string('')
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.caloStage2Params = cms.ESProducer("L1TCaloStage2ParamsESProducer",
    centralityLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/centralityLUT_stage1.txt'),
    centralityNodeVersion = cms.int32(1),
    centralityRegionMask = cms.int32(0),
    egBypassEGVetos = cms.uint32(0),
    egCalibrationLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/EG_Calibration_LUT_FW_v17.04.04_shapeIdentification_adapt0.99_compressedieta_compressedE_compressedshape_v15.12.08_correct.txt'),
    egCalibrationType = cms.string('compressed'),
    egCalibrationVersion = cms.uint32(0),
    egCompressShapesLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/egCompressLUT_v4.txt'),
    egEtaCut = cms.int32(28),
    egHOverEcutBarrel = cms.int32(4),
    egHOverEcutEndcap = cms.int32(3),
    egHcalThreshold = cms.double(0.0),
    egIsoAreaNrTowersEta = cms.uint32(2),
    egIsoAreaNrTowersPhi = cms.uint32(4),
    egIsoLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/EG_Iso_LUT_04_04_2017.txt'),
    egIsoMaxEtaAbsForIsoSum = cms.uint32(27),
    egIsoMaxEtaAbsForTowerSum = cms.uint32(4),
    egIsoPUEstTowerGranularity = cms.uint32(1),
    egIsoVetoNrTowersPhi = cms.uint32(2),
    egIsolationType = cms.string('compressed'),
    egLsb = cms.double(0.5),
    egMaxHOverE = cms.double(0.15),
    egMaxHOverELUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/HoverEIdentification_0.995_v15.12.23.txt'),
    egMaxHcalEt = cms.double(0.0),
    egMaxPtHOverE = cms.double(128.0),
    egMaxPtHOverEIsolation = cms.int32(40),
    egMaxPtJetIsolation = cms.int32(63),
    egMinPtHOverEIsolation = cms.int32(1),
    egMinPtJetIsolation = cms.int32(25),
    egNeighbourThreshold = cms.double(1.0),
    egPUSParams = cms.vdouble(1, 4, 32),
    egPUSType = cms.string('None'),
    egSeedThreshold = cms.double(2.0),
    egShapeIdLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/shapeIdentification_adapt0.99_compressedieta_compressedE_compressedshape_v15.12.08.txt'),
    egShapeIdType = cms.string('compressed'),
    egShapeIdVersion = cms.uint32(0),
    egTrimmingLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/egTrimmingLUT_10_v16.01.19.txt'),
    etSumBypassPUS = cms.uint32(0),
    etSumEcalSumCalibrationLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/lut_etSumPUS_dummy.txt'),
    etSumEcalSumCalibrationType = cms.string('None'),
    etSumEtThreshold = cms.vdouble(0.0, 30.0, 0.0, 30.0, 0.0),
    etSumEtaMax = cms.vint32(28, 26, 28, 28, 28),
    etSumEtaMin = cms.vint32(1, 1, 1, 1, 1),
    etSumEttCalibrationLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/lut_etSumPUS_dummy.txt'),
    etSumEttCalibrationType = cms.string('None'),
    etSumLsb = cms.double(0.5),
    etSumPUSLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/lut_towEtThresh_2017v2.txt'),
    etSumPUSType = cms.string('LUT'),
    etSumXCalibrationLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/lut_etSumPUS_dummy.txt'),
    etSumXCalibrationType = cms.string('None'),
    etSumYCalibrationLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/lut_etSumPUS_dummy.txt'),
    etSumYCalibrationType = cms.string('None'),
    isoTauEtaMax = cms.int32(28),
    isoTauEtaMin = cms.int32(0),
    jetBypassPUS = cms.uint32(0),
    jetCalibrationLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/lut_calib_2017v1.txt'),
    jetCalibrationParams = cms.vdouble(1, 0, 1, 0, 1, 
        1, 1.36123039014, 1024, 1, 0, 
        1, 0, 1, 1, 1.37830172245, 
        1024, 1, 0, 1, 0, 
        1, 1, 1.37157036457, 1024, 1, 
        0, 1, 0, 1, 1, 
        1.42460009989, 1024, 10.1179757811, -697.422255848, 55.9767511168, 
        599.040770412, 0.00930772659892, -21.9921521313, 1.77585386314, 24.1202894336, 
        12.2578170485, -736.96846599, 45.3225355911, 848.976802835, 0.00946235693865, 
        -21.7970133915, 2.04623980351, 19.6049149791, 14.0198255047, -769.175319944, 
        38.687351315, 1072.9785137, 0.00951954709279, -21.6277409602, 2.08021511285, 
        22.265051562, 14.119589176, -766.199501821, 38.7767169666, 1059.63374337, 
        0.00952979125289, -21.6477483043, 2.05901166216, 23.8125466978, 13.7594864391, 
        -761.860391454, 39.9060363401, 1019.30588542, 0.00952105483129, -21.6814176696, 
        2.03808638982, 22.2127275989, 10.2635352836, -466.890522023, 32.5408463829, 
        2429.03382746, 0.0111274121697, -22.0890253377, 2.04880080215, 22.5083699943, 
        5.46086027683, -150.888778124, 18.3292242153, 16968.6469599, 0.0147496053457, 
        -22.4089831889, 2.08107691501, 22.4129703515, 5.46086027683, -150.888778124, 
        18.3292242153, 16968.6469599, 0.0147496053457, -22.4089831889, 2.08107691501, 
        22.4129703515, 10.2635352836, -466.890522023, 32.5408463829, 2429.03382746, 
        0.0111274121697, -22.0890253377, 2.04880080215, 22.5083699943, 13.7594864391, 
        -761.860391454, 39.9060363401, 1019.30588542, 0.00952105483129, -21.6814176696, 
        2.03808638982, 22.2127275989, 14.119589176, -766.199501821, 38.7767169666, 
        1059.63374337, 0.00952979125289, -21.6477483043, 2.05901166216, 23.8125466978, 
        14.0198255047, -769.175319944, 38.687351315, 1072.9785137, 0.00951954709279, 
        -21.6277409602, 2.08021511285, 22.265051562, 12.2578170485, -736.96846599, 
        45.3225355911, 848.976802835, 0.00946235693865, -21.7970133915, 2.04623980351, 
        19.6049149791, 10.1179757811, -697.422255848, 55.9767511168, 599.040770412, 
        0.00930772659892, -21.9921521313, 1.77585386314, 24.1202894336, 1, 
        0, 1, 0, 1, 1, 
        1.42460009989, 1024, 1, 0, 1, 
        0, 1, 1, 1.37157036457, 1024, 
        1, 0, 1, 0, 1, 
        1, 1.37830172245, 1024, 1, 0, 
        1, 0, 1, 1, 1.36123039014, 
        1024),
    jetCalibrationType = cms.string('LUT'),
    jetCompressEtaLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/lut_eta_compress_2017v1.txt'),
    jetCompressPtLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/lut_pt_compress_2017v1.txt'),
    jetLsb = cms.double(0.5),
    jetNeighbourThreshold = cms.double(0.0),
    jetPUSType = cms.string('ChunkyDonut'),
    jetRegionMask = cms.int32(0),
    jetSeedThreshold = cms.double(4.0),
    layer1ECalScaleETBins = cms.vint32(6, 9, 12, 15, 20, 
        25, 30, 35, 40, 45, 
        55, 70, 256),
    layer1ECalScaleFactors = cms.vdouble( (1.23077, 1.208991, 1.215351, 1.21335, 1.208275, 
        1.219069, 1.222985, 1.217729, 1.221262, 1.238302, 
        1.25104, 1.2633, 1.323678, 1.33058, 1.326592, 
        1.348387, 1.444263, 2.278846, 1.519648, 1.64693, 
        1.655937, 1.632773, 1.599511, 1.646612, 1.654494, 
        1.617013, 1.486696, 1.509178, 1.200818, 1.188237, 
        1.183589, 1.208003, 1.181402, 1.225384, 1.225197, 
        1.238568, 1.229019, 1.226685, 1.247974, 1.243772, 
        1.247896, 1.307835, 1.292458, 1.292431, 1.408326, 
        2.08656, 1.375806, 1.47916, 1.471558, 1.472672, 
        1.470455, 1.504425, 1.522293, 1.505404, 1.396942, 
        1.439355, 1.15745, 1.163603, 1.172625, 1.215935, 
        1.164385, 1.192617, 1.175256, 1.189703, 1.194979, 
        1.211745, 1.201289, 1.213436, 1.233816, 1.263384, 
        1.261724, 1.270097, 1.355681, 1.948426, 1.289409, 
        1.380269, 1.429089, 1.409515, 1.402992, 1.432428, 
        1.454425, 1.448494, 1.356177, 1.415035, 1.109329, 
        1.130229, 1.136506, 1.156603, 1.14818, 1.136802, 
        1.157053, 1.146116, 1.147593, 1.16018, 1.15704, 
        1.175752, 1.176997, 1.19245, 1.192074, 1.219774, 
        1.279824, 1.946019, 1.262478, 1.341427, 1.385701, 
        1.349399, 1.344777, 1.377678, 1.428243, 1.404236, 
        1.338994, 1.396023, 1.08977, 1.082103, 1.090228, 
        1.089163, 1.090443, 1.10395, 1.09313, 1.097591, 
        1.112827, 1.115258, 1.115559, 1.11936, 1.139471, 
        1.152378, 1.154278, 1.156148, 1.206562, 1.852929, 
        1.225639, 1.299721, 1.351968, 1.317715, 1.315265, 
        1.349087, 1.395426, 1.382078, 1.313055, 1.375904, 
        1.071911, 1.067929, 1.06629, 1.064308, 1.070857, 
        1.077186, 1.072581, 1.073245, 1.086873, 1.104813, 
        1.080402, 1.086703, 1.096386, 1.114866, 1.122498, 
        1.129279, 1.167211, 1.815989, 1.202916, 1.279602, 
        1.328353, 1.295723, 1.289288, 1.32463, 1.370921, 
        1.360803, 1.295568, 1.360794, 1.059307, 1.055444, 
        1.055547, 1.054844, 1.055633, 1.070619, 1.067176, 
        1.060437, 1.064041, 1.082473, 1.077814, 1.076358, 
        1.083088, 1.096413, 1.110072, 1.117249, 1.141054, 
        1.656952, 1.183193, 1.250519, 1.271871, 1.26493, 
        1.265938, 1.305469, 1.346518, 1.333812, 1.28076, 
        1.349732, 1.050145, 1.045243, 1.048544, 1.045844, 
        1.048177, 1.065325, 1.054551, 1.058521, 1.054766, 
        1.072195, 1.06406, 1.066467, 1.077743, 1.085108, 
        1.080674, 1.098568, 1.129347, 1.505618, 1.177574, 
        1.230855, 1.230263, 1.254251, 1.260679, 1.296709, 
        1.339361, 1.331497, 1.276333, 1.34662, 1.044434, 
        1.046443, 1.044523, 1.045117, 1.042187, 1.054454, 
        1.047753, 1.049621, 1.054001, 1.067735, 1.058934, 
        1.05648, 1.067558, 1.092601, 1.075606, 1.082969, 
        1.119556, 1.487269, 1.163707, 1.220454, 1.211224, 
        1.245848, 1.245011, 1.276404, 1.320622, 1.317634, 
        1.259293, 1.331703, 1.036507, 1.031687, 1.034341, 
        1.038718, 1.03996, 1.056759, 1.042963, 1.047073, 
        1.046287, 1.061804, 1.047322, 1.051865, 1.061811, 
        1.07771, 1.065041, 1.07417, 1.110572, 1.409428, 
        1.161587, 1.209903, 1.200401, 1.237205, 1.239067, 
        1.274367, 1.311375, 1.309819, 1.206232, 1.281656, 
        1.034128, 1.028977, 1.031212, 1.032869, 1.032576, 
        1.048159, 1.035764, 1.037963, 1.03816, 1.0513, 
        1.042707, 1.043292, 1.051796, 1.064664, 1.058869, 
        1.066773, 1.098222, 1.34083, 1.150792, 1.192509, 
        1.188802, 1.222087, 1.222194, 1.261393, 1.296707, 
        1.293975, 1.098204, 1.090501, 1.024842, 1.02276, 
        1.02382, 1.023853, 1.025343, 1.037737, 1.029393, 
        1.028506, 1.0309, 1.041196, 1.031898, 1.034541, 
        1.040246, 1.054993, 1.04825, 1.054786, 1.080644, 
        1.270714, 1.140567, 1.177924, 1.174622, 1.207597, 
        1.215113, 1.250065, 1.286407, 1.284189, 1.284189, 
        1.284189, 1.018863, 1.016991, 1.017559, 1.017933, 
        1.019889, 1.027862, 1.020909, 1.022602, 1.024068, 
        1.031407, 1.025612, 1.02715, 1.0334, 1.043217, 
        1.039784, 1.044029, 1.06309, 1.203727, 1.127824, 
        1.157782, 1.153493, 1.179254, 1.181702, 1.203665, 
        1.236615, 1.223496, 1.223496, 1.223496 ) ),
    layer1HCalScaleETBins = cms.vint32(6, 9, 12, 15, 20, 
        25, 30, 35, 40, 45, 
        55, 70, 256),
    layer1HCalScaleFactors = cms.vdouble( (1.461291, 1.454625, 1.455598, 1.449939, 1.460976, 
        1.47348, 1.466595, 1.468804, 1.481637, 1.497836, 
        1.504469, 1.517996, 1.543596, 1.558518, 1.575825, 
        1.586335, 1.544925, 1.389349, 1.39604, 1.439915, 
        1.398678, 1.441202, 1.451638, 1.471108, 1.491032, 
        1.530464, 1.654074, 1.650121, 1.375991, 1.376866, 
        1.374574, 1.372501, 1.375971, 1.388565, 1.389183, 
        1.393546, 1.396302, 1.418089, 1.422244, 1.443768, 
        1.457298, 1.469873, 1.485083, 1.488035, 1.443898, 
        1.288701, 1.318062, 1.354571, 1.296165, 1.316493, 
        1.324791, 1.329227, 1.329808, 1.347197, 1.385654, 
        1.367404, 1.330324, 1.330662, 1.332125, 1.334518, 
        1.33001, 1.343405, 1.346451, 1.346908, 1.349793, 
        1.374879, 1.374081, 1.391796, 1.40629, 1.417394, 
        1.4335, 1.422528, 1.373563, 1.235496, 1.274484, 
        1.300781, 1.22222, 1.234458, 1.242407, 1.238218, 
        1.231158, 1.229238, 1.248514, 1.261873, 1.301111, 
        1.303505, 1.304342, 1.300883, 1.301955, 1.312233, 
        1.316385, 1.317202, 1.315308, 1.335695, 1.342003, 
        1.353083, 1.362459, 1.370255, 1.379031, 1.369051, 
        1.319807, 1.199383, 1.23589, 1.263149, 1.172396, 
        1.189026, 1.182243, 1.174765, 1.160341, 1.159067, 
        1.211505, 1.281201, 1.275768, 1.275028, 1.274251, 
        1.272298, 1.27209, 1.283374, 1.284263, 1.283754, 
        1.28342, 1.301406, 1.301963, 1.309314, 1.31514, 
        1.319884, 1.327534, 1.312294, 1.264995, 1.168509, 
        1.199964, 1.223081, 1.121649, 1.128651, 1.126169, 
        1.112205, 1.112272, 1.146819, 1.194809, 1.19522, 
        1.247213, 1.246675, 1.246937, 1.246958, 1.242936, 
        1.249726, 1.251084, 1.250033, 1.246985, 1.258533, 
        1.259635, 1.264881, 1.266468, 1.266983, 1.271018, 
        1.255678, 1.213176, 1.138423, 1.164712, 1.181474, 
        1.07551, 1.07628, 1.074546, 1.080937, 1.122946, 
        1.131501, 1.111036, 1.11022, 1.225062, 1.224108, 
        1.223705, 1.222218, 1.218175, 1.223123, 1.224592, 
        1.222768, 1.215725, 1.224004, 1.223652, 1.225737, 
        1.227469, 1.227681, 1.230391, 1.213227, 1.171645, 
        1.115248, 1.13558, 1.145603, 1.037666, 1.05126, 
        1.080362, 1.099305, 1.088466, 1.075173, 1.05663, 
        1.032875, 1.20283, 1.204155, 1.203486, 1.201967, 
        1.194002, 1.197947, 1.198415, 1.196705, 1.188166, 
        1.19668, 1.192931, 1.197918, 1.197352, 1.192337, 
        1.193319, 1.177775, 1.139192, 1.096009, 1.110544, 
        1.116609, 1.042172, 1.074235, 1.080403, 1.064799, 
        1.053359, 1.037543, 1.006759, 1.006759, 1.188028, 
        1.183705, 1.183068, 1.180943, 1.176596, 1.180435, 
        1.176822, 1.172566, 1.167376, 1.172652, 1.171996, 
        1.172278, 1.170926, 1.164278, 1.161894, 1.142646, 
        1.108552, 1.076311, 1.086825, 1.092867, 1.05711, 
        1.060453, 1.051915, 1.037153, 1.02245, 1.00139, 
        1.00139, 1.00139, 1.169376, 1.169865, 1.167855, 
        1.166754, 1.159677, 1.161727, 1.161602, 1.159157, 
        1.149591, 1.155508, 1.150864, 1.150443, 1.147936, 
        1.1379, 1.131026, 1.112978, 1.080918, 1.061229, 
        1.066055, 1.073614, 1.042392, 1.038032, 1.029904, 
        1.012558, 1.012558, 1.012558, 1.012558, 1.012558, 
        1.150175, 1.150513, 1.150216, 1.147693, 1.140891, 
        1.143654, 1.140204, 1.134718, 1.128271, 1.127001, 
        1.12219, 1.119082, 1.114472, 1.102259, 1.089926, 
        1.075835, 1.045855, 1.041539, 1.044984, 1.046205, 
        1.015383, 1.01154, 1.001439, 1.001439, 1.001439, 
        1.001439, 1.001439, 1.001439, 1.125661, 1.124191, 
        1.12325, 1.118812, 1.112736, 1.111236, 1.106057, 
        1.098389, 1.089647, 1.086947, 1.079851, 1.073968, 
        1.068117, 1.051795, 1.03596, 1.02117, 1.001873, 
        1.014026, 1.014703, 1.02376, 1.02376, 1.02376, 
        1.02376, 1.02376, 1.02376, 1.02376, 1.02376, 
        1.02376, 1.0905, 1.08967, 1.086302, 1.082156, 
        1.075398, 1.072158, 1.065357, 1.056707, 1.048909, 
        1.041525, 1.033163, 1.023515, 1.015901, 1.015901, 
        1.015901, 1.137542, 1.188167, 1.01923, 1.01923, 
        1.036922, 1.036922, 1.036922, 1.036922, 1.036922, 
        1.036922, 1.036922, 1.036922, 1.036922 ) ),
    layer1HFScaleETBins = cms.vint32(5, 20, 30, 50, 256),
    layer1HFScaleFactors = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
        1.0, 1.0, 1.0, 1.0, 1.0, 
        1.0, 1.0, 1.76708, 1.76708, 1.755186, 
        1.769951, 1.763527, 1.791043, 1.898787, 1.982235, 
        2.071074, 2.193011, 2.356886, 2.403384, 2.170477, 
        2.170477, 2.12354, 2.019866, 1.907698, 1.963179, 
        1.989122, 2.035251, 2.184642, 2.436399, 2.810884, 
        2.92375, 1.943941, 1.943941, 1.899826, 1.81395, 
        1.714978, 1.736184, 1.785928, 1.834211, 1.94423, 
        2.153565, 2.720887, 2.749795, 1.679984, 1.679984, 
        1.669753, 1.601871, 1.547276, 1.577805, 1.611497, 
        1.670184, 1.775022, 1.937061, 2.488311, 2.618629),
    minimumBiasThresholds = cms.vint32(0, 0, 0, 0),
    q2LUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/q2LUT_stage1.txt'),
    regionLsb = cms.double(0.5),
    regionPUSParams = cms.vdouble(),
    regionPUSType = cms.string('None'),
    regionPUSVersion = cms.int32(0),
    tauCalibrationLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/Tau_Calibration_LUT_2017_Layer1Calibration_FW_v12.0.0.txt'),
    tauCalibrationLUTFileEta = cms.FileInPath('L1Trigger/L1TCalorimeter/data/tauCalibrationLUTEta.txt'),
    tauCompressLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/tauCompressAllLUT_12bit_v3.txt'),
    tauEtToHFRingEtLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/tauHwEtToHFRingScale_LUT.txt'),
    tauIsoAreaNrTowersEta = cms.uint32(2),
    tauIsoAreaNrTowersPhi = cms.uint32(4),
    tauIsoLUTFile = cms.FileInPath('L1Trigger/L1TCalorimeter/data/Tau_Iso_LUT_Option_22_2017_FW_v9.0.0.txt'),
    tauIsoLUTFile2 = cms.FileInPath('L1Trigger/L1TCalorimeter/data/Tau_Iso_LUT_Option_22_2017_FW_v9.0.0.txt'),
    tauIsoVetoNrTowersPhi = cms.uint32(2),
    tauLsb = cms.double(0.5),
    tauMaxJetIsolationA = cms.double(0.1),
    tauMaxJetIsolationB = cms.double(100.0),
    tauMaxPtTauVeto = cms.double(64.0),
    tauMinPtJetIsolationB = cms.double(192.0),
    tauNeighbourThreshold = cms.double(0.0),
    tauPUSParams = cms.vdouble(1, 4, 32),
    tauPUSType = cms.string('None'),
    tauRegionMask = cms.int32(0),
    tauSeedThreshold = cms.double(0.0),
    towerEncoding = cms.bool(True),
    towerLsbE = cms.double(0.5),
    towerLsbH = cms.double(0.5),
    towerLsbSum = cms.double(0.5),
    towerNBitsE = cms.int32(8),
    towerNBitsH = cms.int32(8),
    towerNBitsRatio = cms.int32(3),
    towerNBitsSum = cms.int32(9)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring('kNonRespondingIsolated', 
            'kDeadVFE', 
            'kDeadFE', 
            'kNoDataNoTP'),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring('kDAC', 
            'kNoLaser', 
            'kNoisy', 
            'kNNoisy', 
            'kNNNoisy', 
            'kNNNNoisy', 
            'kNNNNNoisy', 
            'kFixedG6', 
            'kFixedG1', 
            'kFixedG0'),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring('kFaultyHardware', 
            'kDead', 
            'kKilled'),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring('kPoorReco', 
            'kPoorCalib', 
            'kNoisy', 
            'kSaturated'),
        kRecovered = cms.vstring('kLeadingEdgeRecovered', 
            'kTowerRecovered'),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring('kWeird', 
            'kDiWeird')
    ),
    timeThresh = cms.double(2.0)
)


process.emtfForests = cms.ESProducer("L1TMuonEndCapForestESProducer")


process.emtfParams = cms.ESProducer("L1TMuonEndCapParamsESProducer",
    PtAssignVersion = cms.int32(4),
    St1MatchWindow = cms.int32(15),
    St2MatchWindow = cms.int32(15),
    St3MatchWindow = cms.int32(7),
    St4MatchWindow = cms.int32(7),
    firmwareVersion = cms.int32(50)
)


process.fakeBmtfParams = cms.ESProducer("L1TMuonBarrelParamsESProducer",
    AssLUTPath = cms.string('L1Trigger/L1TMuon/data/bmtf_luts/LUTs_Ass/'),
    BX_max = cms.int32(2),
    BX_min = cms.int32(-2),
    DisableNewAlgo = cms.bool(False),
    EtaTrackFinder = cms.bool(True),
    Extrapolation_21 = cms.bool(False),
    Extrapolation_Filter = cms.int32(1),
    Extrapolation_nbits_Phi = cms.int32(8),
    Extrapolation_nbits_PhiB = cms.int32(8),
    Open_LUTs = cms.bool(False),
    OutOfTime_Filter = cms.bool(False),
    OutOfTime_Filter_Window = cms.int32(1),
    PHI_Assignment_nbits_Phi = cms.int32(12),
    PHI_Assignment_nbits_PhiB = cms.int32(10),
    PT_Assignment_nbits_Phi = cms.int32(12),
    PT_Assignment_nbits_PhiB = cms.int32(10),
    configFromXML = cms.bool(False),
    fwVersion = cms.uint32(2),
    hwXmlFile = cms.string('L1Trigger/L1TMuonBarell/test/BMTF_HW.xml'),
    mask_ettf_st1 = cms.vstring('111111111111', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '111111111111'),
    mask_ettf_st2 = cms.vstring('000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000'),
    mask_ettf_st3 = cms.vstring('000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000'),
    mask_phtf_st1 = cms.vstring('111111111111', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '111111111111'),
    mask_phtf_st2 = cms.vstring('000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000'),
    mask_phtf_st3 = cms.vstring('000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000'),
    mask_phtf_st4 = cms.vstring('000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000', 
        '000000000000'),
    topCfgXmlFile = cms.string('L1Trigger/L1TMuonBarell/test/bmtf_top_config_p5.xml'),
    xmlCfgKey = cms.string('RunKey_1')
)


process.gmtParams = cms.ESProducer("L1TMuonGlobalParamsESProducer",
    AbsIsoCheckMemLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/AbsIsoCheckMem.txt'),
    BEtaExtrapolationLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/BEtaExtrapolation_5eta_7pt_4out_0outshift_20170118.txt'),
    BONegMatchQualLUTMaxDR = cms.double(0.15),
    BONegMatchQualLUTPath = cms.string(''),
    BONegMatchQualLUTfEta = cms.double(1),
    BONegMatchQualLUTfEtaCoarse = cms.double(1),
    BONegMatchQualLUTfPhi = cms.double(6),
    BOPosMatchQualLUTMaxDR = cms.double(0.15),
    BOPosMatchQualLUTPath = cms.string(''),
    BOPosMatchQualLUTfEta = cms.double(1),
    BOPosMatchQualLUTfEtaCoarse = cms.double(1),
    BOPosMatchQualLUTfPhi = cms.double(6),
    BPhiExtrapolationLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/BPhiExtrapolation_5eta_7pt_4out_2outshift_20170118.txt'),
    FEtaExtrapolationLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/EEtaExtrapolation_5eta_7pt_4out_0outshift_20170118.txt'),
    FONegMatchQualLUTMaxDR = cms.double(0.075),
    FONegMatchQualLUTPath = cms.string(''),
    FONegMatchQualLUTfEta = cms.double(1),
    FONegMatchQualLUTfEtaCoarse = cms.double(1),
    FONegMatchQualLUTfPhi = cms.double(3),
    FOPosMatchQualLUTMaxDR = cms.double(0.075),
    FOPosMatchQualLUTPath = cms.string(''),
    FOPosMatchQualLUTfEta = cms.double(1),
    FOPosMatchQualLUTfEtaCoarse = cms.double(1),
    FOPosMatchQualLUTfPhi = cms.double(3),
    FPhiExtrapolationLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/EPhiExtrapolation_5eta_7pt_4out_2outshift_20170118.txt'),
    FwdNegSingleMatchQualLUTMaxDR = cms.double(0.05),
    FwdNegSingleMatchQualLUTPath = cms.string(''),
    FwdNegSingleMatchQualLUTfEta = cms.double(1),
    FwdNegSingleMatchQualLUTfPhi = cms.double(1),
    FwdPosSingleMatchQualLUTMaxDR = cms.double(0.05),
    FwdPosSingleMatchQualLUTPath = cms.string(''),
    FwdPosSingleMatchQualLUTfEta = cms.double(1),
    FwdPosSingleMatchQualLUTfPhi = cms.double(1),
    IdxSelMemEtaLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/IdxSelMemEta.txt'),
    IdxSelMemPhiLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/IdxSelMemPhi.txt'),
    OEtaExtrapolationLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/OEtaExtrapolation_5eta_7pt_4out_0outshift_20170118.txt'),
    OPhiExtrapolationLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/OPhiExtrapolation_5eta_7pt_4out_2outshift_20170118.txt'),
    OvlNegSingleMatchQualLUTMaxDR = cms.double(0.05),
    OvlNegSingleMatchQualLUTPath = cms.string(''),
    OvlNegSingleMatchQualLUTfEta = cms.double(1),
    OvlNegSingleMatchQualLUTfEtaCoarse = cms.double(1),
    OvlNegSingleMatchQualLUTfPhi = cms.double(2),
    OvlPosSingleMatchQualLUTMaxDR = cms.double(0.05),
    OvlPosSingleMatchQualLUTPath = cms.string(''),
    OvlPosSingleMatchQualLUTfEta = cms.double(1),
    OvlPosSingleMatchQualLUTfEtaCoarse = cms.double(1),
    OvlPosSingleMatchQualLUTfPhi = cms.double(2),
    RelIsoCheckMemLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/RelIsoCheckMem.txt'),
    SortRankLUTPath = cms.string('L1Trigger/L1TMuon/data/microgmt_luts/SortRank.txt'),
    SortRankLUTPtFactor = cms.uint32(1),
    SortRankLUTQualFactor = cms.uint32(4),
    bmtfInputsToDisable = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0),
    caloInputsDisable = cms.bool(False),
    caloInputsMasked = cms.bool(False),
    configFromXml = cms.bool(False),
    emtfInputsToDisable = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0),
    fwVersion = cms.uint32(67174400),
    hwXmlFile = cms.string('L1Trigger/L1TMuon/data/o2o/ugmt/UGMT_HW.xml'),
    maskedBmtfInputs = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0),
    maskedEmtfInputs = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0),
    maskedOmtfInputs = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0),
    omtfInputsToDisable = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0),
    topCfgXmlFile = cms.string('L1Trigger/L1TMuon/data/o2o/ugmt/ugmt_top_config_p5.xml'),
    uGmtProcessorId = cms.string('ugmt_processor'),
    xmlCfgKey = cms.string('TestKey1')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring('HcalCellMask', 
        'HcalCellOff', 
        'HcalCellDead'),
    RecoveredRecHitBits = cms.vstring('TimingAddedBit', 
        'TimingSubtractedBit'),
    SeverityLevels = cms.VPSet(cms.PSet(
        ChannelStatus = cms.vstring(),
        Level = cms.int32(0),
        RecHitFlags = cms.vstring()
    ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring()
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring('HSCP_R1R2', 
                'HSCP_FracLeader', 
                'HSCP_OuterEnergy', 
                'HSCP_ExpFit', 
                'ADCSaturationBit', 
                'HBHEIsolatedNoise', 
                'AddedSimHcalNoise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring('HBHEHpdHitMultiplicity', 
                'HBHEPulseShape', 
                'HOBit', 
                'HFInTimeWindow', 
                'ZDCBit', 
                'CalibrationBit', 
                'TimingErrorBit', 
                'HBHETriangleNoise', 
                'HBHETS4TS5Noise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring('HFLongShort', 
                'HFPET', 
                'HFS8S1Ratio', 
                'HFDigiTime')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12),
            RecHitFlags = cms.vstring('HBHEFlatNoise', 
                'HBHESpikeNoise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring()
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellOff', 
                'HcalCellDead'),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring()
        ))
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer")


process.hltCombinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltCombinedSecondaryVertexV2 = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPBwdAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPBwdAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.hltESPBwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPBwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPChi2ChargeLooseMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeLooseMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator2000 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    MaxChi2 = cms.double(2000.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutForHI')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeTightMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2MeasurementEstimator16 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator30 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator9 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPCloseComponentsMerger5D = cms.ESProducer("CloseComponentsMergerESProducer5D",
    ComponentName = cms.string('hltESPCloseComponentsMerger5D'),
    DistanceMeasure = cms.string('hltESPKullbackLeiblerDistance5D'),
    MaxComponents = cms.int32(12)
)


process.hltESPDetachedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.2),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.2),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.hltESPDummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.hltESPElectronMaterialEffects = cms.ESProducer("GsfMaterialEffectsESProducer",
    BetheHeitlerCorrection = cms.int32(2),
    BetheHeitlerParametrization = cms.string('BetheHeitler_cdfmom_nC6_O5.par'),
    ComponentName = cms.string('hltESPElectronMaterialEffects'),
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    Mass = cms.double(0.000511),
    MultipleScatteringUpdator = cms.string('MultipleScatteringUpdator')
)


process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFittingSmootherIT = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPFittingSmootherIT'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFittingSmootherRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPFittingSmootherRK'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPKFFittingSmootherForLoopers'),
    standardFitter = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK')
)


process.hltESPFwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPFwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPGlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.hltESPGsfElectronFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPGsfElectronFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPGsfTrajectoryFitter'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPGsfTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPGsfTrajectoryFitter = cms.ESProducer("GsfTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPGsfTrajectoryFitter'),
    GeometricalPropagator = cms.string('hltESPAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGsfTrajectorySmoother = cms.ESProducer("GsfTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPGsfTrajectorySmoother'),
    ErrorRescaling = cms.double(100.0),
    GeometricalPropagator = cms.string('hltESPBwdAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPInitialStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTiny')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2MeasurementEstimator36 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2MeasurementEstimator36'),
    MaxChi2 = cms.double(36.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPKFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitter'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherForLoopers'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPRKTrajectoryFitter'),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPRKTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFUpdator = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('hltESPKFUpdator')
)


process.hltESPKullbackLeiblerDistance5D = cms.ESProducer("DistanceBetweenComponentsESProducer5D",
    ComponentName = cms.string('hltESPKullbackLeiblerDistance5D'),
    DistanceMeasure = cms.string('KullbackLeibler')
)


process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPLowPtStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    )
)


process.hltESPMixedStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPMixedStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape_Phase1TkNewFPix.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    )
)


process.hltESPMixedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPMuonTransientTrackingRecHitBuilder')
)


process.hltESPPixelCPEGeneric = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag(""),
    PixelErrorParametrization = cms.string('NOTcmsim'),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAAlignmentOffsets = cms.bool(False),
    useLAWidthFromDB = cms.bool(False)
)


process.hltESPPixelCPETemplateReco = cms.ESProducer("PixelCPETemplateRecoESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPETemplateReco'),
    DoCosmics = cms.bool(False),
    DoLorentz = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    UseClusterSplitter = cms.bool(False),
    speed = cms.int32(-2)
)


process.hltESPPixelLessStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPPixelLessStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape_Phase1TkNewFPix.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    )
)


process.hltESPPixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelLessStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPPixelPairStepChi2MeasurementEstimator25 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2MeasurementEstimator25'),
    MaxChi2 = cms.double(25.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPPixelPairTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelPairTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.hltESPRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPRKTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPRKTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPRungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.hltESPSmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagator'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite')
)


process.hltESPSoftLeptonByDistance = cms.ESProducer("LeptonTaggerByDistanceESProducer",
    distance = cms.double(0.5)
)


process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPStripCPEfromTrackAngle = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('hltESPStripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.hltESPTTRHBWithTrackAngle = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle')
)


process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPETemplateReco'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle')
)


process.hltESPTTRHBuilderPixelOnly = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.hltESPTobTecStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPTobTecStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape_Phase1TkNewFPix.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    )
)


process.hltESPTobTecStepFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmoother'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitter'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    standardFitter = cms.string('hltESPTobTecStepFitterSmoother')
)


process.hltESPTobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTobTecStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.09)
)


process.hltESPTrackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('hltESPTrackAlgoPriorityOrder'),
    algoOrder = cms.vstring(),
    appendToDataLabel = cms.string('')
)


process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    appendToDataLabel = cms.string(''),
    trackerGeometryLabel = cms.untracked.string('')
)


process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(0.0),
    ValidHitBonus = cms.double(100.0),
    allowSharedFirstHit = cms.bool(False),
    fractionShared = cms.double(0.5)
)


process.hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedSeeds'),
    ComponentType = cms.string('TrajectoryCleanerBySharedSeeds'),
    MissingHitPenalty = cms.double(0.0),
    ValidHitBonus = cms.double(100.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.5)
)


process.hltESPTrajectoryFitterRK = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTrajectoryFitterRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPTrajectorySmootherRK = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTrajectorySmootherRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltPixelTracksCleanerBySharedHits = cms.ESProducer("PixelTrackCleanerBySharedHitsESProducer",
    ComponentName = cms.string('hltPixelTracksCleanerBySharedHits'),
    appendToDataLabel = cms.string(''),
    useQuadrupletAlgo = cms.bool(False)
)


process.hltTrackCleaner = cms.ESProducer("TrackCleanerESProducer",
    ComponentName = cms.string('hltTrackCleaner'),
    appendToDataLabel = cms.string('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    etaBinSize = cms.double(0.125),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.omtfParams = cms.ESProducer("L1TMuonOverlapParamsESProducer",
    configXMLFile = cms.FileInPath('L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0004.xml'),
    patternsXMLFiles = cms.VPSet(cms.PSet(
        patternsXMLFile = cms.FileInPath('L1Trigger/L1TMuon/data/omtf_config/Patterns_0x0003.xml')
    ))
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CSCChannelMapperESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCChannelMapperRecord')
)


process.CSCINdexerESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCIndexerRecord')
)


process.GlobalParametersRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TGlobalParametersRcd')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(0),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('90X_upgrade2017_TSG_Hcal_V2'),
    pfnPostfix = cms.untracked.string('None'),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.L1TGlobalPrescalesVetosRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TGlobalPrescalesVetosRcd')
)


process.StableParametersRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TGlobalStableParametersRcd')
)


process.bmbtfParamsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TMuonBarrelParamsRcd')
)


process.caloParamsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TCaloStage2ParamsRcd')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.emtfForestsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TMuonEndCapForestRcd')
)


process.emtfParamsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TMuonEndcapParamsRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.gmtParamsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TMuonGlobalParamsRcd')
)


process.hltESSBTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.hltESSEcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.hltESSHcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.omtfParamsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TMuonOverlapParamsRcd')
)


process.prefer("L1TriggerMenu")

process.HLTDoLocalPixelSequence = cms.Sequence(process.hltSiPixelDigis+process.hltSiPixelClusters+process.hltSiPixelClustersCache+process.hltSiPixelRecHits)


process.HLTPreshowerSequence = cms.Sequence(process.hltEcalPreshowerDigis+process.hltEcalPreshowerRecHit)


process.HLTRecoPixelTracksSequence = cms.Sequence(process.hltPixelTracksFilter+process.hltPixelTracksFitter+process.hltPixelTracksTrackingRegions+process.hltPixelLayerQuadruplets+process.hltPixelTracksHitDoublets+process.hltPixelTracksHitQuadruplets+process.hltPixelTracks)


process.HLTL1UnpackerSequence = cms.Sequence(process.hltGtStage2Digis+process.hltGtStage2ObjectMap)


process.HLTMuonLocalRecoSequence = cms.Sequence(process.hltMuonDTDigis+process.hltDt1DRecHits+process.hltDt4DSegments+process.hltMuonCSCDigis+process.hltCsc2DRecHits+process.hltCscSegments+process.hltMuonRPCDigis+process.hltRpcRecHits)


process.HLTLooseIsoPFTauSequence = cms.Sequence(process.hltTauPFJets08Region+process.hltTauPFJetsRecoTauChargedHadrons+process.hltPFTauPiZeros+process.hltPFTausSansRef+process.hltPFTaus+process.hltPFTauTrackFindingDiscriminator+process.hltPFTauLooseAbsoluteIsolationDiscriminator+process.hltPFTauLooseRelativeIsolationDiscriminator+process.hltPFTauLooseAbsOrRelIsolationDiscriminator)


process.HLTDoLocalHcalSequence = cms.Sequence(process.hltHcalDigis+process.hltHbhePhase1Reco+process.hltHbhereco+process.hltHfprereco+process.hltHfreco+process.hltHoreco)


process.HLTIter0TrackAndTauJet4Iter1Sequence = cms.Sequence(process.hltTrackIter0RefsForJets4Iter1+process.hltAK4Iter0TrackJets4Iter1+process.hltIter0TrackAndTauJets4Iter1)


process.HLTL2muonrecoNocandSequence = cms.Sequence(process.HLTMuonLocalRecoSequence+process.hltL2OfflineMuonSeeds+process.hltL2MuonSeeds+process.hltL2Muons)


process.SimL1TCalorimeter = cms.Sequence(process.simCaloStage2Layer1Digis+process.simCaloStage2Digis)


process.HLTIter1TrackAndTauJets4Iter2Sequence = cms.Sequence(process.hltIter1TrackRefsForJets4Iter2+process.hltAK4Iter1TrackJets4Iter2+process.hltIter1TrackAndTauJets4Iter2)


process.HLTBeamSpot = cms.Sequence(process.hltScalersRawToDigi+process.hltOnlineBeamSpot)


process.HLTParticleFlowSequenceForTaus = cms.Sequence(process.HLTPreshowerSequence+process.hltParticleFlowRecHitECALUnseeded+process.hltParticleFlowRecHitHBHE+process.hltParticleFlowRecHitHCAL+process.hltParticleFlowRecHitHF+process.hltParticleFlowRecHitPSUnseeded+process.hltParticleFlowClusterECALUncorrectedUnseeded+process.hltParticleFlowClusterPSUnseeded+process.hltParticleFlowClusterECALUnseeded+process.hltParticleFlowClusterHBHE+process.hltParticleFlowClusterHCAL+process.hltParticleFlowClusterHF+process.hltLightPFTracks+process.hltParticleFlowBlockForTaus+process.hltParticleFlowForTaus)


process.HLTEndSequence = cms.Sequence(process.hltBoolEnd)


process.HLTIterativeTrackingIteration2 = cms.Sequence(process.hltIter2ClustersRefRemoval+process.hltIter2MaskedMeasurementTrackerEvent+process.hltIter2PixelLayerTriplets+process.hltIter2PFlowPixelTrackingRegions+process.hltIter2PFlowPixelClusterCheck+process.hltIter2PFlowPixelHitDoublets+process.hltIter2PFlowPixelHitTriplets+process.hltIter2PFlowPixelSeeds+process.hltIter2PFlowCkfTrackCandidates+process.hltIter2PFlowCtfWithMaterialTracks+process.hltIter2PFlowTrackCutClassifier+process.hltIter2PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIteration1 = cms.Sequence(process.hltIter1ClustersRefRemoval+process.hltIter1MaskedMeasurementTrackerEvent+process.hltIter1PixelLayerQuadruplets+process.hltIter1PFlowPixelTrackingRegions+process.hltIter1PFlowPixelClusterCheck+process.hltIter1PFlowPixelHitDoublets+process.hltIter1PFlowPixelHitQuadruplets+process.hltIter1PFlowPixelSeeds+process.hltIter1PFlowCkfTrackCandidates+process.hltIter1PFlowCtfWithMaterialTracks+process.hltIter1PFlowTrackCutClassifierPrompt+process.hltIter1PFlowTrackCutClassifierDetached+process.hltIter1PFlowTrackCutClassifierMerged+process.hltIter1PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIteration0 = cms.Sequence(process.hltIter0PFLowPixelSeedsFromPixelTracks+process.hltIter0PFlowCkfTrackCandidates+process.hltIter0PFlowCtfWithMaterialTracks+process.hltIter0PFlowTrackCutClassifier+process.hltIter0PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIter02 = cms.Sequence(process.HLTIterativeTrackingIteration0+process.HLTIter0TrackAndTauJet4Iter1Sequence+process.HLTIterativeTrackingIteration1+process.hltIter1Merged+process.HLTIter1TrackAndTauJets4Iter2Sequence+process.HLTIterativeTrackingIteration2+process.hltIter2Merged)


process.HLTRecopixelvertexingSequence = cms.Sequence(process.HLTRecoPixelTracksSequence+process.hltPixelVertices+process.hltTrimmedPixelVertices)


process.SimL1TMuonCommon = cms.Sequence(process.simDtTriggerPrimitiveDigis+process.simCscTriggerPrimitiveDigis)


process.SimL1TGlobal = cms.Sequence(process.simGtStage2Digis)


process.HLTDoLocalStripSequence = cms.Sequence(process.hltSiStripExcludedFEDListProducer+process.hltSiStripRawToClustersFacility+process.hltSiStripClusters)


process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence(process.hltEcalDigis+process.hltEcalUncalibRecHit+process.hltEcalDetIdToBeRecovered+process.hltEcalRecHit)


process.SimL1TechnicalTriggers = cms.Sequence(process.simGtExtFakeStage2Digis)


process.HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)


process.HLTTrackReconstructionForPF = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTRecopixelvertexingSequence+process.HLTDoLocalStripSequence+process.HLTIterativeTrackingIter02+process.hltPFMuonMerging+process.hltMuonLinks+process.hltMuons)


process.HLTL3muonTkCandidateSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.hltL3TrajSeedOIState+process.hltL3TrackCandidateFromL2OIState+process.hltL3TkTracksFromL2OIState+process.hltL3MuonsOIState+process.hltL3TrajSeedOIHit+process.hltL3TrackCandidateFromL2OIHit+process.hltL3TkTracksFromL2OIHit+process.hltL3MuonsOIHit+process.hltL3TkFromL2OICombination+process.hltPixelLayerTriplets+process.hltPixelLayerPairs+process.hltMixedLayerPairs+process.hltL3TrajSeedIOHit+process.hltL3TrackCandidateFromL2IOHit+process.hltL3TkTracksFromL2IOHit+process.hltL3MuonsIOHit+process.hltL3TrajectorySeed+process.hltL3TrackCandidateFromL2)


process.HLTLooseIsoPFTau20SequenceMC = cms.Sequence(process.HLTLooseIsoPFTauSequence+process.hltPFTau20+process.hltSelectedPFTausTrackFinding+process.hltPFTau20Track+process.hltSelectedPFTausTrackFindingLooseIsolation+process.hltPFTau20TrackLooseIso+process.hltPFTauAgainstMuonDiscriminator+process.hltSelectedPFTausTrackFindingLooseIsolationAgainstMuon+process.hltPFTau20TrackLooseIsoAgainstMuon)


process.SimL1TMuon = cms.Sequence(process.SimL1TMuonCommon+process.simTwinMuxDigis+process.simBmtfDigis+process.simEmtfDigis+process.simOmtfDigis+process.simGmtCaloSumDigis+process.simGmtStage2Digis)


process.HLTL3muonrecoNocandSequence = cms.Sequence(process.HLTL3muonTkCandidateSequence+process.hltL3TkTracksMergeStep1+process.hltL3TkTracksFromL2+process.hltL3MuonsLinksCombination+process.hltL3Muons)


process.SimL1EmulatorCore = cms.Sequence(process.SimL1TCalorimeter+process.SimL1TMuon+process.SimL1TechnicalTriggers+process.SimL1TGlobal)


process.HLTDoCaloSequencePF = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence+process.HLTDoLocalHcalSequence+process.hltTowerMakerForPF)


process.HLTL2muonrecoSequence = cms.Sequence(process.HLTL2muonrecoNocandSequence+process.hltL2MuonCandidates)


process.HLTL3muonrecoSequence = cms.Sequence(process.HLTL3muonrecoNocandSequence+process.hltL3MuonCandidates)


process.SimL1Emulator = cms.Sequence(process.unpackEcal+process.unpackCSC+process.unpackDT+process.unpackRPC+process.unpackEmtf+process.unpackCsctf+process.unpackBmtf+process.simHcalTriggerPrimitiveDigis+process.SimL1EmulatorCore+process.packCaloStage2+process.packGmtStage2+process.packGtStage2+process.rawDataCollector)


process.HLTPFTriggerSequenceMuTau = cms.Sequence(process.HLTTrackReconstructionForPF+process.HLTParticleFlowSequenceForTaus+process.hltAK4PFJetsForTaus)


process.HLTRecoJetSequenceAK4UncorrectedPF = cms.Sequence(process.HLTDoCaloSequencePF+process.hltAK4CaloJetsPF)


process.HLTRecoJetSequenceAK4PrePF = cms.Sequence(process.HLTRecoJetSequenceAK4UncorrectedPF+process.hltAK4CaloJetsPFEt5)


process.HLTriggerFirstPath = cms.Path(process.SimL1Emulator+process.hltGetConditions+process.hltGetRaw+process.hltBoolFalse)


process.MC_LooseIsoPFTau20_v5 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltPreMCLooseIsoPFTau20+process.HLTL2muonrecoSequence+process.HLTL3muonrecoSequence+process.HLTRecoJetSequenceAK4PrePF+process.hltTauJet5+process.HLTPFTriggerSequenceMuTau+process.HLTLooseIsoPFTau20SequenceMC+process.HLTEndSequence)


process.HLTriggerFinalPath = cms.Path(process.SimL1Emulator+process.hltGtStage2Digis+process.hltScalersRawToDigi+process.hltFEDSelector+process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW+process.hltBoolFalse)


process.HLTAnalyzerEndpath = cms.EndPath(process.SimL1Emulator+process.hltGtStage2Digis+process.hltPreHLTAnalyzerEndpath+process.hltL1TGlobalSummary+process.hltTrigReport)


# process.DQMOutput = cms.EndPath(process.dqmOutput)



