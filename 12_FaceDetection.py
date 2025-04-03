import cv2  # Import OpenCV library for computer vision tasks.
import sys  # Import sys module to access command-line arguments.

s = 0  # Default camera source index (usually 0 for the primary webcam).
if len(sys.argv) > 1:  # Check if a command-line argument is provided.
    s = int(sys.argv[1])  # Use the provided argument as the camera source index.

source = cv2.VideoCapture(s)  # Initialize video capture from the specified camera source.

# Create a named window for displaying the camera preview.
win_name = "Camera Preview"  # Name of the window.
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)  # Create a resizable window.

# Load a pre-trained deep learning model for face detection using Caffe.
net = cv2.dnn.readNetFromCaffe(
    "datos/FaceDetection/deploy.prototxt",  # Path to network architecture file
    "datos/FaceDetection/res10_300x300_ssd_iter_140000_fp16.caffemodel"  # Path to pre-trained weights
)

# Model parameters
in_width = 300  # Input width for the neural network.
in_height = 300  # Input height for the neural network.
mean = [104, 117, 123]  # Mean values for normalization (BGR order).
conf_threshold = 0.7  # Confidence threshold for filtering weak detections.

# Main loop to process frames from the camera until the ESC key (ASCII 27) is pressed.
while cv2.waitKey(1) != 27:
    has_frame, frame = source.read()  # Read a frame from the video source.
    if not has_frame:  # Break the loop if no frame is captured (e.g., camera disconnected).
        break
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally (mirror effect).
    frame_height = frame.shape[0]  # Get the height of the frame.
    frame_width = frame.shape[1]  # Get the width of the frame.

    # Create a 4D blob from the frame for input to the neural network.
    blob = cv2.dnn.blobFromImage(
        frame,  # Input image.
        1.0,  # Scale factor (no scaling in this case).
        (in_width, in_height),  # Target size for the input blob.
        mean,  # Mean values for normalization.
        swapRB=False,  # Do not swap Red and Blue channels.
        crop=False  # Do not crop the image.
    )

    # Set the blob as input to the neural network and perform forward pass.
    net.setInput(blob)  # Set the prepared blob as network input
    detections = net.forward()  # Perform forward pass to get detection results

    # Loop over the detections and draw boxes around detected faces
    for i in range(detections.shape[2]):  # Iterate through all detected objects
        confidence = detections[0, 0, i, 2]  # Get confidence score for this detection
        
        if confidence > conf_threshold:  # Filter weak detections
            # Get coordinates of bounding box (normalized to 0-1)
            x_left_bottom = int(detections[0, 0, i, 3] * frame_width)
            y_left_bottom = int(detections[0, 0, i, 4] * frame_height)
            x_right_top = int(detections[0, 0, i, 5] * frame_width)
            y_right_top = int(detections[0, 0, i, 6] * frame_height)
            
            # Draw rectangle around detected face
            cv2.rectangle(
                frame,  # Image to draw on
                (x_left_bottom, y_left_bottom),  # Bottom-left corner
                (x_right_top, y_right_top),  # Top-right corner
                (0, 255, 0),  # Green color (BGR format)
                2  # Line thickness
            )
            
            # Display confidence score above the box
            label = f"Face: {confidence:.2f}"
            cv2.putText(
                frame,  # Image to draw on
                label,  # Text to display
                (x_left_bottom, y_left_bottom - 10),  # Text position
                cv2.FONT_HERSHEY_SIMPLEX,  # Font type
                0.5,  # Font scale
                (0, 255, 0),  # Text color (green)
                1  # Line thickness
            )

    # Display the resulting frame with detections
    cv2.imshow(win_name, frame)  # Show the processed frame in the window

# Release resources when done
source.release()  # Release the video capture device
cv2.destroyAllWindows()  # Close all OpenCV windows