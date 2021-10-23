# coding: utf-8

import pandas as pd
import numpy as np
from glob import glob
from tqdm import tqdm
from . import JFE_header


def read_csv(fname, sname=False, verbose=False):
    """
    AAQの生データをパースしてpd.DataFrameで返す関数
    """
    header, i = JFE_header(fname, verbose)
    sdate = pd.to_datetime(header['StartTime'])
    lat, _, lon, _ = header['StartPosition'].split(', ')
    lat = float(lat[:2]) + float(lat[2:])/60
    lon = float(lon[:3]) + float(lon[3:])/60

    columns = {'深度 [m]':'depth',
               '水温 [℃]':'temp [degC]',
               '塩分':'salt',
               '電導度 [mS/cm]':'EC [mS/cm]',
               '密度 [kg/m3]':'rho [kg/m3]',
               'シグマＴ':'sigmaT',
               'Chl-Flu. [ppb]':'chl-Flu. [ppb]',
               'Chl-a [μg/l]':'chla [μg/l]',
               '濁度 [FTU]':'turb [FTU]',
               '光量子 [μmol/(m2*s)]':'PFD [μmol/(m2*s)]',
               'シグマＴ':'sigmaT'}

    df = pd.read_csv(fname, skiprows=i+1, encoding="shift_jis").rename(columns=columns)
    df = df[[c for c in df.columns if 'Unnamed' not in c]]
    df['date'] = sdate
    df['day'] = df.date.apply(lambda d: d.date())
    df['sname'] = sname
    df['lon'] = lon
    df['lat'] = lat
    return df
