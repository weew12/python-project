# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    p_content = scrapy.Field()  # 缩略内容
    datetime = scrapy.Field()   # 发布日期
