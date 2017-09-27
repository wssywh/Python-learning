# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?lid=&tid=&keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&start=0#a']

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item = TencentItem()
            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()
            item['position_link'] = node.xpath("./td[1]/a/@href").extract_first()
            item['position_type'] = node.xpath("./td[2]/text()").extract_first()
            item['position_number'] = node.xpath("./td[3]/text()").extract_first()
            item['position_adress'] = node.xpath("./td[4]/text()").extract_first()
            item['position_publishtime'] = node.xpath("./td[5]/text()").extract_first()
            yield item
        if len(response.xpath("//a[@id='next' and @class='noactive']"))==0:
            url = response.xpath("//a[@id='next']/@href").extract_first()
            yield scrapy.Request("http://hr.tencent.com/" + url,callback=self.parse)

