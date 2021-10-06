# coding: utf-8

import pandas as pd
import numpy as np
from glob import glob
from tqdm import tqdm


def read_csv(fname, interpolate_date=True, layer=False):
    """
    AAQの生データをパースしてpd.DataFrameで返す関数
    
    interpolate_date　測定開始と終了時刻で補間する
    """

    # get date, lon, lat
    with open(fname, encoding='shift_jis') as f:
        for i, line in enumerate(f.readlines()[:77]):
            if len(line)>10 and line[3:10]=='Version':
                version = float(line[11:])
            if len(line)>9 and line[:9]=='StartTime':
                sdate = pd.to_datetime(line[10:])
            if len(line)>7 and line[:7]=='EndTime':
                edate = pd.to_datetime(line[8:])
            if len(line)>13 and line[:13]=='StartPosition':
                if line[14] == '-':
                    lat, lon = None, None
                    continue
                lat, _, lon, _ = line[14:].split(', ')
                lat = float(lat[:2]) + float(lat[2:])/60
                lon = float(lon[:3]) + float(lon[3:])/60
            if len(line)>6 and line[:6]=='[Item]':
                item = i
    
    if layer:
        sname = fname.split('_')[-2]
    else:
        sname = fname.split('_')[-1].split('.')[0]
        #if sname == 'C6-2': return

    # read data
    if version <= 1.06: # TokyoBay2019
        names = 'depth temp salt EC EC25 sigma sigmaT flu chla turb pH ORP DOp DO quantum date'.split()
    elif version >= 1.08: #TokyoBay2020
        names = 'depth temp salt EC EC25 sigma sigmaT flu chla turb pH ORP DOp DO quantum DO_GG DO_BK date'.split()
    else:
        print(version)
    df = pd.read_csv(fname, skiprows=item+2, names=names)
    
    # set datetime
    if interpolate_date:
        date = pd.to_datetime(df.date)
        date.iloc[0] = sdate
        date.iloc[-1] = edate
        ndate = pd.to_numeric(date)
        ndate[ndate<0] = np.nan
        df.date = pd.to_datetime(ndate.interpolate()).apply(lambda t: t.round('ms'))
    else:
        df.date = sdate
    df['day'] = df.date.apply(lambda d: d.date())

    # set stations
    df['sname'] = sname
    df['lon'] = lon
    df['lat'] = lat
    
    return df
