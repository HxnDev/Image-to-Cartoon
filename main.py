import cv2      # Install using "pip install opencv-python"

name = input("Enter the name/path of the image (Without extension) = ")
img = cv2.imread(name)  # Read the image

# Getting edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Converting into cartoons
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Displaying all results
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
