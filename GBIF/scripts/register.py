#!/usr/bin/python3
import pandas as pd
import json
import requests
import re
import uuid # TODO remove me after testing


def create_gbif_dataset(api, installation, organization,username, password, headers):
    """Creates a dataset at gbif and returns its UUID

    :param api: GBIF API endpoint. Defined in the config file.
    :param installation: HTTP installation. Defined in the config file.
    :param organization: Organization. Defined in the config file.
    :param username: GBIF user name. Defined in the config file.
    :param password: GBIF password. Defined in the config file.
    :param headers: GBIF crawl request HTTP headers. Defined in the config file.
    :return: GBIF dataset UUID

    Notes
    -----
    Initializes a dataset at GBIF (get a registration ID). Important: Uses no dataset-specific info - Its the equivalent of an EDI accession_no reservation.
    """

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
      dataset_response = create_dataset.json()
      print("GBIF identifier: ", dataset_response)
      gbif_uuid = dataset_response

    # send back gbif response
    return gbif_uuid


def register(level2, filename):
    """
    Register an EDI Data Package with GBIF

    :param level2: EDI identifier (scope.accession.revision) for level 2 dataset (DwC-A)
    :param filename: name of mgt filename where IDs are logged
    :return: GBIF ID

    Notes
    -----
    This function does 2 things:
    1. log into gbif, create a dataset. GBIF's create process returns an identifier
    2. record the gbif dataset id in our management file, using dataset's level 2 (dwca) PASTA id as key

    Records the registration and assign to an EDI package. We are in control of the EDI-id to GBIF-id relationship
    """
    df = pd.read_csv(filename, delimiter=',')
    row_i = df.index[df["L2_dwca"] == level2]
    sa = re.sub("\..$", "", level2)
    df["sa"] = [re.sub("\..$", "", L2_scope_acc_rev) for L2_scope_acc_rev in df.L2_dwca.to_list()]
    if df.iloc[row_i].gbif_id.isnull().any():
        i = df["sa"].isin([sa])
        res = df[i].gbif_id.dropna()
        if len(res) == 0:
            print("Registering " + level2 + " with GBIF")
            # TODO uncomment the line below for actual registration
            # gbif_uuid = create_gbif_dataset(api, installation, organization, username, password, headers)
            gbif_uuid = uuid.uuid4() # TODO Remove this line. It's just for testing.
        else:
            print(sa + " is already registered. Reusing GBIF ID")
            dfsub = df[["sa", "gbif_id"]]
            dfsub = dfsub.drop_duplicates()
            dfsub = dfsub.dropna(subset=["gbif_id"])
            x = dfsub.index[dfsub["sa"] == sa]
            gbif_uuid = dfsub.gbif_id[x].item()
        df.loc[row_i, "gbif_id"] = gbif_uuid
    else:
        # Get the gbif_id for an already registered dataset so it can be
        # returned from this function
        dfsub = df[["sa", "gbif_id"]]
        dfsub = dfsub.drop_duplicates()
        dfsub = dfsub.dropna(subset=["gbif_id"])
        x = dfsub.index[dfsub["sa"] == sa]
        gbif_uuid = dfsub.gbif_id[x].item()
    df.drop("sa", axis=1, inplace=True)
    df.to_csv(filename, sep=',', header=True, index=False)
    return gbif_uuid
