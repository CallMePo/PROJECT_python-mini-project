import pyqrcode
from PIL import Image

link=input("Enter: ")
qr_code=pyqrcode.create(link)
qr_code.png("QR Code.png", scale=5)
Image.open("QR Code.png")