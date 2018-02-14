# DZDP
爬取大众点评网的美食商户数据
代码使用python3编写
我尝试的是爬取成都重要商圈的信息，也可以自己修改想爬取的城市

# 创建数据库

键可参考以下设置
`name`, `address`, `phone`, `comments`, `price`, `taste`, `condition`, `service`,`category`,`district`


# district.txt
大众点评成都的主要商圈的url

`高新区 http://www.dianping.com/chengdu/ch10/r7949`
`春熙路 http://www.dianping.com/chengdu/ch10/r1577`
`宽窄巷子 http://www.dianping.com/chengdu/ch10/r7767`
`科华北路 http://www.dianping.com/chengdu/ch10/r1592`
`盐市口 http://www.dianping.com/chengdu/ch10/r5894`
`金沙 http://www.dianping.com/chengdu/ch10/r7768`
`光华 http://www.dianping.com/chengdu/ch10/r7769`
`锦达万里 http://www.dianping.com/chengdu/ch10/r1601`
`大慈寺 http://www.dianping.com/chengdu/ch10/r7764`
`建设路 http://www.dianping.com/chengdu/ch10/r1974`
`人民公园 http://www.dianping.com/chengdu/ch10/r1597`
`磨子桥 http://www.dianping.com/chengdu/ch10/r7771`
`玉林 http://www.dianping.com/chengdu/ch10/r1578`
`骡马市 http://www.dianping.com/chengdu/ch10/r1604`
`跳伞塔 http://www.dianping.com/chengdu/ch10/r70146`
`桐梓林 http://www.dianping.com/chengdu/ch10/r1596`

每一个商圈里面的商铺有50页，url是有规律的，拿高新区举例，高新区的商铺目录页面就是http://www.dianping.com/chengdu/ch10/r7949p1 - http://www.dianping.com/chengdu/ch10/r7949p50 这样就方便我们爬取数据，其中结尾的“p1”就是page1，以此类推



