# (c) 2021-10-09 OKADA Teruhisa

import pandas as pd

def read_csv(f, verbose=True):
    header = ''
    for i, l in enumerate(open(f, encoding='shift_jis').readlines()):
        if '[Item]' in l:
            break
        else:
            header += l
            
    if verbose:
        print(header)

    return pd.read_csv(f, skiprows=i+2, parse_dates=[0], index_col=0, names='date photon V n'.split()).photon
