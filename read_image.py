import numpy as np
from PIL import Image


def read_image(image_path):
	"""
	Read image to a PIL image, then we can use im.show() or just im 
	(when im.show() not working) to show the image.
	"""
	im = Image.open(image_path)
	return im


def read_image_to_array(image_path):
	"""
	Read image to a PIL image then convert it to an array
	"""
	im = read_image(image_path)
	return np.array(im)


def read_image_from_array(image_array):
	"""
	read image from an numpy array to PIL image.
	"""
	im = Image.fromarray(image_array)
	return im


def resize_image(im, im_size):
	"""
	Resize the PIL image.
	"""
	im_resized = im.resize((im_size, im_size))
	return im_resized


def read_image_cv2(image_path):
	"""
	Read image using cv2, this function returns an array.
	"""
	im = cv2.imread(str(image_path))
	return cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

