# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']

    def parse(self, response):
        products = response.xpath('//ul[@class="productlisting-ul"]/div/li')
        for product in products:
            yield {
                'title': product.xpath('.//a[@class="p_box_title"]/text()').get(),
                'url': response.urljoin(product.xpath('.//a[@class="p_box_title"]/@href').get()),
                'discounted_price': product.xpath('.//div[@class="p_box_price"]/span[@class="productSpecialPrice fl"]/text()').get(),
                'original_price': product.xpath('.//div[@class="p_box_price"]/span[@class="normalprice fl"]/text()').get()
            }
