import sys

import DBUtil


class ScrapyURLDAO:
    dbutil= DBUtil.DBUtil()
    mysqlConn=dbutil.getMysqlConn()

    def getScrapyURL(self,siteType,ukey):
        sql="SELECT * FROM for_scrapy.scrapy_url WHERE site_type= "+ siteType+ " and ukey='" +ukey+"'";
        row=self.dbutil.getData(self.mysqlConn, sql)
        return row


    def addScrapyURL(self,siteType,ukey):
        sql="insert into for_scrapy.scrapy_url(gmt_create,gmt_modified,site_type,ukey) values (now(),now(),"+siteType+",'"+ukey+"')";
        row=self.dbutil.insertData(self.mysqlConn, sql)
        return row



    def closeConn(self):
        self.dbutil.closeConn(self.mysqlConn)

        
if __name__ == "__main__":
    if len(sys.argv)>1:
        stat_date = sys.argv[1]
    else:
        p=ScrapyURLDAO()
        p.getScrapyURL("1","2")
        p.addScrapyURL("1","2")
        p.closeConn()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
