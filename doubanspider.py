import requests
from lxml import etree


url='https://movie.douban.com/cinema/nowplaying/hangzhou/'

headers={

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}

response =requests.get(url,headers=headers)

#print(response.text)
#response.text返回的是处理过的str类型
#response.content 返回的是原生代码没有处理过的bytes类型
with open('douban.html','w',encoding='utf-8') as fp:
    fp.write(response.text)

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("douban.html",parser=parser)

ul = html.xpath("//ul[@class='lists']")[0]
lis =ul.xpath("./li")
movies=[]
for li in lis:
    title =li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    release =li.xpath("@data-release")[0]
    duration = li.xpath("@data-duration")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    category = li.xpath("@data-category")[0]
    posts = li.xpath(".//img/@src")
    movie = {
        '标题': title,
        '分数': score,
        '上映年份': release,
        '时长': duration,
        '导演': director,
        '演员': actors,
        '上映状态': category,
        '海报地址': posts
    }
    movies.append(movie)


print(movies)
    # print(title)
    # print(score)
    # print(release)
    # print(duration)
    # print(director)
    # print(actors)
    # print(category)
    # print(posts)

# movie={
#     '标题':title,
#     '分数':score,
#     '上映年份':release,
#     '时长':duration,
#     '导演':director,
#     '演员':actors,
#     '上映状态':category,
#     '海报地址':posts
# }
# print(movie)





