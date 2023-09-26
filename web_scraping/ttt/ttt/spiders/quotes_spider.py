from pathlib import Path

import scrapy
from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",]

    def parse(self, response):
        quotes = response.css("div.quote")
        
        for quote in quotes:
            item = QuoteItem()
            item["text"] = quote.css("span.text::text").get()
            item["author"] = quote.css("small.author::text").get()
            item["tags"] = quote.css("a.tag::text").getall()
            yield item