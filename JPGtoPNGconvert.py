import sys
import os
from PIL import Image

# Grab first and second argument folders to work on
old_dir = sys.argv[1]
new_dir = sys.argv[2]

# Check if new_dir folder exists, if not create it
if not os.path.exists('New'):
    os.makedirs('New')

# Loop through the Pokedex folder and convert jpg images to png
target_fmt = '.png'

for file in os.listdir(old_dir):
    filename, extension = os.path.splitext(file)
    try:
        jpg_img = Image.open(f'./{old_dir}/{filename}{extension}')
        png_name = filename + target_fmt

        # Save the converted images to the new folder
        jpg_img.save(f'./{new_dir}/{png_name}')
    except OSError as err:
        raise err
