from CRABClient.UserUtilities import config

config = config()

config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.psetName        = 'customise_may2017_aod_cfg.py'
config.JobType.pluginName      = 'Analysis'
config.JobType.outputFiles     = ['outputFULL_ztt.root']
config.JobType.maxMemoryMB     = 2499
config.JobType.priority        = 999

config.Data.unitsPerJob        = 1000
config.Data.splitting          = 'EventAwareLumiBased'

# JSON files:
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/
config.Data.publication        = False
config.Data.outputDatasetTag   = 'HPSatHLT'

config.Site.storageSite        = 'T2_CH_CERN'
config.Site.blacklist          = ['T2_FI_HIP']
config.Site.whitelist          = ['T2_CH_CERN']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    tag = 'HPSatHLT_91X_relax_1p2p'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea   = 'crab_mc_' + tag
    config.Data.outLFNDirBase = '/store/group/phys_tau/HLT2016/' + tag 
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    datasets = {}

    datasets['DYJetsToLL']= ('/GluGluHToTauTau_M125_13TeV_powheg_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/AODSIM','/GluGluHToTauTau_M125_13TeV_powheg_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW')
    
#     datasets['DYJetsToLL_25ns_PUFlat10to50']= ('dummy','/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-25nsFlat10to50ZsecalNzshcalRaw_76X_mcRun2_asymptotic_2016EcalTune_30fb_v1-v1/GEN-SIM-RAW')
#     datasets['DYJetsToLL_25ns_PUFlat10to25']= ('/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-25nsFlat10to25TSG_HCALDebug_76X_mcRun2_asymptotic_v11-v1/MINIAODSIM','/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-25nsFlat10to25TSG_HCALDebug_76X_mcRun2_asymptotic_v11-v1/GEN-SIM-RAW')
#     datasets['HLTPhysics2_Run2016B']= ('dummy','/HLTPhysics2/Run2016B-v1/RAW')
#     datasets['HLTPhysics3_Run2016B']= ('dummy','/HLTPhysics3/Run2016B-v1/RAW')

    for k, v in datasets.iteritems():
        config.General.requestName = k
        config.Data.inputDataset          = v[0]
        config.Data.secondaryInputDataset = v[1]
        config.JobType.numCores = 4
        print 'submitting config:'
        print config
        submit(config)

