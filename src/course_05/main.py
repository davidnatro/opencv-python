import sys

import cv2


def main():
    s = 0
    if len(sys.argv) > 1:
        s = int(sys.argv[1])

    win_name = "OpenCV Video Capture"
    source = cv2.VideoCapture(s)

    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

    while cv2.waitKey(1) != 27:
        has_frame, frame = source.read()
        if not has_frame:
            break
        cv2.imshow(win_name, frame)

    source.release()
    cv2.destroyWindow(win_name)


if __name__ == "__main__":
    main()
