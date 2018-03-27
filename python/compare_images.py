from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
 
def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
	imageA = cv2.imread(imageA)
	imageB = cv2.imread(imageB)
	imageA=cv2.resize(imageA,(0,0),fx=0.25,fy=0.25)
	imageB=cv2.resize(imageB,(0,0),fx=0.25,fy=0.25)
	m = mse(imageA, imageB)
	return m
	'''
	imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
	imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
	s = ssim(imageA, imageB)
	'''
