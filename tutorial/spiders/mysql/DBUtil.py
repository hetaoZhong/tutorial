import MySQLdb
import logging
import logging.config

class DBUtil:
    '''
    No module named MySQLdb
    sudo apt-get install python2.7-mysqldb
    sudo apt-get install python-setuptools
    sudo apt-get install python-dev
    '''
    CONF_LOG = "tutorial/spiders/log/log.conf"
    logging.config.fileConfig(CONF_LOG);
    logger = logging.getLogger("xzs")

    MYSQL_IP= 'localhost'
    MYSQL_PORT=3006
    MYSQL_USER='root'
    MYSQL_PASSWD='root'
    MYSQL_SCHEMA='for_scrapy';
    

    def __init__(self):  
        self.logger.info('init DBUtil...');
        
    def getMysqlConn(self):
        return MySQLdb.Connect(host=self.MYSQL_IP, user=self.MYSQL_USER, passwd=self.MYSQL_PASSWD,
                               db=self.MYSQL_SCHEMA, port=self.MYSQL_PORT, charset='utf8')


    def getData(self,conn,sql):
        try:
            self.logger.info('getData start...')  
            self.logger.info(sql)
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchall()
            cur.close()
            self.logger.info('getData success end...')  
            return row
        except Exception,e:
            self.logger.info('getData faile: ')  
            self.logger.info(e)  
    
    def insertData(self,conn,sql):
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        
    def loadData(self,conn,command):
        try:
            self.logger.info('loadData start...')  
            self.logger.info(command)
            cur=conn.cursor()
            cur.execute(command)
            conn.commit()
            cur.close()
            self.logger.info('loadData success end...')  
        except Exception,e:
            self.logger.info('loadData faile: ')  
            self.logger.info(e)  
        
        
    def delData(self,conn,sql):
        try:
            self.logger.info('delData start...')  
            self.logger.info(sql)
            cur=conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
            self.logger.info('delData success end...')  
        except Exception,e:
            self.logger.info('delData faile: ')  
            self.logger.info(e)  
            
    def closeConn(self,conn):
            conn.close()
        
        
        
        
        
        
        
        
        
    
    
    