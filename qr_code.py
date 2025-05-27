import qrcode

user_input = input('Enter the text or URL to generate a QR code:')

qr = qrcode.QRCode(version= 1, box_size= 5, border = 5)
qr.add_data(user_input)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('generated_qr.png')

print("QR code generated and saved as 'generated_qr.png'")