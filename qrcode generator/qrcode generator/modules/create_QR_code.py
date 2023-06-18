import qrcode 
import os
from tkinter import colorchooser
from PIL import Image, ImageTk
import modules.create_entry as m_entry
import customtkinter as ctk
import modules.create_app as m_app
def generate_qrcode():
    global qr
    url_text = m_entry.url_entry.get()
    user_folder = "media/user1"
    os.makedirs(user_folder, exist_ok = True)
    qr = qrcode.QRCode(version = 1,
                       error_correction = qrcode.constants.ERROR_CORRECT_H,
                       box_size = 6,
                       border = 4)
    qr.add_data(url_text)
    qr.make(fit = True)
    image = qr.make_image(fill_color = "black", back_color = "white")
    image_path = os.path.join(user_folder, "qrcode.png")
    image.save(image_path)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)


def change_back():
    global color
    color = colorchooser.askcolor(title = "select color")[1]
    image = qr.make_image(fill_color = "black", back_color = color)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)

    bg_image_button = ctk.CTkButton(
    master = m_app.app.FRAME_1,
    width = 140,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    # command = m_qr.generate_qrcode,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    bg_color = "transparent",
    text = "Set image as bg"
    )
    bg_image_button.place(x = 150,y = 300)
    

def change_color():
    color1 = colorchooser.askcolor(title = "select color")[1]
    image = qr.make_image(fill_color = color1, back_color = color)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)



def add_logo():
    file_path = ctk.filedialog.askopenfilename(initialdir = "images/", filetypes = (("JPEG files", "*.png;*.jpg"),))
    url_text = m_entry.url_entry.get()
    qr = qrcode.QRCode(version = 1,
                       error_correction = qrcode.constants.ERROR_CORRECT_H,
                       box_size = 6,
                       border = 4)
    qr.add_data(url_text)
    qr.make(fit = True)

    image = qr.make_image(fill_color = "black", back_color = "white")

    logo_image = Image.open(file_path).convert("RGBA")

    # Масштабирование логотипа
    logo_size = image.size[0] // 4
    logo_image = logo_image.resize((logo_size, logo_size), Image.ANTIALIAS)

    # Создание нового изображения с альфа-каналом
    qr_code_with_logo = Image.new("RGBA", image.size)

    # Копирование QR-кода на изображение с альфа-каналом
    qr_code_with_logo.paste(image, (0, 0))

    # Размещение логотипа посередине QR-кода
    position = (
        (qr_code_with_logo.size[0] - logo_image.size[0]) // 2,
        (qr_code_with_logo.size[1] - logo_image.size[1]) // 2,
    )
    qr_code_with_logo.alpha_composite(logo_image, position)

    # Сохранение QR-кода с логотипом
    qr_code_with_logo.save("qr_code_with_logo.png")

    imageTk = ImageTk.PhotoImage(qr_code_with_logo)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)