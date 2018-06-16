from keras.models import model_from_json
from preparing_dataset import *
import cv2


digit = cv2.imread("/Users/Sam/Desktop/numbers/gray/23.png", 0)

test_th = threshold(digit)


#cv2.imshow("Original", digit)
#cv2.imshow("Thresholded", test_th)

#im_res = test_th.shape[:2]
#print(im_res)


# Saving the network architecture
with open("char74k_architecture.json", "r") as f:
    model = model_from_json(f.read())
model.load_weights("char74k_weights.h5")

# how many, w, h, channel
test_th = test_th.reshape(1, 28, 28, 1)

predictions = model.predict(test_th, verbose=True)

#y_labels = model.predict_classes()

#[, 5, 9]

# [x, x, 2, 3, x, x, x, 4 or 8 or 7, x]

print(predictions)

#cv2.waitKey()
#cv2.destroyAllWindows()
