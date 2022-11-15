import pandas as pd
from GBIF.scripts import utils


def test_read_log():
    log = utils.read_log('../data/processing_log.csv')
    assert isinstance(log, pd.DataFrame)
