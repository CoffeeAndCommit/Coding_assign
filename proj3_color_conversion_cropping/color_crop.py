import cv2
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

    # 1. Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(6, 6))
    plt.imshow(image_rgb)
    plt.title("RGB Image")
    plt.axis('off') # Hiding axis for better presentation
    plt.show()

    # 2. Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.figure(figsize=(6, 6))
    plt.imshow(gray_image, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')
    plt.show()

    # 3. Cropping the image
    print("Cropping image (rows 100:300, cols 200:400)...")
    
    # We add a small safeguard here just in case the provided image is smaller than the crop region
    h, w = image.shape[:2]
    if h < 300 or w < 400:
        print(f"Warning: The image ({w}x{h}) is smaller than the crop boundaries. Cropping to available size.")
        cropped_image = image[min(100, h):min(300, h), min(200, w):min(400, w)]
    else:
        cropped_image = image[100:300, 200:400]

    # Display the cropped region if it's not empty
    if cropped_image.size > 0:
        cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
        plt.figure(figsize=(4, 4))
        plt.imshow(cropped_rgb)
        plt.title("Cropped Region")
        plt.axis('off')
        plt.show()
    else:
        print("The cropped region is empty because the image was too small.")

if __name__ == "__main__":
    main()
