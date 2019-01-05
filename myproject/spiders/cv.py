import cv2

classifier = cv2.CascadeClassifier('C:/Users/yohei/Desktop/opencv/build/etc/haarcascades/haarcascade_frontalface_alt.xml')
image = cv2.imread('C:/Users/yohei/Desktop/Grace_Hopper.jpg')

faces = classifier.detectMultiScale(image)

for x, y, w, h in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), color=(255,255,255), thickness=2)

cv2.imwrite('faces.jpg', image)

cv2.imshow('Faces', image)
# cv2.destroyAllWindows()