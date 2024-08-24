import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("600x400")
window.title("Dice Roll")

dice_images = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]

def roll_dice():
    result1 = random.randint(1, 6)
    result2 = random.randint(1, 6)
    
    dice_image1 = Image.open(dice_images[result1 - 1])
    dice_photo1 = ImageTk.PhotoImage(dice_image1)
    
    dice_image2 = Image.open(dice_images[result2 - 1])
    dice_photo2 = ImageTk.PhotoImage(dice_image2)
    
    label1.config(image=dice_photo1)
    label1.image = dice_photo1

    label2.config(image=dice_photo2)
    label2.image = dice_photo2

    result_label.config(text=f"Result: {result1} + {result2} = {result1 + result2}")

dice_image1 = Image.open(dice_images[0])
dice_photo1 = ImageTk.PhotoImage(dice_image1)
label1 = tk.Label(window, image=dice_photo1)
label1.image = dice_photo1
label1.place(x=100, y=100)

dice_image2 = Image.open(dice_images[0])
dice_photo2 = ImageTk.PhotoImage(dice_image2)
label2 = tk.Label(window, image=dice_photo2)
label2.image = dice_photo2
label2.place(x=750, y=100)

result_label = tk.Label(window, text="Result: ", font="Times 20")
result_label.place(x=20, y=639)

roll_button = tk.Button(window, text="ROLL", bg="black", fg="white", font="Times 20", command=roll_dice)
roll_button.place(x=635, y=20)

window.mainloop()