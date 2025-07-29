import scrapy
from retalhos.items import RetalhosItem
import random
from agents import user_agents


class BibliofiliaSpider(scrapy.Spider):
    name = "bibliofilia"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        print("Iniciando parse...")
        for book in books:
            relative_url = book.css('div.image_container a::attr(href)').get()
                
            if relative_url is not None:
                if 'catalogue/' in relative_url:
                    next_book_url = 'https://books.toscrape.com/' + relative_url
                else:
                    next_book_url = 'https://books.toscrape.com/catalogue/' + relative_url
                yield response.follow(next_book_url, callback = self.parse_book_page, headers={
                    'User-Agent': user_agents[random.randint(0, len(user_agents)-1)]
                })

        next_page = response.css('li.next a').attrib['href']

        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback = self.parse)

    
    def parse_book_page(self, response):
        item = RetalhosItem()
        
        item['Title'] = response.css('div.product_main h1::text').get()
        item['Price'] = response.css('div.product_main p.price_color::text').get()
        item['Availability'] = response.xpath('//table//tr[6]/td/text()').get()
        item['Description'] = response.xpath('//article[@class="product_page"]/p/text()').get()

        yield item
