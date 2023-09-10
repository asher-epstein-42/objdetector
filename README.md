# objdetector
Object Detection and Screenshot Generation Tool
This Python script leverages the Ultralytics YOLO framework to perform object detection within a directory containing PNG image files. It detects a user-specified object of interest and extracts screenshots of the identified objects, saving them in a dedicated folder. This tool is designed to facilitate object search and screenshot generation for various use cases, such as data annotation or content analysis.

Key Features:

Utilizes YOLO (You Only Look Once) for object detection.
Supports recursive search within a directory for PNG image files.
Allows users to specify the object of interest.
Provides options for verbose mode (detailed output) and image display during the search.
Offers an advanced search option for increased accuracy (at the cost of longer processing time).
Automatically creates a folder to store the extracted object screenshots.



Usage:
Installation: Before running the script, make sure to install the required packages using pip:

pip install ultralytics

pip install opencv-python

Specify the object you want to search for.
Provide the directory path where you want to perform the search.
Use optional flags for verbose mode, image display, and advanced search (if needed).
Dependencies:


Usage Example:

python objdetector.py [-h] [-v] [-s] [-a] object dir_path

object_to_search: The object you want to detect and extract screenshots of.
directory_path: The directory where the tool will search for PNG images.
-v (optional): Enables verbose mode for detailed output.
-s (optional): Displays images while searching.
-a (optional): Enables advanced search mode for improved accuracy.
