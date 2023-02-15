# Pixelate-Image_V2
this is the update of Pixelate-Image

The first change in the updated code is the addition of the Tk and filedialog modules from the tkinter package. These modules allow the code to create a GUI file dialog that the user can use to select the image file path and destination folder.

The pixelate_image function takes three arguments: image_path, pixel_size, and dest_folder. The image_path argument is the file path of the original image, pixel_size is the size of the pixelation block, and dest_folder is the destination folder for the pixelated image.

Inside the function, the original image is opened using the Image.open method from the PIL package, and its dimensions are obtained using the size attribute. The function then checks that the pixel_size entered by the user is not greater than the dimensions of the original image. If the pixel_size is too big, an error message is printed and the function returns.

Next, the function resizes the image to a smaller size using the resize method with the BOX resampling method. The resampling method determines how the image is resized. BOX is a resampling method that reduces the image size by averaging the pixels in each block of size pixel_size. This creates a pixelated effect.

The function then resizes the image back to its original size using the NEAREST resampling method. This method is used because it preserves the sharp edges of the pixelated blocks.

After that, the function uses the asksaveasfilename method from the filedialog module to ask the user for the destination path and file name. The user can choose the file extension and the destination folder. The save method from the Image class is used to
