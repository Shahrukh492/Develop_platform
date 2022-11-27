import cv2
import dlib
import argparse
import time
import os

#Path
data_path = "E:/GoldenEye/Testing"
training_data, labels = [], []

for path, subdirname, filenames in os.walk(data_path):


    for file_name in filenames:
        if file_name.startswith('.'):
            print('Skipping system file')
            continue

        f_id = os.path.basename(path)
        img_path = os.path.join(path,file_name)
        print('img_path:',img_path)
        print('f_id:',f_id)

        image = cv2.imread(img_path)
        if image is None:
            print('Image not loaded properly !!!')
            continue

# initialize hog + svm based face detector
    hog_face_detector = dlib.get_frontal_face_detector()

    # initialize cnn based face detector with the weights
    cnn_face_detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
    start = time.time()

    # apply face detection (hog)
    faces_hog = hog_face_detector(image, 1)

    end = time.time()
    print("Execution Time (in seconds) :")
    print("HOG : ", format(end - start, '.2f'))

    # loop over detected faces
    for face in faces_hog:
        x = face.left()
        y = face.top()
        w = face.right() - x
        h = face.bottom() - y

        # draw box over face
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)


    start = time.time()

    # apply face detection (cnn)
    faces_cnn = cnn_face_detector(image, 1)

    end = time.time()
    print("CNN : ", format(end - start, '.2f'))

    # loop over detected faces
    for face in faces_cnn:
        x = face.rect.left()
        y = face.rect.top()
        w = face.rect.right() - x
        h = face.rect.bottom() - y

         # draw box over face
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)

    # write at the top left corner of the image
    # for color identification
    img_height, img_width = image.shape[:2]
    cv2.putText(image, "HOG", (img_width-50,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0,255,0), 2)
    cv2.putText(image, "CNN", (img_width-50,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0,0,255), 2)

    # display output image
    cv2.imshow("face detection with dlib", image)

cv2.waitKey(0)



    # save output image 
    #cv2.imwrite(".png", image)

# close all windows
cv2.destroyAllWindows()