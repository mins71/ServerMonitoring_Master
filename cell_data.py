from models.cell_pcdata import cell_pcdata_cpu ,cell_pcdata_disk, cell_pcdata_mem

def pcdata(pcname):
    pcd = {}
    pcd["cpu"] = cell_pcdata_cpu(pcname)
    pcd["mem"] = cell_pcdata_mem(pcname)
    pcd["disk"] = cell_pcdata_disk(pcname)
    
    return pcd
    

if __name__ == "__main__":
    pd = pcdata("com1")
    print(pd)