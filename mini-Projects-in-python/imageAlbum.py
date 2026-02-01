import tkinter as tk
import time 
from PIL import Image, ImageTk

# MinWindow
root= tk.Tk()
root.title("slideShow Album")
root.geometry("900x900")

# List of image paths
image_paths= [
    r"/Users/Krishana Patel/OneDrive/Desktop/IMP pictures/DREAMLANDBECOMESREALITY.jpg",
    r"/Users/Krishana Patel/OneDrive/Desktop/IMP pictures/PIC1.jpg",
    r"/Users/Krishana Patel/OneDrive/Desktop/IMP pictures/PIC2.jpg",
    r"/Users/Krishana Patel/OneDrive/Desktop/IMP pictures/PIC3.jpg",
    r"/Users/Krishana Patel/OneDrive/Desktop/IMP pictures/PIC4.jpg",
    r"/Users/Krishana Patel/OneDrive/Desktop/IMP pictures/PIC5.jpg",
    r"/Users/Krishana Patel/OneDrive/Desktop/IMP pictures/PIC6.jpg",
    r"/Users/Krishana Patel/OneDrive/Desktop/IMP pictures/PIC7.jpg"
]

image_size= (700, 700)
images=[]
for path in image_paths:
    img= Image.open(path)
    img= img.resize(image_size)
    images.append(img)

# Convert PIL to tkinter img:
final_images=[]
for img in images:
    photo= ImageTk.PhotoImage(img)  
    final_images.append(photo)

# lable widget to keep photo

image_label= tk.Label(root)
image_label.pack(pady=30)

# slideShow

def start_slideShow():
    for photo in  final_images:
        image_label.config(image=photo)
        image_label.image = photo
        root.update()
        time.sleep(2)

# button

play_btn= tk.Button(
    root,
    text= "Play the slideShow",
    font= ("Arial",18),
    command= start_slideShow
)

play_btn.pack(pady=40)
root.mainloop()