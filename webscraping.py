
from bs4 import BeautifulSoup
import requests
import webbrowser
def scraper():
    list_links=[]
    list_type=[]
    list_price=[]
    b= input('input the commodity you want :')
    payload = {'q' :b}
    c = requests.get('https://www.jumia.co.ke/catalog/',params=payload).content
    soup  = BeautifulSoup(c,'lxml')

    item  = soup.find_all('h3',class_='name')
    for i in item:
         list_type.append(i.text)

    price = soup.find_all('div',class_='prc')
    for j in price:
         list_price.append(j.text)
    
    links = soup.find_all('article',class_='prd _fb col c-prd')
    for i in links:
        c=i.a['href']
        list_links.append(c)
    
    
    for q in range(len(list_type)):
         print([q , list_type[q] , list_price[q] ])
         
    number = int(input('select your choice :'))
    url = 'https://www.jumia.co.ke//' + list_links[number]
    webbrowser.open(url)
     
    
scraper()

