import tkinter as tk
from PIL import Image, ImageTk
import os
import random

class KatakanaMentor:
    def __init__(self, master, image_path, image_name):
        self.master = master

        self.master.configure(bg="white")

        original_image = Image.open(image_path)
        
        resized_image = original_image.resize((50, 50), Image.BOX)
        
        self.tk_image = ImageTk.PhotoImage(resized_image)

        self.label = tk.Label(master, image=self.tk_image, bd=0, bg="white")
        self.label.place(x=0, y=0)

        row, col = self.extract_row_col(image_name)

        if (row == "a"):
            display_text = f"     {col}"
        else:
            display_text = f"     {row}{col}"
        self.name_label = tk.Label(master, text=display_text, bg="white")
        print(display_text)
        self.name_label.place(x=0, y=50)

        self.master.attributes('-topmost', True)
        self.master.after(5000, self.master.destroy)

    def extract_row_col(self, image_name):
        parts = image_name.split('_')
        row = parts[1]
        col = parts[2].split('.')[0]
        return row, col

class KatakanaMentorManager:
    def __init__(self, folder_path="katakana"):
        self.folder_path = folder_path

    def show_random_katakana_mentor(self):
        image_path, image_name = self.get_random_image()

        root = tk.Tk()
        root.overrideredirect(1)  
        root.geometry("50x80+1550+400") 

        mentor = KatakanaMentor(root, image_path, image_name)

        root.mainloop()

    def get_random_image(self):
        image_files = os.listdir(self.folder_path)

        random_image_name = random.choice(image_files)
        return os.path.join(self.folder_path, random_image_name), random_image_name
