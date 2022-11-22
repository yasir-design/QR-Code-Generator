"""QR Code Generator Configuration"""
import os


class Config:
    QR_CODE_IMAGE_DIRECTORY = os.environ.get('QR_CODE_IMAGE_DIRECTORY')
    QR_CODE_DEFAULT_URL = os.environ.get('QR_CODE_DEFAULT_URL')
    QR_CODE_DEFAULT_FILENAME = os.environ.get('QR_CODE_DEFAULT_FILENAME')
