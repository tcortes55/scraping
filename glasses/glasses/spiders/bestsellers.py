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
                'product_url': glass.xpath('.//descendant::a[contains(@class, "product-title") and not(contains(@class, "none"))]/@href').get(),
                'product_image_link': glass.xpath('.//descendant::a[not(contains(@class, "none"))]/img[contains(@class, "product-img-default")]/@data-src').get(),
                'product_name': glass.xpath('.//descendant::a[contains(@class, "product-title") and not(contains(@class, "none"))]/@title').get(),
                'product_price': glass.xpath('.//descendant::div[contains(@class, "p-price") and not(contains(@class, "none"))]/div[not(contains(@class, "none"))]/span/text()').get()
            }

        next_page = response.xpath('.//a[@rel="next"]/@href').get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)