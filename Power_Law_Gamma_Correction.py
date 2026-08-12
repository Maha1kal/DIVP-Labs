#s=c×rγ
"""c=1
γ = Gamma value
Gamma < 1 → Brightens image
Gamma > 1 → Darkens image"""
import cv2
import numpy as np

image = cv2.imread("image.jpg")

gamma = 2.2

image = image / 255.0

gamma_image = np.power(image, gamma)

gamma_image = np.uint8(gamma_image * 255)

cv2.imshow("Original", cv2.imread("image.jpg"))
cv2.imshow("Gamma Corrected", gamma_image)

cv2.waitKey(0)
cv2.destroyAllWindows()