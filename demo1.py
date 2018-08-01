from lxml import etree


text="""
<li class="multi-chosen"><span class="title">工作性质：</span>
                                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id=8z00 data-lg-tj-no="
                                                                    0001
                                                            " data-lg-tj-cid="idnull">不限                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" class="chosen" data-lg-tj-id=8z00 data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull">应届                        <i class="delete"></i>
                </a>
                                                                                                                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id=8z00 data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">实习                            <i class="delete"></i>

                </a>
                                                </li>

        <li class="multi-chosen"><span class="title">学历要求：</span>

                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0001
                                                            " data-lg-tj-cid="idnull">不限
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">大专
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" class="chosen" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">本科
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">硕士
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">博士
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">不要求
                            <i class="delete"></i>
                </a>
                                        
        </li>
        <li class="multi-chosen"><span class="title">融资阶段：</span>
                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8t00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
            </a>
                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">未融资
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">天使轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">A轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">B轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">C轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">D轮及以上
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">上市公司
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">不需要融资
                            <i class="delete"></i>
                </a>
                                                </li>
        <div class="has-more hy-area">
            <li class="multi-chosen">
                <span class="title">行业领域：</span>
                                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0001
                                                            " data-lg-tj-cid="idnull">不限
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" class="chosen" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">移动互联网
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">电子商务
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">金融
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">企业服务
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">教育
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">文化娱乐
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">游戏
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">O2O
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0010
                                                            " data-lg-tj-cid="idnull">硬件
                            <i class="delete"></i>
                    </a>
                                                                    <span class="btn-more-hy" href="javascript:;">更多&ensp;<i></i></span>
            </li>
            <div class="more-hy more-fields">
                <li class="hot multi-chosen">
                    <span class="title">行业领域：</span>
                                                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0001
                                                            " data-lg-tj-cid="idnull">不限
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" class="chosen" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">移动互联网
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">电子商务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">金融
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">企业服务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">教育
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">文化娱乐
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">游戏
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">O2O
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0010
                                                            " data-lg-tj-cid="idnull">硬件
                            <i class="delete"></i>
                        </a>
                                                                                </li>
                <li class="other multi-chosen other-hy">
                                                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0001
                                                            " data-lg-tj-cid="idnull">社交网络
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">旅游
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">医疗健康
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">生活服务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">信息安全
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">数据服务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">广告营销
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">分类信息
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">招聘
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0010
                                                            " data-lg-tj-cid="idnull">其他
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0011
                                                            " data-lg-tj-cid="idnull">区块链
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0012
                                                            " data-lg-tj-cid="idnull">人工智能
                            <i class="delete"></i>
                        </a>
                                                                                </li>
            </div>
        </div>
    </div>
</ul>



"""

# htmlabc =etree.HTML(text)
#
# print(etree.tostring(htmlabc).decode('utf-8'))
def parse_text():
    htmlabc =etree.HTML(text)
    with open("htmlabc.html",'w',encoding='utf-8') as fp:
        fp.write(etree.tostring(htmlabcencoding='utf-8').decode('utf-8'))
    #print(etree.tostring(htmlabc).decode('utf-8'))

def parse_file():
    htmlabc =etree.parse("htmlabc.html")
    print(etree.tostring(htmlabcencoding='utf-8').decode('utf-8'))

def parse_html_file():
    parser = etree.HTMLParser(encoding="utf-8")
    htmlabc = etree.parse('htmlabc.html',parser=parser)
    print(etree.tostring(htmlabc,encoding='utf-8').decode('utf-8'))

if __name__=='__main__':
    parse_html_file()







