from bs4 import BeautifulSoup
import requests
from pyecharts import Bar,Line,Overlap,Grid
ALL_DATA = []

def parse_page(url):
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

    }
    infos={}
    response = requests.get(url,headers=headers)
    content = response.content.decode('utf-8')
    soup =BeautifulSoup(content,'html5lib')
    #html5lib容错率更高
    conMidtab = soup.find_all('div',class_='conMidtab')[1]
    tables = conMidtab.find_all('table')
    for table in tables:
        # print(ts)
        # print("="*30)
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            #a = tr.find_all('a',target="_blank")
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            #print(city)
            temp_td = tds[-5]
            max_temp = list(temp_td.stripped_strings)[0]
            #print(max_temp)
            infos['city']=city
            infos['max_temp'] = max_temp
            #print(infos)
            ALL_DATA.append({"city":city,"max_temp":int(max_temp)})
            # ALL_DATA.sort(key=lambda data: data['max_temp'])
            # print(ALL_DATA)


if __name__=="__main__":
     url1 = "http://www.weather.com.cn/textFC/hb.shtml"
     url2 = "http://www.weather.com.cn/textFC/db.shtml"
     url3 = "http://www.weather.com.cn/textFC/hd.shtml"
     url4 = "http://www.weather.com.cn/textFC/hz.shtml"
     url5 = "http://www.weather.com.cn/textFC/hn.shtml"
     url6 = "http://www.weather.com.cn/textFC/xb.shtml"
     url7 = "http://www.weather.com.cn/textFC/xn.shtml"
     url8 = "http://www.weather.com.cn/textFC/gat.shtml"
     urls = {

         # 'http://www.weather.com.cn/textFC/hb.shtml',
         # "http://www.weather.com.cn/textFC/db.shtml",
         # "http://www.weather.com.cn/textFC/hd.shtml",
         # "http://www.weather.com.cn/textFC/hz.shtml",
         # "http://www.weather.com.cn/textFC/hn.shtml",
         # "http://www.weather.com.cn/textFC/xb.shtml",
         # "http://www.weather.com.cn/textFC/xn.shtml",
         # "http://www.weather.com.cn/textFC/gat.shtml"
         url1,url2,url3,url4,url5,url6,url7,url8
     }

     for url in urls:
        parse_page(url)




     ALL_DATA.sort(key=lambda data:data['max_temp'])
     data =ALL_DATA[-10:]

     cities = list(map(lambda x:x['city'],data))
     temps = list(map(lambda x:x['max_temp'],data))
     chart = Bar("中国天气最高气温排行榜")
     chart.add('bar',cities,temps,is_stack=True)
     chart.render('chinatemp.html')
     line = Line()
     temp = [i + 10 for i in temps]
     line.add("line", cities, temp,is_stack=True)
     line.render('chinatemp.html')
     overlap =Overlap()
     overlap.add(chart)
     overlap.add(line)

     # grid =Grid()
     # grid.add(chart,line)
     # grid.render('chinatemp.html')

     print(ALL_DATA)
