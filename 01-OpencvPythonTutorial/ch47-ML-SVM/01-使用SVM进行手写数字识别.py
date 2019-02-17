# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-17 上午9:46
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


SZ = 20
bin_n = 16
affine_flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR


# 使用方向梯度直方图作为特征向量
def deskew(img):
	m = cv2.moments(img)
	# print(m)
	if abs(m['mu02']) < 1e-2:
		return img.copy()
	skew = m['mu11'] / m['mu02']
	M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
	img = cv2.warpAffine(img, M, (SZ, SZ), flags=affine_flags)  # 图像的仿射变换
	return img


# 计算图像x,y方向的sobel导数
def hog(img):
	gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
	gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
	mag, ang = cv2.cartToPolar(gx, gy)
	bins = np.int32(bin_n*ang/(2*np.pi))
	bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
	mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]
	hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
	hist = np.hstack(hists)
	return hist


img = cv2.imread('../ch46-ML-KNN/digits.png', 0)
cells = np.array([np.hsplit(row, 100) for row in np.vsplit(img, 50)])

train_cells = np.array([i[:50] for i in cells]).reshape(-1, 400)
test_cells = np.array([i[50:] for i in cells]).reshape(-1, 400)


# deskewed = [map(deskew, row) for row in train_cells]
# hogdata = [map(hog, row) for row in deskewed]  # 返回的迭代器
# print(train_cells.shape)

deskewed = [deskew(row) for row in train_cells]
hogdata = [hog(row) for row in deskewed]

trainData = np.float32(hogdata)
# print(trainData.shape)
responses = np.float32(np.repeat(np.arange(10), 250)[:, np.newaxis])

svm = cv2.ml.SVM_create()
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)
svm.setC(2.67)
svm.setGamma(5.383)
svm.train(np.array(np.float32(hogdata)), cv2.ml.ROW_SAMPLE, responses)
svm.save('svm_data.dat')

deskewed = [deskew(row) for row in test_cells]
hogdata = [hog(row) for row in deskewed]
testData = np.float32(hogdata).reshape(-1, bin_n*4)

result = svm.predict(testData)
mask = result == responses
correct = np.count_nonzero(mask)
print(correct*100.0/result.size)