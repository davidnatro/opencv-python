import os
import cv2

from urllib.request import urlretrieve
from zipfile import ZipFile
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
    url = r"https://www.dropbox.com/s/48hboi1m4crv1tl/opencv_bootcamp_assets_NB3.zip?dl=1"

    asset_zip_path = os.path.join(path, f"opencv_bootcamp_assets_NB3.zip")

    if not os.path.exists(asset_zip_path):
        download_and_unzip(url, asset_zip_path)


def draw_line():
    img_bgr = cv2.imread("Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

    cv2.line(img_bgr, (200, 100), (400, 100), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()


def draw_circle():
    img_bgr = cv2.imread("Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

    cv2.circle(img_bgr, (300, 200), 50, (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()


def draw_rectangle():
    img_bgr = cv2.imread("Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

    cv2.rectangle(img_bgr, (500, 100), (700, 600), (255, 0, 255), thickness=5, lineType=cv2.LINE_8)

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()


def add_text():
    img_bgr = cv2.imread("Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

    cv2.putText(img_bgr, "Apollo 11", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 5, cv2.LINE_AA)

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()


def main():
    path = os.getcwd()
    print(f"Starting opencv... {cv2.__version__}; {path}")
    files(path)

    add_text()


if __name__ == "__main__":
    main()
