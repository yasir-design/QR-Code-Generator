import os.path

from qrcodegenerator import create_qr_code_image
from config import Config


def main():
    full_path = os.getcwd()
    directory_path_and_file_name = os.path.join(full_path, Config.QR_CODE_IMAGE_DIRECTORY,
                                                Config.QR_CODE_DEFAULT_FILENAME)

    qr_image = create_qr_code_image(Config.QR_CODE_DEFAULT_URL)
    for i in range(0, 1):
        while True:
            try:
                qr_image.save(directory_path_and_file_name)
            except FileNotFoundError:
                current_working_directory = os.getcwd()
                qr_image_directory = Config.QR_CODE_IMAGE_DIRECTORY
                new_directory_path = os.path.join(current_working_directory, qr_image_directory)
                os.mkdir(new_directory_path)
                continue
            break


if __name__ == "__main__":
    main()
