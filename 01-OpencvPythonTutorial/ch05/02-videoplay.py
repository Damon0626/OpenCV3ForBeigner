# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-18 下午4:42
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2


cap = cv2.VideoCapture('Minions_banana.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frame per second using video.get(cv2.CAP_PROP_FPS):{0}".format(fps))
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print("共有", num_frames, "帧")
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_wight = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print("高：", frame_height, '宽：', frame_wight)
frame_now = cap.get(cv2.CAP_PROP_POS_FRAMES)
print("当前帧数{0}".format(frame_now))  # 0帧


frame_no = 121  # 想获取的帧数
cap.set(1, frame_no)
ret, frame = cap.read()
cv2.imshow('frame_no'+str(frame_no), frame)

frame_now = cap.get(cv2.CAP_PROP_POS_FRAMES)
print("当前帧数{0}".format(frame_now))  # 122帧

while cap.isOpened():
	ret, frame = cap.read()
	if not ret:  # 处理最后退出错误
		break
	frame_now = cap.get(cv2.CAP_PROP_POS_FRAMES)
	print("当前帧数", frame_now)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow("frame", gray)
	if cv2.waitKey(1) == 27:
		break
cap.release()
cv2.destroyAllWindows()