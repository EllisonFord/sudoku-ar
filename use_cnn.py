from keras.models import model_from_json
from preparing_dataset import *
import cv2
from keras import backend as K



#cv2.createTrackbar("Threshold Trackbar", "Thresholded", 100, 255)

digit = cv2.imread("/Users/Sam/Desktop/numbers/gray/23.png", 0)

board = cv2.imread("/Users/Sam/Desktop/sudaca.png", 0)

board = cv2.medianBlur(board, 5)

test_th = threshold(digit)
board_th = threshold(board)


cv2.imshow("Original", digit)
cv2.imshow("Thresholded", test_th)

cv2.imshow("Original Board", board)
cv2.imshow("Thresholded Board", board_th)



# Saving the network architecture
with open("char74k_architecture.json", "r") as f:
    model = model_from_json(f.read())
model.load_weights("char74k_weights.h5")

input_imgs = []


input_imgs.append(test_th)

input_imgs = np.asanyarray(input_imgs)


if K.image_data_format() == 'channels_first':
    x_test = input_imgs.reshape(input_imgs.shape[0], 1, 28, 28)
    input_shape = (1, 28, 28)
else:
    x_test = input_imgs.reshape(input_imgs.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)

x_test = x_test.astype('float32')
x_test /= 255

predictions = model.predict(x_test, verbose=True)
predicted_classes = model.predict_classes(x_test)

print(predictions)
print(predicted_classes)

cv2.waitKey()
cv2.destroyAllWindows()
