from keras.models import model_from_json
from preparing_dataset import *
import cv2
from keras import backend as K
import glob
from keras.datasets import mnist

def read_images():
    test_images = [cv2.imread(file, 0) for file in glob.glob("extracted_numbers/only_nums/*.png")]
    return np.asanyarray(test_images)




"""
cv2.namedWindow('Optimise')

cv2.createTrackbar('Threshold', 'Optimise', 0, 255, nothing)
cv2.createTrackbar('Gauss Blur', 'Optimise', 0, 255, nothing)
cv2.createTrackbar('Blocksize', 'Optimise', 0, 255, nothing)
cv2.createTrackbar('C', 'Optimise', 0, 255, nothing)

img = cv2.imread("/home/master/sudoku-ar/extracted_numbers/only_nums/12.png", 1)

while(1):
    cv2.imshow('Optimise', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    gb = cv2.getTrackbarPos('Gauss Blur','Optimise')
    th = cv2.getTrackbarPos('Threshold','Optimise')
    bs = cv2.getTrackbarPos('Blocksize','Optimise')
    c = cv2.getTrackbarPos('C','Optimise')

    img[:] = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 33, 5)


    #img[:] = [th]

cv2.destroyAllWindows()
"""


# PROCESS THE IMAGES
input_imgs = read_images()

if K.image_data_format() == 'channels_first':
    x_test = input_imgs.reshape(input_imgs.shape[0], 1, digit_w, digit_h)
    input_shape = (1, digit_w, digit_h)
else:
    x_test = input_imgs.reshape(input_imgs.shape[0], digit_w, digit_h, 1)
    input_shape = (digit_w, digit_h, 1)

x_test = x_test.astype('float32')
x_test /= 255


# LOAD THE NETWORK
with open("char74k_architecture.json", "r") as f:
    model = model_from_json(f.read())
# Loading the weights
model.load_weights("char74k_weights.h5")


# RUN PREDICTIONS
predictions = model.predict(x_test, verbose=True)
predicted_classes = model.predict_classes(x_test)

for img in predictions:
    print(img)



cv2.waitKey()
cv2.destroyAllWindows()
