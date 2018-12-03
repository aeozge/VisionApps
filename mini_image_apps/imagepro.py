# import required libraries

import cv2
import argparse
import numpy as np

# construct the argument parser and parse the argument

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "It's path to the image")
args= vars(ap.parse_args())


# create menu

def menu():
	print (15 * "-", "MENU", 15 * "-")
	print ("1)Show the image ")
	print ("2)Resize the image ")
	print ("3)Convert image color to grayscale ")
	print ("4)Open webcam and take a photo ")
	print ("5)Exit from the menu ")
	print (36 * "-")

# read the image

image = cv2.imread(args["image"])

# If you'd like to resize your image
# resize the image

r = 1000.0/image.shape[1]
dim = (1000, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# convert RGB image to GrayScale image
# the formula for grayscale is C = 0.2126 R + 0.7152 G + 0.0722 B

def gray_convert(resized):
	grayValue = 0.0722 * resized[:,:,2] + 0.7152 * resized[:,:,1] + 0.2126 * resized[:,:,0]
	gray_img = grayValue.astype(np.uint8)
	return gray_img

gray = gray_convert(resized)


# it will keep going to show menu until you exit.

loop = True

while loop:
	menu()
	choice = input("Enter your choice : ")

	if(choice == "1"):
		print ("Menu 1 has been selected.")
		# show the original image

		cv2.imshow("Original Image", image)

		# get dimensions of image

		dimensions = image.shape

		# height, width of image
		height = image.shape[0]
		width = image.shape[1]
		print('Image Dimension    : ',dimensions)
		print('Image Height       : ',height)
		print('Image Width        : ',width)

		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.waitKey(0)
		menu()

	elif(choice == "2"):
		print ("Menu 2 has been selected")
		# show the resized image
		cv2.imshow("Resized Image", resized)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.waitKey(0)
		menu()

	elif(choice == "3"):
		print ("Menu 3 has been selected")
		# show the converted image
		cv2.imshow("GrayScale image", gray)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.waitKey(0)
		menu()

	elif(choice == "4"):
		print ("Menu 4 has been selected")
		# open the webcam and take a capture 

		camera = cv2.VideoCapture(0)
		cv2.namedWindow("your image")

		image_counter = 0

		while True:
			ret, frame = camera.read()
			cv2.imshow("your image", frame)
			if not ret:
				break
			k = cv2.waitKey(1)

			if k%256 == 27:
				# ESC pressed
				print ("Escape hit, it's closing...")
				break
            # s pressed
			elif k == ord('s'): 
				img_name = "new captured picture.jpg".format(image_counter)
				cv2.imwrite(img_name, frame)
				print ("{} written!".format(img_name))

				image_counter += 1

		camera.release()

		cv2.destroyAllWindows()
		
		cv2.waitKey(0)
		menu()

	elif(choice == "5"):
		print ("Menu 5 has been selected")
		print ("Existing...")

		loop = False
		

	else:
		print ("Wrong option selection. Enter any key to try again..")
