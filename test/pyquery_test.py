from pyquery import PyQuery as pq


html='''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''


def main():
    #TODO 字符串初始化
    # doc = pq(html)
    # print(doc("li"))
    #TODO 网址初始化
    # doc = pq(url="https://www.baidu.com")
    # print(doc("head"))
    #TODO 文件初始化
    # doc = pq(filename="index.html")
    # print(doc("head"))
    #TODO css选择器
    #doc = pq(html)
    #print(doc(".item-1"))
    #TODO 子元素
    # item = doc(".list")
    # print(item)
    # print(item.children())
    # print(item.children(".item-1"))
    # print(item.find(".item-0"))
    #TODO 父元素
    # item = doc(".item-0")
    # #最顶层父元素
    # print(item.parent())
    # 父元素
    # print(item.parents())
    # #标签指向的父元素
    # print(item.parents(".list"))
    #TODO 兄弟元素
    # item = doc(".item-0.active")
    # print(item.siblings())
    # #带参数的兄弟元素
    # print(item.siblings(".active"))
    #TODO 遍历元素
    # item = doc(".item-0").items()
    # for i in item:
    #     print(i)
    #TODO 获取信息
    #item = doc(".item-0.active a")
    # print(item.attr("href"))
    # print(item.attr.href)
    # #获取文本
    # print(item.text())
    # #获取html
    # print(item.html())
    # TODO 移除
    # item.remove_class("active")
    # print(item)
    # TODO add
    # item.add_class("active")
    # print(item)
    #TODO add css
    # doc = pq(html)
    # item = doc(".item-0.active")
    # print(item)
    # item.attr("name", "link")
    # print(item)
    # item.css("font-size", "14px")
    # print(item)
    #TODO remove
    # doc = pq(html)
    # item = doc("#container")
    # print(item.text())
    # item.find("p").remove()
    # print(item.text())
    #TODO 伪类选择器
    doc = pq(html)
    # 第一个元素
    li = doc("li:first-child")
    print(li)
    # 最后一个元素
    li = doc("li:last-child")
    print(li)
    # 第二个元素
    li = doc("li:nth-child(2)")
    print(li)
    # 索引大于2的元素
    li = doc("li:gt(2)")
    print(li)
    # 包含某项内容的元素
    li = doc("li:contains(fifth)")
    print(li)



if __name__ == '__main__':
    main()