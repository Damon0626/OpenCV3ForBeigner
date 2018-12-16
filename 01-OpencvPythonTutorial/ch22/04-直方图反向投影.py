# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-16 下午3:29
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
'''
双边滤波
cv2.bilateraFilter()参数介绍：
. InputArray src: 输入图像，可以是Mat类型，图像必须是8位或浮点型单通道、三通道的图像。 
. OutputArray dst: 输出图像，和原图像有相同的尺寸和类型。 
. int d: 表示在过滤过程中每个像素邻域的直径范围。如果这个值是非正数，则函数会从第五个参数sigmaSpace计算该值。 
. double sigmaColor: 颜色空间过滤器的sigma值，这个参数的值月大，表明该像素邻域内有越宽广的颜色会被混合到一起，产生较大的半相等颜色区域。 
. double sigmaSpace: 坐标空间中滤波器的sigma值，如果该值较大，则意味着颜色相近的较远的像素将相互影响，
从而使更大的区域中足够相似的颜色获取相同的颜色。当d>0时，d指定了邻域大小且与sigmaSpace五官，否则d正比于sigmaSpace. 
. int borderType=BORDER_DEFAULT: 用于推断图像外部像素的某种边界模式，有默认值BORDER_DEFAULT.
'''
im1 = cv2.imread('12.png')
im1 = cv2.bilateralFilter(im1, 13, 70, 50)
box_roi = cv2.selectROI('roi', im1)

roi_im = im1[box_roi[1]:box_roi[1]+box_roi[3], box_roi[0]:box_roi[0]+box_roi[2], :]
hsv1 = cv2.cvtColor(im1, cv2.COLOR_BGR2HSV)

hsv2 = cv2.cvtColor(roi_im, cv2.COLOR_BGR2HSV)

hist1 = cv2.calcHist([hsv1], [0, 1], None, [180, 256], [0, 180, 0, 256])  # 两个通道, h和s
hist2 = cv2.calcHist([hsv2], [0, 1], None, [180, 256], [0, 180, 0, 256])

R = hist2/(hist1+1)
h, s, v = cv2.split(hsv1)
B = R[h.ravel(), s.ravel()]
B = np.minimum(B, 1)
B = B.reshape(hsv1.shape[:2])*255

strcture = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
B = cv2.filter2D(B, -1, strcture)
B = np.uint8(B)
ret, thresh = cv2.threshold(B, 50, 255, 0)

thresh = cv2.merge((thresh, thresh, thresh))
res = cv2.bitwise_and(im1, thresh)
cv2.imshow('res', res)

dst = cv2.calcBackProject([hsv1], [0, 1], hist2, [0, 180, 0, 256], 1)
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(dst, -1, disc, dst)
out = cv2.merge([dst, dst, dst]) & im1
cv2.imshow('out', out)

cv2.waitKey(1000)
