import cv2
import os
import numpy as np


# CONSTANTS
# This will resize the images, and the NN will adapt to this too
digit_w, digit_h = 28, 28 # used to be (128, 128)
dir_path = os.path.dirname(__file__)
X = W = 0
Y = H = 1
THRESHOLD_VAL = 126


# FUNCTIONS
# Returns the directory path, and the number it will process
def dir_and_digit():
    # Names of the directories
    directories = range(1, 10)
    # Will be appended for every digit
    dir_and_digit = []
    for dir in directories:
        dir_and_digit.append((os.path.join(dir_path, "digits/"+str(dir)+"/"), dir))
    return dir_and_digit


def resize(image):
    return cv2.resize(image, (digit_w, digit_h))


def threshold(image):
    return cv2.threshold(image, THRESHOLD_VAL, 255, cv2.THRESH_BINARY_INV)
    #return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 33, 5)


# Randomise the list of tuples
def scramble_dataset(list):
    np.random.shuffle(list)
    return list


# Iterates through the directories and returns pairs of x and y
def read():
    x = []
    y = []
    list = []
    for i in range(0, 9):
        for image in os.listdir(dir_and_digit()[i][0]):
            path = os.path.join(dir_path, "cnn_train_digits/" + str(i+1) + "/" + image)
            image = cv2.imread(path, 0)
            image = resize(image)
            ret, image = threshold(image)
            x.append(image)
            y.append(dir_and_digit()[i][1])
            list.append((image, dir_and_digit()[i][1]))
    return np.asanyarray(list)


# Divides the dataset into Training and Test sets and returns (x_train, y_train), (x_test, y_test)
def split_dataset(list_in):
    train, test = list_in[:6000, :], list_in[6000:, :]
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for x in train:
        x_train.append(x[0])
    for y in train:
        y_train.append(y[1])
    for x in test:
        x_test.append(x[0])
    for y in test:
        y_test.append(y[1])
    return (np.asanyarray(x_train), np.asanyarray(y_train)), (np.asanyarray(x_test), np.asanyarray(y_test))


# Visualise 10 items from the dataset about to train
def see_samples(x, y):
    for i in range(10):
        cv2.imshow(str(y[i]), x[i])
        cv2.waitKey()


# Returns list of tuples:
def load_dataset():
    sorted_tuples = read()
    unsorted_tuples = scramble_dataset(sorted_tuples)
    return split_dataset(unsorted_tuples)


# NEEDED FOR THE TRACKBAR
def nothing():
    pass
