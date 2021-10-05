from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

FILE_PATH = "img/img.png"
COLORS_RGB = {"Blue": (0, 0, 255),
              "Green": (0, 255, 0),
              "Red": (255, 0, 0),
              "Orange": (255, 128, 0),
              "Yellow": (255, 255, 0),
              "Pink": (255, 0, 255),
              "Black": (0, 0, 0),
              "White": (255, 255, 255),
              "Brown": (51, 0, 0)}
WATERMARKED_IMG = None


def upload_img():
    global FILE_PATH
    try:
        file_path = filedialog.askopenfilename(initialdir="/Users/home/Downloads",
                                               title="Open Image",
                                               filetypes=[("Image Files", ".png"),
                                                          ("Image Files", ".jpg")])
        new_img_pil = Image.open(file_path)
        new_img = new_img_pil.resize((800, 600))
        new_img = ImageTk.PhotoImage(new_img)
        canvas.itemconfig(img, image=new_img)
        canvas.photo = new_img
        FILE_PATH = file_path
    except AttributeError:
        pass


def save_img():
    try:
        if WATERMARKED_IMG is None:
            messagebox.showerror("No Watermarked Image", "Please watermark an image before saving.")
        else:
            final_img = WATERMARKED_IMG
            save_path = filedialog.asksaveasfilename(title="Save Watermarked Image", filetypes=[("Image Files", ".png")])
            final_img.save(f"{save_path}.png")
    except ValueError:
        pass


def add_watermark():
    global WATERMARKED_IMG
    copy_img = Image.open(FILE_PATH)
    copy_img = copy_img.resize((800, 600))
    draw = ImageDraw.Draw(copy_img)
    font = ImageFont.truetype("arial.ttf", 24)

    draw.text((570, 550), watermark_text.get(), COLOR.get(), font)
    WATERMARKED_IMG = copy_img
    new_img = ImageTk.PhotoImage(copy_img)
    canvas.itemconfig(img, image=new_img)
    canvas.photo = new_img


window = Tk()
window.title("Image Watermarking App")
window.geometry("+0+0")
window.config(padx=50, pady=25, bg="#FFB319")

COLOR = StringVar()

canvas = Canvas(width=800, height=600, bg="#FFB319", highlightthickness=0)
default_img = PhotoImage(file="img/img.png")
img = canvas.create_image(400, 300, image=default_img)
canvas.grid(column=0, row=0, columnspan=3, pady=25)

upload_icon = PhotoImage(file="img/upload.png")
upload_img_b = Button(image=upload_icon, command=upload_img)
upload_img_b.grid(row=1, column=0)

upload_label = Label(text="Upload Image", font=("Times New Roman", 20, "bold"), bg="#FFB319")
upload_label.grid(row=2, column=0, pady=10)

save_icon = PhotoImage(file="img/save.png")
save_img_b = Button(image=save_icon, command=save_img)
save_img_b.grid(row=1, column=1)

save_label = Label(text="Save Image", font=("Times New Roman", 20, "bold"), bg="#FFB319")
save_label.grid(row=2, column=1, pady=10)

add_watermark_icon = PhotoImage(file="img/add.png")
add_watermark_b = Button(image=add_watermark_icon, command=add_watermark)
add_watermark_b.grid(row=1, column=2)

add_watermark_label = Label(text="Add Watermark", font=("Times New Roman", 20, "bold"), bg="#FFB319")
add_watermark_label.grid(row=2, column=2, pady=10)

watermark_l = Label(text="Watermark Text", font=("Helvetica", 30), fg="blue", bg="#FFB319")
watermark_l.grid(row=3, column=0)

watermark_text = Entry(width=50)
watermark_text.grid(row=3, column=2)

colors = Combobox(width=10, textvariable=COLOR)
colors["values"] = ("Blue", "Green", "Red", "Orange", "Yellow", "Pink", "Black", "White", "Brown")
colors.grid(row=3, column=1)
colors.current(0)

window.mainloop()
