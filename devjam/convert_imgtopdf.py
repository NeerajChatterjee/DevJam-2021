import sys
from PIL import Image
# from PIL.Image import core as _imaging

image_full_path=sys.argv[1]
image_name=sys.argv[2]

img=Image.open(str(image_full_path))

image_save_path=image_full_path.replace(image_name,"converted.pdf")

img.save(image_save_path)

print("image save path is ",image_save_path)

# print('/media/converted.pdf')



