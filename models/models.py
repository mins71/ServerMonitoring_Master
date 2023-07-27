import pymysql as db
import bcrypt
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
        sql = "SELECT userid,username,userpw From userlist WHERE userid=%s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        if result is None:
            return None
        check_pw = result[2]        
        if bcrypt.checkpw(pw.encode('utf-8'), check_pw.encode('utf-8')):
            row = (result[0], result[1])
            return row
        else:
            return None
    
    except Exception as e:
        return e
'''
test id pw
user2
passwd
'''