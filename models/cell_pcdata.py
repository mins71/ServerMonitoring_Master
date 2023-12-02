import pymysql as db
from config import db_info

def cell_pcdata_db(pcname):
    try:
        connection = db.connect(
            host = db_info[0],
            user = db_info[1],
            port = db_info[2],
            password = db_info[3],
            database = db_info[4],
        )
        
        cursor = connection.cursor()
        sql = f"SELECT cpu_percent FROM {pcname}_cpu"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        return e
    
def cell_pcdata_cpu(pcname):
    try:
        connection = db.connect(
            host = db_info[0],
            user = db_info[1],
            port = db_info[2],
            password = db_info[3],
            database = db_info[4],
        )
        
        cursor = connection.cursor()
        sql = f"SELECT * FROM (SELECT * FROM {pcname}_cpu ORDER BY time DESC LIMIT 10) AS t ORDER BY time ASC"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        return e
    
def cell_pcdata_mem(pcname):
    try:
        connection = db.connect(
            host = db_info[0],
            user = db_info[1],
            port = db_info[2],
            password = db_info[3],
            database = db_info[4],
        )
        
        cursor = connection.cursor()
        sql = f"SELECT * FROM (SELECT * FROM {pcname}_mem ORDER BY time DESC LIMIT 10) AS t ORDER BY time ASC"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        return e
    
def cell_pcdata_disk(pcname):
    try:
        connection = db.connect(
            host = db_info[0],
            user = db_info[1],
            port = db_info[2],
            password = db_info[3],
            database = db_info[4],
        )
        
        cursor = connection.cursor()
        sql = f"SELECT * FROM (SELECT * FROM {pcname}_disk ORDER BY time DESC LIMIT 10) AS t ORDER BY time ASC"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        return e
    
    
def cell_pcdate_net(pcname):
    try:
        connection = db.connect(
            host = db_info[0],
            user = db_info[1],
            port = db_info[2],
            password = db_info[3],
            database = db_info[4],
        )
        
        cursor = connection.cursor()
        sql = f"SELECT * FROM (SELECT * FROM {pcname}_network_bytes ORDER BY time DESC LIMIT 10) AS t ORDER BY time ASC"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        return e
    