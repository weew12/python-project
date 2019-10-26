# -*- coding: utf-8 -*-
import scrapy
from scrapydocSpider.items import ScrapydocspiderItem


class DocspiderSpider(scrapy.Spider):
    name = 'docspider'
    allowed_domains = ['https://scrapy-chs.readthedocs.io/zh_CN/latest']
    start_urls = ['https://scrapy-chs.readthedocs.io/zh_CN/latest/index.html#/']
    count = 0

    def parse(self, response):
        chapters = response.xpath('/html/body/div[1]/nav/div/div[2]/ul[1]/li/a/@href').extract()
        item = ScrapydocspiderItem()
        item['Btitle'] = response.xpath('//*[@id="scrapy-version"]/h1/text()').extract()
        item['content'] = response.xpath('//*[@id="scrapy-version"]').xpath('string(.)').extract()
        # item['all'] = str(response)
        yield item

        self.count += 1
        print('========', response.xpath('/html/body/div[1]/nav/div/div[2]/ul[1]/li/a/@href').extract())

        # next = response.xpath('/html/body/div[1]/nav/div/div[2]/ul[1]/li[1]/a/@href').extract()[0]
        # url2 = response.urljoin(next)
        # print('url', url2)

        url2 = response.urljoin(chapters[self.count])
        print('url=======', url2)
        yield scrapy.Request(url=url2, callback=self.parse)