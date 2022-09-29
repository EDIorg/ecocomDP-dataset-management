import pandas as pd
import numpy as np
import re


def add_level2(level2, filename):
    """Add level2 data package identifier to log file

    Looks for the level2 data package identifier in the log file and adds it if
    missing.

    :param level2: EDI identifier (scope.accession.revision) for level 2 dataset (DwC-A)
    :param filename: name of mgt filename where IDs are logged
    :return: None

    Notes
    -----
    This function overwrites "filename".
    """
    df = pd.read_csv(filename, delimiter=',')
    row = df.index[df["L2_dwca"] == level2]
    if row.empty:
        print("Adding " + level2 + " to " + filename)
        df.loc[len(df.index)] = [np.nan, np.nan, level2, np.nan, np.nan, np.nan]
    else:
        print(level2 + " is in " + filename)
    df.to_csv(filename, sep=',', header=True, index=False)
    return None


def find_duplicates(filename):
    """Check for data package series with different GBIF registrations

    There should only be one GBIF registration identifier per EDI data
    package scope.accession value. Raise an exception if this is not true.

    :param filename: name of mgt filename where IDs are logged
    :return: None

    Notes
    -----
    This function overwrites "filename".
    """
    df = pd.read_csv(filename, delimiter=',')
    df = df.dropna(subset=["gbif_id"])
    df["sa"] = [re.sub("\..$", "", L2_scope_acc_rev) for L2_scope_acc_rev in df.L2_dwca.to_list()]
    dfsub = df[["sa", "gbif_id"]]
    dfsub = dfsub.drop_duplicates()
    test = dfsub['sa'].value_counts()
    i = test > 1
    if any(i):
        badpkgs = [i.index[i][0]]
        print(
            "Duplicate GBIF IDs registered with data packages: " +
            ', '.join([str(x) for x in badpkgs])
        )
        raise ValueError('Duplicate registrations found in log file. Manual intervention required.')
    return None
