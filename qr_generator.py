import qrcode
info = input("Enter the text you want in your QR code: ")
img = qrcode.make(info)
img.save('text.png')