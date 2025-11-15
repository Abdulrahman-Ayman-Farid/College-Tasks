import cv2
from PIL import Image
import sys
import numpy as np


image_path = r"C:\Users\Lenovo\Downloads\download (2).jpg" 

print(f"--- Analyzing Image: {image_path} ---")

# --- Part 1: OpenCV ---
print("\n--- OpenCV Analysis ---")
try:
    im_color = cv2.imread(image_path, 1)
    if im_color is None:
        raise FileNotFoundError(f"OpenCV could not read {image_path}")

    print(f"Type (OpenCV): {type(im_color)}")
    print(f"Color Shape (H, W, C): {im_color.shape}")
    print(f"Shape Type: {type(im_color.shape)}")

    # Unpack color shape
    h, w, c = im_color.shape
    print(f"Color Width:  {w}")
    print(f"Color Height: {h}")
    print(f"Channels: {c}")
    
    im_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if im_gray is None:
        raise FileNotFoundError(f"OpenCV could not read {image_path} as grayscale")
        
    print(f"\nGrayscale Shape (H, W): {im_gray.shape}")
    
    h_g, w_g = im_gray.shape
    print(f"Grayscale Width:  {w_g}")
    print(f"Grayscale Height: {h_g}")

    h_u, w_u = im_color.shape[0], im_color.shape[1]
    print(f"\nUniversal Width (from color):  {w_u}")
    print(f"Universal Height (from color): {h_u}")

    print(f"\n--- Other OpenCV Properties (from color image) ---")
    print(f"Image DType: {im_color.dtype}")
    print(f"Min Pixel Value: {im_color.min()}")
    print(f"Max Pixel Value: {im_color.max()}")
    print(f"Total Pixels (size): {im_color.size}")

except FileNotFoundError as e:
    print(f"Error (OpenCV): {e}")
except Exception as e:
    print(f"An error occurred with OpenCV: {e}")


# --- Part 2: Pillow (PIL) ---
print("\n--- Pillow (PIL) Analysis ---")
try:
    # Read image
    im_pil = Image.open(image_path)
    
    print(f"Type (PIL): {type(im_pil)}")
    print(f"Size (W, H): {im_pil.size}")
    print(f"Size Type: {type(im_pil.size)}")

    # Unpack size
    w_p, h_p = im_pil.size
    print(f"PIL Width (from size):  {w_p}")
    print(f"PIL Height (from size): {h_p}")

    # Get from attributes
    print(f"PIL Width (from .width):  {im_pil.width}")
    print(f"PIL Height (from .height): {im_pil.height}")

    # Other properties from the PDF
    print(f"Image Format: {im_pil.format}")
    print(f"Image Mode: {im_pil.mode}")

except FileNotFoundError:
    print(f"Error (PIL): Could not find the image at '{image_path}'")
except Exception as e:
    print(f"An error occurred with PIL: {e}")

print("\n--- Analysis Complete ---")