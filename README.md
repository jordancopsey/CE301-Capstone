# CE301-Capstone

# Sports Tracking Analysis

## Overview
This project is for CE301 Capstone Project that focuses on the tracking of players movements in sport. In this case Tennis, although other sports with a similar court layout may work. 

- Python (programming language used)
- Use a Multi Pose tracking tool to track players movements on the court
- Create a mini map which shows the players movements on the court
- Create a court detector with Hough Transform and Canny Edge, which can be used for multiple videos on Tennis



## MediaPipe Single Pose Estimation Gif

![MediaPipe Single Pose Estimation optimised](https://github.com/jordancopsey/CE301-Capstone/assets/77833509/ecafe118-22ca-4595-8141-91db5f14360e)

- Takes a few seconds to detect players
- Only useful for single pose Estimation
- Runs Slow (15FPS), displayed in the top-left corner

## Court detection (not finished)

![court_detection](https://github.com/jordancopsey/CE301-Capstone/assets/77833509/819708a8-7c06-4130-acaf-92f6b473780b)

- Uses OpenCV
- Reads a frame from the video file or camera stream
- Converts to grayscale
- Applies thresholding to remove noise
- Applies morphological operations to remove small holes
- Finds contours in the image
- Shows the image with the detected contours

## Tensorflow MoveNet Pose Estimation

![Tensorflow MoveNet Pose Estimation optimised](https://github.com/jordancopsey/CE301-Capstone/assets/77833509/61841e4e-b775-4f66-8a77-d894081528ce)

- Used in google Colab so outputs video format frame by frame

## MoveNet and Court detection image

![MovenNet and Court Detection Image](https://github.com/jordancopsey/CE301-Capstone/assets/77833509/11f24a10-1e14-47b7-a775-6a1f6f60284b)

- implementation of court detection and pose Estimation

## Implementation of map detection (in progress)

![Map Detection implementation](https://github.com/jordancopsey/CE301-Capstone/assets/77833509/43252314-9a7a-4e9c-bc8f-763b0cc8a659)
