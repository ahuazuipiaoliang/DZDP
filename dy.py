import urllib.request,re
import pymysql
import random
import sys,time



def get_data(url_1):
    """
    proxy_list = ['121.8.98.197:80',
                  '217.170.252.60:3128',
                  '168.63.139.99:3128',
                  '125.62.26.75:3128',
                  '124.193.51.249:3128',
                  '121.8.98.198:80',
                  '125.62.26.75:3128']
    """
    UA = [
        'Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36  ',
        'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19  ',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'
        ]
    # 这里填写全网代理IP提供的API订单号（请到用户中心获取）
    order = "bb8932ed9a66d49b5d16dfc1cf471a04"
    # 获取IP的API接口
    apiUrl = "http://dynamic.goubanjia.com/dynamic/get/" + order + ".html"
    # 要抓取的目标网站地址
    res = urllib.request.Request(apiUrl)
    response = urllib.request.urlopen(res)
    ips = response.read()

    # 按照\n分割获取到的IP
    if(ips):
        ips = re.findall(r"(?<=b').*(?=\\n)",str(ips))
        # 随机选择一个IP
        urlhandle = urllib.request.ProxyHandler({'http': ips[0]})
        opener = urllib.request.build_opener(urlhandle)
        urllib.request.install_opener(opener)
    user_agent = random.choice(UA)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '}
    request = urllib.request.Request(url=url_1,headers=headers)
    try:
        response = urllib.request.urlopen(request)
        data = response.read()
        data = data.decode('utf-8')
        print(ips[0])
        return data
    except:
        print("<< request error")
        return -1



def get_address(data):
    try:
        for address in set(re.findall(r'(?<=address" title=").*?(?=">)', str(data))):
            a = address
        return a
    except:
        return -1

def get_phone(data):
    try:
        for phone in set(re.findall(r'(?<="tel">).*(?=</span> </p> <div class="promosearch-wrapper")',str(data))):
            p = str(phone)
        return p
    except:
        return -1

def get_price(data):
    try:
        for price in set(re.findall(r'(?<=item">人均:)\d*?(?=元)',str(data))):
            pr = int(price)
        return pr
    except:
        return -1

def get_comments(data):
    try:
        for comment in set(re.findall(r'(?<=>)\d*(?=条评论)',str(data))):
            comment = int(comment)
        return comment
    except:
        return -1

def get_taste(data):
    try:
        for taste in set(re.findall(r'(?<=口味:)\d\.\d',str(data))):
            taste = float(taste)
        return taste
    except:
        return -1

def get_condition(data):
    try:
        for condition in set(re.findall(r'(?<=环境:)\d\.\d',str(data))):
            condition = float(condition)
        return condition
    except:
        return -1

def get_service(data):
    try:
        for service in set(re.findall(r'(?<=服务:)\d\.\d',str(data))):
            service = float(service)
        return service
    except:
        return -1

def get_category(data):
    try:
        for category in set(re.findall(r'(?<=<a href="//www.dianping.com/chengdu/ch\d\d/g\d\d\d" itemprop="url"> ).*?(?=\s)',str(data))):
            category = str(category)
        return category
    except:
        return -1

def get_name(data):
    try:
        for name in set(re.findall(r'(?<=shop-name"> ).*?(?=\s)',str(data))):
            name = name
        return name
    except:
        return -1

def upload_2_DZDP(url,district):
    data = get_data(url)
    name = get_name(data)
    address = get_address(data)
    phone = get_phone(data)
    comments = get_comments(data)
    price = get_price(data)
    taste = get_taste(data)
    condition = get_condition(data)
    service = get_service(data)
    category = get_category(data)
    conn = pymysql.connect(host="5997cf86e6880.gz.cdb.myqcloud.com",port=5682,user="root",passwd="j876730851",db="DZDP",charset="UTF8")
    conn.autocommit(False)
    cursor = conn.cursor()
    sql = "INSERT INTO `DZDP`.`restaurant` (`name`, `address`, `phone`, `comments`, `price`, `taste`, `condition`, `service`,`category`,`district`) VALUES ('"+str(name)+"', '"+str(address)+"', '"+str(phone)+"', '"+str(comments)+"', '"+str(price)+"', '"+str(taste)+"', '"+str(condition)+"', '"+str(service)+"', '"+str(category)+"', '"+str(district)+"')"
    try:
        tt = cursor.execute(sql)
        conn.commit()
    except UnicodeEncodeError as e :
        print(e)
        #conn.rollback()
    conn.close()

def get_shop_url(district_url):
    data = get_data(district_url)
    shop = set(re.findall(r'http:.*/shop/\d*',str(data)))
    return shop

def get_file(file_path):
    file = open(file_path)
    district = []
    district_url = []
    for i in file:
        i = i.split()
        district.append(i[0])
        district_url.append(i[1])
    return district,district_url

path = "/Users/jinbeng/python3_study/district.txt"

district, district_url = get_file(path)

for i in range(len(district)):
    for j in range(1,51):
        district_name = district[i]
        shops = get_shop_url(district_url[i]+"p"+str(j))
        for shop in shops:
            try:
                upload_2_DZDP(shop,district_name)
            except:
                print(shop,"failed")








