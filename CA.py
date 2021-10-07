# (c) 2020-06-26 Teruhisa Okada

import seawater as sw
import pandas as pd

def salt(C, T, P):
    Cstd = 42914.0  # Culkin and Smith 1980
    R = C / Cstd
    return sw.salt(R, T, P)

def depth(P, f):
    lat = pd.read_csv(f, nrows=26, index_col=0, names='name value'.split()).loc['% Start latitude'].map(float).values[0]
    return sw.dpth(P, lat)

def read_csv(f):
    mt = pd.read_csv(f, nrows=27, names='name data'.split(), index_col='name')
    cast = mt.loc['% Cast data'].values[0]
    if cast == 'Raw':
        df = pd.read_csv(f, skiprows=28, index_col=0)
        df.columns = 'P temp C'.split()
        df['depth'] = depth(df.P, f)
        df['salt'] = salt(df.C, df.temp, df.P)
    return df
