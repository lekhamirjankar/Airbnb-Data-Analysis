from bs4 import BeautifulSoup
#import requests library
import requests
#import pandas library
import pandas as pd

# Initialize empty lists to store data
Link = []
Title = []
Subtitle =[]
Desc = []
Dates = []
Price = []
Reviews = []

# The website URL
url_link = "https://www.airbnb.co.in/s/India/homes?adults=1&place_id=ChIJkbeSa_BfYzARphNChaFPjNc&refinement_paths%5B%5D=%2Fhomes"

# Make a GET request to the provided URL
result = requests.get(url_link, verify=False)
doc = BeautifulSoup(result.text, "html.parser")

# Get the maximum number of pages
counter=[]
pagination = doc.find_all(class_ = "l1ovpqvx c1ackr0h dir dir-ltr")
for i in pagination :
    count=int(i.get_text())
    counter.append(count)
max_pages = max(counter)

# Loop through each page
for i in range(1,max_pages):
    # Generate the URL for the current page
    nextpage = "https://www.airbnb.co.in" + doc.find("a", class_ = "l1ovpqvx c1ytbx3a dir dir-ltr").get("href")    
    url_link = nextpage
    # Make a GET request to the current page
    result = requests.get(url_link, verify=False)
    doc = BeautifulSoup(result.text, "html.parser")

    # Extract data from each listing on the page
    for item in doc.select('[itemprop=itemListElement]'):

        try:

            # Get link
            getlink =  item.select('a')[0]['href']
            link = "https://www.airbnb.co.in" + getlink
            Link.append(link)
            
            # Get the title
            title = item.select('[data-testid=listing-card-title]')[0].get_text()
            Title.append(title)

            # Get the sub title
            subtitle = item.select('[data-testid=listing-card-subtitle]')[0].get_text()
            Subtitle.append(subtitle)

            # Get the desc
            desc = item.select('[data-testid=listing-card-subtitle]')[1].get_text()
            Desc.append(desc)

            # Get dates
            dates = item.select('[data-testid=listing-card-subtitle]')[2].get_text()
            Dates.append(dates)

            # Get price
            price = item.select('[data-testid=card-container] span span')[4].get_text()
            Price.append(price)

            # Get reveiws
            reviews = item.select('[aria-label]')[0].get_text()
            Reviews.append(reviews)

        except Exception as e:
            # If an exception occurs during data extraction, print the error message
            print('Exception occured: ', e)

    # Create a dictionary to store the collected data
    data_dict = {
        "Name": Title,
        "Sub-title": Subtitle,
        "Details": Desc,
        "Dates": Dates,
        "Price": Price,
        "Reviews": Reviews,
        "Link": Link
        }

    # Convert the dictionary into a Pandas DataFrame
    df = pd.DataFrame(data_dict)

    # Save the data to a CSV file
    df.to_csv("airbnb_data.csv", index=False)