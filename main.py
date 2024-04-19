import cv2
import numpy as np
import pytesseract
import os
from PIL import Image

blank_img = cv2.imread('imgs/test_2.png')
blank_img_pil = Image.fromarray(cv2.cvtColor(blank_img, cv2.COLOR_BGR2RGB))
#cv2.imshow("blank", blank_img)
#cv2.waitKey(0)


answers = []
x= 35
#y=201
width, height = 524, 99
for y in range(201, 698, 124):
    area = (x, y, x + width, y + height)

    cropped_img = blank_img_pil.crop(area)

    extracted_text = pytesseract.image_to_string(cropped_img)[:-2]
    answers.append(extracted_text)

print(answers)