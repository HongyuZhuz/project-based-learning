import scrapy
from ..items import StackItem

class StackSpider(scrapy.Spider):
    name = "stack"
    start_urls = ["https://stackoverflow.com/questions?sort=newest",]

    def parse(self, response):
        
        questions = response.xpath("//a[@class = 's-link']")
        
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath("./text()").get()
            absolute_url = response.urljoin(question.xpath("./@href").get())
            item['url'] = absolute_url
            yield item


    