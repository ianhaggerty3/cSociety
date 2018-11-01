import cv2
import time

def get_images(numSamples: int, secsBetweenSamples: float):
    '''Gets a set number of images in the specified folders'''
    # 0 front camera
    # 1 back camera
    camera = 0
    cap = cv2.VideoCapture(camera)
    categories = {0: 'closed_fist', 1: 'one_finger', 2: 'open_hand', 3: 'thumbs_up', 4: 'two_fingers'}
    name = input('Please input your name: ')
    for key in categories:
        _ = input(f'Press enter if you are ready to take image: {categories[key]}')

        # Capture X number of images
        for x in range(numSamples):
            # take image
            ret, frame = cap.read()

            # display image
            cv2.imshow('frame', frame)

            #   Ensure common resolution
            frame = cv2.resize(frame, (640, 480))

            # write image to file
            out = cv2.imwrite(f'./images/{categories[key]}/{name}_{categories[key]}{x}.jpg', frame)
            cv2.waitKey(1)
            time.sleep(secsBetweenSamples)

    cap.release()

if __name__ == '__main__':
    get_images(50, 0.5)