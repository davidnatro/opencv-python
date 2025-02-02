import os
import cv2
from urllib.request import urlretrieve
from zipfile import ZipFile


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
    url = r"https://www.dropbox.com/s/p8h7ckeo2dn1jtz/opencv_bootcamp_assets_NB6.zip?dl=1"

    asset_zip_path = os.path.join(path, f"opencv_bootcamp_assets_NB6.zip")

    if not os.path.exists(asset_zip_path):
        download_and_unzip(url, asset_zip_path)


def main():
    path = os.getcwd()
    print(f"Starting opencv... {cv2.__version__}; {path}")
    files(path)

    source = cv2.VideoCapture("race_car.mp4")

    if not source.isOpened():
        print("Error: Could not open video.")
        return

    width = int(source.get(3))
    height = int(source.get(4))

    out_avi = cv2.VideoWriter("race_car_out.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 10, (width, height))
    out_mp4 = cv2.VideoWriter("race_car_out.mp4", cv2.VideoWriter_fourcc(*"XVID"), 10, (width, height))

    while source.isOpened():
        has_frame, frame = source.read()
        if not has_frame:
            break

        out_avi.write(frame)
        out_mp4.write(frame)

    out_avi.release()
    out_mp4.release()
    source.release()


if __name__ == "__main__":
    main()
