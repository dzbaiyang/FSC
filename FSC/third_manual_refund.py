import os
import MinioConfig
import datetime
import pandas as pd
import pymysql
from minio import Minio, InvalidResponseError


"""
@project : FSC-Load Data to Minio
@author  : Bai.Yang
@time   : 2022-11-02
"""

localtime = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y%m%d") #多加（减）一天
pathname = '/data/minio/data/third_manual_refund.csv'

conn = pymysql.connect(
    host='172.31.9.100',
    user = "fsc_dataarchive",
    passwd = 'Yumc#1017',
    port = 4000,
    db = 'fsc_prime',
    charset='utf8')
print("执行SQL时间：",datetime.datetime.now())

cpos_tender_info = pd.read_sql("""
select * from fsc_orderdetail_prod.third_manual_refund where refund_time>='2022-09-01'
""",con=conn)

page = pathname
cpos_tender_info.to_csv(page,index = False)

# 上传数据至Minio
try:
    with open('/data/minio/data/third_manual_refund.csv', 'rb') as file_data:
        file_stat = os.stat('/data/minio/data/third_manual_refund.csv')
        print(MinioConfig.minioClient.put_object('fscpilot-bkt', '/third_manual_refund/third_manual_refund.csv',
                                                 file_data, file_stat.st_size))
except InvalidResponseError as err:
    print(err)



