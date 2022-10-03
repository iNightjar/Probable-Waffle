from csv import QUOTE_NONNUMERIC
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# legal github page from the course owner.. to scrape data from
quotesPage = 'https://bluelimelearning.github.io/my-fav-quotes/'


uCleint = uReq(quotesPage)

pageHtml = uCleint.read()
uCleint.close()

pageSoup = soup(pageHtml, "html.parser")

quotes = pageSoup.findAll("div", {"class":"quotes"})



for quote in quotes:
    favQuotes = quote.findAll("p", {"class", "aquote"})
    aqoute = favQuotes[0].text.strip()

    favAuthors = quote.findAll("p", {"class", "author"})
    author = favAuthors[0].text.strip()



    print(aqoute)
    print(author)