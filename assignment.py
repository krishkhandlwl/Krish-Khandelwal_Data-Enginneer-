import csv
import os
import xml.etree.ElementTree as ET


# Parsing
tree = ET.parse('C:/Users/Krish/python/pythoncodes/DLTINS_20210117_01of01.xml')
root = tree.getroot()

with open('C:/Users/Krish/python/pythoncodes/NewData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    
    writer.writerow(['FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm', 'FinInstrmGnlAttrbts.ClssfctnTp', 'FinInstrmGnlAttrbts.CmmdtyDerivInd', 'FinInstrmGnlAttrbts.NtnlCcy', 'Issr'])
    
     
    for fin_instrm in root.findall('FinInstrm'):
        fin_instrm_attr = fin_instrm.findall('FinInstrmGnlAttrbts')
        id = fin_instrm_attr.findall('Id').text
        full_nm = fin_instrm_attr.findall('FullNm').text
        clssfctn_tp = fin_instrm_attr.findall('ClssfctnTp').text
        cmmdty_deriv_ind = fin_instrm_attr.findall('CmmdtyDerivInd').text
        ntnl_ccy = fin_instrm_attr.findall('NtnlCcy').text
        writer.writerow([id, full_nm, clssfctn_tp, cmmdty_deriv_ind, ntnl_ccy])
    
    for fin_instrm in root.findall('TermntdRcrd'):
        fin_instrm_attr = fin_instrm.find('Issr')
        issr = fin_instrm.findall('Issr').text

        writer.writerow([issr])

 
