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
    required_cols = ['id_local', 'id_gbif', 'crawled']
    log = pd.read_csv(f, delimiter=',', usecols=required_cols)
    log['crawled'] = pd.to_datetime(log['crawled'])
    return log


def write_log(f):
    pass