# coding:utf-8
import urllib
from scrapy.selector import Selector
from scrapy import Selector
import scrapy
import socket
from PIL import Image
import os
import datetime
import string
import logging
import logging.config
class XXSpider(scrapy.Spider):
    #全局设置三秒超时
    socket.setdefaulttimeout(10.0)
    CONF_LOG = "tutorial/log/log.conf"
    logging.config.fileConfig(CONF_LOG);
    logger = logging.getLogger("xzs")

    name = "xx_scrapy"
    allowed_domains = ["www.cl652.com"]
    start_urls = [
        "http://www.cl652.com/thread0806.php?fid=7&search=&page=2"
    ]



    def parse(self, response):
        self.logger.info(response.url)
        '''
        filename = 'save_file'  # response.url.split("/")[1]
        open(filename, 'wb').write(response.body)
        '''
        hxs = Selector(response)
        sites = hxs.xpath('//table[@id="ajaxtable"]//h3/a[@id=""]/@href')  # f12可以直接copy xpath
        counter = 0
        for site in sites:
            counter = counter+1
            link = site.extract()
            link = "http://www.cl652.com/"+link
            self.logger.info(response.url)
            yield scrapy.Request(link, self.parse_item) #下级页面自定义爬取规则函数parse_item,配置来调用
            if counter>0:
                break

    def parse_item(self, response):
        #print response.body
        hxs = Selector(response)
        imgs = hxs.xpath('//img/@src')  # f12可以直接copy xpath
        for img in imgs:
            imgLink = img.extract()
            fileName = imgLink.split("/")[-1]
            today = datetime.date.today()
            filePath = str(today.year)+"-"+str(today.month)+"-"+str(today.day)
            if not os.path.exists(filePath):
                os.mkdir(filePath)
            filePath = str(today.year)+"-"+str(today.month)+"-"+str(today.day)+"/"+fileName
            self.down_and_del_img(imgLink,filePath)



    def down_and_del_img(self,imgLink,fileName):
        try:
            urllib.urlretrieve(imgLink,fileName)
        except urllib.ContentTooShortError:
            self.logger.info("Network conditions is not good.Reloading")
            return
        self.logger.info(fileName+" is download over")
        try:
            img = Image.open(fileName)
            imgSize = img.size #图片的长和宽
            print imgSize
            maxSize = max(imgSize) #图片的长边
            print maxSize
            minSize = min(imgSize) #图片的短边
            print minSize
            '''
            if minSize<500:
                os.remove(fileName)
                print fileName+" is deleted"
            '''
        except:
            self.logger.info(fileName+" is not a pic"+",imgLink is  "+imgLink)
            os.remove(fileName)







# 进入生成的项目根目录tutorial/,执行 scrapy crawl dmoz, dmoz是spider的name
