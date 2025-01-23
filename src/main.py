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

    


def main():
    path = os.getcwd()
    logging.info(f"Starting opencv... {cv2.__version__}; {path}")

    files(path)
    lake()


if __name__ == "__main__":
    main()
