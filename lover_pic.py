#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-08-06 18:54

__author__ = 'Ted'

from PIL import Image
import cv2
import os

#读取想生成的主图
img = cv2.imread("start.jpg")
#读取主图尺寸，shape(高，宽，颜色相关) 高1080 宽1440
height,width,channels = img.shape
#设置小格图的尺寸，如果太小，代码对小图处理工作量太大，生成效果也太密不好看，这里采用高、宽公约数120
unit_size = 120

#根据小格尺寸，计算大图可容纳小图数量
y_index = height//unit_size
x_index = width//unit_size

#新建与主图一样大的白色底图
new_img = Image.new('RGB',(width,height),'#FFFFFF')
#读取 pics 文件夹中想要合成的素材图片
pic_list = []
for item in os.listdir("pics"):
    #对文件夹中的 jpg 图片格式筛选
    if item.endswith(".jpg") or item.endswith(".JPG") :
        pic_list.append(item)

#获取素材图片数目
total = len(pic_list)


x=0
y=0
for i in range(x_index*y_index):
    #提醒进度的语句
    print(f"目前进度{i}/{x_index*y_index}")
    #对素材图缩放至小格大小
    test = Image.open("pics/" + pic_list[i%total]).resize((unit_size,unit_size), Image.ANTIALIAS)
    #将缩放成小格的素材图按顺序贴到白色底图上
    new_img.paste(test,(x*unit_size,y*unit_size))
    x+=1
    if x==x_index:
        x=0
        y+=1


print("素材图合成完毕！")
#将合成的素材图存至 out.jpg
new_img.save("out.jpg",quality=100)

#读取主图
src1 = cv2.imread("start.jpg")
#读取合成后的素材图
src2 = cv2.imread("out.jpg")
#将二者融合
result = cv2.addWeighted(src1,0.7,src2,0.3,0)
#融合后的图存至result.jpg
cv2.imwrite("result.jpg",result)






