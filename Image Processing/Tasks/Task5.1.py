import cv2
import matplotlib.pyplot as plt
import sys

# --- User Configuration ---
# IMPORTANT: Replace with paths to your images
image1_path = r"D:\Engeenering Faculty\Level 3\Sem1\Digital Image Processing\Assets\Tom.png"
image2_path = r"D:\Engeenering Faculty\Level 3\Sem1\Digital Image Processing\Assets\Jerry.png"
# --- End Configuration ---

try:
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    if img1 is None:
        raise FileNotFoundError(f"Could not read image 1 at {image1_path}")
    if img2 is None:
        raise FileNotFoundError(f"Could not read image 2 at {image2_path}")

    height, width, _ = img1.shape
    img2_resized = cv2.resize(img2, (width, height))

    img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2_rgb = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2RGB)

    added_image = cv2.add(img1_rgb, img2_rgb)

    # Display the images
    plt.figure(figsize=(18, 10))
    plt.subplot(1, 3, 1)
    plt.imshow(img1_rgb)
    plt.title('Image 1')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(img2_rgb)
    plt.title('Image 2 (Resized)')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(added_image)
    plt.title('cv2.add(Img1, Img2)')
    plt.axis('off')
    
    print(f"Displaying {image1_path}, {image2_path}, and their sum.")
    plt.show()
    print("Plot window closed.")

except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please make sure your image paths are correct.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)