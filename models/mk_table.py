import pymysql as db
from models.models import DBconn
from models.pclist import cell_pc_name

class make_table_pc(DBconn):
    def __init__(self):
        super().__init__()
        
    def add_pclist(self, pcname=None, pcuser=None):
        if pcname == None or pcuser == None:
            return 'None into pcname or username'
        if pcname in cell_pc_name():
            return f"{pcname} pc has already been entered."
        try:
            sql = "INSERT INTO pclist(pcname, pcuser, pcpower) VALUES (%s, %s, 0, 0)"
            self.cursor.execute(sql,(pcname, pcuser))
            self.commit()
        except db.Error as e:
            print(e)
        finally:
            self.cursor.close()
            

    def create_pc_table(self, pcname):
        try:
            sql = f"SHOW tables LIKE '{pcname}_cpu'"
            table_exists = self.cursor.execute(sql)
            if table_exists==0:
                sql = f"""
                CREATE TABLE {pcname}_cpu
                (
                    time        varchar(30)    PRIMARY KEY,
                    cup_percent varchar(30)
                );
                """
                self.cursor.execute(sql)
                
            table_exists = self.cursor.execute(f"SHOW tables LIKE '{pcname}_mem'")
            if table_exists==0:
                sql = f"""
                CREATE TABLE {pcname}_mem
                (
                    time          varchar(30)    PRIMARY KEY,
                    TotalMemory   varchar(30)    not null,
                    UsedMemory    varchar(30)    not null,
                    FreeMemory    varchar(30)    not null,
                    MemoryPercent varchar(30)
                );
                """
                self.cursor.execute(sql)
            table_exists = self.cursor.execute(f"SHOW tables LIKE '{pcname}_disk'")
            if table_exists==0:
                sql = f"""
                CREATE TABLE {pcname}_disk
                (
                    time            varchar(30)    PRIMARY KEY,
                    UsedSpace       varchar(30)    not null,
                    FreeSpace       varchar(30)    ,
                    TotalSpace      varchar(30)    not null,
                    UsagePercentage varchar(30)    
                );
                """
                self.cursor.execute(sql)
            table_exists = self.cursor.execute(f"SHOW tables LIKE '{pcname}_metwork_bytes'")
            if table_exists==0:
                sql = f"""
                CREATE TABLE {pcname}_network_bytes
                (
                    time        varchar(30)     ,
                    interface   varchar(30)     ,
                    sent_bytes  varchar(30)     ,
                    recv_bytes  varchar(30)     ,
                    sent_packet varchar(30)     ,
                    recv_packet varchar(30)     ,
                    PRIMARY KEY (time, interface)
                );
                """
                self.cursor.execute(sql)
            table_exists = self.cursor.execute(f"SHOW tables LIKE '{pcname}_network_connections'")
            if table_exists==0:
                sql = f"""
                CREATE TABLE {pcname}_network_connections
                (
                    time        varchar(30)    not null,
                    local_ip    varchar(30)    not null,
                    local_port  varchar(30)    not null,
                    remote_ip   varchar(30)    not null,
                    remote_port varchar(30)    not null,
                    status      varchar(30)
                );
                """
                self.cursor.execute(sql)
        except Exception as e:
            return e
        self.close()
    