# encoding=utf-8
import random
import base64
from weibo.cookies import weibocookie
from weibo.user_agents import agents


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ 换Cookie """

    def process_request(self, request, spider):
        request.cookies = weibocookie


class ABProxyMiddleware(object):
    """ 阿布云ip代理配置 """
    proxyServer = "http://http-dyn.abuyun.com:9020"
    proxyUser = "H3781HPYG14FG2ED"
    proxyPass = "C496A6E0F92AE818"
    proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")
    def process_request(self, request, spider):
        request.meta["proxy"] = self.proxyServer
        request.headers["Proxy-Authorization"] = self.proxyAuth


