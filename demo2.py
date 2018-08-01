from lxml import etree



# 1.获取所有tr标签
# 2.获取第二个tr标签
# 3.获取所有class等于even的标签
# 4.获取所用a标签的href属性
# 5.获取所有的职位信息（纯文本）





parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html",parser=parser)

# 1.获取所用tr标签
# //tr
# xpath函数返回的是一个列表
#
# trs = html.xpath("//tr")
# for tr in trs:
#     print(etree.tostring(tr,encoding="utf-8").decode("utf-8"))

# 2.获取第二个tr标签
# tr =html.xpath("//tr[2]")[0]
# print(etree.tostring(tr,encoding="utf-8").decode("utf-8"))

# 3.获取所有class等于even的标签
#
# trs =html.xpath("//tr[@class='even']")
# for tr in trs:
#  print(etree.tostring(tr,encoding="utf-8").decode("utf-8"))


# 4.获取所用a标签的href属性的值

# aList = html.xpath("//a/@href")
# for i in range(0,len(aList)):
#
#  print("https://hr.tencent.com/"+aList[i])

 # 5.获取所有的职位信息（纯文本）
trs = html.xpath("//tr[position()>1]")
for tr in trs:
    href = tr.xpath(".//a/@href")[0]
    #(子孙元素)当前目录下的所有a标签 .
    fullurl = "https://hr.tencent.com/"+ href
    # title = tr.xpath("./td[1]//text()")[0]
    title = tr.xpath(".//a/text()")[0]
    catagory =tr.xpath("./td[2]//text()")[0]
    number =tr.xpath("./td[3]//text()")[0]
    place =tr.xpath("./td[4]//text()")[0]
    time = tr.xpath("./td[5]//text()")[0]
    # print("url:  "+fullurl)
    # print("title:  "+title)
    # print("catagory:  "+catagory)
    # print("number:  " + number)
    # print("place:  "+place)
    # print("time:  " + time)
    position={
        'url':fullurl,
        'title':title,
        'catagory':catagory,
        'number':number,
        'place':place,
        'time':time
    }
    print(position)
