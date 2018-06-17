from keras.models import model_from_json
from preparing_dataset import *
import cv2
from keras import backend as K


cv2.namedWindow('Optimise')

cv2.createTrackbar('Threshold', 'Optimise', 0, 255, nothing)
cv2.createTrackbar('Gauss Blur', 'Optimise', 0, 255, nothing)
cv2.createTrackbar('Blocksize', 'Optimise', 0, 255, nothing)
cv2.createTrackbar('C', 'Optimise', 0, 255, nothing)

img = cv2.imread("/Users/Sam/sudoku-ar/extracted_numbers/only_nums/12.png", 0)

while(1):
    cv2.imshow('Optimise', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    th = cv2.getTrackbarPos('Threshold','Optimise')
    gb = cv2.getTrackbarPos('Gauss Blur','Optimise')
    bs = cv2.getTrackbarPos('Blocksize','Optimise')
    c = cv2.getTrackbarPos('C','Optimise')

    img[:] = [th]

cv2.destroyAllWindows()






"""
input_imgs = []

input_imgs.append(test_th)

input_imgs = np.asanyarray(input_imgs)



# Saving the network architecture
with open("char74k_architecture.json", "r") as f:
    model = model_from_json(f.read())
model.load_weights("char74k_weights.h5")

if K.image_data_format() == 'channels_first':
    x_test = input_imgs.reshape(input_imgs.shape[0], 1, 28, 28)
    input_shape = (1, 28, 28)
else:
    x_test = input_imgs.reshape(input_imgs.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)

x_test = x_test.astype('float32')
x_test /= 255

predictions = model.predict(x_test, verbose=True)
predicted_classes = model.predict_classes(x_test, verbose=True)


print(predictions)
print(predicted_classes)


cv2.waitKey()
cv2.destroyAllWindows()
"""