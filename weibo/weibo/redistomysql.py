# -*- coding: utf-8 -*-
import redis
import MySQLdb
from weibo.items import InformationItem, RelationItem
import json

def process_item():
    dbuser = 'root'
    dbpass = '123456'
    dbname = 'myweibo'
    dbhost = 'localhost'
    dbport = '3306'
    mysqlcli = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",use_unicode=True)
    rediscli=redis.Redis(host="127.0.0.1",port=6379,db=0)
    while(True):
        # 将数据从redis里pop出来
        source, data = rediscli.blpop("weibospider:items")
        item = json.loads(data)
        if len(item)==5:
            print("开始写入关注者信息")
            try:
                cursor = mysqlcli.cursor()
                cursor.execute("""INSERT ignore INTO UserInfo(Id,UserName,UserDesc,Num_Follows,Num_Fans)
                                        VALUES (%s, %s, %s, %s, %s)""",
                                    (
                                        item['Id'].encode('utf-8'),
                                        item['UserName'].encode('utf-8'),
                                        item['UserDesc'].encode('utf-8'),
                                        item['Num_Follows'].encode('utf-8'),
                                        item['Num_Fans'].encode('utf-8'),
                                    )
                                    )
                mysqlcli.commit()
                cursor.close
            except MySQLdb.Error as e:
                print("Error %d: %s" % (e.args[0], e.args[1]))
        elif len(item)==2:
            cursor = mysqlcli.cursor()
            print("开始写入关系信息")
            try:
                cursor.execute("""INSERT INTO RelationInfo(FollowedId, FollowingId )
                                        VALUES (%s, %s)""",
                                    (
                                        item['FollowedId'].encode('utf-8'),
                                        item['FollowingId'].encode('utf-8'),
                                    )
                                    )

                mysqlcli.commit()
                cursor.close
            except MySQLdb.Error as e:
                print("Error %d: %s" % (e.args[0], e.args[1]))
        else:
            pass

if __name__ == '__main__':
    process_item()

