# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-14 下午9:19
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np

WINDOW_NAME = "DrawLines"
backgroud = np.zeros((600, 600, 3))
cv2.namedWindow(WINDOW_NAME)

points = np.array([[[150, 7*76], [3*150, 7*76], [3*150, 13*38], [11*38, 13*38], [19*19, 3*75], [3*150, 3*76],
                    [3*150, 76], [26*15, 76], [26*15, 150], [22*15, 150], [22*15, 76], [18*15, 76], [18*15, 150],
                    [14*15, 150], [14*15, 76], [150, 76], [150, 3*76], [13*19, 3*76], [5*38, 13*38], [150, 13*38],
                    ]])
cv2.fillPoly(backgroud, points, (255, 255, 255))
cv2.rectangle(backgroud, (0, 7*76), (600, 600), (0, 255, 255), -1)
cv2.line(backgroud, (0, 15*38), (600, 15*38), (0, 0, 0), 2)
cv2.line(backgroud, (150, 7*76), (150, 600), (0, 0, 0), 2)
cv2.line(backgroud, (300, 7*76), (300, 600), (0, 0, 0), 2)
cv2.line(backgroud, (450, 7*76), (450, 600), (0, 0, 0), 2)
while True:
	cv2.imshow(WINDOW_NAME, backgroud)

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()