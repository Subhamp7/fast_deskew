#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Subham Prasad
"""


"""
importing required libraries
"""
try:
    import cv2
    import numpy as np
    from scipy.ndimage import interpolation as inter
except Exception as e:
    print("Please make sure all the dependencies are installed :",e)


def find_score(arr, angle):
    """

    Parameters
    ----------
    arr : array,
        binary image as 2 dimensional array.
    angle : float or int,
        angle at which the image has to be deskewed.

    Returns
    -------
    score : float or int,
        check for the score at the given input angle and returns the angle.

    DESCRIPTION
    -----------
    Using interpolation from scipy we calculate the hist score for
            the provided angle.

    """
    data = inter.rotate(arr, angle, reshape=False, order=0)
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:] - hist[:-1]) ** 2)
    return score



def image_binary(image_convert):
    """


    Parameters
    ----------
    image_convert : array
        Image as 2 dimensional array.

    Returns
    -------
    image_bina : array
        Image as 2 dimensional array.

    DESCRIPTION
    -----------
    It converts the image into binary 1 and 0, with threshold of a
                a pixel as 125.

    """

    image_bit=cv2.bitwise_not(image_convert)
    _, image_bina = cv2.threshold(image_bit, 125, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    image_bina=image_bina/255.0
    return image_bina


def deskew_image(img_input, array = True, delta = 0.5, limit = 5):
    """


    Parameters
    ----------
    img_input : array or image path
        image array is passed if the image is already converted to an array,
        else image path is provided with array argument as false.
    array : Boolean, optional
        Send True if passing an image array or pass false if passing a file path. The default is True.
    delta : TYPE, optional
        DESCRIPTION. The default is 0.5.
    limit : TYPE, optional
        DESCRIPTION. The default is 5.

    Returns
    -------
    array
        gives the deskewed image as array.
    float or int
        gives the best angle at which the image is skewed.

    DESCRIPTION
    -----------
    It calculates the interpolation and find the best angle at which the
                image has to be shifted and then shifts the image.
    """

    try:
        if array == False:
            img_input = cv2.imread(img_input,cv2.IMREAD_GRAYSCALE)
    except AttributeError:
        return img_input, 0
    image_original=img_input.copy()
    image_skew=cv2.resize(img_input,(int(img_input.shape[1]*0.5),int(img_input.shape[0]*0.5)))
    angles = np.arange(-limit, limit + delta, delta)
    scores = [find_score(image_binary(image_skew),angle) for angle in angles]
    best_angle = angles[scores.index(max(scores))]
    image_inv=image_binary(image_original)
    data = inter.rotate(image_inv, best_angle, reshape=False, order=0)
    image_skewed=((~data.astype(bool)).astype(int))*255
    return image_skewed, best_angle
