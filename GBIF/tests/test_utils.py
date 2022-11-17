import pandas as pd
from GBIF.scripts import utils


def test_read_log():
    log = utils.read_log('../data/processing_log.csv')
    expected_cols = {'id_gbif', 'id_local', 'crawled'}
    assert isinstance(log, pd.DataFrame)
    expected_cols.issubset(set(log.columns))
    assert pd.core.dtypes.common.is_datetime64_dtype(log['crawled'])

