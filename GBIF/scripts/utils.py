import pandas as pd


def read_log(f):
    """
    Read log file to Pandas Dataframe

    Parameters
    ----------
    f
        Path to the log file.

    Returns
    -------
    Dataframe

    See Also
    --------
    init_log : Initialize a log file.
    """
    required_cols = ['id_local', 'id_gbif', 'crawled']
    log = pd.read_csv(f, delimiter=',', usecols=required_cols)
    log['crawled'] = pd.to_datetime(log['crawled'])
    return log


def write_log(f):
    pass