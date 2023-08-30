# CE301-Capstone

# Sports Tracking Analysis

## Overview
This project is for CE301 Capstone Project that focuses on the tracking of players movements in sport. In this case Tennis, although other sports with a similar court layout may work. 

- Python (programming language used)
- Use a Multi Pose tracking tool to track players movements on the court
- Create a mini map which shows the players movements on the court
- Create a court detector with Hough Transform and Canny Edge, which can be used for multiple videos on Tennis



## MediaPipe Single Pose Estimation Gif

![MediaPipe_Gif](/uploads/6db50e0d72e4685eddcb0711169b10e7/MediaPipe_Gif.gif)

- Takes a few seconds to detect players
- Only useful for single pose Estimation
- Runs Slow (15FPS), displayed in the top-left corner

## Court detection (not finished)

![court_detection](/uploads/2c7b2be6eae319a4b04fa36710137be1/court_detection.gif)

- Uses OpenCV
- Reads a frame from the video file or camera stream
- Converts to grayscale
- Applies thresholding to remove noise
- Applies morphological operations to remove small holes
- Finds contours in the image
- Shows the image with the detected contours

## Tensorflow MoveNet Pose Estimation

![court_detection_gif](/uploads/6efc4bc4fb58e0656c67985a43a86add/court_detection_gif.gif)

- Used in google Colab so outputs video format frame by frame

## MoveNet and Court detection image

![image_detection_movenet](/uploads/c357d806c6468e50248601f9144e4c0f/image_detection_movenet.PNG)

- implementation of court detection and pose Estimation

## Implementation of map detection (in progress)

![Warped_Image](/uploads/dd963292362382d975a206ef47f0f2f9/Warped_Image.PNG)
