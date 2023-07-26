import PIL
from PIL import Image, ImageEnhance, ImageDraw, ImageFont

image = Image.open("readonly/msi_recruitment.gif")
image = image.convert("RGB")

enhancer = ImageEnhance.Brightness(image)
images = []
valr = 0.1
valg = 0.1
valb = 0.1
myf = ImageFont.truetype("readonly/fanwood-webfont.ttf", size=30)
for i in range(1, 10):
    r, g, b = image.split()
    if i < 4:
        r = r.point(lambda j: j * valr)
        res = Image.merge("RGB", (r, g, b))
        img1 = ImageDraw.Draw(res)
        img1.line([(0, 440), (700, 440)], fill="black", width=50)
        img1.text((0, 420), f"channel 0 intesity {valr}", font=myf, fill="white")
        images.append(res)
        valr += 0.4
    elif 4 <= i < 7:
        g = g.point(lambda j: j * valg)
        res = Image.merge("RGB", (r, g, b))
        img1 = ImageDraw.Draw(res)
        img1.line([(0, 440), (700, 440)], fill="black", width=50)
        img1.text((0, 420), f"channel 1 intesity {valg}", font=myf, fill="white")
        images.append(res)
        valg += 0.4
    else:
        b = b.point(lambda j: j * valb)
        res = Image.merge("RGB", (r, g, b))
        img1 = ImageDraw.Draw(res)
        img1.line([(0, 440), (700, 440)], fill="black", width=50)
        img1.text((0, 420), f"channel 2 intesity {valb}", font=myf, fill="white")
        images.append(res)
        valb += 0.4

first_image = images[0]
contact_sheet = PIL.Image.new(
    first_image.mode, (first_image.width * 3, first_image.height * 3)
)
x = 0
y = 0

for img in images:
    contact_sheet.paste(img, (x, y))
    if x + first_image.width == contact_sheet.width:
        x = 0
        y = y + first_image.height
    else:
        x = x + first_image.width

contact_sheet = contact_sheet.resize(
    (int(contact_sheet.width / 2), int(contact_sheet.height / 2))
)
contact_sheet.save("Week1_result.png")
