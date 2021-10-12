# -*- coding: utf-8 -*-
import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        glasses = response.xpath('//div[@id="product-lists"]/div[contains(@class, "product-list-item")]')
        for glass in glasses:
            yield {
                'product_url': glass.xpath('.//descendant::a[not(contains(@class, "none"))]/img[contains(@class, "product-img-default")]/@data-src').get()
            }