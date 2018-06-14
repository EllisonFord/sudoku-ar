import random
import cv2
import os
import numpy as np

# CONSTANTS
# This will resize the images, and the NN will adapt to this too
digit_size_px = (128, 128)
dir_path = os.path.dirname(__file__)


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


# Resize any image to the constants specified above
def resize_img(input_img):
    return cv2.resize(input_img, (digit_size_px[0], digit_size_px[1]))


# Randomise the list of tuples
def scramble_dataset(list):
    np.random.shuffle(list)
    return list


# Iterates through the directories and returns pairs of x and y
def read():
    x_and_y = []

    for i in range(0, 9):
        for image in os.listdir(dir_and_digit()[i][0]):
            path = os.path.join(dir_path, "digits/" + str(i+1) + "/" + image)
            x_and_y.append((cv2.imread(path, 0), dir_and_digit()[i][1]))
    return np.asanyarray(x_and_y)


# Divides the dataset into Training and Test sets and returns (x_train, y_train), (x_test, y_test)
def split_dataset(list_in):
#    print(list_in.shape[0])
#    percent = int(0.75*list_in.shape)
    train, test = list_in[:8000, :], list_in[8000:,:]
    return train, test


# Returns list of tuples:
def load_dataset():

    sorted_tuples = read()

    print(type(sorted_tuples))

    shuffled_tuples = scramble_dataset(sorted_tuples)

    train, test = split_dataset(shuffled_tuples)

    return train, test



load_dataset()


# print("Digit is", dir_and_digit()[8][1], ", Data size:", len(os.listdir(dir_and_digit()[8][0])))
