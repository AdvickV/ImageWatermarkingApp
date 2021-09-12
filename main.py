from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

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
        FILE_PATH = file_path
    except AttributeError:
        messagebox.showerror("No path chosen!", "Please choose a image.")
        return
    new_img_pil = Image.open(file_path)
    new_img = new_img_pil.resize((800, 600))
    new_img = ImageTk.PhotoImage(new_img)
    canvas.itemconfig(img, image=new_img)
    canvas.photo = new_img


def save_img():
    if WATERMARKED_IMG is None:
        messagebox.showerror("No Watermarked Image", "Please watermark an image before saving!")
        return
    else:
        final_img = WATERMARKED_IMG
        save_path = filedialog.asksaveasfilename(title="Save Watermarked Image", filetypes=[("Image Files", ".png")])
        final_img.save(f"{save_path}.png")



def add_watermark():
    global WATERMARKED_IMG
    copy_img = Image.open(FILE_PATH)
    copy_img = copy_img.resize((800, 600))
    draw = ImageDraw.Draw(copy_img)
    font = ImageFont.truetype("arial.ttf", 24)

    draw.text((650, 550), watermark_text.get(), COLORS_RGB[listbox.get(listbox.curselection())], font)
    WATERMARKED_IMG = copy_img
    new_img = ImageTk.PhotoImage(copy_img)
    canvas.itemconfig(img, image=new_img)
    canvas.photo = new_img


window = Tk()
window.title("Image Watermarking App")
window.config(padx=50, pady=50, bg="#FFB319")

canvas = Canvas(width=800, height=600, bg="#FFB319", highlightthickness=0)
default_img = PhotoImage(file="img/img.png")
img = canvas.create_image(400, 300, image=default_img)
canvas.grid(column=0, row=0, columnspan=2)

upload_icon = PhotoImage(file="img/upload.png")
upload_img_b = Button(image=upload_icon, highlightthickness=0, command=upload_img)
upload_img_b.grid(row=1, column=0, pady=50)

save_icon = PhotoImage(file="img/save.png")
save_img_b = Button(image=save_icon, highlightthickness=0, command=save_img)
save_img_b.grid(row=1, column=1, pady=50)

watermark_l = Label(text="Watermark Text", font=("Helvetica", "36"), fg="blue", bg="#FFB319")
watermark_l.grid(row=2, column=0)

watermark_text = Entry(width=50)
watermark_text.grid(row=2, column=1)

add_watermark_icon = PhotoImage(file="img/add.png")
add_watermark_b = Button(image=add_watermark_icon, highlightthickness=0, command=add_watermark)
add_watermark_b.grid(row=3, column=0, pady=50)

listbox = Listbox(height=4)
fruits = ["Blue", "Green", "Red", "Orange", "Yellow", "Pink", "Black", "White", "Brown"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>")
listbox.grid(row=3, column=1, pady=50)

window.mainloop()
