# TIFF-to-JPEG-conversion-python-program
The program converts all TIFF format images in the provided source directory from TIFF to JPEG. It further on saves the converted file as a new copy with the keyword new_ before the file name. So suppose your jpeg file has the name image.tiff it will be converted and stored in the destination directory as new_image.jpg

To make the code act on your required directory enter absolute path of the directory where the files are stored in the interpreter once code is run.

For the converted files to be stored in a new directory input absolute path of new directory in the interpreter once code is run.

if the file in the directory is of a format other than TIFF or a non image format the code will throw and exception and move to the next file

Pre requisits for the code to run:
1.Python version 3.8.1 (https://www.python.org/downloads/release/python-381/)
2.installation of Pillow Library for Python (https://pillow.readthedocs.io/en/stable/installation.html)
