#!/usr/bin/python3


##########
### PASTA config settings
##########
def pasta_config():
  # configuration settings, PASTA
  # PASTA endpoint
  pasta_api = "https://pasta-s.lternet.edu/package/archive/eml/"


##########
###  FUNCTION: log_gbif_id
##   sets the value for gbif identifier for a L2 dataset in our registry file
##########
def log_gbif_uuid(logfile_name, working_L2_dwca, working_gbif_id): 
  print()
  print("hello from log_gbif_id")
  import pandas as pd

  # print the inputs (during testing)
  print("logfile_name:", logfile_name)
  print("working_L2_dwca: ", working_L2_dwca)
  print("working_gbif_id: ", working_gbif_id)

  # create a dataframe
  try: 
    df= pd.read_csv(logfile_name, delimiter=',')
  except FileNotFoundError:
    print("no file: ", logfile_name)
    exit()
  else:  
    print("reading ", logfile_name)   
    # set row index to be the L2 column. retain original col, modify the original df (non-default settings)
    # see https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html
    df.set_index('L2_dwca', drop=False, inplace=True, verify_integrity=True)


#  # confirm this L2 id is listed in the index   
  if working_L2_dwca in df.L2_dwca.unique():
    df.at[working_L2_dwca,'gbif_id'] = working_gbif_id
    print(df)
  else:
    print("no entry for: ", working_L2_dwca)
    exit()
  
  ###  Do this outside this function ?
  # # save output log file
  # df.to_csv(logfile_name, sep=',', header=True, index=False)
  return df

##########
###  FUNCTION: create_gbif_dataset
##   creates a dataset at gbif, returns its uuid
##########  
def create_gbif_dataset(api, installation, organization,username, password, headers):
  import json
  import requests

  data_type = "SAMPLING_EVENT"
  title = "Placeholder title, to be written over by EML metadata from EDI" 

  dataset_example = {
    "installationKey": installation,
    "publishingOrganizationKey": organization,
    "type": data_type,
    "title": title
  }

  create_dataset = requests.post(api,
                               data=json.dumps(dataset_example),
                               auth=(username, password),
                               headers=headers)
                               
  if create_dataset.ok:
    # dataset POST responds with the UUID
    dataset_response = create_dataset.json()
    print("GBIF identifier: ", dataset_response)
    gbif_uuid = dataset_response
    
  # send back gbif response
  return gbif_uuid
 
 
 
 
############################
# testing
# gbif_config()
# print(registry)

# gbif_uuid = create_gbif_dataset()
# print("GBIF identifier: ", gbif_uuid)
