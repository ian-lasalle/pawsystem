import tkinter as tk
from tkinter import *
from customtkinter import CTkButton as Btn, CTkImage, CTk
from PIL import Image, ImageDraw, ImageFont

def emoji(emoji, size=32):
    # convert emoji to CTkImage
    font = ImageFont.truetype("seguiemj.ttf", size=int(size/1.5))
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((size/2, size/2), emoji,
              embedded_color=True, font=font, anchor="mm")
    img = CTkImage(img, size=(size, size))
    return img


app = Tk()

texto = "hola"

msg = tk.Message(app, text = texto)
msg.config(bg='lightgreen', font=('arial', 24, 'bold'))
msg.pack()

app.mainloop()