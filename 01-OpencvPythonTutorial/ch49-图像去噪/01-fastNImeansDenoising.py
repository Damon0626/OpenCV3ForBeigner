# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-19 下午9:58
# @Email : wwymsn@163.com
# @Software: PyCharm


import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('die.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)
plt.show()
