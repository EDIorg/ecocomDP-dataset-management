#!/usr/bin/python3

# registration script does 2 things:
# 1. log into gbif, create a dataset. GBIF's create process returns an identifier
# 2. record the gbif dataset id in our management file, using dataset's level 2 (dwca) PASTA id as key

# script inputs: 
# level 2 id to register (must be a dwca, although this is not yet checked!)
# name of our management file

import argparse
from functions import create_gbif_dataset
from functions import log_gbif_uuid
# maybe import functions individually?
# from functions import gbif_config
# from functions import pasta_config
#######################################  

##########
### parse arguments
##########

# initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("level2", help="EDI identifier (scope.accession.revision) for level 2 dataset (DwC-A)")
parser.add_argument("filename", help="name of mgt filename where IDs are logged")
args = parser.parse_args()

level2_id=args.level2
mgt_filename=args.filename


##########
### Checks 
##########


# 1. check that this level2_id is a DwC-A
# if yes, continue, else exit
# ?? should it be possible to register a DwC-A before it exists ?? [no. this way, we do this check only once, here. ]


# 2. check that level2_id does not already have a GBIF id registered
# if no continue, else exit






##########
### configuration settings, GBIF
##########

# import config vars from file gbif_config.py
from config_gbif import api, headers, username, password, organization, installation, registry, public



##########
### PASTA config settings
##########
# PASTA endpoint - NOT USED HERE
pasta_api = "https://pasta-s.lternet.edu/package/archive/eml/"


##########
### Initialize a dataset at GBIF
# Important: uses no dataset-specific info - its the equivalent of an EDI accession_no reservation.
gbif_uuid = create_gbif_dataset(api, installation, organization, username, password, headers)

##########
### Record the registration and assign to an EDI package
# We are in control of the EDI-id to GBIF-id relationship
df = log_gbif_uuid(mgt_filename, level2_id, gbif_uuid)

##########
### Save edited file
df.to_csv(mgt_filename, sep=',', header=True, index=False)




    