import numpy as np
import cv2 
import os
import random
import matplotlib.pyplot as plt
import pickle #to serialize and save data


WORKING_DIRECTORY = r"/home/davidfaianunes/compsci/datasci/dogsvscats/train"

CATEGORIES = ["cat", "dog"]

IMG_SIZE = 100

data = []

for category in CATEGORIES:
    folder = os.path.join(WORKING_DIRECTORY, category)
    label = CATEGORIES.index(category)
    for img in os.listdir(folder):
        img_path = os.path.join(folder, img)
        img_arr = cv2.imread(img_path)
        img_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))

        #plt.imshow(img_arr)
        #plt.show()

        data.append((img_arr, label)) # save image array + label

random.shuffle(data)

X = []
Y = []

for feature, label in data:
    X.append(feature)
    Y.append(label)

X = np.array(X)
Y = np.array(Y)

pickle.dump(X, open("X.pkl", "wb")) # wb stands for write in binary
pickle.dump(Y, open("Y.pkl", "wb"))