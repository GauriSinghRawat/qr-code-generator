import qrcode
from PIL import Image

data = "Hello, this is my QR Code!"

qr = qrcode.QRCode(
    version=1,  # controls size (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # size of each box
    border=4,  # border thickness
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("custom_qrcode.png")

print("Custom QR Code generated!")