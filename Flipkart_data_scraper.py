import requests
from bs4 import BeautifulSoup as bs 
products=[]
ratings=[]
prices=[] 

link = 'https://www.flipkart.com/search?sid=6bo%2Cb5g&p%5B%5D=facets.processor_generation%255B%255D%3D11th%2BGen&p%5B%5D=facets.processor_brand%255B%255D%3DIntel&pageUID=1622458269615&otracker=clp_banner_1_11.banner.BANNER_laptops-store_AYUHKLJ0IY14'
page = requests.get(link)
page.content
soup = bs(page.content, 'html.parser')
for detail in soup.findAll('div',class_='_3pLy-c row'):
        names=detail.find('div', attrs={'class':'_4rR01T'})
        price=detail.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        products.append(names.text)
        prices.append(price.text)
        
for rate in soup.findAll('div',class_='gUuXy-'):
        rating=rate.find('div', attrs={'class':'_3LWZlK'})
        ratings.append(rating.text)
ratings.append(4.4)
print(len(ratings))
df=pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
