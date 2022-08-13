import requests
import bs4

url = "https://weather.cma.cn/web/weather/54511"

# 爬取网页内容
def get_web(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}
    res = requests.get(url, headers=header, timeout=5)
    content = res.text.encode('utf-8')
    return content

# 得到一个天气预报的list
def parse_content(content):
    # 将网页爬取内容转化为可视化内容
    s = bs4.BeautifulSoup(content, 'lxml')

    # 存放天气预报内容,准备好循环体
    list_temp = s.find_all('div', class_='pull-left day')

    # 生成原始预测列表
    temp_str = list_temp[0].text.strip()
    temp_list = temp_str.split('\n')

    # 删除list中空值
    temp_list = [i for i in temp_list if i != '']

    return  temp_list

def convert(list_1):
    # 转化为不包括湿度的所需列表
    temp_list = []
    temp_list.append('----Weather Forocast----\n')
    temp_list.append(f'日期：{list_1[0]}\n')

    # 判断天气情况的输出
    if list_1[1] != list_1[5]:
        temp_list.append(f'天气:{list_1[1]}-{list_1[5]}\n')
    else:
        temp_list.append(f'天气:{list_1[1]}\n')

    # 判断风力的输出
    if list_1[3] != list_1[7]:
        temp_list.append(f'风力:{list_1[3]}-{list_1[7]}\n')
    else:
        temp_list.append(f'风力:{list_1[3]}\n')

    return temp_list

# 获取湿度信息
def get_wet(content):
    s = bs4.BeautifulSoup(content, 'lxml')
    list_hum = s.find_all('table', class_='hour-table')

    # 生成列表，并去除空值
    hum = list_hum[0].text.strip()
    hum_list = hum[hum.find('湿'):hum.find('云')].split('\n')
    hum_list = [i for i in hum_list if i != '' or i != ' ']
    return hum_list
    ...



# 准备一个入口函数
def result(url):
    web_content = get_web(url)
    weather_content = parse_content(web_content)
    weather_convert = convert(weather_content)
    hum = get_wet(web_content)

    return weather_convert, hum


if __name__ == '__main__':
    print(result(url))
