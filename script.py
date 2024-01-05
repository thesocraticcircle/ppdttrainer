import tkinter as tk
from PIL import Image, ImageTk
import os
import time

def display_image(image_path, display_time=30):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Display Image")

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo)
    label.pack(fill=tk.BOTH, expand=True)

    root.after(display_time * 1000, root.destroy)  # Close the window after display_time seconds

    root.mainloop()

def show_text_screen(color, text, display_time=30):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Text Screen")

    root.configure(bg=color)

    label = tk.Label(root, text=text, font=("Helvetica", 16), fg="white", bg=color)
    label.pack(expand=True)

    root.after(display_time * 1000, root.destroy)  # Close the window after display_time seconds

    root.mainloop()

def main():
    image_folder = "ppdt"
    images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    for image_file in images:
        image_path = os.path.join(image_folder, image_file)

        # Display image for 30 seconds
        display_image(image_path, display_time=30)

        # Black screen with text "Start Writing Action" for 30 seconds
        show_text_screen("black", "Start Writing Action", display_time=30)

        # Maroon screen with text "Write Story" for 4 minutes
        show_text_screen("#800000", "Write Story", display_time=240)

        # Blank screen showing countdown of 10 seconds with text "Take Rest"
        show_text_screen("black", "Take Rest", display_time=10)

if __name__ == "__main__":
    main()
