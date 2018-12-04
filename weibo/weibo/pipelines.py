# -*- coding: utf-8 -*-
import MySQLdb
from weibo.items import InformationItem, RelationItem



dbuser = 'root'
dbpass = '123456'
dbname = 'myweibo'
dbhost = 'localhost'
dbport = '3306'

class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, InformationItem):
            print ("开始写入用户信息")
            try:
                self.cursor.execute("""INSERT ignore INTO UserInfo(Id,UserName,UserDesc,Num_Follows,Num_Fans)
                                VALUES (%s, %s, %s, %s, %s)""",
                                    (
                                        item['Id'].encode('utf-8'),
                                        item['UserName'].encode('utf-8'),
                                        item['UserDesc'].encode('utf-8'),
                                        item['Num_Follows'].encode('utf-8'),
                                        item['Num_Fans'].encode('utf-8'),
                                    )
                                    )

                self.conn.commit()
            except MySQLdb.Error as e:
                print ("Error %d: %s" %(e.args[0], e.args[1]))
            return item
        elif isinstance(item, RelationItem):
            print ("开始写入关系信息")
            try:
                self.cursor.execute("""INSERT INTO RelationInfo(FollowedId, FollowingId )
                                VALUES (%s, %s)""",
                                    (
                                        item['FollowedId'].encode('utf-8'),
                                        item['FollowingId'].encode('utf-8'),
                                    )
                                    )

                self.conn.commit()
            except MySQLdb.Error as e:
                print ("Error %d: %s" %(e.args[0], e.args[1]))
            return item