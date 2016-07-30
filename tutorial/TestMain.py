from PIL import Image
import logging
import logging.config
if __name__=="__main__":

    CONF_LOG = "./log/log.conf"
    logging.config.fileConfig(CONF_LOG);
    logger = logging.getLogger("xzs")
    #im=Image.open("/home/mint/PycharmProjects/work/tutorial/2016-7-28/01.jpeg")
    im=Image.open("/home/mint/PycharmProjects/work/tutorial/2016-7-28/006eqDR2gw1f182c40wutj30a50ebaag.jpg")
    print("main")
    logger.info("wocaocao")
