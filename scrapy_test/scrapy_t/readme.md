# Scrapy 练手 1.1

## project:

     scrapy_t

## 爬取站点:

     个人站点：weew12.top

## 爬取内容:

    title # 标题
    p_content # 缩略内容
    datetime # 发布日期

## spider:

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
