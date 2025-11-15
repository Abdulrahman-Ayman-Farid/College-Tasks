import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

img1_path = r"D:\Engeenering Faculty\Level 3\Sem1\Digital Image Processing\Assets\ImageC.png"
img2_path = r"D:\Engeenering Faculty\Level 3\Sem1\Digital Image Processing\Assets\ImageD.png"

try:
    img1 = cv2.imread(img1_path, 0)
    img2 = cv2.imread(img2_path, 0)

    if img1 is None:
        raise FileNotFoundError(f"Could not read image 1 at {img1_path}")
    if img2 is None:
        raise FileNotFoundError(f"Could not read image 2 at {img2_path}")
    if img1.shape != img2.shape:
        print(f"Warning: Images are not the same size. Resizing image 2 to match image 1.")
        height, width = img1.shape
        img2 = cv2.resize(img2, (width, height))
        
    img1_float = img1.astype(np.float32)
    img2_float = img2.astype(np.float32)   
    epsilon = 1e-5    
    result_div = img1_float / (img2_float + epsilon)   
    result_norm = cv2.normalize(result_div, None, 0, 255, cv2.NORM_MINMAX)
    result_norm = result_norm.astype(np.uint8)

    plt.figure(figsize=(18, 10))
    plt.subplot(1, 3, 1)
    plt.imshow(img1, cmap='gray')
    plt.title('Image 1 (Original)')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(img2, cmap='gray')
    plt.title('Image 2 (Illumination)')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(result_norm, cmap='gray')
    plt.title('Image 1 / Image 2 (Corrected)')
    plt.axis('off')
    
    print(f"Displaying {img1_path}, {img2_path}, and their division.")
    plt.show()
    print("Plot window closed.")

except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please make sure your image paths are correct.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)