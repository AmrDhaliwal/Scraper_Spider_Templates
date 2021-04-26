from random import randint
from time import sleep

import numpy as np
import requests
from bs4 import BeautifulSoup

##If the website uses javascript to render or change pages
##selenium may need to be used to interact with the website
##from selenium import webdriver

##Functions below only need to be used if
##Making a lot fo calls to the sites servers
def save_html(html, path):
    """Function saves the parsed URL
    as a html object to reduce the
    impact on the sites servers.

    Args:
        html ([URL]): [HTML from parsed website]
        path ([File]): [The file path to the saved HTML file]
    """
    with open(path, "wb") as f:
        f.write(html)

def open_html(path):
    """Function that opens the saved html file
    from the "save_html" function

    Args:
        path ([File]): [The file path to the saved HTML file]

    Returns:
        [type]: [description]
    """
    with open(path, "rb") as f:
        return f.read()

##books.toscrape.com is a website built to practice web scraping
url = "http://books.toscrape.com/"
r = requests.get(url)
headers = {"Accept-Language": "en-US, en;q=0.9"}

##Example usage of the functions save_html and open_html
#save_html(r.content, "books_toscrape")
html = open_html("books_toscrape")
##List to store scraped data
data = []

##Build a soup object and for loops to loop through
##multiple web pages with help from the numpy library
pages = np.arange(1, 51, 1)
for page in pages:
    page = requests.get("https://books.toscrape.com" + "/catalogue/page-" + str(page) + ".html", headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    book_ratings = soup.find_all("p", class_="star-rating")
    ##Use the sleep and randomint functions
    ##to slow speed of calls to reduce stress
    ##on website servers
    sleep(randint(5, 10))
    data.append(book_ratings)