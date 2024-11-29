from PIL import Image
from os import listdir, getcwd
from os.path import isfile, join, exists, makedirs
import re
import sys
import math

def image_title_repl(matchobj):
    """replace img_title with img_title_resized"""
    file_name = matchobj.group(0)
    return "/resized/" + file_name

percentage = int(sys.argv[1]) if len(sys.argv) > 1 else 50

print("Resizing to " + str(percentage) + "%")

if not isinstance(percentage, (int, float, complex)):
    raise TypeError("Argument must be a percentage number, argument was " + percentage)

# list all images in the folder
current_dir = getcwd()
print("The current directory is " + current_dir)
onlyimagefiles = [
    f
    for f in listdir(current_dir)
    if isfile(join(current_dir, f))
    and bool(re.search(r"\.(gif|jpe?g|tiff?|png|webp|bmp)", f))
]

# list files in image
print("Found the following image files: ", onlyimagefiles)

if not exists(current_dir + "/resized/"):
    makedirs(current_dir + "/resized/")

for image_file in onlyimagefiles:
    image = Image.open(image_file)

    new_height = math.floor(image.height * (percentage / 100))
    new_width = math.floor(image.width * (percentage / 100))

    new_image = image.resize((new_width, new_height))

    link_regex = re.compile(
        r"[^\.]+"
    ) 
    new_filename = link_regex.sub(image_title_repl, image_file, 1)

    # save under the new filename
    print(new_filename)
    new_image.save(new_filename)

