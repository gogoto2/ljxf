import scrapy
from ..items import LjxfItem


class ljxfSpider(scrapy.Spider):
    name = "ljxf"
    start_urls = ['https://xa.fang.lianjia.com/loupan/nht1pg66/']

    def start_requests(self):
        return [scrapy.Request("https://xa.fang.lianjia.com/loupan/nht1pg{0}/".format(x)) for x in range(66, 98)]

    def parse(self, response):
        ljxf = LjxfItem()
        title_list =  response.xpath(".//a[@class='name']/text()").extract()  # 标题
        district_list = response.xpath(".//div[@class='resblock-location']/span[1]/text()").extract() # 区
        region_list = response.xpath(".//div[@class='resblock-location']/span[2]/text()").extract() # 区域
        address_list = response.xpath(".//div[@class='resblock-location']/a/text()").extract()  # 地址
        status_list = response.xpath(".//span[@class='sale-status']/text()").extract()  # 状态
        money_list =  response.xpath(".//div[@class='main-price']/span[1]/text()").extract() # 每平方单价
        for i1, i2, i3, i4,i5,i6 in zip(title_list,district_list, region_list,address_list, status_list, money_list):
            ljxf['title'] = i1
            ljxf['district'] = i2
            ljxf['region'] = i3
            ljxf['address'] = i4
            ljxf['status'] = i5
            ljxf['money'] = i6
            yield ljxf