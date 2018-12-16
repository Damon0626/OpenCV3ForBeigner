# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-16 下午2:53
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import matplotlib.pyplot as plt
'''
1、为什么要做直方图均衡化
在现实的拍摄过程中，比如说视频监控领域，由于其图像的灰度分布集中在较窄的范围内，这就导致了图像的细节不够清晰。
为什么不清晰呢，因为灰度分布较窄时，那么，在计算对比度的时候，对比度就很小，所以就不清晰。为了使得图像变得清晰，
那么就需要使得灰度值的差别变大，为了使得灰度值的差别变大，就意味着灰度分布就变的较宽，使得灰度值分布变得均匀，
在某个灰度级区间内，像素的个数分布大致相同，这样才能使得图像的对比度增强，细节变得清晰可见。
'''

image = cv2.imread('tsukuba_l.png', 0)
plt.subplot(221), plt.hist(image.ravel(), 256, [0, 256])
plt.subplot(223), plt.imshow(image)
clahe = cv2.createCLAHE(2.0, (8, 8))
cl1 = clahe.apply(image)
plt.subplot(222), plt.hist(cl1.ravel(), 256, [0, 256])
plt.subplot(224), plt.imshow(cl1)
plt.show()