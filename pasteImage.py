import cv2
import numpy as np


def cvpaste(img, imgback, x, y, angle, scale):
    # x and y are the distance from the center of the background image

    r = img.shape[0]
    c = img.shape[1]
    rb = imgback.shape[0]
    cb = imgback.shape[1]
    hrb = round(rb/2)
    hcb = round(cb/2)
    hr = round(r/2)
    hc = round(c/2)

    # Copy the forward image and move to the center of the background image
    imgrot = np.zeros((rb, cb, 3), np.uint8)
    imgrot[hrb-hr:hrb+hr, hcb-hc:hcb+hc, :] = img[:hr*2, :hc*2, :]

    # Rotation and scaling
    M = cv2.getRotationMatrix2D((hcb, hrb), angle, scale)
    imgrot = cv2.warpAffine(imgrot, M, (cb, rb))
    # Translation
    M = np.float32([[1, 0, x], [0, 1, y]])
    imgrot = cv2.warpAffine(imgrot, M, (cb, rb))

    # Makeing mask
    imggray = cv2.cvtColor(imgrot, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(imggray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of the forward image in the background image
    img1_bg = cv2.bitwise_and(imgback, imgback, mask=mask_inv)

    # Take only region of the forward image.
    img2_fg = cv2.bitwise_and(imgrot, imgrot, mask=mask)

    # Paste the forward image on the background image
    imgpaste = cv2.add(img1_bg, img2_fg)

    return imgpaste
