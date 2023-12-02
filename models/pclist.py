import pymysql as db
from config import db_info

def CellPc():
    try:
        connection = db.connect(
            host = db_info[0],
            user = db_info[1],
            port = db_info[2],
            password = db_info[3],
            database = db_info[4],
        )
        
        cursor = connection.cursor()
        sql = "SELECT pcname,pcuser,pcpower,pcshare FROM pclist"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        return e
    
def cell_pc_name():
    pcname = CellPc()
    pc_name_lsit = list(map(lambda i: i[0], pcname))
    return pc_name_lsit

def cell_pc_column(pcname):
    try:
        connection = db.connect(
            host = db_info[0],
            user = db_info[1],
            port = db_info[2],
            password = db_info[3],
            database = db_info[4],
        )
        
        cursor = connection.cursor()
        sql = "SELECT pcname,pcuser,pcpower,pcshare FROM pclist WHERE pcname='{pcname}'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        return e