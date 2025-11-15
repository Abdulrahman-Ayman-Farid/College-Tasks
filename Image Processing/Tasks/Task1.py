import cv2
import sys

image_path = r'C:\Users\Lenovo\Downloads\download.jpg' 

image = cv2.imread(image_path, 1)


if image is None:
    print(f"Error: Could not open or find the image at '{image_path}'")
    print("Please make sure the image file exists and is in the correct path.")
    sys.exit(1) #


window_name = 'Task 1: OpenCV Image'


cv2.imshow(window_name, image)

print(f"Displaying '{image_path}'. Press any key in the 'Task 1' window to close it.")


cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()

print("OpenCV windows closed.")