import pandas as pd


def init_log(f):
    """
    Initialize log and write to file

    Parameters
    ----------
    f
        Log file path.

    Returns
    -------
    None
    """
    df = pd.DataFrame(columns=['id_local', 'id_gbif', 'crawled'])
    df.to_csv(f, index=False, mode='x')


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
    validate_log(log)
    log['crawled'] = pd.to_datetime(log['crawled'])
    return log


def validate_log(df):
    """
    Validate log file contents

    Parameters
    ----------
    df
        Pandas dataframe.

    Returns
    -------
    None

    """
    required_cols = {'id_local', 'id_gbif', 'crawled'}.issubset(set(df.columns))
    if not required_cols:
        raise ValueError('One or more required columns missing')
    duplicate_keys = df.duplicated(subset=['id_local', 'id_gbif'])
    if any(duplicate_keys):
        i = duplicate_keys.index[duplicate_keys].to_list()
        msg = 'Duplicate keys ("id_local" + "id_gbif") at row: ' + ', '.join([str(x+1) for x in i])
        raise ValueError(msg)


def write_log(f):
    pass