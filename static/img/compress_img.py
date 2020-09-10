from PIL import Image
import glob, os

size = 1500, 1000
thumb_size = 1500, 1125

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    if 'thumb' in file:
        im.thumbnail(thumb_size)
        print(file)
    else:
        im.thumbnail(size)
    im.save(file + '.JPG', "JPEG")
