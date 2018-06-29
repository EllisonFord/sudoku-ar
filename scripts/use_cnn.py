from keras.models import model_from_json
from preparing_dataset import *
import cv2
from keras import backend as k
import glob
from params import *
import os

dir_path = os.path.dirname(__file__)

from keras.applications.imagenet_utils import decode_predictions


def read_images(dir):
    test_images = [prepare_image(cv2.imread(file, GRAYSCALE)) for file in glob.glob(dir+"/*.png")]
    return np.asanyarray(test_images)


def predict(input_imgs):

    if k.image_data_format() == 'channels_first':
        x_test = input_imgs.reshape(input_imgs.shape[LEN], 1, digit_w, digit_h)
    else:
        x_test = input_imgs.reshape(input_imgs.shape[LEN], digit_w, digit_h, 1)

    x_test = x_test.astype('float32')
    x_test /= 255

    # LOAD THE NETWORK
    with open(dir_path+"/trained_net/char74k_architecture.json", "r") as f:
        model = model_from_json(f.read())

    # Loading the weights
    model.load_weights(dir_path+"/trained_net/char74k_weights.h5")

    # RUN and KEEP PREDICTIONS
    predicted_classes = model.predict_classes(x_test)

    return predicted_classes


def disp_predictions(input_imgs, predictions):
    # SHOW IMAGES AND PREDICTIONS
    for i, img in enumerate(predictions):
        win_name = "Prediction: " + str(img)
        cv2.namedWindow(win_name)
        cv2.moveWindow(win_name, 700, 400)
        enlarged_im = cv2.resize(input_imgs[i], (200, 200))
        cv2.imshow(win_name, enlarged_im)
        cv2.waitKey()
        cv2.destroyWindow(win_name)


#  Takes in imags list, returns predicted classes
def cpp_sudoku_call(imgs_list):
    th_imgs = [prepare_image(cv2.imread(im, GRAYSCALE)) for im in imgs_list]
    predicted_classes = predict(th_imgs)

    print(type(predicted_classes))

    return predicted_classes


def test_predictions(dir="../extracted_numbers/gray"):
    # PROCESS THE IMAGES
    imgs_array = read_images(dir)
    prediction = predict(imgs_array)
    disp_predictions(imgs_array, prediction)


#test_predictions(dir="../extracted_numbers/gray")

#im_list = read_images()

#cpp_sudoku_call()

""" 
EXTRA CODE
#predictions = model.predict(x_test, verbose=True)

"""
