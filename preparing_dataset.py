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

def resize(image):
    return cv2.resize(image, (28, 28))

def threshold(image):

    #cv2.imshow("Original in", image)
    #cv2.waitKey(0)

    #th, dst = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
    #cv2.imshow("Thresholded Image", th)
    #cv2.waitKey(0)

    #cv2.imshow("DST Image", dst)
    #cv2.waitKey(0)


    #cv2.destroyAllWindows()
    return image #change to th or whatever

# Resize any image to the constants specified above
def resize_img(input_img):
    return cv2.resize(input_img, (digit_size_px[0], digit_size_px[1]))


# Randomise the list of tuples
def scramble_dataset(list):
    np.random.shuffle(list)
    x = []
    y = []
    for x_item in list:
        x.append(x_item)
    for y_item in list:
        y.append(y_item)
    return np.asanyarray(x)[0], np.asanyarray(y)[0]


# Iterates through the directories and returns pairs of x and y
def read():

    x = []
    y = []

    #some_image = None

    for i in range(0, 9):
        for image in os.listdir(dir_and_digit()[i][0]):
            path = os.path.join(dir_path, "digits/" + str(i+1) + "/" + image)


            image = cv2.imread(path, 0)
            image = resize(image)

            x.append(image)
            y.append(dir_and_digit()[i][1])
            #some_image = image
            #image = threshold(image)
            #x_and_y.append((image, dir_and_digit()[i][1]))

#    threshold(some_image)
    return np.asanyarray(x), np.asanyarray(y)


# Divides the dataset into Training and Test sets and returns (x_train, y_train), (x_test, y_test)
def split_dataset(list_in):
#    print(list_in.shape[0])
#    percent = int(0.75*list_in.shape)
    train, test = list_in[:8000, :], list_in[8000:,:]
    return train, test


# Returns list of tuples:
def load_dataset():
    x, y = read()
    #x, y = scramble_dataset(sorted_tuples)
    #split
    return x, y
