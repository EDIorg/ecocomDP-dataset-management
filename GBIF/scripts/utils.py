import pandas as pd


def init_log(f):
    pass


def read_log(f):
    """
    Read log file to Pandas Dataframe

    Parameters
    ----------
    f
        Log file path.

    Returns
    -------
    Dataframe

    Notes
    -----
    The log file is a .csv with the minimum column set: 'id_local', 'id_gbif', and 'crawled', where 'crawled' is a
    datetime of a format parsable by pandas `read_csv()`.

    See Also
    --------
    init_log : Initialize log file.
    """
    log = pd.read_csv(f, delimiter=',')
    log['crawled'] = pd.to_datetime(log['crawled'])
    return log


def validate_log(df):
    required_cols = {'id_local', 'id_gbif', 'crawled'}.issubset(set(df.columns))
    if not required_cols:
        raise ValueError('One or more required columns missing')


def write_log(f):
    pass