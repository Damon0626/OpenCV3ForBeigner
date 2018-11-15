# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-15 下午7:48
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import time
import numpy as np


image = cv2.imread("27.jpg")
rows = open("synset_words.txt").read().strip().split("\n")
classes = [r[r.find(" ") + 1: ].split(",")[0] for r in rows]  # 获得文件中的分类

blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))
print("[INFO]loading model...")
net = cv2.dnn.readNetFromCaffe("bvlc_googlenet.prototxt", "bvlc_googlenet.caffemodel")

net.setInput(blob)
start = time.time()
preds = net.forward()
end = time.time()

print("[INFO] classification took{:.5} seconds".format(end - start))
print(preds.shape)
idexs = np.argsort(preds[0])[:: -1][:5]  # 返回五个最大值索引
for (i, idx) in enumerate(idexs):
	if i == 0:
		print(idx)
		test = "Label: {}, {:.2f}%".format(classes[idx], preds[0][idx]*100)
		cv2.putText(image, test, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)