
# 2021/03/11 (c) Teruhisa Okada

import pandas as pd

def read_csv(f, verbose=True):
    
    txt = ''
    for i, line in enumerate(open(f, encoding='shift_jis').readlines(1000)):
        if '[Item]' in line: break
        txt += line
    
    if verbose:
        print(txt)
    
    # 日時 水温[℃] DO[%] Weiss-DO[mg/l] 電池電圧[V] G&G-DO[mg/l] B&K-DO[mg/l]

    col = pd.read_csv(f, skiprows=i+2).columns
    if col.size == 7:
        names = 'date temp DOp DO n0 DO_gg DO_bk n1'.split()
    else:
        names = 'date temp DOp DO n0 DO_gg DO_bk n1 n2 n3 n4'.split()
    
    df = pd.read_csv(f, skiprows=i+2, names=names,
                     parse_dates=['date'], index_col='date')
    
    return df['temp DOp DO DO_gg DO_bk'.split()]
