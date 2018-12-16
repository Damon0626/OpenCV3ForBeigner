# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-16 下午2:43
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt


'''
n, bins, patches = plt.hist(arr, bins=10, normed=0, facecolor='black', edgecolor='black',alpha=1，histtype='bar')
hist的参数非常多，但常用的就这六个，只有第一个是必须的，后面四个可选

arr: 需要计算直方图的一维数组

bins: 直方图的柱数，可选项，默认为10

normed: 是否将得到的直方图向量归一化。默认为0

facecolor: 直方图颜色

edgecolor: 直方图边框颜色

alpha: 透明度

histtype: 直方图类型，‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’

返回值 ：

n: 直方图向量，是否归一化由参数normed设定

bins: 返回各个bin的区间范围

patches: 返回每个bin里面包含的数据，是一个list
'''

image = cv2.imread('home.jpg')
plt.hist(image.ravel(), bins=256, range=[0, 256])
plt.show()