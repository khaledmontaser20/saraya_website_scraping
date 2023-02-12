import scrapy


class NewsspiderSpider(scrapy.Spider):
    name = "newsspider"
    allowed_domains = ["sarayanews.com/category/2"]
    start_urls = ["http://sarayanews.com/category/2/"]

    def parse(self, response):
        news = response.css('li.cleaner')
        for new in news:
            item = {
                'title': new.css('a::text').get(),
                'content': new.css('p::text').get(),
                'created_at': new.css('cite.date::text').get(),
                'link': new.css('a').attrib['href'],
                'img': new.css('img').attrib['src']
            }
            yield item
        pass
