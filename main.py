# Import necessary libraries
from cvzone.FaceMeshModule import FaceMeshDetector  # Import the FaceMeshDetector class from cvzone module
import cv2  # Import OpenCV library

# Create a VideoCapture object to capture video from the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Create an instance of the FaceMeshDetector class with a maximum of 2 faces to detect
detector = FaceMeshDetector(maxFaces=2)

# Infinite loop to continuously process frames from the camera
while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # Use the detector to find face meshes in the current frame
    img, faces = detector.findFaceMesh(img)

    # Check if any face meshes are detected
    if faces:
        # Print the face mesh data for the first detected face
        print(faces[0])

    # Display the image with detected face meshes
    cv2.imshow("Image", img)

    # Check if the 'q' key is pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
