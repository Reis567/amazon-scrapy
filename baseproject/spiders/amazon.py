import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = ["https://www.amazon.com.br/s?k=SSD+1TB"]

    def parse(self, response):
        product = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-spacing-base", " " ))]')
        price = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-price-whole", " " ))]')
        name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-color-base", " " )) and contains(concat( " ", @class, " " ), concat( " ", "a-text-normal", " " ))]')

        
