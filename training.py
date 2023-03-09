from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

# for model's logs
NAME = f"cat-vs-dog-prediction-{int(time.time())}"
tensorboard = TensorBoard(log_dir=f"logs/{NAME}/")

X = pickle.load(open("X.pkl", "rb"))
Y = pickle.load(open("Y.pkl", "rb"))

X = X/255   # because all color values are in 0-255
            # and lower values are faster to work with

model = Sequential()

model.add(Conv2D(64,(3,3), activation = "relu"))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64,(3,3), activation = "relu"))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())

model.add(Dense(128, input_shape = X.shape[1:], activation = "relu"))

model.add(Dense(2, activation = "softmax"))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(X, Y, epochs = 5, validation_split=0.1, batch_size = 32, callbacks = [tensorboard])