from models.cell_pcdata import cell_pcdata_cpu ,cell_pcdata_disk, cell_pcdata_mem
from time import time

def pcdata(pcname):
    pcd = {}
    pcd["cpu"] = cell_pcdata_cpu(pcname)
    pcd["mem"] = cell_pcdata_mem(pcname)
    pcd["disk"] = cell_pcdata_disk(pcname)
    pcd["cpu_list"] = [float(row[1]) for row in cell_pcdata_cpu(pcname)]
    pcd["time_s"] = [str(int(time() - float(row[0]))) for row in cell_pcdata_cpu(pcname)]
    
    return pcd
    
