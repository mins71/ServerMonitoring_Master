from datetime import timedelta
import pymysql as db

# DB연결 정보
db_info = ["bangwol08.iptime.org", "SMDBuser", 30002, "SMDBuser123!@#", "ServerMonitoring"]

# secret key
class Config:
    SECRET_KEY ='7bd2b2d360a9fb56ce5f6cb984522c8b8ff6e04e110a1d88345ba7b9fe7a0455'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=180)