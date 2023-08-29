import requests
import pandas as pd
from bs4 import BeautifulSoup
res=requests.get("https://www.flipkart.com/6bo/b5g/~cs-yr1vxer28o/pr?sid=6bo,b5g&collection-tab-name=Intel+Laptops")
soup=BeautifulSoup(res.content,"html.parser")
name=[]
names=soup.find_all('div',class_="_4rR01T")
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
price=[]
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
for i in prices[0:20]:
    p=i.get_text()
    price.append(p[1:])
image=[]
images=soup.find_all('img',class_="_396cs4")
for i in images[0:20]:
    im=i['src']
    image.append(im)
rating=[]    
ratings=soup.find_all('div',class_="_3LWZlK")
for i in ratings[0:20]:
    ra=i.get_text()
    rating.append(ra)
df=pd.DataFrame()
df['Laptop_Names']=name
df['Laptop_prices']=price
df['Images']=image
df['Ratings']=rating
df.to_csv("laptop_webscrap_data.csv")





