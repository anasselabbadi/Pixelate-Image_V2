from PIL import Image
import tkinter as tk
from tkinter import filedialog

def pixelate_image(image_path, pixel_size):
    with Image.open(image_path) as im:
        # Check if the pixel size is valid
        if pixel_size > min(im.width, im.height):
            print("Invalid pixel size. Please enter a smaller value.")
            return
        # Resize the image to a smaller size
        im = im.resize((im.width // pixel_size, im.height // pixel_size), Image.BOX)
        # Resize the image back to its original size
        im = im.resize((im.width * pixel_size, im.height * pixel_size), Image.NEAREST)
        # Show the pixelated image
        im.show()
        # Get the destination folder from the user
        root = tk.Tk()
        root.withdraw()
        save_path = filedialog.askdirectory()
        # Save the pixelated image in the selected folder
        im.save(save_path + "/pixelated_" + image_path.split("/")[-1])

if __name__ == '__main__':
    # Get the image path from the user
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename()
    # Get the pixel size from the user
    pixel_size = int(input("Enter the pixel size:(The best size 10)"))
    # Pixelate the image and save it in the selected folder
    pixelate_image(image_path, pixel_size)
