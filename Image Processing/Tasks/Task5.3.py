import cv2
import matplotlib.pyplot as plt
import sys
import numpy as np

image_path = r"D:\Engeenering Faculty\Level 3\Sem1\Digital Image Processing\Assets\girl in hat.png"

try:
    img = cv2.imread(image_path, 0)
    
    if img is None:
        raise FileNotFoundError(f"Could not read image at {image_path}")

    sub_opencv = cv2.subtract(img, 128)
    sub_numpy_wrap = img - 128 

    plt.figure(figsize=(18, 10))
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(sub_opencv, cmap='gray', vmin=0, vmax=255)
    plt.title('cv2.subtract(img, 128) (Saturated)')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(sub_numpy_wrap, cmap='gray', vmin=0, vmax=255)
    plt.title('NumPy (img - 128) (Modulo)')
    plt.axis('off')
    
    print(f"Displaying {image_path} and two types of subtraction.")
    plt.show()
    print("Plot window closed.")

except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please make sure your image path is correct.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)