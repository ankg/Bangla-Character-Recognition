from skimage import data
import skimage
import PIL
import numpy as np
from PIL import Image
from skimage.transform import rescale,resize

import cPickle
import numpy 
import numpy as np

import os
import sys

def get_image_vector(filename):
# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
	im = Image.open(filename)
	im = im.convert("L")

	out = im.resize((32,32))

	#out.save("abc_modified.jpg")
	result = np.asarray(list(out.getdata()))

	return result
	
if __name__ == '__main__':

	size = 170 #insert size of folder

	classes = []
	for i in range(1,size+1):
		classes.append(i)

	data = []
	labels = []

	for instance in classes:
		foldername = "3.1.3.1/Train/"
		directory = foldername+str(instance)+"/"

		content_list = []

		for root, directories, filenames in os.walk(directory):
			for filename in filenames:
				content_list.append(os.path.join(root,filename))

		for filename in content_list:
			data.append(get_image_vector(filename))
			labels.append(instance)

		print "Successful " + str(instance) 

	data = np.array(data)
	labels = np.array(labels)


	csvfile_train = "train.npy"
	train_file = open(csvfile_train,"w")
	np.save(train_file,data)
	train_file.close()

	csvfile_labels = "labels.npy"
	labels_file = open(csvfile_labels,"w")
	np.save(csvfile_labels,labels)
	labels_file.close()
