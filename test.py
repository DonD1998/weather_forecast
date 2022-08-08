import requests
import bs4
import os

url = "https://weather.cma.cn/web/weather/54511"

def get_web(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}
    res = requests.get(url, headers=header, timeout=5)
    content = res.text.encode('utf-8')
    return content

def parse_content(content):
    s = bs4.BeautifulSoup(content, 'lxml')

    # 存放天气预报内容,准备好循环体
    list_temp = s.find_all('div', class_='pull-left day')
    temp_list = []
    i = 0

    # 通过for循环存放需要日期的天气预报
    for item in list_temp:
        if i == 0:
            str_temp = item.text.strip()
            temp_list.append(item.text.strip())
        i += 1
    return  str_temp

def convert(str):
    repl
# 准备一个如果口函数
def result(url):
    web_content = get_web(url)
    weather_content = parse_content(web_content)
    return weather_content


if __name__ == '__main__':
    print(result(url))