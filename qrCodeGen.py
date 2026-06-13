# Write a program to generate a QR code based on user input, such as text or a
# URL. The QR code should be saved as an image file that can be scanned with a
# smartphone.

import qrcode

def qrCodeGenerator():

    data=input("enter the data or link ")

    image = qrcode.make(data)
    image.save("qr.png")

qrCodeGenerator()


