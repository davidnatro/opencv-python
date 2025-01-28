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


def crop():
    img_bgr = cv2.imread("New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    img_rgb_cropped = img_rgb[200:400, 300:600]
    plt.imshow(img_rgb_cropped)
    plt.show()


def resize():
    img_bgr = cv2.imread("New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    img_rgb_cropped = img_rgb[200:400, 300:600]
    img_rgb_resized = cv2.resize(img_rgb_cropped, None, fx=2, fy=2)

    plt.imshow(img_rgb_resized)
    plt.show()

def resize_with_dim():
    img_bgr = cv2.imread("New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    img_rgb_cropped = img_rgb[200:400, 300:600]

    desired_width = 100
    desired_height = 200
    dim = (desired_width, desired_height)

    resized_cropped_region = cv2.resize(img_rgb_cropped, dsize=dim, interpolation=cv2.INTER_AREA)
    plt.imshow(resized_cropped_region)

    plt.show()

def resize_with_aspect_ratio():
    img_bgr = cv2.imread("New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    img_rgb_cropped = img_rgb[200:400, 300:600]

    desired_width = 100
    aspect_ratio = desired_width / img_rgb_cropped.shape[1]
    desired_height = int(img_rgb_cropped.shape[0] * aspect_ratio)
    dim = (desired_width, desired_height)

    resized_cropped_region = cv2.resize(img_rgb_cropped, dsize=dim, interpolation=cv2.INTER_NEAREST)
    plt.imshow(resized_cropped_region)
    plt.show()

def flip():
    img_NZ_bgr = cv2.imread("New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
    img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)
    img_NZ_rgb_flipped_horz = cv2.flip(img_NZ_rgb, 1)
    img_NZ_rgb_flipped_vert = cv2.flip(img_NZ_rgb, 0)
    img_NZ_rgb_flipped_both = cv2.flip(img_NZ_rgb, -1)

    # Show the images
    plt.figure(figsize=(18, 5))
    plt.subplot(141);
    plt.imshow(img_NZ_rgb_flipped_horz);
    plt.title("Horizontal Flip");
    plt.subplot(142);
    plt.imshow(img_NZ_rgb_flipped_vert);
    plt.title("Vertical Flip");
    plt.subplot(143);
    plt.imshow(img_NZ_rgb_flipped_both);
    plt.title("Both Flipped");
    plt.subplot(144);
    plt.imshow(img_NZ_rgb);
    plt.title("Original");

    plt.show()

def main():
    path = os.getcwd()
    print(f"Starting opencv... {cv2.__version__}; {path}")
    files(path)

    resize_with_aspect_ratio()


if __name__ == "__main__":
    main()
