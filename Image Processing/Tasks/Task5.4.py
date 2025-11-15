import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

xray_path = r"D:\Engeenering Faculty\Level 3\Sem1\Digital Image Processing\Assets\vagabond.jpg"

try:
    xray = cv2.imread(xray_path, 0)
    if xray is None:
        raise FileNotFoundError(f"Could not read image at {xray_path}")

    mask_xray = np.zeros(xray.shape, dtype="uint8")
    pt1 = (400, 200)
    pt2 = (650, 700)

    h, w = xray.shape
    if pt2[0] > w or pt2[1] > h:
        print(f"Warning: Mask coordinates {pt1}, {pt2} are outside image bounds {w}x{h}.")
    
        pt1 = (min(pt1[0], w), min(pt1[1], h))
        pt2 = (min(pt2[0], w), min(pt2[1], h))
        print(f"Using adjusted coordinates: {pt1}, {pt2}")

    cv2.rectangle(mask_xray, pt1, pt2, 255, -1) 
    masked_xray = cv2.bitwise_and(xray, xray, mask=mask_xray)

    plt.figure(figsize=(18, 10))
    plt.subplot(1, 3, 1)
    plt.imshow(xray, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(mask_xray, cmap='gray')
    plt.title('Mask')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(masked_xray, cmap='gray')
    plt.title('Masked Image (bitwise_and)')
    plt.axis('off')
    
    print(f"Displaying {xray_path}, the generated mask, and the masked result.")
    plt.show()
    print("Plot window closed.")

except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please make sure your image path is correct.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)