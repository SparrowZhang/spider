=====爬虫原理=====
通过python访问新闻首页，获取首页所有新闻链接，并存放到URL集合中
逐一取出集合中到URL，并访问链接获取源码，解析出新到URL链接添加到集合中
为防止重复访问，设置一个历史访问，用于对新天际对URL进行过滤
解析dom树，获取文章相关信息，并将信息存储到article对象中
将article对象中到数据通过pymysql保存到数据库中
完成一次数据存储，计算器增加并打印文章标题，否则打印错误信息

