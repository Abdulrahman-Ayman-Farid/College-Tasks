import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

image_path = r"C:\Users\Lenovo\Downloads\download (1).jpg"

try:
    img = mpimg.imread(image_path)
    
    plt.figure()
    plt.imshow(img)
    
    plt.title('Task 2: Matplotlib Image')
    
    plt.axis('off')
    
    print(f"Displaying '{image_path}' using Matplotlib...")
    
    plt.show()
    
    print("Matplotlib window closed.")

except FileNotFoundError:
    print(f"Error: Could not find the image at '{image_path}'")
    sys.exit(1)