这是一个基于mysql，scrapy和redis的分布式爬虫，目的是爬取微博某个用户的三层关注网络。
使用scrapy_redis模块实现爬虫与redis交互，使得redis中保存一个request队列，同时另一个队列保存爬取到的 item。
另需启动redistomysql程序阻塞等待，不断从redis的item队列中读取信息保存到mysql中去。
数据表有两个，一个记录关系数据，一个记录用户信息。
爬取页面是微博提供的json页面含关注信息，每次只能读取前十页
