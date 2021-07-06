#author: Subham Prasad

"""
importing required libraries
"""
import cv2
import sys
import numpy as np
from sys import argv
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


def deskew_grayscale(image_skew, delta = 0.5, limit = 5):
    """
    Input-Image as 2 dimensional array, delta as float or int and limit as float or int
    Output- Image as 2 dimensional deskewed array
    function: It calculates the interpolation and find the best angle at which the
                image has to be shifted and then shifts the image.
    """
    try:
        print("TESTED1")
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
        print(image_skewed, best_angle)
        return image_skewed, best_angle
    except AttributeError:
        print("OOPS1")
        return image_skew, 0

def deskew_image(image, delta = 0.5, limit = 5):
    """
    Input-Image , delta as float or int and limit as float or int
    Output- Image as 2 dimensional deskewed array
    function: It calculates the interpolation and find the best angle at which the
                image has to be shifted and then shifts the image.
    """
    try:
        print("TESTED")
        img_input_array = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
        image_original=img_input_array.copy()
        image_skew=cv2.resize(img_input_array,(int(img_input_array.shape[1]*0.5),int(img_input_array.shape[0]*0.5)))
        image_bin=image_binary(image_skew)
        angles = np.arange(-limit, limit + delta, delta)
        scores = [find_score(image_bin,angle) for angle in angles]
        best_score = max(scores)
        best_angle = angles[scores.index(best_score)]
        image_inv=image_binary(image_original)
        data = inter.rotate(image_inv, best_angle, reshape=False, order=0)
        image_skewed=((~data.astype(bool)).astype(int))*255
        print(image_skewed, best_angle)
        return image_skewed, best_angle
    except AttributeError:
        print("OOPS")
        return img_input_array, 0

if __name__ == "__main__":
    print("started")
    print(len(sys.argv))
    if len(sys.argv) == 0: 
        print("Please pass the reuqired input data")
    elif len(sys.argv) == 2:
        try:
            input_img= sys.argv[1]
            deskew_grayscale(input_img)
        except IndexError:
            print("Please pass the grayscale image as input")
    elif len(sys.argv) == 3:
        try:
            input_img= sys.argv[1]
            mode = sys.argv[2]
            if mode == "0":
                deskew_grayscale(input_img)
            elif mode == "1":
                deskew_image(input_img)
            else:
                print("Please pass the array/images argument as TRUE or FALSE only")
        except IndexError:
            print("Please pass the grayscale image as input")
    else:
        print("INVALID ARGUMENT PASSED")