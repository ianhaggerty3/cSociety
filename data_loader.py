import cv2
import numpy
import glob

X_RES = 640
Y_RES = 480

def load_images():
    folders = glob.glob('images/train_*')
    size = 0
    for folder in folders:
        images = glob.glob(folder + '/*')
        size += len(images)

    X_train = numpy.zeros((size, Y_RES, X_RES))
    y_train = numpy.zeros((size))

    image_num = 0
    for category in range(len(folders)):
        images = glob.glob(folders[category] + '/*')
        for image in images:
            y_train[image_num] = category
            X_train[image_num] = cv2.imread(image, 0)
            image_num += 1

    folders = glob.glob('images/test_*')
    size = 0
    for folder in folders:
        images = glob.glob(folder + '/*')
        size += len(images)

    X_test = numpy.zeros((size, Y_RES, X_RES))
    y_test = numpy.zeros((size))

    image_num = 0
    for category in range(len(folders)):
        images = glob.glob(folders[category] + '/*')
        for image in images:
            y_test[image_num] = category
            X_test[image_num] = cv2.imread(image, 0)
            image_num += 1

    return (X_train, y_train), (X_test, y_test)


if '__name__' == '__main__':
    (X_test, y_test) = load_images()

    print(X_test.shape)
    print(y_test.shape)
