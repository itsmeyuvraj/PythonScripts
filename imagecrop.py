import sys
import os
from PIL import Image

filepath = "C:\\Users\\Yuvraj Sharma\\Pictures\\source\\"

# Loop through all provided arguments
for filename in os.listdir(filepath):
    if "." not in filename:
        continue
    ending = filename.split(".")[1]
    if ending not in ["jpg", "gif", "png"]:
        continue

    try:
        # Attempt to open an image file
        image = Image.open(os.path.join(filepath, filename))
    except (IOError, e):
        # Report error, and then skip to the next argument
        print("Problem opening", filepath, ":", e)
        continue

    # Perform operations on the image here
    image = image.crop((4, 5, 2 ,3))

    # Split our origional filename into name and extension 
    name, extension = os.path.splitext(filename)

    # Save the image as "(origional_name)_thumb.jpg
    print(name + '_cropped.jpg')
    image.save(os.path.join("C:\\Users\\Yuvraj Sharma\\Pictures\\cropped\\", name + '_cropped.jpg'))