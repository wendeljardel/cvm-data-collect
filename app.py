from collect.data_collect import Collect
from datetime import datetime
import os




CRI_YEARS = [x for x in range(2019,datetime.now().year + 1)]
FII_YEARS = [x for x in range(2018,datetime.now().year + 1)]


if __name__ == '__main__':    
    #CRI
    # for i in CRI_YEARS:
    #     save_path = f"collect/files/cri_{i}.zip"
    #     directory = f"collect/files/cri/{i}"
    #     url = f"https://dados.cvm.gov.br/dados/SECURIT/DOC/INF_MENSAL_CRI/DADOS/inf_mensal_cri_{i}.zip"
    #     cri_collect = Collect(url,save_path,directory)
    #     cri_collect.download_files()
    #     cri_collect.unzip_files()
    
    #FII TRIMESTRAL
    for i in FII_YEARS:
        save_path = f"collect/files/fii_quarterly_{i}.zip"
        directory = f"collect/files/fii_quarterly/{i}"
        url = f"https://dados.cvm.gov.br/dados/FII/DOC/INF_TRIMESTRAL/DADOS/inf_trimestral_fii_{i}.zip"
        fii_collect = Collect(url,save_path,directory)
        fii_collect.download_files()
        fii_collect.unzip_files()
        os.remove(save_path)

    
    

    

    
    
