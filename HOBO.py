import pandas as pd


def dateparser(inp):
    date = pd.to_datetime(inp[:-3])
    if date.hour == 12:
        return date
    if inp.split()[-1] == u'午後':
        date += pd.Timedelta(hours=12)
        return date
    return date


def read_csv(f, raw=False):
    if raw:
        df = pd.read_csv(f, skiprows=2, 
                         names='No date press temp'.split(), 
                         date_parser=dateparser, 
                         parse_dates=['date'],
                         index_col='date')
        return df['press temp'.split()]
    else:
        df = pd.read_csv(f, skiprows=2, 
                         names='No date Pw temp Pa depth ID'.split(), 
                         date_parser=dateparser, 
                         parse_dates=['date'],
                         index_col='date')
        return df['depth ID'.split()]


if __name__ == '__main__':
    assert(dateparser('08/21/20 01:46:22 午後')==pd.to_datetime('2020-08-21 13:46:22'))