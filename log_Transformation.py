#s=clog(1+r)
import cv2
import numpy as np

image = cv2.imread("image.jpg")

c = 255 / np.log(1 + np.max(image))

log_image = c * np.log(image + 1)

log_image = np.array(log_image, dtype=np.uint8)

cv2.imshow("Original", image)
cv2.imshow("Log Transformation", log_image)

cv2.waitKey(0)
cv2.destroyAllWindows()