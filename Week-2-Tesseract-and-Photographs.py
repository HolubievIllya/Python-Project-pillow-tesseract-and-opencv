from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    "C:/Program Files/Tesseract-OCR/tesseract.exe"  # your path may be different
)


image = Image.open("readonly/storefront.jpg")
bounding_box = (315, 170, 700, 270)
title_image = image.crop(bounding_box)
title_image.show()
print(pytesseract.image_to_string(title_image))
