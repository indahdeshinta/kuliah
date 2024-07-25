import cv2
image = cv2.imread("asset/2.png")
cv2.imshow("Original Image", image)
cropped = image[230:380,140:470]
cv2.imshow("Crop Image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()