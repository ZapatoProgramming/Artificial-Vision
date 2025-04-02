import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


video_input_file_name = "datos/ObjectTracking/formula_1.mp4"


# Function to draw a rectangle on the frame
def drawRectangle(frame, bbox):
    p1 = (int(bbox[0]), int(bbox[1]))  # Top-left corner of the bounding box
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))  # Bottom-right corner of the bounding box
    cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)  # Draw the rectangle on the frame


# Function to display the frame with the bounding box
def displayRectangle(frame, bbox):
    plt.figure(figsize=(20, 10))  # Set the figure size for visualization
    frameCopy = frame.copy()  # Create a copy of the frame to avoid modifying the original
    drawRectangle(frameCopy, bbox)  # Draw the bounding box on the copied frame
    frameCopy = cv2.cvtColor(frameCopy, cv2.COLOR_BGR2RGB)  # Convert the frame from BGR to RGB for proper display
    plt.imshow(frameCopy)  # Display the frame with the bounding box
    plt.axis("off")  # Turn off axis labels


# Function to draw text on the frame
def drawText(frame, txt, location, color=(50, 170, 50)):
    cv2.putText(frame, txt, location, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)  # Add text to the frame


tracker_type = "GOTURN"
tracker = cv2.TrackerGOTURN.create()  # Initialize the GOTURN tracker

video = cv2.VideoCapture(video_input_file_name)  # Open the input video file
ok, frame = video.read()  # Read the first frame of the video

# Check if the video was opened successfully
if not video.isOpened():
    print("Could not open video")
    sys.exit()
elif not ok or frame is None:  # Verify that the first frame was read correctly
    print("Error: Could not read the first frame.")
    sys.exit()
else:
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # Get the video's width
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Get the video's height

video_output_file_name = f"datos/ObjectTracking/Saved/formula_1-{tracker_type}.mp4"
video_out = cv2.VideoWriter(video_output_file_name, cv2.VideoWriter_fourcc(*'avc1'), 10, (width, height))  # Create a video writer object

# Define a bounding box
bbox = (245, 555, 210, 160)  # Initial bounding box coordinates (x, y, width, height)

# Initialize the tracker with the first frame and the bounding box
ok = tracker.init(frame, bbox)

try:
    while True:
        ok, frame = video.read()  # Read the next frame from the video

        if not ok:  # Exit the loop if no more frames are available
            break

        # Start the timer to calculate FPS
        timer = cv2.getTickCount()

        # Update the tracker with the current frame
        ok, bbox = tracker.update(frame)

        # Calculate Frames Per Second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        if np.isinf(fps) or np.isnan(fps):  # Ensure FPS is valid
            fps = 0

        # Draw the bounding box if tracking is successful
        if ok:
            drawRectangle(frame, bbox)
        else:
            drawText(frame, "Tracking failure detected", (80, 140), (0, 0, 255))  # Display a message if tracking fails

        # Display information about the tracker and FPS
        drawText(frame, f"{tracker_type} Tracker", (80, 60))
        drawText(frame, f"FPS : {int(fps)}", (80, 100))

        # Write the processed frame to the output video file
        video_out.write(frame)

finally:
    video.release()  # Release the video capture object
    video_out.release()  # Release the video writer object

print(f"Video saved for {tracker_type}: {video_output_file_name}")  # Print confirmation message