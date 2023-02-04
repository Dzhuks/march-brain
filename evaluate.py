import cv2
import imutils
import numpy as np
from keras.models import load_model
from matplotlib import pyplot as plt

MODEL_PATH = "cnn-parameters-improvement-23-0.91.model"
best_model = load_model(filepath=MODEL_PATH)


def _convert_grayscale(img):
    # Convert the img to grayscale, and blur it slightly
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    return gray


def _clear_img(img):
    # Threshold the img, then perform a series of erosions +
    # dilations to remove any small regions of noise
    thresh = cv2.threshold(img, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    return thresh


def _grab_largest_contour(img):
    cntrs = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntrs = imutils.grab_contours(cntrs)
    cntr_max = max(cntrs, key=cv2.contourArea)
    return cntr_max


def crop_brain_contour(img, plot=False):
    # segment the brain from the rest of the img
    gray = _convert_grayscale(img)
    thresh = _clear_img(gray)
    cntr = _grab_largest_contour(thresh)

    # Find the extreme points
    extLeft = tuple(cntr[cntr[:, :, 0].argmin()][0])
    extRight = tuple(cntr[cntr[:, :, 0].argmax()][0])
    extTop = tuple(cntr[cntr[:, :, 1].argmin()][0])
    extBot = tuple(cntr[cntr[:, :, 1].argmax()][0])

    # crop new img out of the original img using the four extreme points (left, right, top, bottom)
    new_img = img[extTop[1]:extBot[1], extLeft[0]:extRight[0]]

    if plot:
        plt.figure()
        plt.subplot(1, 2, 1)
        plt.imshow(img)
        plt.tick_params(axis='both', which='both',
                        top=False, bottom=False, left=False, right=False,
                        labelbottom=False, labeltop=False, labelleft=False, labelright=False)
        plt.title('Original img')

        plt.subplot(1, 2, 2)
        plt.imshow(new_img)
        plt.tick_params(axis='both', which='both',
                        top=False, bottom=False, left=False, right=False,
                        labelbottom=False, labeltop=False, labelleft=False, labelright=False)
        plt.title('Cropped img')
        plt.show()

    return new_img


def predict(filepath):
    img_width, img_height = 240, 240

    img = cv2.imread(filepath)
    img = crop_brain_contour(img, plot=False)
    img = cv2.resize(img, dsize=(img_width, img_height), interpolation=cv2.INTER_CUBIC)
    img = img / 255.  # normalize values

    imgs = np.array([img])
    return best_model.predict(imgs)
