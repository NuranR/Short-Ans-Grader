import cv2
import numpy as np
import pytesseract
import os

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
#
# imgQ = cv.imread('blank_form.png')
# cv.imshow("Output", imgQ)
# cv.waitKey(0)

# Load the image
image = cv2.imread('mitobw.jpg')

# Preprocess the image (grayscale conversion, thresholding, etc.)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Add any necessary preprocessing steps here

# Use pytesseract to perform OCR
extracted_text = pytesseract.image_to_string(gray)

# Print the extracted text
print(extracted_text)

# 7‘/\?’(o c.\'\onArs‘ Q