# CatOS-type package
author = "catweird"
command_ru = "демотиватор"
deps = "None"
identificator = "dem2"
description = "Создание демотиваторов. Используйте ; для разделения текста"
mode = "pic"

"""

editmessage("Создание демотиватора: разбор текста...")

try:
    try:
        text1, text2 = parameter.split(";")[0], parameter.split(";")[1]
    except:
        text1, text2 = parameter, ""
except:
    text1, text2 = "блять текст забыл.", "ладно."

if text2 == "":
    text2 = "  "

editmessage("Создание демотиватора: загрузка изображения...")
Download(ReadFF("argv_picture.txt"), "usr/download.jpg")

img = Image.open("usr/download.jpg")
width, height = img.size

coef_pix = int(width + height / 2 - int(width + height / 2 / 1.7))
if coef_pix < 100:
    coef_pix = 100
#message(f"debug: coef_pix = {coef_pix}")
if width * height < 350 or width * height < 60000:
    img.save("usr/download.jpg")
    resize_image("usr/download.jpg", "usr/download.jpg", (width * coef_pix, height * coef_pix))
    img = Image.open("usr/download.jpg")
    width, height = img.size

editmessage("Создание демотиватора: загрузка шрифтов...")

font1 = ImageFont.truetype(font="usr/demfont.ttf", size=int(coef_pix / 2), encoding="unic")
font2 = ImageFont.truetype(font="usr/demfont2.ttf", size=int(coef_pix / 3), encoding="unic")

#if imagetext.size[1] > height+coef_pix:
#    wid = imagetext.size[0]
#else:
wid = width+coef_pix#+imagetext.size[0]

text1 = "\n".join(textwrap.wrap(text1, width=18, replace_whitespace=False))
text2 = "\n".join(textwrap.wrap(text2, width=20, replace_whitespace=False))

editmessage("Создание демотиватора: форматирование текста...")

notformatted = True
drawtext = ImageDraw.Draw(img)
w1, h1 = drawtext.textsize(text1, font=font1)
w2, h2 = drawtext.textsize(text2, font=font2)
del drawtext

#if imagetext.size[1] > height+coef_pix:
#    heighd = imagetext.size[1]
#else:
heighd = height+coef_pix+h1+h2+int(int(coef_pix / 3) * 1.1)

editmessage("Создание демотиватора: отрисовка изображения...")

imagetext = Image.new("RGB", (int(width+int(coef_pix*2)), h1+h2+90+int(coef_pix*2)), (0,0,0,0))
imagetextd = ImageDraw.Draw(imagetext)
need = int(imagetext.size[0] / 3.7 - int(w2 / 2))
# готово нахуй, суём это
center1 = int(wid / 2 - int(w1 / 2))
center2 = int(wid / 2 - int(w2 / 2))
imagetextd.multiline_text((center1,5), text1, fill="white", font=font1, align="center")
imagetextd.multiline_text((center2,5+h1+10), text2, fill="white", font=font2, align="center")
#module_center = int(imagetext.size[0] / 2)

image = Image.new("RGB", (wid,heighd), (0,0,0,0))
shape = [(width+int(coef_pix / 2) + 3,height+int(coef_pix / 2) + 3),(int(coef_pix / 2) - 2,int(coef_pix / 2) - 2)]
draw = ImageDraw.Draw(image)
draw.rectangle(shape, outline="white")
image.paste(img, (int(coef_pix / 2) + 1, int(coef_pix / 2) + 1))
#image.paste(imagetext, (int(image.size[0] / 1.8) - int(imagetext.size[0] / 3), height + int(coef_pix / 2 + int(coef_pix / 2) - int(coef_pix / 4))))
image.paste(imagetext, (0, height + int(coef_pix / 2 + int(coef_pix / 2) - int(coef_pix / 4))))
image.save("usr/dem.jpg")
picturedata("usr/dem.jpg", "Ваш демотиватор готов:")
del image
del shape
del draw
del center1
del center2
del text1
del text2
del h1
del h2
del w1
del w2
del imagetext
del imagetextd
del width
del height
del wid
del heighd
del font1
del font2
del coef_pix
del need
del img
"""

def bReadFF(file): # Read From File
    try:
        Ff = open(file, 'rb')
        Contents = Ff.read()
        Ff.close()
        return Contents
    except Exception as e:
        print(f'[ReadFF] Error - {str(e)}')
        return None

try:
    try:
        text1, text2 = parameter.split(";")[0], parameter.split(";")[1]
    except:
        text1, text2 = parameter, ""
except:
    text1, text2 = "блять текст забыл.", "ладно."

message("Загрузка изображения на сервер...")
Download(ReadFF('argv_picture.txt'), 'tmp/file.jpg')
a = requests.post('http://artificalintellect.pythonanywhere.com/uploadfile', data={'filename': 'usr/img.jpg', 'content': str(bReadFF('tmp/file.jpg'))}).text
Download(f"http://artificalintellect.pythonanywhere.com/demotivator?path=__home__artificalintellect__usr__img.jpg&text1={text1}&text2={text2}", 'tmp/dem.jpg')
picturedata('tmp/dem.jpg', 'Демотиватор готов: ')
