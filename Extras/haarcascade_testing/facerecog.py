# Can use this article to learn more about harcascade https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08


import cv2
img = cv2.imread('Extras\haarcascade_testing\cric.png')
greyimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
harcascade = cv2.CascadeClassifier('static\haarcascade_frontalface_default.xml')
face = harcascade.detectMultiScale(greyimg, 1.1, 9)
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+h, y+w), (255, 255, 255), 2)
cv2.imshow('detectface', img)
cv2.waitKey(0)