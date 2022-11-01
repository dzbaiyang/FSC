import datetime
import os
import zipfile
import pandas as pd
import sqlite3
import pymysql

localtime = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y%m%d") #多加（减）一天
pathname = 'D:\Project\FSC\data\{}_test.csv'.format(localtime)

conn = pymysql.connect(
    host='localhost',
    user = "root",
    passwd = 'hirisun',
    port = 3306,
    db = 'fakebob',
    charset='utf8')
print("执行SQL时间：",datetime.datetime.now())

test1 = pd.read_sql("""
select * from test1
""",con=conn)

print(test1)

page = pathname
test1.to_csv(page,index = False)
