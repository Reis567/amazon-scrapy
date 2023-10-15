import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = ["https://www.amazon.com.br/s?k=SSD+1TB"]

    def parse(self, response):
        products = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-spacing-base", " " ))]')
        

        for product in products:
            price = product.xpath('.//span[contains(@class, "a-price-whole")]/text()').get()
            name = product.xpath('.//span[contains(@class, "a-color-base") and contains(@class, "a-text-normal")]/text()').get()
            yield{
                'nome':name,
                'preço':price
            }

        
