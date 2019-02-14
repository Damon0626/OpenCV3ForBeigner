# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-14 下午8:52
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
x = np.array(cells)
# print(x.shape)  # 50, 100, 20, 20

train = x[:, :50].reshape(-1, 400).astype(np.float32)  # 2500train
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)

k = np.arange(10)  # 10分类
train_labels = np.repeat(k, 250)[:, np.newaxis]  # 2500*1
test_labels = train_labels.copy()


knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

ret, result, neighbours, dist = knn.findNearest(test, 5)
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100/result.size
print("Accuracy:", accuracy, "%")

np.savez('knn_data.npz', train=train, train_labels=train_labels, test=test, test_labels=test_labels)

# 载入上述保存的不可压缩npz文件
with np.load('knn_data.npz') as data:
	print(data.files)
	train = data['train']
	train_labels = data['train_labels']
	test = data['test']
	test_labels = data['test_labels']

pre_item = np.random.randint(1, 2500)
pre_pic = test[pre_item].reshape(20, 20)
_, result = knn.predict(test[pre_item - 1: pre_item])
plt.imshow(pre_pic)
print("The Prediction Result is:", int(result[0][0]))
plt.show()
