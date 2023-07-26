import cv2 as cv
from PIL import Image, ImageDraw


face_cascade = cv.CascadeClassifier("readonly/haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("readonly/haarcascade_eye.xml")


img = cv.imread("readonly/test2.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)

pil_img = Image.fromarray(gray, mode="L")

drawing = ImageDraw.Draw(pil_img)
rec = faces.tolist()[0]

drawing.rectangle((rec[0], rec[1], rec[0] + rec[2], rec[1] + rec[3]), outline="white")

pil_img.show()