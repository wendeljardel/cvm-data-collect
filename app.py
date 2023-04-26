from collect.data_collect import Collect
from utils.date_utils import Utils
from datetime import datetime
import os




CRI_YEARS = [x for x in range(2019,datetime.now().year + 1)]
FII_YEARS = [x for x in range(2018,datetime.now().year + 1)]
FII_YEARLY = [x for x in range(2018,datetime.now().year - 1)]


if __name__ == '__main__':    
    #CRI
    # for i in CRI_YEARS:
    #     save_path = f"collect/files/cri_{i}.zip"
    #     directory = f"collect/files/cri/{i}"
    #     url = f"https://dados.cvm.gov.br/dados/SECURIT/DOC/INF_MENSAL_CRI/DADOS/inf_mensal_cri_{i}.zip"
    #     cri_collect = Collect(url,save_path,directory)
    #     cri_collect.download_files()
    #     cri_collect.unzip_files()
    
    # #FII TRIMESTRAL
    # for i in FII_YEARS:
    #     save_path = f"collect/files/fii_quarterly_{i}.zip"
    #     directory = f"collect/files/fii_quarterly/{i}"
    #     url = f"https://dados.cvm.gov.br/dados/FII/DOC/INF_TRIMESTRAL/DADOS/inf_trimestral_fii_{i}.zip"
    #     fii_collect = Collect(url,save_path,directory)
    #     fii_collect.download_files()
    #     fii_collect.unzip_files()
    #     os.remove(save_path)

    # # FII MENSAL
    # for i in FII_YEARS:
    #     save_path = f"collect/files/fii_monthly_{i}.zip"
    #     directory = f"collect/files/fii_monthly/{i}"
    #     url = f"https://dados.cvm.gov.br/dados/FII/DOC/INF_MENSAL/DADOS/inf_mensal_fii_{i}.zip"
    #     fii_collect = Collect(url,save_path,directory)
    #     fii_collect.download_files()
    #     fii_collect.unzip_files()
    #     os.remove(save_path)
    
    # FII YEARLY
    # for i in FII_YEARLY:
    #     save_path = f"collect/files/fii_yearly_{i}.zip"
    #     directory = f"collect/files/fii_yearly/{i}"
    #     url = f"https://dados.cvm.gov.br/dados/FII/DOC/INF_ANUAL/DADOS/inf_anual_fii_{i}.zip"
    #     fii_collect = Collect(url,save_path,directory)
    #     fii_collect.download_files()
    #     fii_collect.unzip_files()
    #     os.remove(save_path)
    
    #FII/FIDC - INFORMAÇÃO CADASTRAL
    # save_path = f"collect/files/fii_fidc_registration/fii_fidc_registration.csv"
    # directory = f"collect/files/fii_fidc_registration/"
    # url = "https://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi.csv"
    # fii_collect = Collect(url,save_path,directory)
    # fii_collect.download_files()
    
    #OFERTAS DE DISTRIBUIÇÃO
    # save_path = f"collect/files/distribution_offer/distribution_offer.csv"
    # directory = f"collect/files/distribution_offer/"
    # url = "https://dados.cvm.gov.br/dados/OFERTA/DISTRIB/DADOS/oferta_distribuicao.csv"
    # fii_collect = Collect(url,save_path,directory)
    # fii_collect.download_files()

    # #CRA
    # for i in CRI_YEARS:
    #     save_path = f"collect/files/cra_{i}.zip"
    #     directory = f"collect/files/cra/{i}"
    #     url = f"https://dados.cvm.gov.br/dados/SECURIT/DOC/INF_MENSAL_CRA/DADOS/inf_mensal_cra_{i}.zip"
    #     cra_collect = Collect(url,save_path,directory)
    #     cra_collect.download_files()
    #     cra_collect.unzip_files()
    #     os.remove(save_path)

    # FII/FIDC FUNDOS ESTRUTURADOS: MEDIDAS

    # print(f"{datetime.now().year}{str(datetime.now().month - 1).zfill(2)}")
    Utils.time_structured_funds(start_year=2017)
    

    

    
    
