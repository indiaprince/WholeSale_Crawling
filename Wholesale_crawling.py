
import requests
import json
import pandas as pd
from datetime import datetime, timedelta
url = 'http://www.kamis.or.kr/service/price/xml.do?action=dailyPriceByCategoryList'
p_product_cls_code = '02'
item_code = ['100','200','300', '400', '500', '600']
p_country_code = '1101'



now = datetime.now()
year = []
for i in range(0, 1994):
  day = now - timedelta(days=i)
  d = day.strftime("%Y-%m-%d") 
  year.append(d)
print(year)


def rice(url, p_product_cls_code, p_item_category_code, p_country_code, start_date):
  params ={
    'p_cert_key' : '111' , 
    'p_cert_id' : '222', 
    'p_returntype' : 'json', 
    'p_product_cls_code' : p_product_cls_code, 
    'p_item_category_code' : p_item_category_code,
    'p_country_code' : p_country_code,
    'p_regday' : start_date,
    'p_convert_kg_yn' : 'N',
    }
    
  response = requests.get(url, params=params)
  content = response.text
  j_content = json.loads(content)
  #print(j_content)
  if(type(j_content['data']) == list): return []
  rices = j_content['data']['item']
  return rices

r_year = []
for item in item_code:
  for y in year:
    rices = rice(url, p_product_cls_code, item, p_country_code,y)
    if(rices == []) : continue
    for i in range(len(rices)): 
      tmp= dict()
      for key in rices[i].keys():
        if(key=='day2') : break 
        elif(key=='day1') : tmp[key] = y 
        else : tmp[key] = rices[i][key]
      r_year.append(tmp)
      print(tmp)
  p = pd.DataFrame(r_year)
  p= p.set_index('day1')
  p.to_csv(f'/content/drive/MyDrive/Colab_Notebooks/price/{item}_220617_170101.csv')


