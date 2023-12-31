import pymysql as db
import bcrypt
from dataclasses import dataclass
from config import db_info



def SelectUser(id, pw):
    try:
        connection = db.connect(
            host = db_info[0],
            user = db_info[1],
            port = db_info[2],
            password = db_info[3],
            database = db_info[4],
        )
        '''
        패스워드 생성
        pwhash = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        '''
        cursor = connection.cursor()
        sql = "SELECT userid,username,userpw,level From userlist WHERE userid=%s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        if result is None:
            return None
        check_pw = result[2]        
        if bcrypt.checkpw(pw.encode('utf-8'), check_pw.encode('utf-8')):
            row = (result[0], result[1], result[3])
            return row
        else:
            return None
    
    except Exception as e:
        return e
'''
test id pw
user
passwd
'''

class DBconn:
    def __init__(self):
        self.db_info = db_info
        try:
            self.db_info = db_info
            self.connenction = db.connect(
                host = db_info[0],
                user = db_info[1],
                port = db_info[2],
                password = db_info[3],
                database = db_info[4],
            )
            self.cursor = self.connenction.cursor()
            
        except:
            raise Exception("DB Connection Error.")
    
    def commit(self):
        self.connenction.commit()
    
    def close(self):
        self.connenction.close()
     
     
class Auth(DBconn):
    def Auth(self, connection, id, pw):
        cursor = connection.cursor()
        
        