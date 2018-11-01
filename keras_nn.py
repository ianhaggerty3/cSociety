import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras import backend as kbackend
import data_loader

(X_train, y_train), (X_test, y_test) = data_loader.load_images()
print("X_train shape", X_train.shape)
print("y_train shape", y_train.shape)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NOTE: Change this when working with other images for the project
img_rows, img_cols = 640, 480
num_category = 5
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Keras can work with datasets that have their channels as the first dimension ('channels_first') or 'channels_last'
if kbackend.image_data_format() == 'channels_first':
    X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)   # 1 is used here because MNIST is B&W
    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

# Convert datatypes of the numpy arrays to 32 bit floats and divide by 255 (batch normalization)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

print('X_train shape:', X_train.shape)     # Shape should be 60000 X 28 X 28 X 1
print(X_train.shape[0], 'train samples')   # 60000 Training Samples
print(X_test.shape[0], 'test samples')     # 10000 Testing Samples

# Convert the labels to one hot form
y_train = keras.utils.to_categorical(y_train, num_category)
y_test = keras.utils.to_categorical(y_test, num_category)

# Creating the Model
model = Sequential()
model.add(Conv2D(16, kernel_size=(5, 5), activation='relu', input_shape=input_shape))   # 32 - 3 X 3 filters with ReLU Activation Function
model.add(Conv2D(32, (5, 5), activation='relu'))   # 64 - 3 X 3 filters with ReLU Activation Function
model.add(MaxPooling2D(pool_size=(5, 5)))   # Max Pool the bitmaps 4 bit squares at a time
model.add(Flatten())                        # Flatten the dimensions
model.add(Dense(32, activation='relu'))    # Adding a dense layer at the end
model.add(Dense(num_category, activation='softmax'))   # Softmax activation function to get probability distributions
# Categorical Crossentropy loss function with Adadelta optimizer
# model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])

model.compile(loss=keras.losses.categorical_crossentropy, optimizer='sgd', metrics=['accuracy'])

# Training Hyperparameters
batch_size = 3   # Mini batch sizes
num_epoch = 25     # Number of epochs to train for
try:
    model_log = model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=batch_size, epochs=num_epoch, verbose=1)
except KeyboardInterrupt:
    print("Interrupted learning process")

score = model.evaluate(X_test, y_test, batch_size=batch_size, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

model_digit_json = model.to_json()
with open("model_digit.json", "w") as json_file:
    json_file.write(model_digit_json)
model.save_weights("model_digit.h5")
print("Saved model to disk")
