# OpenCv版本：opencv-python 4.6.0.66
# 内容：MSER区域检测
# 博客：http://www.bilibili996.com/Course?id=
# 作者：高仁宝
# 时间：2023.11

"""
MSER_create1.py:
https://stackoverflow.com/questions/40443988/python-opencv-ocr-image-segmentation
"""

import cv2

img = cv2.imread('WQbGH.jpg')
img = img[5:-5, 5:-5, :]

mser = cv2.MSER_create()

# Resize the image so that MSER can work better
img2 = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))#扩大

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
vis = img2.copy()

regions = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
cv2.polylines(vis, hulls, 1, (0, 255, 0))

img3 = cv2.resize(vis, (img.shape[1], img.shape[0]))
cv2.namedWindow('img', 0)
cv2.imshow('img', img3)
# cv2.imwrite('mser-result.jpg', vis)
cv2.waitKey(0)
cv2.destroyAllWindows()

