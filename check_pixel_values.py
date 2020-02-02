import numpy
import cv2
import matplotlib.pyplot as plt

image_path = '/home/hri/Jupyter_Notebooks/dataset/all/images/masks/maskcolor/9.png'
image = cv2.imread(image_path)
image.shape
plt.imshow(image)
plt.show()

image_gray = cv2.imread(image_path,0)
print ("PIXEL VALUES:\n", image_gray[151, 250]) # [151, 250] is a coordinate where a pixel of the object is, background is 0