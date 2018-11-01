import keras
from keras import backend as kbackend
import data_loader

fid = open("model_digit.json", "r")
json_string = fid.read()
model = keras.models.model_from_json(json_string)
model.load_weights('model_digit.h5', by_name=False)
fid.close()

(X_test, y_test) = data_loader.load_images()

X_test = X_test.astype('float32')
X_test /= 255

img_rows, img_cols = 640, 480
num_category = 5

if kbackend.image_data_format() == 'channels_first':
    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

y_test = keras.utils.to_categorical(y_test, num_category)

batch_size = 3   # Mini batch sizes
num_epoch = 10     # Number of epochs to train for

model.compile(loss=keras.losses.categorical_crossentropy, optimizer='sgd', metrics=['accuracy'])

score = model.evaluate(X_test, y_test, batch_size=batch_size, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])