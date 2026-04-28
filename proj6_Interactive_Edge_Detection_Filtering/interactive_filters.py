import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    """Interactive activity for edge detection and filtering."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Image '{image_path}' not found!")
        print("Please ensure you have placed an image named 'example.jpg' in the current directory.")
        return

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Displaying Original Grayscale Image... (Close the image window to proceed to the menu)")
    display_image("Original Grayscale Image", gray_image)

    while True:
        print("\nSelect an option:")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gaussian Smoothing")
        print("5. Median Filtering")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Sobel Edge Detection
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
            print("Displaying Sobel Edge Detection... (Close the image window to continue)")
            display_image("Sobel Edge Detection", combined_sobel)

        elif choice == "2":
            # Canny Edge Detection
            print("Adjust thresholds for Canny (default: 100 and 200)")
            try:
                lower_thresh = int(input("Enter Lower threshold: "))
                upper_thresh = int(input("Enter Upper threshold: "))
                edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
                print("Displaying Canny Edge Detection... (Close the image window to continue)")
                display_image("Canny Edge Detection", edges)
            except ValueError:
                print("Invalid input. Please enter integers for thresholds.")

        elif choice == "3":
            # Laplacian Edge Detection
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            print("Displaying Laplacian Edge Detection... (Close the image window to continue)")
            display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))

        elif choice == "4":
            # Gaussian Smoothing
            print("Adjust kernel size for Gaussian blur (must be odd, default: 5)")
            try:
                kernel_size = int(input("Enter kernel size (odd number): "))
                if kernel_size % 2 == 0:
                    print("Kernel size must be an odd number. Using default: 5")
                    kernel_size = 5
                blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
                print("Displaying Gaussian Smoothed Image... (Close the image window to continue)")
                display_image("Gaussian Smoothed Image", blurred)
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == "5":
            # Median Filtering
            print("Adjust kernel size for Median filtering (must be odd, default: 5)")
            try:
                kernel_size = int(input("Enter kernel size (odd number): "))
                if kernel_size % 2 == 0:
                    print("Kernel size must be an odd number. Using default: 5")
                    kernel_size = 5
                median_filtered = cv2.medianBlur(image, kernel_size)
                print("Displaying Median Filtered Image... (Close the image window to continue)")
                display_image("Median Filtered Image", median_filtered)
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == "6":
            # Exit
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    # Provide the path to an image for the activity
    interactive_edge_detection('example.jpg')
