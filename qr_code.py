import qrcode


def generate_qr(
        link,
        version,
        box_size,
        border,
):
    qr = qrcode.QRCode(
        version=version,
        box_size=int(box_size),
        border=int(border),
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filename = "qr_code.png"
    img.save(filename)

    return filename

