import cv2
import matplotlib.pyplot as plt
import sys

img1_path = r"D:\Engeenering Faculty\Level 3\Sem1\Digital Image Processing\Assets\Image A.png"
img2_path = r"D:\Engeenering Faculty\Level 3\Sem1\Digital Image Processing\Assets\Image B.png"

try:
    img1_sub = cv2.imread(img1_path, 0)
    img2_sub = cv2.imread(img2_path, 0)

    if img1_sub is None:
        raise FileNotFoundError(f"Could not read image 1 at {img1_path}")
    if img2_sub is None:
        raise FileNotFoundError(f"Could not read image 2 at {img2_path}")
    
    if img1_sub.shape != img2_sub.shape:
        print(f"Warning: Images are not the same size. Resizing image 2 to match image 1.")
        height, width = img1_sub.shape
        img2_sub = cv2.resize(img2_sub, (width, height))

    changes = cv2.subtract(img1_sub, img2_sub)

    plt.figure(figsize=(18, 10))
    plt.subplot(1, 3, 1)
    plt.imshow(img1_sub, cmap='gray')
    plt.title('Image 1')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(img2_sub, cmap='gray')
    plt.title('Image 2')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(changes, cmap='gray')
    plt.title('cv2.subtract(Img1, Img2)')
    plt.axis('off')
    
    print(f"Displaying {img1_path}, {img2_path}, and their difference.")
    plt.show()
    print("Plot window closed.")

except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please make sure your image paths are correct.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)