# coding:utf-8
import datetime
import logging
import logging.config
import os
import socket
import urllib
from PIL import Image
import scrapy
from scrapy import Selector
from tutorial.spiders.constant.Constant import Constant
from tutorial.spiders.mysql.ScrapyURLDAO import ScrapyURLDAO
class CLSpider(scrapy.Spider):
    #全局设置三秒超时
    socket.setdefaulttimeout(10.0)
    CONF_LOG = "tutorial/spiders/log/log.conf"
    logging.config.fileConfig(CONF_LOG);
    logger = logging.getLogger("xzs")

    scrapyUrlDao = ScrapyURLDAO()
    name = "cl_scrapy"
    allowed_domains = ["www.cl652.com"]
    start_urls = [
        "http://www.cl652.com/thread0806.php?fid=7&search=&page=2"
    ]


    def parse(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//table[@id="ajaxtable"]//h3/a[@id=""]/@href')  # f12可以直接copy xpath
        counter = 0;
        for site in sites:
            try:
                link = site.extract()
                if "htm_data" not in link:
                    continue;
                ukey = link;
                ukey= ukey.replace(".html","")
                ukey= ukey.replace("htm_data/","")
                link = "http://www.cl652.com/"+link
                self.logger.info("begin crawing "+link)
                row = self.scrapyUrlDao.getScrapyURL(Constant.cl_url,ukey)
                if len(row)>0:
                    self.logger.info("this site is crawed  "+link)
                    continue
                self.scrapyUrlDao.addScrapyURL(Constant.cl_url,"1")
                yield scrapy.Request(link, self.parse_item) #下级页面自定义爬取规则函数parse_item,配置来调用
                '''
                counter = counter+1
                if counter>5:
                    break
                '''
            except Exception,e:
                self.logger.error(e)



    def parse_item(self, response):
        #print response.body
        hxs = Selector(response)
        imgs = hxs.xpath('//img/@src')  # f12可以直接copy xpath
        for img in imgs:
            try:
                imgLink = img.extract()
                fileName = imgLink.split("/")[-1]
                today = datetime.date.today()
                filePath = str(today.year)+"-"+str(today.month)+"-"+str(today.day)
                if not os.path.exists(filePath):
                    os.mkdir(filePath)
                filePath = str(today.year)+"-"+str(today.month)+"-"+str(today.day)+"/"+fileName
                self.down_and_del_img(imgLink,filePath)
            except Exception,e:
                self.logger.error(e)


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







# 进入生成的项目根目录tutorial/,执行 scrapy crawl cl_scrapy, cl_scrapy是spider的name
