# encoding=utf-8

from scrapy.item import Item, Field


class InformationItem(Item):
    #关注对象的相关个人信息
    Id = Field()  # 用户ID
    UserName = Field()  # 用户名
    UserDesc= Field()  #描述
    Num_Fans = Field()  # 粉丝数
    Num_Follows = Field()  # 关注数




class RelationItem(Item):
    #关注关系
    FollowedId = Field()  # 被关注者
    FollowingId = Field()  # 关注者


