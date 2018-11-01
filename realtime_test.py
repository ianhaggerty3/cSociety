import keras
from keras import backend as kbackend
import cv2
import time
import numpy

fid = open("model_digit.json", "r")
json_string = fid.read()
model = keras.models.model_from_json(json_string)
model.load_weights('model_digit.h5', by_name=False)
fid.close()

img_rows, img_cols = 640, 480
num_category = 5
categories = {0: 'closed_fist', 1: 'one_finger', 2: 'open_hand', 3: 'thumbs_up', 4: 'two_fingers'}
# 0 front camera
# 1 back camera
camera = 0
cap = cv2.VideoCapture(camera)

font = cv2.FONT_HERSHEY_SIMPLEX

def realtime_test(secsBetweenSamples: float):
    """Tests on images provided from a laptop camera using a preloaded neural network"""
    try:
        while 1:
            # Capture a single image
            ret, frame = cap.read()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Ensure common resolution
            X_test = cv2.resize(img, (640, 480))

            # Run the image through the neural network
            '''if kbackend.image_data_format() == 'channels_first':
                X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
            else:
                print('I use the second part of the if statement')
                X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)'''
            X_test = X_test.reshape(1, img_rows, img_cols, 1)
            prediction = model.predict(X_test)
            # display image
            index = numpy.amax(prediction)
            cv2.putText(img, categories[int(prediction[0])], (10, 10), font, 0.8, 255, 2, cv2.LINE_AA)
            cv2.imshow('current image', img)
            cv2.waitKey(1)
            time.sleep(secsBetweenSamples)
    except KeyboardInterrupt:
        print('')
    cap.release()

if __name__ == '__main__':
    realtime_test(0.5)