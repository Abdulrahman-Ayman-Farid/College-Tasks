import cv2
import sys

image_path = r"C:\Users\Lenovo\Downloads\download (3).jpg"

image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not open or find the image at '{image_path}'")
    sys.exit(1)

print(f"Original image size (OpenCV): {image.shape[1]}x{image.shape[0]} (WxH)")

start_y = 50
end_y = 250
start_x = 50
end_x = 250

crop_image = image[start_y : end_y, start_x : end_x]

print(f"Cropped image to [y={start_y}:{end_y}, x={start_x}:{end_x}]")
print(f"New image size: {crop_image.shape[1]}x{crop_image.shape[0]} (WxH)")

cv2.imshow("Task 4: OpenCV Original", image)
cv2.imshow("Task 4: OpenCV Cropped", crop_image)

print("Displaying original and cropped images. Press any key in one of the windows to close.")
cv2.waitKey(0)
cv2.destroyAllWindows()
print("OpenCV windows closed.")