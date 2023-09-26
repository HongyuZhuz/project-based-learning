import scrapy



class StackSpider(scrapy.Spider):
    name = "stack"
    #start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest",]
    start_urls = ["https://realpython.com/web-scraping-with-scrapy-and-mongodb/",]

    def parse(self, response):
        questions = response.css("h1::text").get()
        #questions = response.xpath("//div[@class ='s-post-summary--content']").getall()
        yield questions

 #       for question in questions:
 #           item = StackItem()
 #           item['title'] = question.xpath('//*[@class="s-link"]/text()').getall()
 #           yield item


    