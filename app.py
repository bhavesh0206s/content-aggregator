import urllib, os, requests, datetime, subprocess

# reddit imports
import praw, pprint

# pip install feedparser
import feedparser

# stockexchange
from bsedata.bse import BSE

with open('content.txt', 'w'): pass

class News:
    def Indian_News(self):
        newsfeed = feedparser.parse(
            "http://feeds.feedburner.com/ndtvnews-india-news"
        )
        with open('content.txt', 'a+') as file:
          file.write("Today's News: \n")
          for i in range(5):
            entry = newsfeed.entries[i]
            file.write(f'{entry.title} \n')
            file.write("------News Link-------- \n")
            file.write(f'{entry.summary} \n')
            file.write(f'{entry.link} \n')
            file.write("########################################### \n")
          file.write("-------------------------------------------------------------------------------------------------------\n")


class Medium:
    # https://github.com/thepracticaldev/dev.to/issues/28#issuecomment-325544385
    def medium_programming(self):
        feed = feedparser.parse(
            "https://medium.com/feed/tag/programming"
        )
        with open('content.txt', 'a+') as file:
          file.write("Programming Today: \n")
          for i in range(5):
            entry = feed.entries[i]
            file.write(f'{entry.title} \n')
            file.write(f'URL: {entry.link} \n')
            file.write("########################################### \n")
          file.write('-------------------------------------------------------------------------------------------------------\n')
       
    def medium_python(self):
        feed_python = feedparser.parse(
            "https://medium.com/feed/tag/python"
        )
        with open('content.txt', 'a+') as file:
          file.write("Python Today: \n")
          for i in range(5):
            entry = feed_python.entries[i]
            file.write(f'{entry.title} \n')
            file.write(f'URL: {entry.link} \n')
            file.write("########################################### \n")
          file.write('-------------------------------------------------------------------------------------------------------\n')
      
    # def medium_developer(self):
    #     feed_developer = feedparser.parse(
    #         "https://medium.com/feed/tag/developer"
    #     )
    #     # for i in range(1,6):
    #     #   entry = feed_developer.entries[i]
    #     #   print(entry.title, entry.link)
    #     with open('content.txt', 'a+') as file:
    #       file.write("Developer News Today: \n")
    #       for i in range(5):
    #         entry = feed_developer.entries[i]
    #         file.write(f'{entry.title} \n')
    #         file.write(f'URL: {entry.link} \n')
    #         file.write("########################################### \n")
    #       file.write('-------------------------------------------------------------------------------------------------------\n')

class StockExchange:
    def bse_stock(self):
      bse = BSE()
      gainers = bse.topGainers()
      losers = bse.topLosers()
      with open('content.txt', 'a+') as file:
        file.write("TOP GAINERS: \n")
        for stock in gainers:
          file.write(f"Stock: {stock['securityID']}, Price: {stock['LTP']}, Change: {stock['change']}, %change: {stock['pChange']} % \n");
          file.write("########################################### \n")
        file.write('-------------------------------------------------------------------------------------------------------\n')

        file.write("TOP LOSERS: \n")
        for stock in losers:
          file.write(f"Stock: {stock['securityID']}, Price: {stock['LTP']}, Change: {stock['change']}, %change: {stock['pChange']} % \n");
          file.write("########################################### \n")
        file.write('-------------------------------------------------------------------------------------------------------\n')


# objects inititalization
# reddit_object = Reddit()
News_object = News()
Medium_object = Medium()
StockExchange_object = StockExchange()

News_object.Indian_News()
Medium_object.medium_python()
Medium_object.medium_programming()
# Medium_object.medium_developer()
StockExchange_object.bse_stock()