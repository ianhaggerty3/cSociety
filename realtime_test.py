import keras
import numpy
import cv2
import time

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
            X_test = X_test.reshape(1, img_rows, img_cols, 1) #One BW image is 1 x 640 x 480 x 1
            prediction = model.predict(X_test)

            # Display image with the correct prediction in text format
            index = numpy.argmax(prediction)
            cv2.putText(frame, categories[index], (30, 30), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('current image', frame)
            cv2.waitKey(1)
            time.sleep(secsBetweenSamples)

    except KeyboardInterrupt:
        # Note: Pycharm KeyboardInterrupt is ctrl + f2, normally it is ctrl + c
        print('')
    cap.release()

if __name__ == '__main__':
    realtime_test(0.5)