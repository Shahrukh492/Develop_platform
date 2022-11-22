import cv2
import numpy as np
import os
cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
face_classifier = cv2.CascadeClassifier(cascPath)
data_path = "Enter your Path"
training_data, labels = [], []

for path, subdirname, filenames in os.walk(data_path):
#     print('path:',path)
#     print('subdirname:',subdirname)
#     print('filenames:',filenames)

    for file_name in filenames:
        if file_name.startswith('.'):
            print('Skipping system file')
            continue

        f_id = os.path.basename(path)
        img_path = os.path.join(path,file_name)
        print('img_path:',img_path)
        print('f_id:',f_id)

        img = cv2.imread(img_path)
        if img is None:
            print('Image not loaded properly !!!')
            continue
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5,minSize=(30, 30))
        print("Found {0} faces!".format(len(faces)))

        # show face detections
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Faces found", img)
cv2.waitKey(0)
