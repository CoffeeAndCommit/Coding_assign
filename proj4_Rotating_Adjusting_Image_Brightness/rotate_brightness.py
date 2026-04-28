import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    # Load the image
    image_path = 'example.jpg'
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not load image '{image_path}'.")
        print("Please place an 'example.jpg' file in your working directory.")
        sys.exit(1)

    print(f"Successfully loaded '{image_path}'.")

    # 1. Rotate the image by 45 degrees around its center
    print("Applying a 45-degree rotation...")
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0)    # Create the rotation matrix
    rotated = cv2.warpAffine(image, M, (w, h))      # Apply the transformation

    # Convert from BGR (OpenCV) to RGB (Matplotlib)
    rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
    
    plt.figure(figsize=(6, 6))
    plt.imshow(rotated_rgb)
    plt.title("Rotated Image (45 degrees)")
    plt.axis('off')
    plt.show()

    # 2. Increase brightness by adding 50 to all pixel values
    print("Adjusting image brightness...")
    # Use cv2.add to avoid negative values or overflow (it clips max values to 255)
    brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
    brighter = cv2.add(image, brightness_matrix)

    # Convert from BGR (OpenCV) to RGB (Matplotlib)
    brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
    
    plt.figure(figsize=(6, 6))
    plt.imshow(brighter_rgb)
    plt.title("Brighter Image (+50)")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
