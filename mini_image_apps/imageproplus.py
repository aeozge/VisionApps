# import required libraries

import cv2
import argparse
import numpy as np
import imutils


# construct the argument parser and parse the argument

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "It's path to the image")
args= vars(ap.parse_args())


# create menu

def menu():
	print (15 * "*", "MENU", 15 * "*")
	print ("** 1 Show the image               **")
	print ("** 2 Resize the image             **")
	print ("** 3 Open webcam and take a photo **")
	print ("** 4 Rotate the image             **")
	print ("** 5 Flip the image               **")
	print ("** 6 Filter the image             **")
	print ("** 7 Exit from the menu           **")
	print (36 * "*")

# read the image

image = cv2.imread(args["image"])

# If you'd like to resize your image
# resize the image

r = 1000.0/image.shape[1]
dim = (1000, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)


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
		#menu()

	elif(choice == "2"):
		print ("Menu 2 has been selected")

		# show the resized image

		cv2.imshow("Resized Image", resized)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.waitKey(0)
		#menu()


	elif(choice == "3"):
		print ("Menu 3 has been selected")

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
				img_name = "newcapturedpicture.jpg".format(image_counter)
				cv2.imwrite(img_name, frame)
				print ("{} written!".format(img_name))

				image_counter += 1

		camera.release()

		cv2.destroyAllWindows()
		
		cv2.waitKey(0)
		#menu()

	elif(choice == "4"):
		print ("Menu 4 has been selected")

		# this menu for choosing to rotate the image as left or right

		def menu_rotate():
			print (15 * "-", "Menu Rotate", 15 * "-")
			print("Rotate the image to the left, press L")
			print("Rotate the image to the right, press R")
			print("Press 'e' for exit")
			print (36 * "-")

		loop = True

		while loop:
			menu_rotate()
			choice = input("Enter your choice : ")


			# left rotation

			if (choice == "l"):
				for angle in np.arange(0, 180, 90):
					rotated = imutils.rotate(resized, angle)
					cv2.imshow("Rotated Left ", rotated)
					cv2.waitKey(0)
					cv2.destroyAllWindows()

				break
				menu()


			# right rotation

			elif(choice == "r"):
				for angle in np.arange(0, 180, 90):
					rotated = imutils.rotate_bound(resized, angle)
					cv2.imshow("Rotated Right", rotated)
					cv2.waitKey(0)
					cv2.destroyAllWindows()
				break
				menu()  

			elif(choice == "e"):
				print ("Existing...")
				break

			else:
				print("Wrong option selection.")

		cv2.waitKey(0)
		cv2.destroyAllWindows()

	
	elif(choice == "5"):
		print("Menu 5 has been selected")

		# this menu for choosing to flip the image as left - right - down - up

		def menu_flip():
			print (15 * "-", "MENU FLIP", 15 * "-")
			print("Flip the image to the left, press L")
			print("Flip the image to the right, press R")
			print("Flip the image to the down, press D")
			print("Flip the image to the up, press u")
			print("Press 'e' for exit")
			print (36 * "-")

		loop = True

		while loop:
			menu_flip()
			choice = input("Enter your choice : ")

			# the flip() function which allows for flipping the image horizontally, vertically, or both.

			if(choice == "l"):
				left_flip = cv2.flip(resized, 1);
				cv2.imshow("left flip", left_flip)
				cv2.imshow("original image", resized)
				cv2.waitKey(0)
				cv2.destroyAllWindows()
				break
				menu()

			elif(choice == "r"):
				right_flip = cv2.flip(resized, 1);
				cv2.imshow("right flip", right_flip)
				cv2.imshow("original image", resized)
				cv2.waitKey(0)
				cv2.destroyAllWindows()
				break
				menu()

			elif(choice == "d"):
				#Flip (Mirror) Vertically

				down_flip = cv2.flip(resized, 0);
				cv2.imshow("down flip", down_flip)
				cv2.imshow("original image", resized)
				cv2.waitKey(0)
				cv2.destroyAllWindows()
				break
				menu()

			elif(choice == "u"):
				#Flip (Mirror) Vertically

				up_flip = cv2.flip(resized, 0);
				cv2.imshow("up flip", up_flip)
				cv2.imshow("original image", resized)
				cv2.waitKey(0)
				cv2.destroyAllWindows()
				break
				menu()

			elif(choice == "e"):
				print ("Existing...")
				break

			else:
				print("Wrong option selection.")

		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.waitKey(0)
		

	

	elif(choice == "6"):
		print("Menu 6 has been selected")

		# this menu will apply the filters on the images

		def menu_filter():
			print (15 * "-", "MENU FILTER", 15 * "-")
			print("1) Blur Filter")
			print("2) Vignettte Filter")
			print("3) GrayScale Filter")
			print("4) Red Filter")
			print("5) Blue Filter")
			print("6) Green Filter")
			print("Press 'e' for exit")
			print (36 * "-")

		loop = True

		while loop:
			menu_filter()
			choice = input("Enter your choice : ")
			

			if(choice == "1"):
				print("You've chosen blur filter")

				#Blurring image

				blurImg = cv2.blur(resized,(10,10))
				cv2.imshow('blurred image', blurImg)
				cv2.waitKey(0) 
				cv2.destroyAllWindows()
				break
				menu() 

			elif(choice == "2"):
				print("You've chosen Vignette filter")
				rows, cols = resized.shape[:2]

				# generating vignette mask using Gaussian kernels

				kernel_x = cv2.getGaussianKernel(cols,200)
				kernel_y = cv2.getGaussianKernel(rows,200)
				kernel = kernel_y * kernel_x.T
				mask = 255 * kernel / np.linalg.norm(kernel)


				def vignette_menu():
					print (15 * "-", "VIGNETTE FILTER", 15 * "-")
					print("1) Yellow vignette Filter")
					print("2) Purple vignette Filter")
					print("3) Blue vignette Filter")
					print("Press 'e' for exit")
					print (36 * "-")

				loop = True

				while loop:
					vignette_menu()
					choice = input("Enter your choice : ")

					if(choice == "1"):
						print("You've chosen Yellow Vignette filter")
						yellow = np.copy(resized)

						# applying the mask to the image

						yellow[:,:,0] = yellow[:,:,0] * mask
						cv2.imshow('Yellow Filter', yellow)
						cv2.waitKey(0)
						cv2.destroyAllWindows()
						break
						menu()

					elif(choice == "2"):
						print("You've chosen Purple Vignette filter")
						purple = np.copy(resized)

						# applying the mast to the image

						purple[:,:,1] = purple[:,:,1] * mask
						cv2.imshow('Purple Filter',purple)
						cv2.waitKey(0)
						cv2.destroyAllWindows()
						break
						menu()

					elif(choice == "3"):
						print("You've chosen Blue Vignette filter")
						blue = np.copy(resized)

						# applying the mast to the image

						blue[:,:,2] = blue[:,:,2] * mask
						cv2.imshow('Blue Filter',blue)
						cv2.waitKey(0)
						cv2.destroyAllWindows()
						break
						menu()

				cv2.waitKey(0)
				cv2.destroyAllWindows()
				cv2.waitKey(0)

				
			elif(choice == "3"):
				print ("Convert image color to grayscale ")

				# convert RGB image to GrayScale image
				# the formula for grayscale is C = 0.2126 R + 0.7152 G + 0.0722 B

				def gray_convert(resized):
					grayValue = 0.0722 * resized[:,:,2] + 0.7152 * resized[:,:,1] + 0.2126 * resized[:,:,0]
					gray_img = grayValue.astype(np.uint8)
					return gray_img

				gray = gray_convert(resized)

				# show the converted image
				cv2.imshow("GrayScale image", gray)
				cv2.waitKey(0)
				cv2.destroyAllWindows()
				break
				menu()

			elif(choice == "4"):
				print ("Applying red color filter : ")

				r = resized.copy()

				# set blue and green channels to 0

				r[:, :, 0] = 0
				r[:, :, 1] = 0

				# RGB - Red

				cv2.imshow('R-RGB', r)

				cv2.waitKey(0)
				cv2.destroyAllWindows()
				break
				menu()

			elif(choice == "5"):
				print("Applying blue color filter : ")
				b = resized.copy()

				# set green and red channels to 0

				b[:, :, 1] = 0
				b[:, :, 2] = 0

				# RGB - Blue

				cv2.imshow('B-RGB', b)
				
				cv2.waitKey(0)
				cv2.destroyAllWindows()
				break
				menu()

			elif(choice == "6"):
				print("Applying green color filter : ")
				g = resized.copy()

				# set blue and red channels to 0

				g[:, :, 0] = 0
				g[:, :, 2] = 0

				# RGB - Green

				cv2.imshow('G-RGB', g)

				cv2.waitKey(0)
				cv2.destroyAllWindows()
				break
				menu()


			elif(choice == "e"):
				print ("Existing...")
				break

			else:
				print("Wrong option selection.")

		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.waitKey(0)
				

	elif(choice == "7"):
		print ("Menu 7 has been selected")
		print ("Existing...")

		loop = False
		

	else:
		print ("Wrong option selection. Enter any key to try again..")
