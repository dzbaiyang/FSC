import os
import FakebobMinioConfig
import datetime
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import sqlite3
from minio import Minio, InvalidResponseError


"""
@project : Fakebob Load Minio
@author  : Bai.Yang
@time   : 2022-11-02
"""

localtime = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y%m%d") #多加（减）一天
pathname = 'D:\Project\FSC\data\\test.csv'
print("执行SQL时间：",datetime.datetime.now())

conn = create_engine("mysql+pymysql://root:hirisun@localhost:3306/fakebob")
sql = '''select * from test1'''
fakebob = pd.read_sql_query(sql,conn)
page = pathname
fakebob.to_csv(page,index= False)
# 上传数据至Minio
try:
    with open('D:\Project\FSC\data\\test.csv', 'rb') as file_data:
        file_stat = os.stat('D:\Project\FSC\data\\test.csv')
        print(FakebobMinioConfig.minioClientFakebob.put_object('fakebob', '/test/test.csv',
                                                 file_data, file_stat.st_size))
except InvalidResponseError as err:
    print(err)



