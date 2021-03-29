import numpy as np
import cv2

image = cv2.imread("C:/Users/user/AppData/Local/Programs/Python/images/moon.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("Moon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
