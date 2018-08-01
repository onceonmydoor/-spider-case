from bs4 import BeautifulSoup


html_doc = """<div class="clr"></div>
		    	</div>
		    	<div id="searchrow3">
		    		<div class="srow2l left"></div>
		    		<div class="left items pl9">
		    			<a href="position.php?keywords=&lid=0" class="item active"><span><font>全部</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&lid=0&tid=87"><span><font>技术类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&lid=0&tid=82"><span><font>产品/项目类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&lid=0&tid=83"><span><font>市场类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&lid=0&tid=81"><span><font>设计类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&lid=0&tid=84"><span><font>职能类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&lid=0&tid=85"><span><font>内容编辑类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=&lid=0&tid=86"><span><font>客户服务类</font></span></a>
		    					    		</div>
		    		<div class="clr"></div>
		    	</div>
		    </form>
		    <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43034&keywords=&tid=0&lid=0">MIG09-Android客户端开发（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43036&keywords=&tid=0&lid=0">OMG08-产品市场经理</a></td>
					<td>市场类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43027&keywords=&tid=0&lid=0">WXG10-321 企业微信商务推广经理（智慧零售方向）</a></td>
					<td>市场类</td>
					<td>1</td>
					<td>广州</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43028&keywords=&tid=0&lid=0">24012-新手游3D动画设计师（深圳）</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43029&keywords=&tid=0&lid=0">WXG10-321 企业微信商务推广经理（餐饮行业）</a></td>
					<td>市场类</td>
					<td>1</td>
					<td>广州</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43031&keywords=&tid=0&lid=0">WXG10-321 企业微信商务推广经理（建筑/房地产行业）</a></td>
					<td>市场类</td>
					<td>1</td>
					<td>广州</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43021&keywords=&tid=0&lid=0">24012-新手游UI视觉设计师</a><span class="hot">&nbsp;</span></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43024&keywords=&tid=0&lid=0">23294-互娱移动电竞测试开发工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43025&keywords=&tid=0&lid=0">24012-新手游后台开发工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43026&keywords=&tid=0&lid=0">24012-新手游角色原画设计师（深圳）</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-01</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">3592</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?&start=10#a">2</a><a href="position.php?&start=20#a">3</a><a href="position.php?&start=30#a">4</a><a href="position.php?&start=40#a">5</a><a href="position.php?&start=50#a">6</a><a href="position.php?&start=60#a">7</a><a href="position.php?&start=70#a">...</a><a href="position.php?&start=3590#a">360</a><a href="position.php?&start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </table>
		</div>
		<div class="right wcont_s box">
		    <div class="blueline"><div class="butcjwt"></div></div>
		 """
soup = BeautifulSoup(html_doc, 'lxml')

#print(soup.prettify())
#获取所有的tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     # print('=='*10)
#     break
#     from bs4.element import Tag
#获取第二个tr标签
tr = soup.find_all('tr',limit=2)
print(tr)
#获取所有class等于even的tr标签
#trs =soup.find_all('tr',class_='even')#要加_进行区分
# trs = soup.find_all('tr',attrs={'class':'even'})
# for tr in trs:
#     print(tr)
#     print('='*30)

#将所有id等于test，class也等于test的标签
#
# aList= soup.find_all('a',id='searchrow3',class_='left items pl9')
# #aList= soup.find_all('a',attrs={'class':'even'，'id':'xxxx'})
#
# print (aList)


#获取所有a标签的href属性

# aList =soup.find_all('a')
# for a in aList:
#     # 1.通过下标操作
#     # href =a['href']
#     # print(href)
#
#     #2.通过attrs属性的方式
#     href =a.attrs['href']
#     print(href)

#获取所有的职位信息

trs =soup.find_all('tr')[1:]
infoss=[]
for tr in trs:
    infos ={}
    # tds = tr.find_all("td")
    # title = tds[0].string
    # category = tds[1].string
    # nums = tds[2].string
    # city = tds[3].string
    # pubtime =tds[4].string
    # infos['title']=title
    # infos['category']=category
    # infos['nums']=nums
    # infos['pubtime']=pubtime
    # infoss.append(infos)



    info=list(tr.stripped_strings)
    # print(infos)
    # print('='*10)
    infos['title'] = info[0]
    infos['category']=info[1]
    infos['nums']=info[2]
    infos['place']=info[3]
    infos['time'] = info[4]
    infoss.append(infos)

print(infoss)
# print(infoss)
