from matplotlib import pyplot as plt
from imutils import face_utils
import imutils
import dlib
import cv2
import os

data_path = "E:\\GoldenEye\\motioneye"
training_data, labels = [], []

for path, subdirname, filenames in os.walk(data_path):

    for file_name in filenames:
        if file_name.startswith('.'):
            print('Skipping system file')
            continue

        f_id = os.path.basename(path)
        img_path = os.path.join(path, file_name)
        print('Image Path:', img_path)
        # print('f_id:', f_id)

        def plt_imshow(title, image):

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            plt.imshow(image)
            plt.title(title)
            plt.grid(False)
            plt.show()

        args = {
            "shape_predictor": "shape_predictor_68_face_landmarks.dat",
            "image": img_path
        }

        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(args["shape_predictor"])

        try:
            image = cv2.imread(args["image"])
            image = imutils.resize(image, width=500)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception as err:
            print("Please Enter Currect path...")
        else:
            rects = detector(gray, 1)

            detection = False
            for (i, rect) in enumerate(rects):

                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

                (x, y, w, h) = face_utils.rect_to_bb(rect)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

                cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                for (x, y) in shape:
                    cv2.circle(image, (x, y), 1, (0, 255, 0), -1)
                detection = True
                # print(f'Face Found ')
        
            if detection == True:
                plt_imshow("Face Found", image)
                print("Face Not Found")
            else:
                os.remove(img_path)
                print('Image Deleted')