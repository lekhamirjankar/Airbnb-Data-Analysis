from bs4 import BeautifulSoup
#import requests library
import requests
#the website URL
url_link = "https://www.airbnb.co.in/s/India/homes?adults=1&place_id=ChIJkbeSa_BfYzARphNChaFPjNc&refinement_paths%5B%5D=%2Fhomes"
result = requests.get(url_link, verify=False)

#  .text
doc = BeautifulSoup(result.text, "html.parser")

for item in doc.select('[itemprop=itemListElement]'):
    # print(item.find("a").get("href"))

    try:
        print(item.select('[data-testid=listing-card-title]')[0].get_text())

    except:
        print('Exception occured')
    
    print('-----------------------------------------')