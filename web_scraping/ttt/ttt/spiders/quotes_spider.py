from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",]

    def parse(self, response):
        a = response.xpath("//span[has-class('text')]/text()").getall()
        yield a

        #may have some problem of yield.