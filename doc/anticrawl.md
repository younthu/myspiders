# 反爬

## 反爬文章

1. http://doc.scrapy.org/en/master/topics/practices.html#avoiding-getting-banned
    动态设置user agent
    禁用cookies 
    设置延迟下载
    使用Google cache
    使用IP地址池（Tor project、VPN和代理IP）
    使用Crawlera
1. http://blkstone.github.io/2016/03/02/crawler-anti-anti-cheat/, 这里面有很多反爬设置
2. https://www.cnblogs.com/zhangxiaolei521/p/5632791.html , 反爬的一些思考
3. https://www.jb51.net/article/131736.htm
   1. X-Forwarded-For
   
     在请求头中添加X-Forwarded-For字段，将自己申明为一个透明的代理服务器，一些网站对代理服务器会手软一些。

     X-Forwarded-For头一般格式如下

     X-Forwarded-For:client1,proxy1,proxy2

     这里将client1，proxy1设置为随机IP地址，把自己的请求伪装成代理的随机IP产生的请求。然而由于X-Forwarded-For可以随意篡改，很多网站并不会信任这个值。
    
    1. 