from bs4 import BeautifulSoup
#import requests library
import requests
#import pandas library
import pandas as pd

Link = []
Title = []
Subtitle =[]
Desc = []
Dates = []
Price = []
Reviews = []

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

    nextpage = "https://www.airbnb.co.in" + doc.find("a", class_ = "l1ovpqvx c1ytbx3a dir dir-ltr").get("href")    
    url_link = nextpage
    result = requests.get(url_link, verify=False)
    doc = BeautifulSoup(result.text, "html.parser")

    for item in doc.select('[itemprop=itemListElement]'):

        try:

            #get link
            getlink =  item.select('a')[0]['href']
            link = "https://www.airbnb.co.in" + getlink
            Link.append(link)
            
            # get the title
            title = item.select('[data-testid=listing-card-title]')[0].get_text()
            Title.append(title)

            # get the sub title
            subtitle = item.select('[data-testid=listing-card-subtitle]')[0].get_text()
            Subtitle.append(subtitle)

            # get the desc
            desc = item.select('[data-testid=listing-card-subtitle]')[1].get_text()
            Desc.append(desc)

            # get dates
            dates = item.select('[data-testid=listing-card-subtitle]')[2].get_text()
            Dates.append(dates)

            # get price
            price = item.select('[data-testid=card-container] span span')[4].get_text()
            Price.append(price)

            # get reveiws
            reviews = item.select('[aria-label]')[0].get_text()
            Reviews.append(reviews)
            
            # create dataframe
            df = {"Name":Title, "Sub-title":Subtitle, "Details":Desc, "Dates":Dates, "Price":Price, "Reviews":Reviews, "Link":Link}
            listdf=pd.DataFrame(df)

            # convert to csv
            listdf.to_csv("airbnb_data.csv")

        except Exception as e:
            print('Exception occured: ', e)
            
        print('-----------------------------------------')