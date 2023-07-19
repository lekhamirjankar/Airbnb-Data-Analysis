from bs4 import BeautifulSoup
#import requests library
import requests
#the website URL
url_link = "https://www.airbnb.co.in/s/India/homes?adults=1&place_id=ChIJkbeSa_BfYzARphNChaFPjNc&refinement_paths%5B%5D=%2Fhomes"

result = requests.get(url_link, verify=False)

doc = BeautifulSoup(result.text, "html.parser")

# get the maximum number of pages
counter=[]
_as = doc.find_all(class_ = "l1ovpqvx c1ackr0h dir dir-ltr")
for a in _as :
    count=int(a.get_text())
    counter.append(count)
max = max(counter)

# loop through each page
for i in range(1,max):
    np=doc.find("a", class_ = "l1ovpqvx c1ytbx3a dir dir-ltr").get("href")

    cnp = "https://www.airbnb.co.in" + np

    url_link = cnp
    result = requests.get(url_link, verify=False)
    doc = BeautifulSoup(result.text, "html.parser")

    for item in doc.select('[itemprop=itemListElement]'):

        try:

            #get link
            Link =  item.select('a')[0]['href']
            print("https://www.airbnb.co.in" + Link)
            
            # get the title
            print(item.select('[data-testid=listing-card-title]')[0].get_text())

            # get the sub title
            print(item.select('[data-testid=listing-card-subtitle]')[0].get_text())

            # get the desc
            print(item.select('[data-testid=listing-card-subtitle]')[1].get_text())

            # get dates
            print(item.select('[data-testid=listing-card-subtitle]')[2].get_text())

            # get price
            print(item.select('[data-testid=card-container] span span')[4].get_text()) 

            # get reveiws
            print(item.select('[aria-label]')[0].get_text())

        except Exception as e:
            print('Exception occured: ', e)
            
        print('-----------------------------------------')