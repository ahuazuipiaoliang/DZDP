import re
import pymysql
import requests


def get_data(url_1):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Cookie':'_lxsdk_cuid=15eea339434c8-0d2cff6b34e61c-c313760-100200-15eea339434c8; _lxsdk=15eea339434c8-0d2cff6b34e61c-c313760-100200-15eea339434c8; _hc.v=cec4c6d7-039d-1717-70c0-4234813c6e90.1507167802;\
            s_ViewType=1; __mta=218584358.1507168277959.1507176075960.1507176126471.5; JSESSIONID=48C46DCEFE3A390F647F52FED889020D; aburl=1; cy=2; cye=beijing; _lxsdk_s=15eea9307ab-17c-f87-123%7C%7C48',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host':'www.dianping.com'}
    data = requests.get(url_1,headers=headers).content
    data = data.decode('utf-8')
    return data




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
    conn = pymysql.connect(host="",port=,user="",passwd="",db="",charset="UTF8")
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
