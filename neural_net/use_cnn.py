from keras.models import model_from_json
from neural_net.preparing_dataset import *
import cv2
from keras import backend as k
import glob
from neural_net.params import *
from keras.applications.imagenet_utils import decode_predictions


def read_images():
    test_images = [prepare_image(cv2.imread(file, 0)) for file in glob.glob("../extracted_numbers/gray/*.png")]
    return np.asanyarray(test_images)


def predict(input_imgs):

    if k.image_data_format() == 'channels_first':
        x_test = input_imgs.reshape(input_imgs.shape[0], 1, digit_w, digit_h)
    else:
        x_test = input_imgs.reshape(input_imgs.shape[0], digit_w, digit_h, 1)

    x_test = x_test.astype('float32')
    x_test /= 255

    # LOAD THE NETWORK
    with open("trained_net/char74k_architecture_comb.json", "r") as f:
        model = model_from_json(f.read())

    # Loading the weights
    model.load_weights("trained_net/char74k_weights_comb.h5")

    # RUN and KEEP PREDICTIONS
    predicted_classes = model.predict_classes(x_test)

    probabilities = model.predict(x_test)

    for item in predicted_classes:
        print(item)

    decode_predictions(probabilities)

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


# PROCESS THE IMAGES
imgs_array = read_images()

prediction = predict(imgs_array)

disp_predictions(imgs_array, prediction)


""" 
EXTRA CODE
#predictions = model.predict(x_test, verbose=True)

"""
