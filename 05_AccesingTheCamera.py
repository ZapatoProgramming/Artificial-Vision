# Import the OpenCV library for computer vision tasks
import cv2  
# Import the sys module to handle command-line arguments
import sys  

# Initialize the video source to 0 (default camera)
s = 0 
# Check if additional command-line arguments are provided 
if len(sys.argv) > 1: 
    # Use the first argument as the video source (camera index or file path)
    s = int(sys.argv[1])  

# Create a VideoCapture object to capture video from the specified source
source = cv2.VideoCapture(s)

# Define the name of the window to display the video
win_name = 'Camera Preview'  
# Create a resizable window with the specified name
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# Loop until the user presses the "Escape" key (ASCII code 27)
while cv2.waitKey(1) != 27:  
    # Read a frame from the video source; has_frame indicates success/failure
    has_frame, frame = source.read()  
    # If no frame is captured (e.g., camera disconnected or end of video file)
    if not has_frame:
        # Exit the loop  
        break  
    # Display the captured frame in the named window
    cv2.imshow(win_name, frame) 

# Release the video capture resource (e.g., free the camera or close the video file)
source.release() 
# Close the window and clean up GUI resources
cv2.destroyWindow(win_name) 