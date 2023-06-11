import qrcode

def generate_qrcode(link, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

link = input("Enter the link: ")
filename = "qrcode.png"
generate_qrcode(link, filename)
print(f"A QR code has been generated and saved as {filename}.")
