#!/usr/bin/python3
# define gbif config variables
# question: I thought these vars would automatically be namespaced "gbif_config". but that does not seem to be the case - they seem to be global.
api = "http://api.gbif-uat.org/v1/dataset"
headers = {'Content-Type': 'application/json'}

username = "ws_client_demo"
password = "Demo123"
 
# GBIF params, from example (could move these to a config)
organization = "0a16da09-7719-40de-8d4f-56a15ed52fb6" # Test organization
installation = "92d76df5-3de1-4c89-be03-7a17abad962a" # Test HTTP installation

registry = "https://registry.gbif-uat.org/dataset/"
public =  "https://www.gbif-uat.org/dataset/"

