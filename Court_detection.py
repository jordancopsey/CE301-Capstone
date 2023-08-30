import cv2
import numpy as np

# Open the video file or camera stream
cap = cv2.VideoCapture('Tennish.mp4')

# Loop over the frames
while True:
    # Read a frame from the video file or camera stream
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to remove noise
    thresh = cv2.threshold(gray, 165, 250, cv2.THRESH_BINARY)[1]

    # Apply morphological operations to remove small holes
    kernel = np.ones((1, 1), np.uint8)
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Find contours in the image
    contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # Ignore small contours that are likely noise
        if area < 1000:
            continue

        # Draw the contour on the original image
        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

    # Show the image with the detected contours
    cv2.imshow("Frame", frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release the video file or camera stream and close all windows
cap.release()

cv2.destroyAllWindows()
