# -*- coding: utf-8 -*-
import scrapy


class AmazonReviewSpider(scrapy.Spider):
    name = 'amazon_review'
    allowed_domains = ['your-link-here']
    start_urls = ['http://your-link-here/']

    def parse(self, response):
        pass
