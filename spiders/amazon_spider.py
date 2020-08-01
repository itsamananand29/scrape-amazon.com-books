import scrapy
from ..items import ScrapeamanzonItem
#from scrapy.http import FormRequest

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=1&fst=as%3Aoff&qid=1596279271&rnid=1250225011&ref=sr_pg_1']
    page_number=2
    def parse(self, response):
        items = ScrapeamanzonItem()  
        all_div = response.css('.s-latency-cf-section')
        for d in all_div:
            product_name=d.css('.a-color-base.a-text-normal::text').extract()
            product_author=d.css('.sg-col-12-of-28 .a-size-base+ .a-size-base').css('::text').extract()
            product_price=d.css('.a-spacing-top-small .a-price-whole::text').extract()
            product_imagelink=d.css('.s-image::attr(src)').extract()
            items['product_name']=product_name
            items['product_author']=product_author
            items['product_price']=product_price
            items['product_imagelink']=product_imagelink
            yield items
        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page='+str(AmazonSpiderSpider.page_number)+'&fst=as%3Aoff&qid=1596288050&rnid=1250225011&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number <=75:
            AmazonSpiderSpider.page_number+=1
            yield response.follow(next_page,callback=self.parse)

