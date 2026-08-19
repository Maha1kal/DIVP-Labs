import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read Images
source = cv2.imread("source.png", 0) 
reference = cv2.imread("reference.png", 0)

# Histogram Matching Function
def histogram_matching(source, reference):

    src_hist, _ = np.histogram(source.flatten(), 256, [0,256])
    ref_hist, _ = np.histogram(reference.flatten(), 256, [0,256])

    src_cdf = src_hist.cumsum()
    ref_cdf = ref_hist.cumsum()

    src_cdf = src_cdf / src_cdf[-1]
    ref_cdf = ref_cdf / ref_cdf[-1]

    lookup = np.zeros(256)

    j = 0
    for i in range(256):
        while j < 255 and ref_cdf[j] < src_cdf[i]:
            j += 1
        lookup[i] = j

    matched = lookup[source].astype(np.uint8)

    return matched

matched = histogram_matching(source, reference)

cv2.imshow("Source Image", source)
cv2.imshow("Reference Image", reference)
cv2.imshow("Matched Image", matched)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Histograms
plt.figure(figsize=(10,5))

plt.subplot(131)
plt.hist(source.ravel(),256,[0,256])
plt.title("Source")

plt.subplot(132)
plt.hist(reference.ravel(),256,[0,256])
plt.title("Reference")

plt.subplot(133)
plt.hist(matched.ravel(),256,[0,256])
plt.title("Matched")

plt.show()