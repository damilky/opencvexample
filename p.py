import cv2
import numpy
import matplotlib.pyplot as plt
import tkinter
def showimage():
	imgfile = 'lion.jpg'
	img = cv2.imread(imgfile,cv2.IMREAD_COLOR)
	
	plt.imshow(img, cmap='gray', interpolation='bicubic')
	plt.xticks([])
	plt.yticks([])
	plt.title('model')
	plt.show()

showimage()
