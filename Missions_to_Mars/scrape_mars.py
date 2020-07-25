from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd


def init_browser():
    executable_path = {
        "executable_path": "/Users/rober/Desktop/web-scraping-challenge/Missions_to_Mars/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    time.sleep(1)
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # stuff = soup.find_all('div', class_="content_title").get_text()
    title = soup.find_all('div', class_="content_title")[1].get_text()
    atext = soup.find('div', class_="article_teaser_body").get_text()

    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser2 = init_browser()
    browser2.visit(url2)
    html2 = browser2.html
    soup2 = BeautifulSoup(html2, "html")

    featured_image_url = soup2.find("a", class_="button fancybox").get_text()

    url4 = "https://space-facts.com/mars/"

    tables = pd.read_html(url4)
    space_df = tables[0]
    space_df.columns = ["0", "1"]
    space_df

    hemisphere_image_urls = [
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
        # "Test1": stuff,
        "Test2": title,
        "Test3": atext,
        "Test4": featured_image_url,
        "Test5": space_df,
        "Test6": hemisphere_image_urls
    }
    return listings
