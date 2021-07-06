import cv2
import fast_deskew
print("fas", fast_deskew.__version__)

INPUT_IMAGE_PATH = "input_image.png"

img_input = cv2.imread(INPUT_IMAGE_PATH,cv2.IMREAD_GRAYSCALE)
result_image, best_angle =fast_deskew.deskew_image(img_input)
print('Best angle: {}'.format(best_angle))

result_image, best_angle =fast_deskew.deskew_image(INPUT_IMAGE_PATH, False)
print('Best angle: {}'.format(best_angle))

#cv2.imwrite("result_image.png", result_image)
