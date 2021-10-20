import pandas as pd

def parse_header(f):
    header = {'header':''}
    for i, line in enumerate(open(f, encoding='shift_jis').readlines(4000)):
        if '[Item]' in line:
            break
        elif '=' in line:
            k, v = line.strip('\n').split('=')
            header[k] = v
        elif '//' in line:
            header['header'] += line.strip('\n')
    return header, i

def read_csv(f):
    header, i = parse_header(f)
    columns = {'日時':'date', '圧力[MPa]':'press', '深度[m]':'depth', '水温[℃]':'temp', '濁度中ﾚﾝｼﾞ[FTU]':'turb'}
    df = pd.read_csv(f, skiprows=i+1, encoding="shift_jis", parse_dates=[0]).rename(columns=columns)
    df = df[[c for c in df.columns if 'Unnamed' not in c]]
    df.index = pd.date_range(df.date[0], freq=header['Interval']+'ms', periods=df.date.size)
    return df