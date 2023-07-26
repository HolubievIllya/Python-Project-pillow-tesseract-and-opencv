from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    "C:/Program Files/Tesseract-OCR/tesseract.exe"  # your path may be different
)

image = Image.open("readonly/text.png")

text = pytesseract.image_to_string(image)
print(text)
