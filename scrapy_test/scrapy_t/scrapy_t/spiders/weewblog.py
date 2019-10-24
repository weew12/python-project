# -*- coding: utf-8 -*-
import scrapy
from scrapy_t.items import ScrapyTItem


class WeewblogSpider(scrapy.Spider):
    name = 'weewblog'
    allowed_domains = ['new.weew12.top']
    start_urls = ['http://new.weew12.top/']

    def parse(self, response):
        infos = response.css('.post-entry')
        for info in infos:
            item = ScrapyTItem()
            item['title'] = info.css('.entry-title a::text').extract()[0]
            item['p_content'] = info.css('p::text').extract()[0]
            item['datetime'] = info.xpath('//*[@id="main"]/article[1]/div/div[2]/text()').extract()[1].strip()
            yield item

        next = response.css('#pagination > a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
