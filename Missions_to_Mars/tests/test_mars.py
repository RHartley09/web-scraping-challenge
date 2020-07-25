# from splinter import Browser
# from bs4 import BeautifulSoup


# def init_browser():
#     # @NOTE: Replace the path with your actual path to the chromedriver
#     executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
#     return Browser("chrome", **executable_path, headless=False)


# def scrape():
#     browser = init_browser()
#     listings = {}

#     url = "https://raleigh.craigslist.org/search/hhh?max_price=1500&availabilityMode=0"
#     browser.visit(url)

#     html = browser.html
#     soup = BeautifulSoup(html, "html.parser")

#     listings["headline"] = soup.find("a", class_="result-title").get_text()
#     listings["price"] = soup.find("span", class_="result-price").get_text()
#     listings["hood"] = soup.find("span", class_="result-hood").get_text()

#     return listings


from splinter import Browser
from bs4 import BeautifulSoup
import time


def init_browser():
    executable_path = {"executable_path": "/Users/rober/Desktop/web-scraping-challenge/Missions_to_Mars/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()   
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html")

    listings["1"] = soup.find_all('div', class_="content_title")[1].text

    listings["2"] = title = soup.find('div', class_="content_title").text
    listings["3"] = atext = soup.find('div', class_="article_teaser_body").text

    print(title)
    print("------")
    print(atext)

    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser2 = Browser('chrome', **executable_path, headless=False)
    browser2.visit(url2)
    html2 = browser2.html
    soup2 = BeautifulSoup(html2, "html")

    listings["4"] = featured_image_url = soup2.find("a", class_="button fancybox")
    featured_image_url

    url4 = "https://space-facts.com/mars/"
    listings["5"] = tables = pd.read_html(url4)
    tables

    space_df = tables[0]
    space_df.columns = ["0", "1"]
    space_df

    listings["6"] = hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere",
            "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere",
            "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere",
            "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere",
            "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]

listings = {
    "Test1": listings["1"],
    "Test2": listings["2"],
    "Test3": listings["3"],
    "Test4": listings["4"],
    "Test5": listings["5"],
    "Test6": listings["6"] 
}

return listings 