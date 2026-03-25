import qrcode

# Data you want to encode
data = "https://www.google.com"

# Generate QR Code
qr = qrcode.make(data)

# Save the image
qr.save("qrcode.png")

print("QR Code generated and saved as qrcode.png")