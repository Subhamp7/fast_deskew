#author: Subham Prasad

"""
importing required libraries
"""
import cv2
import numpy as np
from scipy.ndimage import interpolation as inter


def find_score(arr, angle):
    """
    Input-Image as 2 dimensional array and angle as float or int
    Output- score as int
    function: Using interpolation from scipy we calculate the hist score for
              an certain angle.
    """
    data = inter.rotate(arr, angle, reshape=False, order=0)
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:] - hist[:-1]) ** 2)
    return score

def image_binary(image_convert):
    """
    Input-Image as 2 dimensional array
    Output- Image as 2 dimensional array
    function: It converts the image into binary 1 and 0, with threshold of a
                a pixel as 125.
    """
    image_bit=cv2.bitwise_not(image_convert)
    _, image_bina = cv2.threshold(image_bit, 125, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    image_bina=image_bina/255.0
    return image_bina


def deskew(image_skew, delta = 0.5, limit = 5):
    """
    Input-Image as 2 dimensional array, delta as float or int and limit as float or int
    Output- Image as 2 dimensional deskewed array
    function: It calculates the interpolation and find the best angle at which the
                image has to be shifted and then shifts the image.
    """
    image_original=image_skew.copy()
    image_skew=cv2.resize(image_skew,(int(image_skew.shape[1]*0.5),int(image_skew.shape[0]*0.5)))
    image_bin=image_binary(image_skew)
    angles = np.arange(-limit, limit + delta, delta)
    scores = [find_score(image_bin,angle) for angle in angles]
    best_score = max(scores)
    best_angle = angles[scores.index(best_score)]
    image_inv=image_binary(image_original)
    data = inter.rotate(image_inv, best_angle, reshape=False, order=0)
    image_skewed=((~data.astype(bool)).astype(int))*255
    return image_skewed, best_angle


#test
INPUT_IMAGE_PATH = "input_image.png"
img_input = cv2.imread(INPUT_IMAGE_PATH,cv2.IMREAD_GRAYSCALE)
result_image, best_angle = deskew(img_input)
print('Best angle: {}'.format(best_angle))
cv2.imwrite("result_image.png", result_image)


