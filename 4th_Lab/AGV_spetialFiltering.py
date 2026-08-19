import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Read Image (Grayscale)
# -------------------------------------------------
img = cv2.imread("image.jpg", 0)

if img is None:
    print("Image not found!")
    exit()

# -------------------------------------------------
# Add Gaussian Noise
# -------------------------------------------------
def add_gaussian_noise(image, sigma):

    noise = np.random.normal(0, sigma, image.shape)

    noisy = image + noise

    noisy = np.clip(noisy,0,255)

    return noisy.astype(np.uint8)

# -------------------------------------------------
# Motion Blur
# -------------------------------------------------
def motion_blur(image,length=9):

    kernel=np.zeros((length,length))

    kernel[length//2,:]=1

    kernel=kernel/length

    return correlate2d(image,kernel)

# -------------------------------------------------
# Correlation From Scratch
# -------------------------------------------------
def correlate2d(image,kernel):

    m,n=kernel.shape

    pad=m//2

    padded=np.pad(image,pad,mode='edge')

    output=np.zeros_like(image,dtype=np.float32)

    for i in range(image.shape[0]):

        for j in range(image.shape[1]):

            region=padded[i:i+m,j:j+n]

            output[i,j]=np.sum(region*kernel)

    return np.clip(output,0,255).astype(np.uint8)

# -------------------------------------------------
# Averaging Filter
# -------------------------------------------------
def averaging_filter(image,size):

    kernel=np.ones((size,size),dtype=np.float32)/(size*size)

    return correlate2d(image,kernel)

# -------------------------------------------------
# Laplacian Sharpening
# -------------------------------------------------
lap4=np.array([[0,-1,0],
               [-1,4,-1],
               [0,-1,0]])

lap8=np.array([[-1,-1,-1],
               [-1,8,-1],
               [-1,-1,-1]])

def sharpen(image,kernel):

    lap=correlate2d(image,kernel)

    result=image+lap

    return np.clip(result,0,255).astype(np.uint8),lap

# -------------------------------------------------
# Unsharp Mask / High Boost
# -------------------------------------------------
def highboost(image,k):

    blur=averaging_filter(image,5)

    mask=image.astype(np.float32)-blur.astype(np.float32)

    result=image+k*mask

    return np.clip(result,0,255).astype(np.uint8)

# -------------------------------------------------
# Generate Test Images
# -------------------------------------------------
noise10=add_gaussian_noise(img,10)

noise25=add_gaussian_noise(img,25)

blurred=motion_blur(img)

# -------------------------------------------------
# Task 1
# -------------------------------------------------
avg3=averaging_filter(noise10,3)
avg5=averaging_filter(noise10,5)
avg9=averaging_filter(noise10,9)

# -------------------------------------------------
# Task 2
# -------------------------------------------------
sharp4,lapimg4=sharpen(blurred,lap4)

sharp8,lapimg8=sharpen(blurred,lap8)

# -------------------------------------------------
# Task 3
# -------------------------------------------------
unsharp=highboost(noise10,1)

boost15=highboost(noise10,1.5)

boost2=highboost(noise10,2)

boost3=highboost(noise10,3)

# -------------------------------------------------
# Display
# -------------------------------------------------

titles=["Original",
        "Noise σ=10",
        "Noise σ=25",
        "Average 3x3",
        "Average 5x5",
        "Average 9x9",
        "Motion Blur",
        "Laplacian 4",
        "Laplacian 8",
        "Unsharp k=1",
        "Boost k=1.5",
        "Boost k=2",
        "Boost k=3"]

images=[img,
        noise10,
        noise25,
        avg3,
        avg5,
        avg9,
        blurred,
        sharp4,
        sharp8,
        unsharp,
        boost15,
        boost2,
        boost3]

plt.figure(figsize=(15,10))

for i in range(len(images)):

    plt.subplot(4,4,i+1)

    plt.imshow(images[i],cmap="gray")

    plt.title(titles[i])

    plt.axis("off")

plt.tight_layout()

plt.show()