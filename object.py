import numpy as np
import os
import importlib
from keras import backend as k
from keras.preprocessing import image
from keras.applications import mobilenet
from keras.applications import imagenet_utils
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
mobile=mobilenet.MobileNet()
mobile._make_predict_function()
def prepare(file):
	img =image.load_img(file, target_size=(224,224))
	img_array = image.img_to_array(img)
	image_array_expanded_dims = np.expand_dims(img_array, axis=0)
	return(mobilenet.preprocess_input(image_array_expanded_dims))
def itl(path):
	l=[]
	preprocessed_image = prepare(path)
	predictions=mobile.predict(preprocessed_image)
	result=imagenet_utils.decode_predictions(predictions)
	for i in result[0]:
		l.append(i[1])
	return(l)
