# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-15 下午8:46
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("../../Chapter03/dota.jpg")
print(image.shape)
image = image[..., ::-1]  # BGR to RGB
plt.imshow(image)  # opencv读取图片为BGR模式，需修改才可以

plt.xticks([])
plt.yticks([])
plt.show()
