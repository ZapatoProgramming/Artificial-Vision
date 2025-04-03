# Artificial Vision
This repository contains modified versions of the Jupyter Notebooks and Python scripts from the OpenCV Bootcamp, adapted to a new application scenario with updated data and expanded documentation, all developed for evaluating the Artificial Vision course.

## Important Notes for Running Scripts

### Notebook: **All Notebooks**
Make sure you are using the correct environment on your notebook and have installed the opencv library.
You can do this in Anaconda with the following commands.
1. To create the virtual environment:
``` bash
    conda create --name opencv-env 
```
2. To activate the virtual environment:
``` bash
    conda activate opencv-env 
```
3. To install the OpenCV library:
``` bash
    conda install -c conda-forge opencv
```

### Script: 01_GettingStartedWithImages

**IMPORTANT: Ensure that the other Python environment has the cv2 library installed. This is necessary for the code to run correctly, as it relies on OpenCV functionality.**

To install the OpenCV library, use the following command in your Python environment:

``` bash
pip3 install numpy opencv-python
```

### Script: 05_AccessingTheCamera

When running the 05_AccessingTheCamera script, there are a few essential considerations to ensure proper functionality:

1. Virtual Camera Software (e.g., OBS):
- If a software like OBS that uses a virtual camera is installed, it may override the default camera settings on your system.
As a result, the native camera (e.g., FaceTime HD Camera or built-in webcam) might not be accessible at its default index (0).

2. Specifying the Correct Camera Index:
- To use the correct camera, you need to pass the appropriate camera index as a command-line argument when running the script.
```bash
python3 05_AccessingTheCamera.py <camera_index>
```


### Script: 07_ImageFilteringEdgeDetection

When running the 07_ImageFilteringEdgeDetection script, there are a few essential considerations to ensure proper functionality:

1. Virtual Camera Software (e.g., OBS):
- If a software like OBS that uses a virtual camera is installed, it may override the default camera settings on your system.
As a result, the native camera (e.g., FaceTime HD Camera or built-in webcam) might not be accessible at its default index (0).

2. Specifying the Correct Camera Index:
- To use the correct camera, you need to pass the appropriate camera index as a command-line argument when running the script.
```bash
python3 07_ImageFilteringEdgeDetection.py <camera_index>
```

3. The keys assigned for the different filters are the following:
    - C for Canny filter
    - B for Blur filter
    - L for Bilateral Blur filter
    - F for features filter
    - P for no filter

### Script: 12_FaceDetection.py

When running the 12_FaceDetection.py script, there are a few essential considerations to ensure proper functionality:

1. Virtual Camera Software (e.g., OBS):
- If a software like OBS that uses a virtual camera is installed, it may override the default camera settings on your system.
As a result, the native camera (e.g., FaceTime HD Camera or built-in webcam) might not be accessible at its default index (0).

2. Specifying the Correct Camera Index:
- To use the correct camera, you need to pass the appropriate camera index as a command-line argument when running the script.

```bash
python3 12_FaceDetection.py <camera_index>
```