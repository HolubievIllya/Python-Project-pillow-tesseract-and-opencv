import zipfile
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    "C:/Program Files/Tesseract-OCR/tesseract.exe"  # your path may be different
)

def find_word(word: str, path: str) -> str:
    with zipfile.ZipFile(path) as archieve:
        unzipped_lst = archieve.infolist()
        for i in range(len(unzipped_lst)):
            ifile = archieve.open(unzipped_lst[i])
            img = Image.open(ifile)
            if word in pytesseract.image_to_string(img):
                print(f"Results found in {archieve.namelist()[i]}")


find_word("The", "readonly/images.zip")

