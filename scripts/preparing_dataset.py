import cv2
import os
import numpy as np
from keras.datasets import mnist
from params import *

# CONSTANTS
# This will resize the images, and the NN will adapt to this too
dir_path = os.path.dirname(__file__)


# FUNCTIONS
# Returns the directory path, and the number it will process
def dir_and_digit():
    directories = range(1, 10)  # Names of the directories
    dir_and_digit = []
    for dir in directories:
        dir_and_digit.append((os.path.join(dir_path, "cnn_train_digits/" + str(dir) + "/"), dir))
    return dir_and_digit


# NEEDED FOR THE TRACK BAR
def nothing(x):
    pass


def resize(image):
    return cv2.resize(image, (digit_w, digit_h))


def threshold(image):
    return cv2.threshold(image, THRESHOLD_VAL, 255, cv2.THRESH_BINARY_INV)


# Randomise the list of tuples
def scramble_dataset(list):
    np.random.shuffle(list)
    return list


def prepare_image(image):
    image = resize(image)
    #ret, image = threshold(image)
    return image


# Iterates through the directories and returns pairs of x and y
def read_dirs():
    x = []
    y = []
    list = []
    for i in range(0, 9):
        for image in os.listdir(dir_and_digit()[i][0]):
            path = os.path.join(dir_path, "cnn_train_digits/" + str(i+1) + "/" + image)

            image = cv2.imread(path, 0)
            image = prepare_image(image)
            x.append(image)
            y.append(dir_and_digit()[i][1])
            list.append((image, dir_and_digit()[i][1]))
    return np.asanyarray(list)


def exclusions(exclude_label, x_train, y_train, x_test, y_test):

    for i, item in enumerate(y_train):
        if item == exclude_label:
            #x_train[i] = 0
            x_train[i] = np.zeros([img_cols, img_rows], dtype=np.uint8)
            x_train[i].fill(0)

    for i, item in enumerate(y_test):
        if item == exclude_label:
            x_test[i] = np.zeros([img_cols, img_rows], dtype=np.uint8)
            x_test[i].fill(0)

    """
    for i, item in enumerate(y_train):
        if item == exclude_label:
            #print("Deleting Train", exclude_label)
            np.delete(x_train, i)
            np.delete(y_train, i)

    for i, item in enumerate(y_test):
        if item == exclude_label:
            #print("Deleting", exclude_label)
            np.delete(x_test, i)
            np.delete(y_test, i)
    """

    return x_train, y_train, x_test, y_test


# Divides the dataset into Training and Test sets and returns (x_train, y_train), (x_test, y_test)
def split_dataset(list_in, combined=True, exclude_label=None):
    train, test = list_in[:6000, :], list_in[6000:, :]

    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for x in train:
        x_train.append(x[X])
    for y in train:
        y_train.append(y[Y])
    for x in test:
        x_test.append(x[X])
    for y in test:
        y_test.append(y[Y])

    x_train = np.asanyarray(x_train)
    y_train = np.asanyarray(y_train)
    x_test = np.asanyarray(x_test)
    y_test = np.asanyarray(y_test)

    # This adds MNIST to the loaded dataset
    if combined is True:
        (x_train_mn, y_train_mn), (x_test_mn, y_test_mn) = mnist.load_data()
        x_train = np.concatenate((x_train, x_train_mn))
        y_train = np.concatenate((y_train, y_train_mn))
        x_test = np.concatenate((x_test, x_test_mn))
        y_test = np.concatenate((y_test, y_test_mn))

    # If exclude was chosen, it calls a function to remove labels
    if exclude_label is not None:
        x_train, y_train, x_test, y_test = exclusions(exclude_label, x_train, y_train, x_test, y_test)

    return (x_train, y_train), (x_test, y_test)


# Visualise 10 items from the dataset about to train
def see_samples(x, y):
    for i in range(10):
        win_name = "y = " + str(y[i])
        cv2.imshow(win_name, x[i])
        cv2.waitKey()
        cv2.destroyWindow(win_name)


# Returns list of tuples:
def load_our_dataset(dataset='combination', exclude=None):

    # Read the Directories with the CHAR74k images stored
    sorted_tuples = read_dirs()

    # Scramble their order
    unsorted_tuples = scramble_dataset(sorted_tuples)

    if dataset is 'combination':
        return split_dataset(unsorted_tuples, combined=True, exclude_label=exclude)
    if dataset is 'char74k':
        return split_dataset(unsorted_tuples, combined=False, exclude_label=exclude)
    if dataset is 'mnist':
        if exclude is not None:
            (x_train, y_train), (x_test, y_test) = mnist.load_data()
            x_train, y_train, x_test, y_test = exclusions(exclude, x_train, y_train, x_test, y_test)
            return (x_train, y_train), (x_test, y_test)
        else:
            return mnist.load_data()
