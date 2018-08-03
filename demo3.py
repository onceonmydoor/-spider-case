from bs4 import BeautifulSoup
from pyecharts import Bar,Line,Overlap

html_doc = """<html>
    <head>
        <title>

        </title>
        <style type="text/css">
        .box > p {
            background-color: pink;
        }
        </style>
    </head>

    <body>
        <div class="box">
            <div>
                <p>第零行</p>
            </div>
            <p class="line1">第一行数据</p>
            <p class="line1">第二行数据</p>
            <p id='line3'>第仨行数据</p>
            <p>第四行数据</p>
        
        </div>
        <p>第五行数据</p>
        <form>
            <input type="text" name="username">
            <input type="text" name="password">
        </form>
    </body>
</html>
		 """


soup =BeautifulSoup(html_doc,'lxml')

# tes = soup.select('tr')#TAG数据类型
# #获取所有的tr标签
# for tr in tes:
#     print(tr)
#     print('='*10)

#2.获取第二个tr标签
# tr =soup.select('tr')[1]
# print(tr)
#3.获取所有的class等于even的tr标签
#trs = soup.select('tr.even')
# trs = soup.select("tr[class='even']")
# for tr in trs:
#     print(trs)



# aList = soup.select('a')
# for a in aList:
#     href =a['href']
#     print(href)



# trs =soup.select('tr')
# for tr in trs:
#     infos =list(tr.stripped_strings)
#     print(infos)
div = soup.find('div')
print(div.contents)


attr=['A','B','C','D','E','F']
v1 = [12,34,124,51,12,32,45,66]
v2 = [11,4,5,6,8,9,1,2]
bar =Bar('linr-BAr实例')
bar.add('bar',attr,v1)
line =Line()
line.add('line',attr,v2)

overlap =Overlap()
overlap.add(bar)
overlap.add(line)

overlap
