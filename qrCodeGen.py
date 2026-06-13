# Write a program to generate a QR code based on user input, such as text or a
# URL. The QR code should be saved as an image file that can be scanned with a
# smartphone.

import qrcode

def userInput():

    data=input("enter the data or link : ")
    fill_color = input(" the color of the qr : ")
    back_color = input("the background color of qr : ")
    return data,fill_color,back_color


def qrCodeGenerator():
    data,fill_color,back_color= userInput()

    qr = qrcode.QRCode()

    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color= fill_color, back_color=back_color)
    image.save("qr.png")

qrCodeGenerator()


