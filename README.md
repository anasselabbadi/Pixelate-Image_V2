Pixelate-Image_V2
This is an updated version of the Pixelate-Image script, which includes the following changes:

The addition of the Tk and filedialog modules from the tkinter package, which enable the creation of a GUI file dialog for the user to select the image file path and destination folder.
The pixelate_image function, which takes three arguments: image_path, pixel_size, and dest_folder. Image_path is the file path of the original image, pixel_size is the size of the pixelation block, and dest_folder is the destination folder for the pixelated image.
Opening the original image using the Image.open method from the PIL package, and obtaining its dimensions using the size attribute.
Checking that the pixel_size entered by the user is not greater than the dimensions of the original image. If the pixel_size is too big, an error message is printed and the function returns.
Resizing the image to a smaller size using the resize method with the BOX resampling method. The BOX resampling method reduces the image size by averaging the pixels in each block of size pixel_size, creating a pixelated effect.
Resizing the image back to its original size using the NEAREST resampling method, which preserves the sharp edges of the pixelated blocks.
Asking the user for the destination path and file name using the asksaveasfilename method from the filedialog module. The user can choose the file extension and destination folder.
Using the save method from the Image class to save the pixelated image to the specified destination folder and file name.
To use this script, follow these steps:

Install the required packages by running the following command:
Copy code
```python
pip install Pillow
```
1-Copy the code to a Python file, and save it to your desired location.

2-Open the Python file in a code editor or IDE of your choice.

3-Run the script.

4-When prompted, select the original image file using the file dialog.

5-Enter the desired pixel size for the pixelation block.

6-When prompted, select the destination folder using the file dialog.

7-The pixelated image will be saved in the destination folder with the file name and extension of your choice.
