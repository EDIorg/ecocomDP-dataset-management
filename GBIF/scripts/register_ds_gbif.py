#!/usr/bin/python3

from functions import create_gbif_dataset
from functions import log_gbif_id

#######################################  
# CONFIG

##########
### configuration settings, GBIF
##########

api = "http://api.gbif-uat.org/v1/dataset"
headers = {'Content-Type': 'application/json'}

# not needed for registration script. only used after ingestion ?confirm (reg uses installation key)
registry = "https://registry.gbif-uat.org/dataset/"
public =  "https://www.gbif-uat.org/dataset/"

username = "ws_client_demo"
password = "Demo123"

# GBIF params, from example (could move these to a config)
organization = "0a16da09-7719-40de-8d4f-56a15ed52fb6" # Test organization
installation = "92d76df5-3de1-4c89-be03-7a17abad962a" # Test HTTP installation


##########
### PASTA config settings
##########
# PASTA endpoint
pasta_api = "https://pasta-s.lternet.edu/package/archive/eml/"


##########
### Register the dataset
gbif_uuid = create_gbif_dataset(api, installation, organization, username, password, headers)

##########
### Record the registration locally
df = log_gbif_id('test.csv', 'edi.3', gbif_uuid)

##########
### Save edited file
df.to_csv('test.csv', sep=',', header=True, index=False)




    