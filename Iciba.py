import json
import requests


# 爬取爱词霸每日鸡汤
def get_iciba_everyday_chicken_soup():
    url = 'http://open.iciba.com/dsapi/'  # 词霸免费开放的jsonAPI接口
    r = requests.get(url)
    all = json.loads(r.text)  # 获取到json格式的内容，内容很多
    # print(all) json内容，通过这行代码来确定每日一句的键名
    # Englis = all['content']  # 提取json中的英文鸡汤
    Chinese = all['note']  # 提取json中的中文鸡汤
    # everyday_soup = Englis + '\n' + Chinese   合并需要的字符串内容
    everyday_soup = Chinese
    return everyday_soup  # 返回结果


print(get_iciba_everyday_chicken_soup())
