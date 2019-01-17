# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-17 下午8:44
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
角点是一类具有特定特征的点，角点也是处在一个无论框框往哪边移动, 框框内像素值都会变化很大的情况而定下来的点.

Open 中的函数 cv2.cornerHarris() 可以用来进行角点检测。参数如
下:
• img - 数据类型为 float32 的输入图像。
• blockSize - 角点检测中要考虑的领域大小。
• ksize - Sobel 求导中使用的窗口大小
• k - Harris 角点检测方程中的自由参数,取值参数为 [0,04,0.06].
'''

import cv2
import numpy as np


img = cv2.imread('chessboard.png')
img = cv2.resize(img, (640, 480))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)  # 膨胀，目的是提升图像角点标注的清晰准确度

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()