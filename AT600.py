
# 2021/01/20 (c) Teruhisa Okada

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def parse_html(html):
    bs = BeautifulSoup(open(html), "html.parser")

    names = bs.find_all('table')[0].find_all('tr', {'class':'dataHeader'})[0].find_all('td')

    sensor = {'717433':'depth',
             '720541':'temperature',
             '717648':'salinity',
             '708120':'chlorophyll',
             '718968':'DO',
             '718332':'turbidity'}

    ptype = {'3':'depth',
             '1':'temperature',
             '12':'salinity',
             '50':'chlorophyll',
             '20':'DO',
             '25':'turbidity'}

    columns = []
    for name in names:
        if name.attrs['isi-data-column-header'] == 'DateTime':
            column = 'date'
        elif name.attrs['isi-data-column-header'] == 'Marked':
            column = 'mark'
        elif name.attrs['isi-parameter-type'] == '6':
            column = 'latitude'
        elif name.attrs['isi-parameter-type'] == '7':
            column = 'longitude'
        elif name.attrs['isi-parameter-type'] in ptype.keys():
            column = ptype[name.attrs['isi-parameter-type']]
        else:
            column = 'none'
        columns.append(column)

    rows = bs.find_all('table')[0].find_all('tr', {'class':'data'})

    data = []
    for row in rows:
        data.append([x.get_text() if len(x)>0 else np.nan for x in row.find_all('td')])

    df = pd.DataFrame(data, columns=columns)
    #print(df.columns)
    df.date = pd.to_datetime(df.date)
    df = df.applymap(lambda x: float(x) if type(x)==str else x)
    
    #i = np.where(df.depth==df.depth.max())[0][0]
    #df = df.iloc[:i]
    df = df.set_index('date')
    
    return df[ptype.values()]
