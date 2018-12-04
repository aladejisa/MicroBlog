# coding=utf-8


BOT_NAME = 'weibo'

SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    "weibo.middleware.ABProxyMiddleware": None,
    "weibo.middleware.UserAgentMiddleware": 401,
    "weibo.middleware.CookiesMiddleware": 402,
}

""" 阿布云启用限速设置 
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0.2  # 初始下载延迟
DOWNLOAD_DELAY = 0.2  # 每次请求间隔时间
"""
ITEM_PIPELINES = {
    'weibo.pipelines.MySQLStorePipeline': 300,
}



