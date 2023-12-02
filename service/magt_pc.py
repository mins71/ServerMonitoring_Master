from models.mk_table import make_table_pc

obj = make_table_pc()

def add_pclist(pcname,pcuser):
    obj.add_pclist(pcname,pcuser)
    obj.create_pc_table(pcname)
    
def delect_pc():
    ...