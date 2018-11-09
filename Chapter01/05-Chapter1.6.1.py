# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-6 下午10:48
# @Email : wwymsn@163.com
# @Software: PyCharm

# 读取和播放视频
import cv2
import time


cap = cv2.VideoCapture('./test.avi')


while True:
	ret, frame = cap.read()
	if not ret:
		break
	cv2.imshow('video', frame)
	time.sleep(0.04)  # 添加一个延时，不然每帧太快了
	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()
