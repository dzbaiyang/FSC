from minio import Minio
from minio import Minio, InvalidResponseError

# 使用endpoint、access key和secret key来初始化minioClient对象
minioClientFakebob = Minio('localhost:9000',
                    access_key='eEJXyp17wlfiyQtc',
                    secret_key='TbD0XZm3MBBgy8zImEv4hX0Z7I5PXs0S',
                    secure=False)