#!/usr/bin/python3

# crawl script does 1 thing:
# 1. GBIF process reads the dataset from pasta 

# script inputs: 
# level 2 id to be crawled
# name of our management file (gbif id read from here)

import argparse
# from functions import create_gbif_dataset
# from functions import log_gbif_id

#######################################  

# usage example: register_ds_gbif.py edi.3 test.csv
##########
### parse arguments
##########

# initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("level2", help="id for level 2 dataset (dwca)")
parser.add_argument("filename", help="name of mgt filename where ids are logged")
args = parser.parse_args()

level2_id=args.level2
mgt_filename=args.filename

##########
### configuration settings, GBIF
##########

# import config vars from file gbif_config.py
from gbif_config import api, headers, username, password, organization, installation, registry, public

##########
###  config settings, PASTA
##########
# PASTA endpoint 
pasta_api = "https://pasta-s.lternet.edu/package/archive/eml/"


##########
### Create PASTA endpoint


##########
### Read the GBIF id from the local file



# Add endpoint to GBIF registration
my_endpoint = {
            "url": pasta_endpoint,
            "type": "DWC_ARCHIVE"
            }
            
# crawl dataset
update_dataset = requests.post(api + "/" + dataset_response + "/endpoint",
                                  data=json.dumps(my_endpoint),
                                   auth=(username, password),
                                   headers=headers)
if update_dataset.ok:
        print("Endpoint added")


# notifications? send to log?
dataset_url = public+gbif_uuid
api_url = api+gbif_uuid
registry_url = registry+gbif_uuid

print("dataset URL: ",dataset_url)
print("registry URL: ",registry_url)
print("API URL: ",api_url)



    