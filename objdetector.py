from ultralytics import YOLO
import cv2
import os
import argparse
from consts import NAMES


def main():
    object_to_search, dir_path, verbose, show, advanced = menu(NAMES)
    if object_to_search not in NAMES.values():
        exit_program()
    screenshots_count = 0

    # Search recursively png files in folder
    for foldername, subfolders, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if filename.endswith(".png"):
                # Load the chosen YOLO model
                if advanced:
                    model = YOLO('yolov8l.pt')
                else:
                    model = YOLO('yolov8n.pt')
                if show:
                    results = model(f"{file_path}", show=True)
                else:
                    results = model(f"{file_path}")

                output_folder = create_folder(object_to_search)

                # Load the input image
                img = cv2.imread(file_path)

                # Check if the image was loaded successfully
                if img is None:
                    print(f"Error: Unable to load the image from {file_path}")
                else:
                    # Create a counter for object screenshots
                    object_counter = 1

                    for r in results:
                        for box in r.boxes:
                            cls = int(box.cls[0])
                            class_name = NAMES[cls]

                            # Check if the detected object is the object
                            if class_name == object_to_search:
                                # Extract the coordinates of the bounding box
                                x1, y1, x2, y2 = map(int, box.xyxy[0])

                                # Crop the region of interest (ROI) containing the person
                                object_roi = img[y1:y2, x1:x2]

                                # Define a filename for the screenshot
                                screenshot_filename = f'{object_to_search}_{object_counter}{filename[:-4]}.png'

                                # Define the full path to save the screenshot
                                screenshot_path = os.path.join(output_folder, screenshot_filename)

                                # Save the screenshot
                                cv2.imwrite(screenshot_path, object_roi)

                                # Increment the object and screenshot counter
                                object_counter += 1
                                screenshots_count += 1

                    # Print the total number of object screenshots taken for each image in verbose mode
                    if verbose:
                        print(f"Total {object_counter - 1}  {object_to_search} screenshots taken from {file_path}.")
                # cv2.waitKey(0)
                cv2.destroyAllWindows()
    print(f"\nTotal {screenshots_count} screenshots were created in {output_folder}")


def create_folder(Item_to_search):
    # Create a folder to store person screenshots
    output_folder = f"{Item_to_search}_screenshots"
    os.makedirs(output_folder, exist_ok=True)
    return output_folder


def menu(NAMES: dict):
    parser = argparse.ArgumentParser(
        description="Search for an object in png files recursively inside a directory and save screenshots of them ")
    parser.add_argument("object", help=f"The object to search for. objects:{[value for value in NAMES.values()]} ")
    parser.add_argument("dir_path", help="The directory path to search in")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="verbose version")
    parser.add_argument("-s", "--show", action="store_true",
                        help="show each image while searching")
    parser.add_argument("-a", "--advanced", action="store_true",
                        help="advanced search, might take more time")
    args = parser.parse_args()
    return args.object, args.dir_path, args.verbose, args.show, args.advanced


def exit_program():
    print("Invalid object option")
    print("Exit")
    exit()


if __name__ == '__main__':
    main()
