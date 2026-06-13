import qrcode

def userInput( ):
    
    data= input("enter the data or link : ").lower()
    fill_color= input(" the color of the qr : ").lower()
    back_color= input("the background color of qr : ").lower()
    return data,fill_color,back_color


def qrCodeGenerator():
    try:
        n=int(input("how many qr would u like to generate : "))
    except ValueError:
        print("enter valid number ")

    for i in range(n):
            print(f"for qr no {i+1}")
            try:

                data,fill_color,back_color=userInput()

                qr = qrcode.QRCode()

                qr.add_data(data)
                qr.make(fit=True)
                image = qr.make_image(fill_color= fill_color, back_color=back_color)
                image.save(f"qr{i+1}.png")

            except ValueError:
                 print("invalid color ")
        

qrCodeGenerator()


