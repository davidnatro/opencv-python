import os
import cv2
import logging

from zipfile import ZipFile
from urllib.request import urlretrieve

import matplotlib.pyplot as plt


def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assests....", end="")

    # Downloading zip file using urllib package.
    urlretrieve(url, save_path)

    try:
        # Extracting zip file using the zipfile package.
        with ZipFile(save_path) as z:
            # Extract ZIP file contents in the same directory.
            z.extractall(os.path.split(save_path)[0])

        print("Done")

    except Exception as e:
        print("\nInvalid file.", e)


def files(path):
    url = r"https://www.dropbox.com/s/rys6f1vprily2bg/opencv_bootcamp_assets_NB2.zip?dl=1"

    asset_zip_path = os.path.join(path, f"opencv_bootcamp_assets_NB2.zip")

    if not os.path.exists(asset_zip_path):
        download_and_unzip(url, asset_zip_path)


def modify_pixels():
    img_bgr = cv2.imread("checkerboard_18x18.png", cv2.IMREAD_GRAYSCALE)
    img_bgr[2:3, 2:3] = 200

    plt.imshow(img_bgr, cmap="gray")
    plt.show()


def main():
    path = os.getcwd()
    print(f"Starting opencv... {cv2.__version__}; {path}")
    files(path)

    modify_pixels()


if __name__ == "__main__":
    main()
