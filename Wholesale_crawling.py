
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