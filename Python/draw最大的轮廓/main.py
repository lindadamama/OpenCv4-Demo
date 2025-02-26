# OpenCv版本：opencv-python 4.6.0.66
# 内容：draw最大的轮廓
# 博客：http://www.bilibili996.com/Course?id=5528010000260
# 作者：高仁宝
# 时间：2023.11

import cv2
import numpy as np

org = cv2.imread('../images/cards.png')

imgray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgray', imgray)

# 白色背景
ret, threshold = cv2.threshold(imgray, 244, 255, cv2.THRESH_BINARY_INV)  # 把黑白颜色反转
cv2.imshow('after threshold', threshold)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

areas = list()
for i, cnt in enumerate(contours):
    areas.append((i, cv2.contourArea(cnt)))#面积大小

#按面积大小，从大到小排序
a2 = sorted(areas, key=lambda d: d[1], reverse=True)

cv2.waitKey(10)#要先按一下键盘
for i, are in a2:
    if are < 150:
        continue
    img22 = org.copy()#逐个contour 显示
    cv2.drawContours(img22, contours, i, (0, 0, 255), 3)
    print(i, are)

    cv2.imshow('drawContours', img22)
    k = cv2.waitKey(200)
    if k == ord('q'):
        break

# 获取最大或某个contour，剪切
idx = a2[1][0]
mask = np.zeros_like(org)  # Create mask where white is what we want, black otherwise
cv2.drawContours(mask, contours, idx, (0, 255, 0), -1)  # Draw filled contour in mask
out = np.zeros_like(org)  # Extract out the object and place into output image
out[mask == 255] = org[mask == 255]
cv2.imshow('out_contour.jpg', out)

# roi方法
idx = a2[4][0]
x, y, w, h = cv2.boundingRect(contours[idx])
roi = org[y:y + h, x:x + w]
cv2.imshow('out_contour-roi4.jpg', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()







