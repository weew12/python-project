# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydocspiderItem(scrapy.Item):
    Btitle = scrapy.Field()  # 章节标题
    content = scrapy.Field()  # 章节内容