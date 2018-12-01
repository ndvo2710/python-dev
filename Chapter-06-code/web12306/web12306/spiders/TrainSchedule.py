# -*- coding: utf-8 -*-
import scrapy


class TrainscheduleSpider(scrapy.Spider):
    name = 'TrainSchedule'
    start_urls = ['http://www.12306.com/#/train/search/SZQ/SJP/2018-12-01/']

    def parse(self, response):
        print(response.css('p.ng-binding::text').extract())
