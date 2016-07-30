
CREATE TABLE `scrapy_url` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `gmt_create` datetime DEFAULT NULL COMMENT '爬取过的站点',
  `gmt_modified` datetime DEFAULT NULL,
  `site_type` int(11) NOT NULL COMMENT 'url类型或者渠道',
  `ukey` varchar(32) NOT NULL COMMENT '唯一标示',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4