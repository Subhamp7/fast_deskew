# fast_deskew
An optimised way to deskew images faster.

• Available on :The Python Package Index (PyPI)  :<br /> https://pypi.org/
## Installation
```pip install fast_deskew```

## How to use it?
import fast_deskew

INPUT_IMAGE_PATH = "example/input_image.png"

img_input = cv2.imread(INPUT_IMAGE_PATH,cv2.IMREAD_GRAYSCALE)

result_image, best_angle = fast_deskew.deskew_image(img_input)

OR 

import fast_deskew

INPUT_IMAGE_PATH = "example/input_image.png"

result_image, best_angle = fast_deskew.deskew_image(INPUT_IMAGE_PATH, False) #0 for image array and 1 for image_path.

<br /> 
<br /> 

## Input Image:

 ![alt tag](https://github.com/Subhamp7/fast_deskew/blob/master/readme_resources/input_image.png)

<br /> 
<br /> 

 ## Output Image:

 ![alt tag](https://github.com/Subhamp7/fast_deskew/blob/master/readme_resources/result_image.png)


 ## License

© 2021 Subham Prasad

This repository is licensed under the MIT license. See LICENSE for details.