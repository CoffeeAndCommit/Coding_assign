import cv2
import sys

def main():
    # Load the image
    image = cv2.imread('example.jpg')
    
    if image is None:
        print("Error: Could not load image. Please ensure 'example.jpg' is placed in your working directory.")
        sys.exit(1)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the grayscale image to 224x224
    resized_image = cv2.resize(gray_image, (224, 224))

    # Display the resized grayscale image in a single window
    cv2.imshow('Processed Image', resized_image)
    print("Press 's' to save the image, or any other key to close without saving.")

    # Wait for a key press
    key = cv2.waitKey(0)  # Wait indefinitely for a key press

    # Check if the "S" key was pressed (ASCII for 's' or 'S')
    if key == ord('s') or key == ord('S'):
        # Save the processed image when "S" is pressed
        cv2.imwrite('grayscale_resized_image.jpg', resized_image)
        print("Image saved as grayscale_resized_image.jpg")
    else:
        print("Image not saved")

    # Close the window
    cv2.destroyAllWindows()

    # Print processed image properties
    print(f"Processed Image Dimensions: {resized_image.shape}")

if __name__ == "__main__":
    main()
