
from __future__ import unicode_literals

'''''''''''''糗图图片爬取程序'''''''''''''''
'''
第一步:导入需要用到的模块

第二步:首先对程序进行UA伪装，防止被网站检测到这是爬虫，被称为:反爬机制
    headers={
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

第三步:对网页进行url请求，获取网页源码数据
    

第四步:对网页的源码数据进行糗图图片的数据进行解析，提取

第五步:对解析的数据进行文件创建并保存，简称:持久化存储

第六步:创建糗图图片的可视化
'''

import requests
from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.charts import Pie
from lxml import etree
import re
import os

if __name__ == "__main__":

    # 首先对程序进行UA伪装，防止被网站检测到这是爬虫，被称为:反爬机制
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

    # 创建一个文件夹，保存所有的图片，如果没有这个文件就重新创建
    if not os.path.exists("./qiutulibs"):
        os.mkdir("./qiutulibs")

    # 设置一个通用的url模板
    post_url = "https://www.qiushibaike.com/imgrank/page/%d/"

    # 得到糗图图片页数的源码数据
    for pageNum in range(1, 3):
        # 对应页码的url
        new_url = format(post_url % pageNum)

    # 获取url的相应数据
    page_text = requests.get(url=post_url, headers=headers).text
    # 使用聚焦爬虫将页面中所有的糗图进行解析/提取
    # 使用正则表达式获取所有图片的url
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    # 对得到的图片进行二进制数据解析
    tree = etree.HTML(page_text)
    # 对作者的标签进行定位
    img_names = tree.xpath('//div[@class="col1 old-style-col1"]//div[@class="author clearfix"]')
    # print(img_names)
    # 对作者的标好笑值进行定位
    haoxiaos = tree.xpath('//div[@class="col1 old-style-col1"]//span[@class="stats-vote"]')

    # 用于糗图图片好笑值的存储
    myhaoxiao = []

    # 用于糗图图片作者的存储
    myname_list = []

    # 循环得到所有的好笑值数据
    for haoxiao in haoxiaos:
        # 用xpath定位到标签
        haoxiao_i = haoxiao.xpath('./i/text()')[0]
        # 将得到的标签值储存到myhaoxiaod的列表中
        myhaoxiao.append(haoxiao_i)
    # print(myhaoxiao)

    # 循环得到所有的作者名
    for img_name in img_names:
        # 用xpath定位到作者名的标签
        img_name_a = img_name.xpath('./a[2]/h2/text()')[0]
        # 将定位到的标签值储存到列表中
        myname_list.append(img_name_a)
        # 将列表中的'\n'去除
        t = (item.replace("\n", "") for item in myname_list)

    # 定位所有糗图的src，并形成列表
    img_src_list = re.findall(ex, page_text, re.S)

    for src in img_src_list:
        # 拼接到了图片完整的图片url
        src = "https:" + src
        # 请求到了图片的二进制数据
        img_data = requests.get(url=src, headers=headers).content
        # 生成图片名称
        img_name = src.split("/")[-1]
        # print(img_name)
        # 保存存储图片路径
        imgpath = "./qiutulibs/" + img_name

        # 将数据写入到文件中
        with open(imgpath, "wb") as fp:
            fp.write(img_data)
            print(img_name + "   下载成功！！！")

    # '''''''''糗图图片之可视化分析''''''''''
    # 创建一个实例化对象
    bar = Bar()
    # 水平轴糗图作者
    bar.add_xaxis(list(t))
    # 垂直轴显示好笑值
    bar.add_yaxis("好笑值", myhaoxiao)
    # 创建标题和副标题
    bar.set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="糗事百科之好笑榜", subtitle="糗图图片"),
    )
    # 使用render()函数将图片生成HTML文件
    bar.render('糗图图片之柱状图.html')

    inner_x_data = ["好笑", "很好笑", "特好笑"]
    inner_y_data = [200, 400, 600]
    # zip函数两个部分组合在一起list(zip(x,y))-----> [(x,y)]
    inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]
    # 水平轴显示作者名称
    outer_x_data =myname_list
    # 垂直轴显示数据
    outer_y_data = myhaoxiao
    # zip函数两个部分组合在一起list(zip(x,y))-----> [(x,y)]
    outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]
    (
        # 设置pie图大小
        # center指定每个图形的位置，radius指定每个饼图内外圈的大小

        Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
            # 图表内容设置
            .add(
            series_name="糗事百科",
            data_pair=inner_data_pair, # 系列数据项，格式为 [(key1, value1), (key2, value2)]

            # 饼图内圈和外圈的大小比例
            radius=[0, "30%"],

            # 显示数据和百分比
            label_opts=opts.LabelOpts(position="inner"),
        )
            .add(
            series_name="糗事百科",
            # 饼图内圈和外圈的大小比例
            radius=["40%", "55%"],
            data_pair=outer_data_pair,
            label_opts=opts.LabelOpts(formatter="{a} - {b} - {c} - {d}"),
        )
            # 图例在左边和垂直显示
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
            # 系统配置项
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"

            )
        )
            # 使用render()函数将图片生成HTML文件
        .render("糗图图片之饼图(1).html")
    )

    x_data = myname_list
    y_data = myhaoxiao
    data_pair = [list(z) for z in zip(x_data, y_data)]
    data_pair.sort(key=lambda x: x[1])  # 排序

    c = (
        # 设置长、宽、背景色
        Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
            .add(
            series_name="访问来源-糗事百科",
            data_pair=data_pair,
            # 是否展示成南丁格尔图，通过半径区分数据大小。可选择两种模式：
            # 'radius' 扇区圆心角展现数据的百分比，半径展现数据的大小。
            # 'area' 所有扇区圆心角相同，仅通过半径展现数据大小。
            rosetype="radius",
            # 饼图的半径，数组的第一项是内半径，第二项是外半径（如果两项均设置则为环状图）
            # 默认设置成百分比，相对于容器高宽中较小的一项的一半
            radius="50%",
            # 饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
            # 默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
            center=["50%", "50%"],
            # 标签配置项，参考 `series_options.LabelOpts`
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .set_global_opts(
            # 标题设置项
            title_opts=opts.TitleOpts(
                title="Customized Pie",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            # 图例设置 隐藏
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
        )
            .render("糗图图片之饼图(2).html")
    )

