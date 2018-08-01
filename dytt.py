import requests
from lxml import etree

BASE = "http://dytt8.net"
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}

def get_detail_urls(url):
    #url = "http://dytt8.net/html/gndy/dyzz/list_23_1.html"
    response = requests.get(url, headers=headers)

    text = response.text

    html = etree.HTML(text)

    hrefs = html.xpath("//table[@style='margin-top:6px']//a/@href")
    details = map(lambda url:BASE+url,hrefs)
    return details
    #==
    #def abc(url):
        #return BASE+url


def parse_detail_page(url):
    movive={}
    response = requests.get(url,headers)

    text = response.content.decode("gbk")
    html = etree.HTML(text)
    title = html.xpath("//font[@color='#07519a']/text()")[0]
    movive['title'] = title
    img = html.xpath("//p//img/@src")[0]
    infos =html.xpath("//p//text()")
    movive['post']= img
    # print(img)
    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    for index,info in enumerate(infos):
        # print(info)
        # print(index)
        # print("="*30)
        if info.startswith("◎年　　代"):
            info = parse_info(info,"◎年　　代")
            #strip()取消字符串中的空格
            movive['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info,"◎产　　地")
            movive['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info,"◎类　　别")
            movive['category'] = info
        elif info.startswith("◎语　　言"):
            info = parse_info(info,"◎语　　言")
            movive['len'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info,"◎豆瓣评分")
            movive['score'] = info
        elif info.startswith("◎上映日期"):
            info = parse_info(info,"◎上映日期")
            movive['movietime'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info,"◎导　　演")
            movive['director'] = info
        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            profiles = [info]
            for x in range(index+1,len(infos)):
                profile =infos[x].strip()
                profiles.append(profile)
                if profile.startswith("【下载地址】"):
                    profile = parse_info(profile, "【下载地址】")
                    break
                # print(profile)
                movive['profile'] = profiles
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演" )
            actors =[info]
            for x in range(index+1,len(infos)):
                actor =infos[x].strip()
                actors.append(actor)
                if actor.startswith("◎简　　介"):
                    actor = parse_info(actor, "◎简　　介")
                    break
                # print(actors)
                movive['actors'] = actors
    download_url =html.xpath("//td[@bgcolor='#fdfddf']/a/@href")
    movive['download_url']=download_url
    return movive


def spider():
    base_url = "http://dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1,8):
        #总共有7页
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            #遍历一页中所有电影的url
            movive = parse_detail_page(detail_url)
            movies=[]
            movies.append(movive)
            print(movies)





if __name__=="__main__":
    spider()





