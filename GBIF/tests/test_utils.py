import pandas as pd
from GBIF.scripts import utils
import pytest


def test_read_log():
    log = utils.read_log('../data/processing_log.csv')
    assert isinstance(log, pd.DataFrame)
    assert pd.core.dtypes.common.is_datetime64_dtype(log['crawled'])


def test_validate_log():
    log = pd.read_csv('../data/processing_log.csv', delimiter=',')
    bad_log = log[['id_local', 'id_gbif']]  # Log missing a required column
    with pytest.raises(ValueError):
        utils.validate_log(bad_log)
