import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageFont
from PIL import ImageDraw


def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        watermark_image = img.copy()
        draw = ImageDraw.Draw(watermark_image)
        w, h = (watermark_image.width, watermark_image.height)
        x, y = int(w * 0.1), int(h * 0.9)

        draw.text((x, y), "python", font=ImageFont.load_default(),
                  fill=(0, 0, 0), anchor='ms')

        watermark_image.save('new.png')

        watermark_img = ImageTk.PhotoImage(watermark_image)

        panel.config(image=watermark_img)
        panel.image = watermark_img


root = tk.Tk()
root.title("Image Upload Interface")

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

panel = tk.Label(root)
panel.pack()

root.mainloop()
