import os
import cv2
import colorlog
import logging

from zipfile import ZipFile
import matplotlib.pyplot as plt
from urllib.request import urlretrieve

# Configure colored logging
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
))

logger = colorlog.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def download_and_unzip(url, save_path):
    logging.info(f"Downloading and extracting assests....")

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
    url = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"
    asset_zip_path = os.path.join(path, f"opencv_bootcamp_assets_NB1.zip")
    if not os.path.exists(asset_zip_path):
        download_and_unzip(url, asset_zip_path)


def coke():
    coke_img = cv2.imread("coca-cola-logo.png", cv2.IMREAD_COLOR)
    # coke_reversed = coke_img[:, :, ::-1]
    coke_reversed = cv2.cvtColor(coke_img, cv2.COLOR_RGB2BGR)
    plt.imshow(coke_reversed)

    plt.show()

    print(coke_img)
    print(coke_img.shape)
    print(coke_img.dtype)


def lake():
    lake_img = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
    lake_reverse = cv2.cvtColor(lake_img, cv2.COLOR_RGB2BGR)
    plt.imshow(lake_reverse)
    plt.show()


def split_and_merge():
    # Split the image into the B,G,R components
    img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
    b, g, r = cv2.split(img_NZ_bgr)

    # Show the channels
    plt.figure(figsize=[20, 5])

    plt.subplot(141);
    plt.imshow(r, cmap="gray");
    plt.title("Red Channel")
    plt.subplot(142);
    plt.imshow(g, cmap="gray");
    plt.title("Green Channel")
    plt.subplot(143);
    plt.imshow(b, cmap="gray");
    plt.title("Blue Channel")

    # Merge the individual channels into a BGR image
    imgMerged = cv2.merge((b, g, r))
    img = cv2.cvtColor(imgMerged, cv2.COLOR_BGR2RGB)
    # Show the merged output
    plt.subplot(144)
    plt.imshow(img)
    plt.title("Merged Output")

    plt.show()


def hsv():
    img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
    img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)

    # Split the image into the B,G,R components
    h, s, v = cv2.split(img_hsv)

    # Show the channels
    plt.figure(figsize=[20, 5])
    plt.subplot(141);
    plt.imshow(h, cmap="gray");
    plt.title("H Channel");
    plt.subplot(142);
    plt.imshow(s, cmap="gray");
    plt.title("S Channel");
    plt.subplot(143);
    plt.imshow(v, cmap="gray");
    plt.title("V Channel");
    plt.subplot(144);
    plt.imshow(img_NZ_rgb);
    plt.title("Original");

    h_new = h + 10
    img_NZ_merged = cv2.merge((h_new, s, v))
    img_NZ_rgb = cv2.cvtColor(img_NZ_merged, cv2.COLOR_HSV2RGB)

    # Show the channels
    plt.figure(figsize=[20, 5])
    plt.subplot(141);
    plt.imshow(h, cmap="gray");
    plt.title("H Channel");
    plt.subplot(142);
    plt.imshow(s, cmap="gray");
    plt.title("S Channel");
    plt.subplot(143);
    plt.imshow(v, cmap="gray");
    plt.title("V Channel");
    plt.subplot(144);
    plt.imshow(img_NZ_rgb);
    plt.title("Original");


def main():
    path = os.getcwd()
    logging.info(f"Starting opencv... {cv2.__version__}; {path}")
    files(path)

    coke()


if __name__ == "__main__":
    main()
