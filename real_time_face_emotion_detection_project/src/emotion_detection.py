import cv2
import numpy as np
import sys
import os

# Suppress noisy TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

try:
    from tensorflow.keras.models import load_model
    from keras.preprocessing.image import img_to_array
except ImportError:
    print("Error: Required libraries not found.")
    print("Please ensure you have installed TensorFlow and Keras by running:")
    print("pip install keras tensorflow")
    sys.exit(1)

def main():
    # Load the pre-trained Haar Cascade Classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Ensure the model file exists before trying to load it
    model_path = 'emotion_model.h5'
    if not os.path.exists(model_path):
        print(f"Error: Emotion detection model '{model_path}' not found!")
        print("Please download a pre-trained emotion model (e.g., fer2013) and save it as 'emotion_model.h5' in the src folder.")
        sys.exit(1)

    print("Loading the emotion detection model... (This may take a few seconds)")
    emotion_model = load_model(model_path)

    # Define emotion labels (must match the model's training outputs)
    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    # Start video capture from the default webcam
    print("Starting webcam... Press 'q' on the video window to quit.")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        sys.exit(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image from camera.")
            break

        # Convert frame to grayscale (Face detection works better on grayscale)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # For each detected face, perform emotion recognition
        for (x, y, w, h) in faces:
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Extract the ROI (Region of Interest) for emotion detection
            roi_gray = gray[y:y + h, x:x + w]

            try:
                # Resize the face to match the input shape of the emotion model (typically 48x48)
                roi_resized = cv2.resize(roi_gray, (48, 48))
                roi_resized = roi_resized.astype('float32') / 255.0 # Normalize
                roi_resized = img_to_array(roi_resized)
                roi_resized = np.expand_dims(roi_resized, axis=0)
                
                # Predict emotion
                emotion_pred = emotion_model.predict(roi_resized, verbose=0)
                max_index = np.argmax(emotion_pred[0])
                predicted_emotion = emotion_labels[max_index]

                # Display the predicted emotion on the frame
                cv2.putText(frame, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            except Exception as e:
                pass # If resizing or prediction fails (e.g. out of bounds), safely ignore for this frame

        # Display the resulting frame
        cv2.imshow('Face and Emotion Detection', frame)

        # Exit on pressing the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting application...")
            break

    # Release the capture and close any open windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
