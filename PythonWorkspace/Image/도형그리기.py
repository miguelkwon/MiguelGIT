import cv2
import numpy as np

src = np.zeros((2752, 2064, 3), dtype=np.uint8)

'src = cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA)'
src = cv2.circle(src, (130,130), 120, (0, 255, 0), 0, cv2.LINE_4)
src = cv2.circle(src, (400,130), 120, (0, 255, 0), -1, cv2.LINE_4)
src = cv2.circle(src, (670,130), 120, (0, 255, 0), 0, cv2.LINE_4)
src = cv2.circle(src, (940,130), 120, (0, 255, 0), 0, cv2.LINE_4)
src = cv2.circle(src, (1210,130), 120, (0, 255, 0), 0, cv2.LINE_4)
src = cv2.circle(src, (1480,130), 120, (0, 255, 0), 0, cv2.LINE_4)
src = cv2.circle(src, (1750,130), 120, (0, 255, 0), 0, cv2.LINE_4)

'src = cv2.rectangle(src, (500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)'
'src = cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)'

pts1 = np.array([[100, 500], [300, 500], [200, 600]])
pts2 = np.array([[600, 500], [800, 500], [700, 600]])
'src = cv2.polylines(src, [pts1], True, (0, 255, 255), 2)'
'src = cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA)'

'src = cv2.putText(src, "YUNDAEHEE", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)'

cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()