# Object Detection and Screenshot Generation Tool

This Python script is designed to streamline object detection using the Ultralytics YOLO framework within a directory containing PNG image files. It identifies a user-specified object of interest and captures screenshots of the detected objects, storing them in a designated folder. This tool is versatile and can be used for various purposes, such as data annotation and content analysis.

## Key Features

- Utilizes YOLO (You Only Look Once) for efficient object detection.
- Supports recursive searching within a directory for PNG image files.
- Allows users to specify the object they want to detect.
- Provides options for verbose mode (detailed output) and image display during the search.
- Offers an advanced search option for increased detection accuracy (though it may take longer).
- Automatically creates a folder to store the extracted object screenshots.

## Usage

### Installation

Before running the script, ensure that you have installed the necessary packages using pip:

```bash
pip install ultralytics
pip install opencv-python
```

### Running the Script

```bash
python objdetector.py [-h] [-v] [-s] [-a] object dir_path
```

object_to_search: The object you want to detect and extract screenshots of.
directory_path: The directory where the tool will search for PNG images.
-v (optional): Enables verbose mode for detailed output.
-s (optional): Displays images while searching.
-a (optional): Enables advanced search mode for improved accuracy.
