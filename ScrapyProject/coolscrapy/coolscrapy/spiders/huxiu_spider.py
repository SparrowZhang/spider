#coding:utf-8
import scrapy
from coolscrapy.items import CoolscrapyItem

class HuXiuSpider(scrapy.Spider):
    name = 'huxiu'
    allowed_domains = ['huxiu.com']
    start_urls = ["http://www.huxiu.com/index.php"]

    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = CoolscrapyItem()
            item['title'] = sel.xpath('h3/a/text()')[0].extract()
            item['link'] = sel.xpath('h3/a/@href')[0].extract()
            url = response.urljoin(item['link'])
            item['desc'] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract()
            # print(item['title'], item['link'], item['desc'])
            yield scrapy.Request(url,callback=self.parse_article)

    def parse_article(self, response):
        detail = response.xpath('//div[@class="article-wrap"]')
        item = CoolscrapyItem()
        item['title'] = detail.xpath('h1/text()')[0].extract()
        item['link'] = response.url
        item['posttime'] = detail.xpath(
            'div[@class="article-author"]/span[@class="article-time"]/text()')[0].extract()
        print(item['title'], item['link'], item['posttime'])
        yield item