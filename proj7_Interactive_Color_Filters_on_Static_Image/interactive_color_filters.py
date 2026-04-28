import cv2
import numpy as np
import sys

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    # Create a copy of the image to avoid modifying the original
    filtered_image = image.copy()
    if filter_type == "red_tint":
        # Remove blue and green channels for red tint
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 0] = 0  # Blue channel to 0
    elif filter_type == "blue_tint":
        # Remove red and green channels for blue tint
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
    elif filter_type == "green_tint":
        # Remove blue and red channels for green tint
        filtered_image[:, :, 0] = 0  # Blue channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
    elif filter_type == "increase_red":
        # Increase the intensity of the red channel
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)  # Increase red channel
    elif filter_type == "decrease_blue":
        # Decrease the intensity of the blue channel
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)  # Decrease blue channel
    return filtered_image

def main():
    # Load the image
    image_path = 'example.jpg'
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Image '{image_path}' not found!")
        print("Please place an 'example.jpg' file in the current working directory.")
        sys.exit(1)

    filter_type = "original"  # Default filter type

    print("Make sure the image window is active (selected) and press the following keys:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("o - Revert to Original")
    print("q - Quit")

    while True:
        # Apply the selected filter
        filtered_image = apply_color_filter(image, filter_type)
        
        # Display the filtered image
        cv2.imshow("Interactive Color Filters - Press 'q' to Quit", filtered_image)
        
        # Wait for key press
        key = cv2.waitKey(0) & 0xFF

        # Map key presses to filters
        if key == ord('r'):
            filter_type = "red_tint"
            print("Applied Red Tint")
        elif key == ord('b'):
            filter_type = "blue_tint"
            print("Applied Blue Tint")
        elif key == ord('g'):
            filter_type = "green_tint"
            print("Applied Green Tint")
        elif key == ord('i'):
            filter_type = "increase_red"
            print("Applied Increase Red Intensity")
        elif key == ord('d'):
            filter_type = "decrease_blue"
            print("Applied Decrease Blue Intensity")
        elif key == ord('o'):
            filter_type = "original"
            print("Reverted to Original Image")
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', 'o', or 'q'.")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
