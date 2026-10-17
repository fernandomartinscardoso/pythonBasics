"""Capture a picture from a webcam on Ubuntu."""

import sys
from pathlib import Path

import cv2


OUTPUT_PATH = Path("qpython.jpg")


def main() -> int:
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Could not open the default camera. Check that it is connected and available.")
        camera.release()
        return 1

    try:
        print("Camera preview opened. Press SPACE to capture or Q/Esc to cancel.")
        while True:
            success, frame = camera.read()
            if not success:
                print("Could not read a frame from the camera.")
                return 1

            cv2.imshow("Camera capture", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord(" "):
                if not cv2.imwrite(str(OUTPUT_PATH), frame):
                    print(f"Could not save the picture to {OUTPUT_PATH}.")
                    return 1
                print(f"Picture saved to {OUTPUT_PATH.resolve()}")
                return 0
            if key in (ord("q"), 27):
                print("Capture cancelled.")
                return 0
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    sys.exit(main())
