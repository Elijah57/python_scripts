import numpy as np 
import cv2 as cv 
import os 



def sort(path):
	"""
	sorts out files in a path (directory) and 
	returns a list of image files(jpg, png) in the specified path

	Arg(s):
		path- str, the path to the directory 

	Returns:
		list of all the image files in the directory

	"""

	files = os.listdir(path)
	img_files = []

	for file in files:
		if file.endswith("jpg") or file.endswith("png"):
			img_files.append(file)

	return img_files





def Img_resizer(path, name, width= 250 , height=250, ):

	"""Resizes images to a specified dimension
	Args:
		path- str, the path where the image is located
		name- str, the name to save the resized image file
		width- int, default(width=250) resize the image to the width
		height- int, default(height=250) resize the image to the height

	Returns:
		a resized image with the dimensions (width, height) and name= name
	"""

	img = cv.imread(path) #read the image file

	dimension = (width, height) #set the dimension
	img = cv.resize(img, dimension, interpolation= cv.INTER_AREA)
	
	return cv.imwrite(name, img)
	

def run_save(path):

	"""
	Takes path to a directory, resize all the images in that path(directory)
	and save the resized images

	Arg(s):
		path- str, the path to the directory where the images to be resized are

	Return:
		None

	"""
	jpg_files = sort(path)
	print(jpg_files)

	for file in jpg_files:
		route = path + file
		name = file
		Img_resizer(route, name)
		print(f"Image: {file}  path: {route}  has been resized and saved as {file}")

