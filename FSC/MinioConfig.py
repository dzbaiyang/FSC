from minio import Minio
from minio import Minio, InvalidResponseError

# 使用endpoint、access key和secret key来初始化minioClient对象
minioClient = Minio('172.25.247.200:9000',
                    access_key='fscpilot-account',
                    secret_key='R25PNR$oDCoA',
                    secure=False)


