# -*- coding: utf-8 -*-

import requests
import bs4

url = "https://weather.cma.cn/web/weather/54511"

def get_web(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}
    res = requests.get(url, headers=header, timeout=5)
    # print(res.encoding)
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
            temp_list.append(item.text.strip())
        i += 1

    # 生成所需日期的字符串
    wen_str = temp_list[0]

    # print(temp_list)
    # 生成不同的字符串，通过切割把'\n'切掉
    wen_list = wen_str.split('\n')
    # print(wen_list)

    # 准备循环体所需列表
    i1 = 0
    list_wet_str = []

    # 去除'\n'
    for each in wen_list:
        if i1 != 1 and i1 != 6:
            list_wet_str.append(each)
        i1 += 1


    # 列表形式保存的数据
    # print(list_wet_str)

    # 储存天气数据
    date = list_wet_str[0]
    weather1 = list_wet_str[1]
    wind1 = list_wet_str[2]
    wind2 = list_wet_str[3]
    temp = list_wet_str[4]
    weather2 = list_wet_str[5]
    winda = list_wet_str[6]
    windb = list_wet_str[7]

    # 生成标准温度显示
    temp2 = temp.split('℃')
    temp3 = temp2[0]
    temp4 = temp2[1]
    temp5 = temp3 + '℃' + '-' +temp4 + '℃'

    # 生成天气状况
    if weather2 == weather1:
        weather3 = weather1
    else:
        weather3 = weather1 + '-' + weather2

    # 存放未来二十四小时湿度，准备
    list_hum = s.find_all('table', class_='hour-table')
    hum_list = []
    i = 0


    # 生成未来二十四小时的湿度
    for each in list_hum:
        if i == 1:
            hum_list.append(each.text.strip())
        i += 1

    # 生成湿度字符串
    hum_str = hum_list[0]

    # 通过空格去切割字符串
    hum_list_list = hum_str.split(" ")
    # print(hum_list_list)

    # 获取湿度信息
    hum_str2 =  hum_list_list[-2]
    # print(hum_str2)

    # 将湿度信息转化为列表
    hum_list3 = hum_str2.split('\n')

    # 储存湿度信息
    def wet_float(h):
        wet_float_value = float(hum_list3[h].replace('%', ''))
        return wet_float_value

    # 数据化字符串
    hui1 = wet_float(1)
    hui2 = wet_float(2)
    hui3 = wet_float(3)
    hui4 = wet_float(4)
    hui5 = wet_float(5)
    hui6 = wet_float(6)
    hui7 = wet_float(7)
    hui8 = wet_float(8)

    # print(hum_list3)

    # 生成最大值最小值
    hui_final = [hui1, hui2, hui3, hui4, hui5, hui6, hui7, hui8]
    hui_final_max = max(hui_final)
    hui_final_min = min(hui_final)
    hui_final_min_str = str(hui_final_min)
    hui_final_max_str = str(hui_final_max)
    hui_final_final = hui_final_max_str + '%' + '-' + hui_final_min_str + '%'

    # 注意模块生成
    # 穿衣模块
    temp_int = int(temp3)

    if temp_int >= 24:
        att1 = "适宜短袖👚"

    # 雨伞模块
    str1 = '晴'
    str2 = ''
    str3 = ""

    if weather1 == '晴' and weather2 == '晴':
        att2 = "带伞防晒"
    elif weather3.find('雨') != -1:
        att2 = "有雨请带伞"
    else:
        att2 = '不需要带伞'

    # 紫外线模块
    if weather1 == '晴' and weather2 == '晴':
        att3 = '紫外线强注意防晒'
    else:
        att3 = '适当防晒'

    # 湿度模块
    if hui3 < 30:
        att4 = '傍晚湿度很低💧'
    else:
        att4 = '今天湿度高💧'

    # 转化为字符串模块
    f1 = '日期' + ':' + date + '\n'
    f2 = '天气' + ':' + weather3 + '\n'
    f3 = '气温' + ":" + temp5 + '\n'
    f4 = '风向' + ':' + wind1 + wind2 + '\n'
    f5 = '湿度' + ':' + hui_final_final + '\n'
    f6 = '注意' + ':' + att1 + ';' + '\n'
    f7 = '\t' + '   ' + '  ' + att2 + ';' + '\n'
    f8 = '\t' + '   ' + '  ' + att3 + ';' + '\n'
    f9 = '\t' + '   ' + '  ' + att4 + ';' + '\n'

    # 输出
    with open('weather.txt', mode='w', encoding='utf-8') as file:
        file.write('—WeatherForecast—\n')
        file.write(f1)
        file.write(f2)
        file.write(f3)
        file.write(f4)
        file.write(f5)
        file.write(f6)
        file.write(f7)
        file.write(f8)
        file.write(f9)

# test
if __name__ == "__main__":
    url = "https://weather.cma.cn/web/weather/54511"
    parse_content(get_web(url))
    print("完成天气预报")



