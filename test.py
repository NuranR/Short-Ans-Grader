for y in range(201, 698, 124):
    print(y)


answers = []
x= 35
#y=201
width, height = 524, 99
for y in range(201, 698, 124):
    area = (x, y, x + width, y + height)

    cropped_img = blank_img_pil.crop(area)
    # cropped_img1.show()
    # cv2.imshow("Q1", cropped_img1)
    # cv2.waitKey(0)
    # cropped_img.save("cropped_image.jpg")

    extracted_text = pytesseract.image_to_string(cropped_img)

    print(extracted_text)