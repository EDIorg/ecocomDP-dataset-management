import os.path
import pandas as pd
from GBIF.scripts import utils
import pytest


@pytest.fixture
def log():
    return pd.read_csv('../data/processing_log.csv', delimiter=',')


def test_read_log():
    log = utils.read_log('../data/processing_log.csv')
    assert isinstance(log, pd.DataFrame)
    assert pd.core.dtypes.common.is_datetime64_dtype(log['crawled'])


def test_validate_log(log):
    bad_log = log[['id_local', 'id_gbif']]  # Log missing a required column
    with pytest.raises(ValueError):
        utils.validate_log(bad_log)
    log_duplicate_keys = pd.concat([log, log.iloc[[-1]]])
    with pytest.raises(ValueError):
        utils.validate_log(log_duplicate_keys)


def test_init_log(tmp_path):
    f = tmp_path / "log.csv"
    utils.init_log(f)
    assert os.path.exists(f)
    log = utils.read_log(f)
    assert utils.validate_log(log) is None
    with pytest.raises(FileExistsError):
        utils.init_log(f)
