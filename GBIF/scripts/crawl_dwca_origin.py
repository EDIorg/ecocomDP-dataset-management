#!/usr/bin/python3

# crawl script does 1 thing:
# 1. GBIF process reads the dataset from pasta 

# script inputs: 
# level 2 id to be crawled
# name of our management file (gbif id read from here)

import json
import requests
import argparse
# from functions import create_gbif_dataset
# from functions import log_gbif_id

#######################################  

# usage example: crawl_dwca_origin.py edi.3 test.csv
##########
### parse arguments
##########

# initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("level2", help="id for level 2 dataset (dwca)")
parser.add_argument("filename", help="name of mgt filename where ids are logged")
args = parser.parse_args()

level2_id = args.level2
mgt_filename = args.filename

##########
### configuration settings, GBIF
##########

# import from file gbif_config.py
from config_gbif import api, headers, username, password, organization, installation, registry, public

##########
###  config settings, PASTA
##########

# import from file pasta_config.py 
from config_pasta import pasta_api
# pasta_api = "https://pasta-s.lternet.edu/package/archive/eml/"


##########
### Create PASTA endpoint

pkg_uri = pasta_api+level2_id.replace('.','/')
pasta_headers = requests.utils.default_headers()
response = requests.post(pkg_uri, headers=pasta_headers)
transaction_id = response.text

pasta_endpoint = pkg_uri+'/'+transaction_id
print("pasta_endpoint: ", pasta_endpoint)

##########
### Check - this is a valid PASTA endpoint
## TO DO - write this check


##########
### Read the GBIF id from the local management file
### TO DO - rm hard codeing
gbif_id = "80d795f5-f3e0-41e5-b370-d20428fc07b0"

##########
# Add PASTA endpoint to GBIF registration
##########

# create endpoint
my_endpoint = {
            "url": pasta_endpoint,
            "type": "DWC_ARCHIVE"
            }
            
# update datset at GBIF to initiate crawl
update_dataset = requests.post(api + "/" + gbif_id + "/endpoint",
                                  data=json.dumps(my_endpoint),
                                   auth=(username, password),
                                   headers=headers)
if update_dataset.ok:
        print("Endpoint added")


# notifications? send to log?
dataset_url = public+gbif_id
api_url = api+gbif_id
registry_url = registry+gbif_id

print("dataset URL: ",dataset_url)
print("registry URL: ",registry_url)
print("API URL: ",api_url)



    