#!/usr/bin/python3
from config import api, headers, username, password, registry, public, pasta_api
import requests
import pandas as pd
import json


def crawl(level2, gbif_id):
    """Request GBIF crawl of a data package in the EDI Data Repository

    :param level2: EDI identifier (scope.accession.revision) for level 2 dataset (DwC-A)
    """
    # usage example: crawl_dwca_origin.py edi.3 processing_log.csv

    # TODO Stop if level2 is already crawled

    # Create EDI endpoint
    print("Creating EDI endpoint")
    pkg_uri = pasta_api + level2.replace('.', '/')

    # TODO Uncomment to actually let it run
    # pasta_headers = requests.utils.default_headers()
    # response = requests.post(pkg_uri, headers=pasta_headers)
    # transaction_id = response.text
    # pasta_endpoint = pkg_uri + '/' + transaction_id
    # print("PASTA endpoint: ", pasta_endpoint)

    print("PASTA endpoint: PLACEHOLDER") # TODO remove this line. For testing only.
    # TODO Check - this is a valid PASTA endpoint



    # TODO Uncomment after testing
    print("Add PASTA endpoint to GBIF registration")
    # # Add PASTA endpoint to GBIF registration
    # # create endpoint
    # my_endpoint = {"url": pasta_endpoint, "type": "DWC_ARCHIVE"}
    #
    # # Update datset at GBIF to initiate crawl
    # update_dataset = requests.post(
    #     api + "/" + gbif_id + "/endpoint",
    #     data=json.dumps(my_endpoint),
    #     auth=(username, password),
    #     headers=headers
    # )
    # if update_dataset.ok:
    #     print("Endpoint added")
    #
    # # notifications? send to log?
    # dataset_url = public + gbif_id
    # api_url = api + gbif_id
    # registry_url = registry + gbif_id
    #
    # print("dataset URL: ", dataset_url)
    # print("registry URL: ", registry_url)
    # print("API URL: ", api_url)

    # TODO Implement GBIF Crawl Monitor here
