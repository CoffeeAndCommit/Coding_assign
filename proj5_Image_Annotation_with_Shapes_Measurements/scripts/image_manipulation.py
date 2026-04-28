import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

def main():
    """
    Image Manipulation Challenge
    
    Description of Changes:
    For this portfolio transformation, we first converted the image to grayscale to emphasize lighting and contrast. 
    Next, we cropped the image to highlight the core subject and rotated the original image by 45 degrees to add dynamic alignment. 
    Finally, we brightened the image by 50 units to give it a more vibrant and appealing look suitable for a photography portfolio.
    """
    
    # Define directories relative to where this script is located
    # This assumes the script is in the "scripts" folder, and original_images/output_images are in the parent folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(script_dir, ".."))
    
    original_images_dir = os.path.join(project_dir, 'original_images')
    output_images_dir = os.path.join(project_dir, 'output_images')
    
    # Ensure output directory exists, if not create it
    if not os.path.exists(output_images_dir):
        os.makedirs(output_images_dir)

    # 1. Load the Image from the original_images folder
    image_path = os.path.join(original_images_dir, 'example.jpg')
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Could not load image from '{image_path}'.")
        print("Please ensure you have created an 'original_images' folder and placed 'example.jpg' inside it.")
        sys.exit(1)

    print("Image loaded successfully.")

    # 2. Convert the Image to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3. Display the Grayscale Image
    plt.figure(figsize=(6, 6))
    plt.imshow(gray_image, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')
    plt.show() # NOTE: You will need to close the plot window for the script to continue saving files.

    # Save Grayscale Image
    gray_out_path = os.path.join(output_images_dir, 'grayscale_image.jpg')
    cv2.imwrite(gray_out_path, gray_image)
    print(f"Saved: {gray_out_path}")

    # 4. Crop the Image
    # Adding a safeguard for image dimensions in case the image is smaller than the crop region
    h, w = image.shape[:2]
    if h >= 300 and w >= 400:
        cropped_image = image[100:300, 200:400]
    else:
        cropped_image = image[0:min(200, h), 0:min(200, w)] # Fallback crop
    
    # Save Cropped Image
    crop_out_path = os.path.join(output_images_dir, 'cropped_image.jpg')
    cv2.imwrite(crop_out_path, cropped_image)
    print(f"Saved: {crop_out_path}")

    # 5. Rotate the Image
    # Create a rotation matrix using cv2.getRotationMatrix2D() to rotate the image by 45 degrees
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0)
    
    # Apply the rotation with cv2.warpAffine()
    rotated_image = cv2.warpAffine(image, M, (w, h))
    
    # Save Rotated Image
    rotate_out_path = os.path.join(output_images_dir, 'rotated_image.jpg')
    cv2.imwrite(rotate_out_path, rotated_image)
    print(f"Saved: {rotate_out_path}")

    # 6. Adjust the Brightness
    # Use np.ones() to create a matrix to increase the brightness by a fixed amount (50)
    brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
    
    # Add the matrix to the image using cv2.add()
    brightened_image = cv2.add(image, brightness_matrix)
    
    # Save Brightened Image
    bright_out_path = os.path.join(output_images_dir, 'brightened_image.jpg')
    cv2.imwrite(bright_out_path, brightened_image)
    print(f"Saved: {bright_out_path}")

    print("\nSuccess! All transformed images have been processed and saved.")

if __name__ == "__main__":
    main()
