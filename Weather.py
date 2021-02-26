# import urllib.request  # 需要安装 urllib 库
# from bs4 import BeautifulSoup  # 需要安装 bs4 库
#
#
# def get_weather(city_pinyin):
#     # 声明头，模拟真人操作，防止被反爬虫发现
#     header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64;\
#  rv:23.0) Gecko/20100101 Firefox/23.0'}
#     # 通过传入的城市名拼音参数来拼接出该城市的天气预报的网页地址
#     website = "http://www.tianqi.com/" + city_pinyin + ".html"
#     req = urllib.request.Request(url=website, headers=header)
#     page = urllib.request.urlopen(req)
#     html = page.read()
#     soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
#     # html.parser表示解析使用的解析器
#     nodes = soup.find_all('dd')
#     tody_weather = ""
#     for node in nodes:  # 遍历获取各项数据
#         temp = node.get_text()
#         if (temp.find('[切换城市]')):
#             temp = temp[:temp.find('[切换城市]')]
#         tody_weather += temp
#     # 去除字符串中的空行:
#     tianqi = "".join([s for s in tody_weather.splitlines(True)
#                       if s.strip()])
#
#     return tianqi  # 返回结果
#
#
# # 调用封装号好的函数获取天气预报，想查询哪个城市的天气情况，直接将参数替换为它的拼音即可
# print(get_weather('wulumuqi'))
import re
import requests
from bs4 import BeautifulSoup

# 获取URL


def get_page(url):
  try:
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
    r = requests.get(url,headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return '出现异常'  # 异常处理，防止出现错误


def parse_page(html, weather_list):
  soup = BeautifulSoup(html, 'html.parser')
  day_list = soup.find('ul', 't clearfix').find_all('li')
  for day in day_list:
    date = day.find('h1').get_text()
    wea = day.find('p', 'wea').get_text()
    if day.find('p', 'tem').find('span'):  # 判断标签'p','tem'下是否有标签'span'，以此判断是否有最高温
        tem_h = day.find('p', 'tem').find('span').get_text()
    else:
        tem_h = ''  # 最高温
    tem_l = day.find('p', 'tem').find('i').get_text()  # 最低温
    win1 = re.findall('(?<= title=").*?(?=")', str(day.find('p','win').find('em')))
    win2 = '-'.join(win1)  # 风向，win1-win2
    level = day.find('p', 'win').find('i').get_text()  # 风力
    weather_list.append([date, wea, tem_l, tem_h, win2, level])


def print_wea(weather_list):
  s = ' \t' * 3
  print(s.join(('日期', '天气', '最低温', '最高温', '风向', '风力')))
  for i in weather_list:
    print(i[0], '\t',i[1],'\t\t\t',i[2],'\t\t\t',i[3],'\t\t',i[4],'\t\t',i[5])  # 按格式输出


def get_weather():
  url = 'http://www.weather.com.cn/weather/101130106.shtml'
  html = get_page(url)
  wea_list = []
  parse_page(html, wea_list)
  print("\t\t\t\t\t\t\t\t\t乌鲁木齐新市区近7天天气预报")
  print_wea(wea_list)
  return wea_list


# if __name__ == '__main__':
#   get_weather()


