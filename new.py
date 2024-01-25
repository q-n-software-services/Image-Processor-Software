import cv2
import numpy as np


def calculateCenterSpot(results):
    startX, endX = results[0][0], results[0][2]
    startY, endY = results[0][1], results[0][3]
    centerSpotX = (endX - startX) / 2 + startX
    centerSpotY = (endY - startY) / 2 + startY
    return [centerSpotX, centerSpotY]


img = cv2.imread('test.jpg')
res2 = img.copy()

cords = [[1278, 704, 1760, 1090]]
center = calculateCenterSpot(cords)
cv2.circle(img, (int(center[0]), int(center[1])), 1, (0,0,255), 30)
cv2.line(img, (int(center[0]), 0), (int(center[0]), img.shape[0]), (0,255,0), 10)
cv2.line(img, (0, int(center[1])), (img.shape[1], int(center[1])), (255,0,0), 10)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# You can either use threshold or Canny edge for HoughLines().
_, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Perform HoughLines transform.
lines = cv2.HoughLines(thresh, 0.5, np.pi/180, 1000)
for line in lines:
    for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 5000*(-b))
            y1 = int(y0 + 5000*(a))
            x2 = int(x0 - 5000*(-b))
            y2 = int(y0 - 5000*(a))
            if x2 == int(center[0]):
                cv2.circle(img, (x2,y1), 100, (0,0,255), 30)

            if y2 == int(center[1]):
                print('hell2o')
                # cv2.line(res2,(x1,y1),(x2,y2),(0,0,255),2)

# Display the result.
cv2.imwrite('h_res1.png', img)
cv2.imwrite('h_res3.png', res2)

cv2.imwrite('image.png', img)