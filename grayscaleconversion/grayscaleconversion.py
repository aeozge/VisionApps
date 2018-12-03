#import required libraries

import cv2
import argparse
import numpy as np

#construct the argument parser and parse the argument

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "It's path to the image")
args= vars(ap.parse_args())

#read the image

image = cv2.imread(args["image"])

#If you'd like to resize your image
#resize the image

r = 1000.0/image.shape[1]
dim = (1000, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

#show the original image

cv2.imshow("Original Image", resized)

#convert RGB image to GrayScale image
#the formula for grayscale is C = 0.2126 R + 0.7152 G + 0.0722 B

def gray_convert(resized):
	grayValue = 0.0722 * resized[:,:,2] + 0.7152 * resized[:,:,1] + 0.2126 * resized[:,:,0]
	gray_img = grayValue.astype(np.uint8)
	return gray_img

gray = gray_convert(resized)

#show the converted image

cv2.imshow("GrayScale image", gray)

#save the grayscale image as a new image

cv2.imwrite("new_image.jpg", gray)	

cv2.waitKey(0)
cv2.destroyAllWindows()