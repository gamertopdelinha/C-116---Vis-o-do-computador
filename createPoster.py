import cv2
import numpy as np
img = cv2.imread ("./poster.jpg")
rocket = img [120:360,400:500]

img[0:240, 500:600] = rocket

text = "Imagem1"

cv2.putText(img,text,(20,220),fontFace = cv2.font,fontScale = 0.6,color = (130,110,45))
cv2.imshow("Imagem legal", img)
cv2.waitKey(0)