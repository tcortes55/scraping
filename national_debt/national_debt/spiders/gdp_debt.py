# -*- coding: utf-8 -*-
import scrapy
import logging

class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath('//table[@class="jsx-2139574911 table table-striped tp-table-body"]/tbody/tr')
        for row in rows:
            country_name = row.xpath('.//td[1]/a/text()').get()
            gdp_debt = row.xpath('.//td[2]/text()').get()
            
            yield {
                'country_name': country_name,
                'gdp_debt': gdp_debt
            }
        
