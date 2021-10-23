import pandas as pd
from . import JFE_header

def read_csv(f, verbose=False):
    header, i = JFE_header(f, verbose)
    columns = {'日時':'date',
               '圧力[MPa]':'press',
               '深度[m]':'depth',
               '水温[℃]':'temp',
               '濁度中ﾚﾝｼﾞ[FTU]':'turb',
               '電池電圧[V]':'battery'}
    df = pd.read_csv(f, skiprows=i+1, encoding="shift_jis", parse_dates=[0]).rename(columns=columns)
    df = df[[c for c in df.columns if 'Unnamed' not in c]]
    df.index = pd.date_range(df.date[0], freq=header['Interval']+'ms', periods=df.date.size)
    return df