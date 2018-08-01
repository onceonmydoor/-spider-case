import requests
from lxml import etree

BASE = "https://hr.tencent.com/"
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}

def get_detail_urls(url):
    response =requests.get(url ,headers=headers)

    text =response.content.decode('utf-8')

    html=etree.HTML(text)

    href = html.xpath("//td[@class='l square']/a/@href")
    # print(href)
    details = map(lambda url:BASE+url,href)
    return details



def parse_datail_page(url):
    infor={}
    response =requests.get(url,headers=headers)

    text =response.content.decode("utf-8")
    # print(text)
    html =etree.HTML(text)

    title =html.xpath("//tr[@class='h']/td/text()")
    # print(title)
    infor['title']=title
    workplace = html.xpath("//tr[@class='c bottomline']/td[1]//text()")[1]
    # print(workplace)
    infor['workplace'] = workplace
    category = html.xpath("//tr[@class='c bottomline']/td[2]//text()")[1]
    infor['category'] = category
    number = html.xpath("//tr[@class='c bottomline']/td[3]//text()")[1]
    infor['number'] = number
    # infos =html.xpath("//tr[@class='c']//text()")
    # for index,info in enumerate(infos):
    #     resbs=[info]
    #     claims=[info]
    #     if info.startswith("工作职责："):
    #         for x in range(index+1,len(infos)):
    #             resb = infos[x].strip()
    #             resbs.append(resb)
    #             if resb.startswith("工作要求："):
    #                 resb.replace("工作要求：", "").strip()
    #                 break
    #             infor['resb'] = resbs
    #             # print(resb)
    #     elif info.startswith("工作要求："):
    #         for x in range(index+1,len(infos)):
    #             claim = infos[x].strip()
    #             claims.append(claim)
    #             if claim.endswith("申请岗位"):
    #                 claim.replace("申请岗位","").strip()
    #                 break
    #             # print(claim)
    #             infor['claim'] = claims
    more_infos = html.xpath("//ul[@class='squareli']")
    resb = more_infos[0].xpath(".//text()")
    claim = more_infos[1].xpath(".//text()")
    infor['claim'] = claim
    infor['resb'] = resb
    return infor



def spider():
    base_url ="https://hr.tencent.com/position.php?&start={}#a"
    for x in range(0,3600,10):
        url = base_url.format(x)
        # print(url)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
              infor = parse_datail_page(detail_url)
              infors =[]
              infors.append(infor)
              print(infors)


if __name__=="__main__":
    spider()

