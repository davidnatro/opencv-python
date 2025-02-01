import os
import cv2

import matplotlib.pyplot as plt
import numpy as np

from zipfile import ZipFile
from urllib.request import urlretrieve


def files(path):
    url = r"https://www.dropbox.com/s/0oe92zziik5mwhf/opencv_bootcamp_assets_NB4.zip?dl=1"

    asset_zip_path = os.path.join(path, f"opencv_bootcamp_assets_NB4.zip")

    if not os.path.exists(asset_zip_path):
        download_and_unzip(url, asset_zip_path)


def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assests....", end="")

    urlretrieve(url, save_path)

    try:
        with ZipFile(save_path) as z:
            z.extractall(os.path.split(save_path)[0])
        print("Done")

    except Exception as e:
        print("\nInvalid file.", e)


def brightness():
    img_bgr = cv2.imread("New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    matrix = np.ones(img_bgr.shape, dtype="uint8") * 50

    img_darker = cv2.subtract(img_rgb, matrix)
    img_brighter = cv2.add(img_rgb, matrix)

    plt.figure(figsize=[18, 5])
    plt.subplot(131)
    plt.imshow(img_darker)
    plt.title("Darker")
    plt.subplot(132)
    plt.imshow(img_rgb)
    plt.title("Original")
    plt.subplot(133)
    plt.imshow(img_brighter)
    plt.title("Brighter")

    plt.show()


def contrast():
    img_bgr = cv2.imread("New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    matrix1 = np.ones(img_rgb.shape) * 0.8
    matrix2 = np.ones(img_rgb.shape) * 1.2

    img_contrast1 = np.uint8(cv2.multiply(np.float64(img_rgb), matrix1))
    img_contrast2 = np.uint8(np.clip(cv2.multiply(np.float64(img_rgb), matrix2), 0, 255))

    plt.figure(figsize=[18, 5])
    plt.subplot(131)
    plt.imshow(img_contrast1)
    plt.title("Contrast 0.8")
    plt.subplot(132)
    plt.imshow(img_rgb)
    plt.title("Original")
    plt.subplot(133)
    plt.imshow(img_contrast2)
    plt.title("Contrast 1.2")

    plt.show()


def threshold():
    img_bgr = cv2.imread("building-windows.jpg", cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    img = cv2.imread("building-windows.jpg", cv2.IMREAD_GRAYSCALE)

    retval, dst = cv2.threshold(img, 100, 255, type=cv2.THRESH_BINARY)

    print(dst)

    plt.figure(figsize=[7, 10])
    plt.subplot(211)
    plt.imshow(img_rgb)
    plt.title("original")
    plt.subplot(212)
    plt.imshow(dst, cmap="gray")
    plt.title("threshold")
    plt.show()


def adaptive_threshold():
    # Read the original image
    img_read = cv2.imread("Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)

    # Perform global thresholding
    retval, img_thresh_gbl_1 = cv2.threshold(img_read, 50, 255, cv2.THRESH_BINARY)

    # Perform global thresholding
    retval, img_thresh_gbl_2 = cv2.threshold(img_read, 130, 255, cv2.THRESH_BINARY)

    # Perform adaptive thresholding
    img_thresh_adp = cv2.adaptiveThreshold(img_read, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 7)

    # Show the images
    # plt.figure(figsize=[8, 8])
    # plt.subplot(221)
    # plt.imshow(img_read, cmap="gray")
    # plt.title("Original")
    # plt.subplot(222)
    # plt.imshow(img_thresh_gbl_1, cmap="gray")
    # plt.title("Thresholded (global: 50)")
    # plt.subplot(223)
    # plt.imshow(img_thresh_gbl_2, cmap="gray")
    # plt.title("Thresholded (global: 130)")
    # plt.subplot(224)
    # plt.imshow(img_thresh_adp, cmap="gray")
    # plt.title("Thresholded (adaptive)")

    plt.imshow(img_thresh_adp, cmap="gray")

    plt.show()


def bitwise_and():
    img_rectangle = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
    img_circle = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)

    img_and = cv2.bitwise_and(img_rectangle, img_circle)

    plt.subplot(311)
    plt.imshow(img_rectangle, cmap="gray")
    plt.title("Rectangle")
    plt.subplot(312)
    plt.imshow(img_circle, cmap="gray")
    plt.title("Circle")
    plt.subplot(313)
    plt.imshow(img_and, cmap="gray")
    plt.title("Bitwise AND")
    plt.show()


def bitwise_or():
    img_rectangle = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
    img_circle = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)

    img_or = cv2.bitwise_or(img_rectangle, img_circle)

    plt.subplot(311)
    plt.imshow(img_rectangle, cmap="gray")
    plt.title("Rectangle")
    plt.subplot(312)
    plt.imshow(img_circle, cmap="gray")
    plt.title("Circle")
    plt.subplot(313)
    plt.imshow(img_or, cmap="gray")
    plt.title("Bitwise OR")
    plt.show()


def bitwise_xor():
    img_rectangle = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
    img_circle = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)

    img_xor = cv2.bitwise_xor(img_rectangle, img_circle)

    plt.subplot(311)
    plt.imshow(img_rectangle, cmap="gray")
    plt.title("Rectangle")
    plt.subplot(312)
    plt.imshow(img_circle, cmap="gray")
    plt.title("Circle")
    plt.subplot(313)
    plt.imshow(img_xor, cmap="gray")
    plt.title("Bitwise XOR")
    plt.show()


def logo_manipulation():
    img_cola = cv2.imread("coca-cola-logo.png", cv2.IMREAD_COLOR)
    w = img_cola.shape[0]
    h = img_cola.shape[1]

    img_background_bgr = cv2.imread("checkerboard_color.png")
    img_background_rgb = cv2.cvtColor(img_background_bgr, cv2.COLOR_BGR2RGB)

    aspect_ratio = w / img_background_rgb.shape[1]
    dim = (w, int(img_background_rgb.shape[0] * aspect_ratio))

    img_background_rgb = cv2.resize(img_background_rgb, dim, interpolation=cv2.INTER_AREA)

    img_cola_rgb = cv2.cvtColor(img_cola, cv2.COLOR_BGR2RGB)
    img_cola_gray = cv2.cvtColor(img_cola, cv2.COLOR_BGR2GRAY)

    retval, img_cola_threshold = cv2.threshold(img_cola_gray, 200, 255, cv2.THRESH_BINARY)

    img_cola_gray_inv = cv2.bitwise_not(img_cola_threshold)
    img_cola_back = cv2.bitwise_and(img_background_rgb, img_background_rgb, mask=img_cola_threshold)

    img_cola_inv_back = cv2.bitwise_and(img_cola_rgb, img_cola_rgb, mask=img_cola_gray_inv)

    img_cola_inv_back = cv2.add(img_cola_inv_back, img_cola_back)

    plt.imshow(img_cola_inv_back, cmap="gray")
    plt.show()


def main():
    path = os.getcwd()
    print(f"Starting opencv... {cv2.__version__}; {path}")
    files(path)

    # logo_manipulation()

    arr1 = np.array([200, 250], dtype=np.uint8).reshape(-1, 1)
    arr2 = np.array([40, 40], dtype=np.uint8).reshape(-1, 1)
    add_numpy = arr1 + arr2
    add_cv2 = cv2.add(arr1, arr2)
    print(add_numpy)
    print(add_cv2)


if __name__ == '__main__':
    main()
