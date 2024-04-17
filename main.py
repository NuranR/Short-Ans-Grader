import cv2
import numpy as np
import pytesseract
import os
from PIL import Image

blank_img = cv2.imread('imgs/test_1.png')
blank_img_pil = Image.fromarray(cv2.cvtColor(blank_img, cv2.COLOR_BGR2RGB))
cv2.imshow("blank", blank_img)
cv2.waitKey(0)

answers = []
x, y = 35, 201
width, height = 524, 99

area = (x, y, x+width, y+height)


cropped_img1 = blank_img_pil.crop(area)
# cropped_img1.show()
# cv2.imshow("Q1", cropped_img1)
# cv2.waitKey(0)
# cropped_img.save("cropped_image.jpg")

extracted_text = pytesseract.image_to_string(cropped_img1)

print(extracted_text)