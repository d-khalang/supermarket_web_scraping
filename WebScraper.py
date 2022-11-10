import requests
from bs4 import BeautifulSoup

#web scraping function for collecting information of the desired product on the carrefour website
def WebScrap(searched_product):
    URL = "https://www.carrefour.it/search?q={}".format(searched_product)
    page = requests.get(URL)
    print(page)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", class_="product-item")  #exploring only the cart of products

    for item in results:
        titles = item.prettify()
        printy = titles.index("productName")
        value = titles[1896:2125]    #an stimate of where the name, brand, and cost are apperent
        for item in value.split(","):
            print(item)

        print()
        print()

#the input for the product that should be searched on the site
search = input("what product are you interested in(like: milk, nutella, raviolli ...): ")
try:
    WebScrap(search)
except:   #if there is not the exact product on the site
    print("product is not available on the site!!!")

