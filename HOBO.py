import pandas as pd


def dateparser(inp):
    date = pd.to_datetime(inp[:-3])
    ampm = inp.split()[-1]
    if ampm == u'午前' and date.hour == 12:
        date -= pd.Timedelta(hours=12)
    elif ampm == u'午後' and date.hour != 12:
        date += pd.Timedelta(hours=12)
    return date


def read_csv(f, raw=False):
    df = pd.read_csv(f, skiprows=1, 
                         date_parser=dateparser, 
                         parse_dates=[1],
                         index_col=1)
    df.index.name = 'date'
    names = df.columns.values
    for i, name in enumerate(names):
        if 'DO' in name:
            names[i] = 'DO'
        elif u'温度' in name:
            names[i] = 'temp'
    df.columns = names
    #df = df.rename(columns={"DO 濃度, mg/L (LGR S/N: 20758290, SEN S/N: 20758290)":'DO',
    #                    "温度, °C (LGR S/N: 20758290, SEN S/N: 20758290)":'temp'})
    return df

if __name__ == '__main__':
    assert(dateparser('08/21/20 01:46:22 午後')==pd.to_datetime('2020-08-21 13:46:22'))