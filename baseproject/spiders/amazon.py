import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    def start_requests(self):
        base_url = "https://www.amazon.com.br/s?k=SSD+1TB&page={page}&qid=1697392045&ref=sr_pg_2"

        # Defina o número máximo de páginas a serem raspadas
        max_pages = 30

        for page in range(1, max_pages + 1):
            url = base_url.format(page=page)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        products = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-spacing-base", " " ))]')
        

        for product in products:
            price = product.xpath('.//span[contains(@class, "a-price-whole")]/text()').get()
            name = product.xpath('.//span[contains(@class, "a-color-base") and contains(@class, "a-text-normal")]/text()').get()
            yield{
                'nome':name,
                'preço':price
            }

        
