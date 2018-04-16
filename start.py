# coding: utf-8

from settings import *
import os
import pandas as pd
import datetime
from database import conn_required, Config


def add_date_col(in_file, out_file):
    """

    :param in_file: input file name: str
    :param out_file: output file name: str
    :return: None
    """
    df = pd.read_csv(in_file, encoding='utf-8')
    date_col = df[['日期', '时间']].apply(lambda row: datetime.datetime.strptime(' '.join(row), '%Y-%m-%d %H:%M:%S'),
                                      axis=1)
    df.insert(0, 'Date', date_col)
    df.drop(['日期', '时间'], axis=1, inplace=True)
    df.to_csv(out_file, index=False)


@conn_required
def to_mongo(in_file):
    df = pd.read_csv(in_file, encoding='utf-8')
    date_col = df[['日期', '时间']].apply(lambda row: datetime.datetime.strptime(' '.join(row), '%Y-%m-%d %H:%M:%S'),
                                      axis=1)
    df.insert(0, 'Date', date_col)
    df.drop(['日期', '时间'], axis=1, inplace=True)
    cols = list(df)
    data = []
    for idx, row in df.iterrows():
        item = {}
        for col in cols:
            item.update({
                col: row[col]
            })
        data.append(item)
    Config.db.Price.insert_many(data)


if __name__ == '__main__':
    in_file = os.path.join(INPUT, 'NIMI_20160105.csv')
    to_mongo(in_file)
