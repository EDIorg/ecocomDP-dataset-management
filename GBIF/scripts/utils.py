import pandas as pd


def read_log(f: str):
    """
    Read log file to Pandas Dataframe
    :param f: Absolute path to log file
    :return: Pandas Dataframe
    """
    log = pd.read_csv(f, delimiter=',')
    return log

def write_log(f):
    pass