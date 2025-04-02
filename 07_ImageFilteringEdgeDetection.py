import cv2  # Import OpenCV library for computer vision tasks
import sys  # Import sys module to handle command-line arguments
import numpy  # Import NumPy for numerical operations

# Define constants for different image filters/modes
PREVIEW  = 0  # Preview Mode: Show the raw camera feed
BLUR     = 1  # Blurring Filter: Apply a blur effect to the frame
FEATURES = 2  # Corner Feature Detector: Detect corners in the frame
CANNY    = 3  # Canny Edge Detector: Detect edges in the frame
BILATERAL = 4  # Bilateral Filter: Edge-preserving smoothing filter

# Parameters for the corner feature detector (cv2.goodFeaturesToTrack)
feature_params = dict(
    maxCorners=1000,      # Maximum number of corners to detect
    qualityLevel=0.5,    # Quality level for corner detection (higher values mean stricter criteria)
    minDistance=10,      # Minimum distance between detected corners
    blockSize=8          # Size of the averaging block used for corner detection
)

# Default camera index (usually the built-in webcam)
s = 0 
# Check if a camera index is provided as a command-line argument
if len(sys.argv) > 1:  
    # Use the provided camera index
    s = int(sys.argv[1])  

# Start in Preview mode
image_filter = PREVIEW 
# Flag to keep the main loop running
alive = True  

# Name of the OpenCV window
win_name = "Camera Filters"  
# Create a resizable OpenCV window
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL) 
# Variable to store the processed frame 
result = None

# Initialize video capture from the specified camera index
source = cv2.VideoCapture(s)  

# Main loop to process frames
while alive:  
    # Read a frame from the camera
    has_frame, frame = source.read()  
    # If no frame is read (e.g., camera disconnected), exit the loop
    if not has_frame: 
        break

    # Flip the frame horizontally (mirror effect)
    frame = cv2.flip(frame, 1) 

    # If in Preview mode, show the raw frame
    if image_filter == PREVIEW: 
        result = frame
    # If in Canny Edge Detector mode
    elif image_filter == CANNY:
        low_treshold = 70  
        high_treshold = 200
        result = cv2.Canny(frame, low_treshold, high_treshold) 
    # If in Blur mode
    elif image_filter == BLUR:  
        kernel_size = (30, 30)
        result = cv2.blur(frame, kernel_size) 
    # If in Corner Feature Detector mode
    elif image_filter == FEATURES:
        # Start with the original frame  
        result = frame  
        # Convert frame to grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect corners 
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
        # If corners are detected  
        if corners is not None:  
            # Iterate over detected corners
            for x, y in numpy.float32(corners).reshape(-1, 2):  
                # Draw circles at corner locations
                center = (int(x), int(y))
                radius = 10
                color = (0, 255, 0)
                thickness = 1
                cv2.circle(result, center, radius, color, thickness)  
    # If in Bilateral Blur mode
    elif image_filter == BILATERAL:
        d = 15  # Diameter of each pixel neighborhood
        sigma_color = 75  # Filter sigma in the color space
        sigma_space = 75  # Filter sigma in the coordinate space
        result = cv2.bilateralFilter(frame, d, sigma_color, sigma_space)

    cv2.imshow(win_name, result)  # Display the processed frame in the OpenCV window

    # Wait for a key press for 1 ms
    key = cv2.waitKey(1)  
    # Exit if 'Q', 'q', or Esc is pressed
    if key == ord("Q") or key == ord("q") or key == 27:  
        alive = False
    # Switch to Canny Edge Detector mode if 'C' or 'c' is pressed
    elif key == ord("C") or key == ord("c"):  
        image_filter = CANNY
    # Switch to Blur mode if 'B' or 'b' is pressed
    elif key == ord("B") or key == ord("b"): 
        image_filter = BLUR
    # Switch to Bilateral Blur mode if 'L' or 'l' is pressed
    elif key == ord("L") or key == ord("l"): 
        image_filter = BILATERAL
    # Switch to Corner Feature Detector mode if 'F' or 'f' is pressed
    elif key == ord("F") or key == ord("f"):  
        image_filter = FEATURES
    # Switch to Preview mode if 'P' or 'p' is pressed
    elif key == ord("P") or key == ord("p"):  
        image_filter = PREVIEW

# Release the camera resource
source.release() 
# Close the OpenCV window 
cv2.destroyWindow(win_name)  