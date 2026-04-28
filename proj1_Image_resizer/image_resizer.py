import cv2
import sys

def main():
    # 1. Load the specified image
    image_path = 'input_image.jpg'
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not load image at '{image_path}'.")
        print("Please ensure 'input_image.jpg' is placed in your working directory.")
        sys.exit(1)

    print(f"Successfully loaded '{image_path}'.")

    # 2. Resize Image to three different sizes
    small_size = (200, 200)
    medium_size = (400, 400)
    large_size = (600, 600)

    print("Resizing images...")
    img_small = cv2.resize(img, small_size)
    img_medium = cv2.resize(img, medium_size)
    img_large = cv2.resize(img, large_size)

    # 3. Display Resized Images in separate windows
    cv2.imshow('Small Image (200x200)', img_small)
    cv2.imshow('Medium Image (400x400)', img_medium)
    cv2.imshow('Large Image (600x600)', img_large)

    # 4. Save Resized Images with appropriate filenames
    cv2.imwrite('input_image_small.jpg', img_small)
    cv2.imwrite('input_image_medium.jpg', img_medium)
    cv2.imwrite('input_image_large.jpg', img_large)
    
    print("Resized images have been saved as:")
    print("  - input_image_small.jpg")
    print("  - input_image_medium.jpg")
    print("  - input_image_large.jpg")
    
    print("\nPress any key in any of the image windows to close them and exit.")

    # 5. Exit: Close all image windows after displaying
    cv2.waitKey(0) # Wait infinitely until a key is pressed
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
