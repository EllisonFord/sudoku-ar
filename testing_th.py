from preparing_dataset import *


# PREPARING THE WINDOW
kNW_FindParams = 'Optimise'
cv2.namedWindow(kNW_FindParams)
cv2.resizeWindow(kNW_FindParams, 400, 400)

# CREATING THE TRACKBARS
cv2.createTrackbar('Gauss Blur', kNW_FindParams, 0, 255, nothing)
cv2.createTrackbar('Threshold', kNW_FindParams, 0, 255, nothing)
cv2.createTrackbar('Blocksize', kNW_FindParams, 0, 255, nothing)
cv2.createTrackbar('C', kNW_FindParams, 0, 255, nothing)

# LOAD AN IMAGE
img = cv2.imread("/home/master/sudoku-ar/extracted_numbers/only_nums/12.png", 0)

# START THE SLIDER
while(1):

    # Get current positions of four trackbars
    gb = cv2.getTrackbarPos('Gauss Blur', kNW_FindParams)
    th = cv2.getTrackbarPos('Threshold', kNW_FindParams)
    bs = cv2.getTrackbarPos('Blocksize', kNW_FindParams)
    c = cv2.getTrackbarPos('C', kNW_FindParams)


    #cv2.

    ret, thresh = cv2.threshold(img, th, 255, cv2.THRESH_BINARY_INV)
    #thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, bs, c)



    cv2.imshow(kNW_FindParams, thresh)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break



    #img[:] = [th]

cv2.destroyAllWindows()





"""
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
"""
