import sys
import os
from PIL import Image

# Grab first and second argument folders to work on
# We expect the CLI arguments to be in the format <dir>/
image_dir = sys.argv[1]
output_dir = sys.argv[2]

# Check if new_dir folder exists, if not create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through the Pokedex folder and convert jpg images to png

for filename in os.listdir(image_dir):
    img = Image.open(f'{image_dir}{filename}')
    clean_name = os.path.splitext(filename)[0]

    # Save the converted images to the new folder
    img.save(f'{output_dir}{clean_name}.png', 'png')
    print(f'{filename} saved to {output_dir} as PNG')
 