# -*- coding: utf-8 -*-
import scrapy
from getlinkspider.items import GetlinkspiderItem


class GlinkspiderSpider(scrapy.Spider):
    name = 'glinkspider'
    allowed_domains = ['scrapy-chs.readthedocs.io/zh_CN/latest/index.html']
    start_urls = ['https://scrapy-chs.readthedocs.io/zh_CN/latest/index.html']
    urls = []
    count = 0

    def parse(self, response):
        titles = response.xpath('/html//a[contains(@class, "reference internal")]//text()').extract()
        self.start_urls = response.xpath('/html//a[contains(@class, "reference internal")]//@href').extract()

        item = GetlinkspiderItem()
        item['title'] = titles[self.count]
        item['url'] = response.urljoin(self.start_urls[self.count])
        item['content'] = response.xpath('//div[contains(@itemprop, "articleBody")]').xpath('string(.)').extract()
        next = response.urljoin(self.start_urls[self.count+1])
        self.count += 1
        yield item

        yield scrapy.Request(url=next, callback=self.parse, dont_filter=True)



