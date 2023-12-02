from models.models import DBconn

class Issue(DBconn):
    def __inti__(self):
        super().__inti__(self)
    def select_issue(self, pc=None):
        if pc == None:
            sql = f'SELECT * FROM warning;'
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        else:
            pclist = ""
            for s in pc:
                pclist += "'" + s + "'" + ","
            pclist = pclist[0:-1]
            sql = f"SELECT * FROM warning where slave_name in ({pclist})"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
    
    def cpu_event(self, pcname=None):
        if pcname == None:
            sql = f"SELECT count(*) FROM warning where LOWER(message) LIKE '%cpu%'"
            self.cursor.execute(sql)
            cpu_event = self.cursor.fetchone()
            return cpu_event
            
    def mem_event(self, pcname=None):
        if pcname == None:
            sql = f"SELECT count(*) FROM warning where LOWER(message) LIKE '%mem%'"
            self.cursor.execute(sql)
            mem_event = self.cursor.fetchone()
            return mem_event

    def disk_event(self, pcname=None):
        if pcname == None:
            sql = f"SELECT count(*) FROM warning where LOWER(message) LIKE '%disk%'"
            self.cursor.execute(sql)
            disk_event = self.cursor.fetchone()
            return disk_event
            
    def net_event(self, pcname=None):
        if pcname == None:
            sql = f"SELECT count(*) FROM warning where LOWER(message) LIKE '%net%'"
            self.cursor.execute(sql)
            net_event = self.cursor.fetchone()
            return net_event