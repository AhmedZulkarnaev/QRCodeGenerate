import flet as ft
import base64
from qr_code import generate_qr


def main(page: ft.Page):
    page.title = "QR Code Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50
    page.theme_mode = ft.ThemeMode.DARK

    header = ft.Text("QR Code Generator", size=28, weight=ft.FontWeight.BOLD, color="white")
    subheader = ft.Text("Generate a custom QR code with ease", size=16, italic=True, color="gray")

    input_link = ft.TextField(label="Enter link", width=320, border_radius=10, bgcolor="#333", color="white")
    input_version = ft.TextField(label="Version", width=320, border_radius=10, bgcolor="#333", color="white")
    input_box_size = ft.TextField(label="Box size", width=320, border_radius=10, bgcolor="#333", color="white")
    input_border = ft.TextField(label="Border", width=320, border_radius=10, bgcolor="#333", color="white")

    qr_image = ft.Image(src_base64="", width=200, height=200, visible=False)
    download_button = ft.ElevatedButton("Download QR Code", width=320, visible=False, bgcolor="#007BFF", color="white")

    def on_generate_click(e):
        if not input_link.value:
            page.snack_bar = ft.SnackBar(ft.Text("Please enter a link!"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        qr_file = generate_qr(
            input_link.value,
            version=int(input_version.value) if input_version.value else None,
            box_size=int(input_box_size.value) if input_box_size.value else 4,
            border=int(input_border.value) if input_border.value else 1,
        )

        with open(qr_file, "rb") as image_file:
            qr_base64 = base64.b64encode(image_file.read()).decode("utf-8")

        qr_image.src_base64 = qr_base64
        qr_image.visible = True
        download_button.visible = True
        download_button.url = qr_file

        page.update()

    generate_button = ft.ElevatedButton("Generate QR Code", width=320, on_click=on_generate_click, bgcolor="#28A745",
                                        color="white")

    page.add(
        header, subheader,
        input_link, input_version, input_box_size, input_border,
        generate_button,
        qr_image,
        download_button,
    )


ft.app(target=main)


