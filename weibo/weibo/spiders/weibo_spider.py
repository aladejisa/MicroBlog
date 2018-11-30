# coding=utf-8
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider
import json
from weibo.items import InformationItem,RelationItem

class Weibo(RedisSpider):
    name = "weibospider"
    redis_key="weibospider:start_urls"
    pre_url='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_'
    crawlId = ['1464484735']
    page=1
    index=0
    def parse(self,response):
        json_data = json.loads(response.body)
        data=json_data['data']
        cards=data['cards']
        if len(cards)!=0:
            card_group = cards[-1]['card_group']
            for userinfo in card_group:
                informationItems = InformationItem()
                relationItems = RelationItem()
                tmpId=str(userinfo['user']['id'])
                informationItems['Id']=tmpId
                informationItems['UserName'] = userinfo['user']['screen_name']
                informationItems['UserDesc'] = userinfo['desc1']
                informationItems['Num_Fans'] = str(userinfo['user']['followers_count'])
                informationItems['Num_Follows'] = str(userinfo['user']['follow_count'])
                relationItems['FollowedId']=tmpId
                relationItems['FollowingId'] = self.crawlId[self.index]
                if self.index==0:
                    self.crawlId.append(tmpId)
                yield informationItems
                yield relationItems
        self.page+=1
        if self.page<11:
            tail = "&page=%s" % str(self.page)
            nexturl = self.pre_url+self.crawlId[self.index]+ tail
            yield Request(url=nexturl, callback=self.parse)
        else:
            self.index+=1
            if self.index<len(self.crawlId):
                yield Request(url=self.pre_url + self.crawlId[self.index], callback=self.parse)
                self.page = 1
            else:
                pass













