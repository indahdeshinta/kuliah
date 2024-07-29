import cv2
import osgit
from datetime import datetime

# Load the image
image = cv2.imread("asset/bg.jpg")

# Convert to grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform thresholding to create a binary image
(thresh, bw) = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)

# Get current timestamp
current_time = datetime.now().strftime('%Y%m%d%H%M%S')

# Define the folder to save images
folder_name = "storage"

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Save the grayscale image with timestamp in filename
gray_filename = os.path.join(folder_name, f"bg_gray_{current_time}.jpg")
cv2.imwrite(gray_filename, grayscale)

# Save the binary image with timestamp in filename
bw_filename = os.path.join(folder_name, f"bg_binary_{current_time}.jpg")
cv2.imwrite(bw_filename, bw)

# Display the original image
cv2.imshow("Original Image", image)

# Display the grayscale image
cv2.imshow("Grayscale", grayscale)

# Display the binary image
cv2.imshow("BW Image", bw)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
