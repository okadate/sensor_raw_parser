# coding: utf-8
# update: 2020/08/30

import pandas as pd
import numpy as np


def trim(df1):
    dz = df1.depth.diff().abs()
    dz = dz.where(dz>0.01, 0.01)
    dtdz = df1.turb.diff() / dz
    dmax = df1.depth.max()
    i = np.where((dtdz.abs()>50) & (df1.depth>dmax-0.5))[0]
    j = np.where((dtdz.abs()>50) & (df1.depth<0.5))[0]
    if len(i) > 0:
        i = i[0]
        df1 = df1.iloc[:i]
    if len(j) > 0:
        j = j[-1]
        df1 = df1.iloc[j+1:]
    return df1


def read_csv(f, query=None, trimming=True):
    for i, l in enumerate(open(f, encoding='shift_jis').readlines()):
        if 'SondeName=' in l:
            sonde_name = l.split('=')[-1]
        if '[Item]' in l:
            break

    if 'ASTD102' in sonde_name:  # w/ DO
        names = 'day time depth temp salt EC EC25 dens sigT chlf chla turb DOp DO v DOgg DObk pres n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11'.split()
        names_out = names[2:-11]
        
    elif 'ASTD151' in sonde_name:  # w/o DO
        names = 'day time depth temp salt EC EC25 dens sigT chlf chla turb v n'.split()
        names_out = names[2:-2]
        
    else:
        print(sonde_name)

    df = pd.read_csv(f, skiprows=i+2, names=names, parse_dates={'date':['day','time']}, index_col='date')[names_out]
    if query is not None:
        df = df.query(query)

    N = int(df.shape[0])
    sur = np.where(df.iloc[:N//2].depth==df.iloc[:N//2].depth.min())[0][0]
    #sur = np.where(df.depth==df.depth.min())[0][-1]
    bot = np.where(df.depth==df.depth.max())[0][0]
    df_down = df.iloc[sur:bot]
    
    if trimming:
        df_down = trim(df_down)
    
    return df, df_down
