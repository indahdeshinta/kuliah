import cv2
from PIL import Image
image = Image.open("asset/2.png")
image.show()
cropped= (100,40,80,90)
img_crop = image.crop(cropped)
img_crop.show()
