# -*- coding: utf-8 -*-
# import scrapy


# class AmazonProductListSpider(scrapy.Spider):
#     name = 'amazon_product_list'
#     allowed_domains = ['your-link-here']
#     start_urls = ['http://your-link-here/']

#     def parse(self, response):
#         pass

    # Importing Scrapy Library
import scrapy
 
# Creating a new class to implement Spide
class AmazonProductListSpider(scrapy.Spider):
     
    # Spider name
    name = 'amazon_product_list'
     
    # Domain names to scrape
    allowed_domains = ['amazon.in']
    page_number=2
    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.in/s?k=ghee&page=2&qid=1592391783&ref=sr_pg_2"
    start_urls=[]
    start_urls.append(myBaseUrl)
    
    # Creating list of urls to be scraped by appending page number a the end of base url
    # for i in range(2,4):
    #     page_number=i
    #     myBaseUrl = "https://www.amazon.in/s?k=ghee&page="+str(page_number)+"&qid=1592391783&ref=sr_pg_"+str(page_number)
    #     start_urls.append(myBaseUrl)
    
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#MAIN-SEARCH_RESULTS')
             
            # Collecting product star ratings
            # star_rating = data.css('.review-rating')
            product_name=data.css('.a-size-mini')
            # Collecting user reviews
            # comments = data.css('.review-text')
            count = 0
             
            # Combining the results
            for review in product_name:
                yield{'product_name': '\t'.join(review.xpath('.//span[@class=a-size-mini]/text()').extract())
                     }
                count=count+1
