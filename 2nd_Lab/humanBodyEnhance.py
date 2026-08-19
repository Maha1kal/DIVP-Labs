# from PIL import Image, ImageEnhance

# Load images
# image = Image.open("image.jpg")
# mask = Image.open("mask.png").convert("L")   # White = body, Black = background

# # Increase contrast
# enhancer = ImageEnhance.Contrast(image)
# enhanced = enhancer.enhance(2.0)

# # Combine enhanced body with original background
# result = Image.composite(enhanced, image, mask)

# result.show()
# result.save("enhanced_body.jpg")