import sys

from PIL import Image  #pillow lib
#from PIL import ImageFilter is lik bluring image etc using ImageFilter class from Pillow lib

images = []

for arg in sys.argv [1:]:
    image = Image.open(arg)
    images.append(image)


images[0].save(
    "costumes.gif", save_all= True, append_images = images[1], duration=200, loop =0 )


#Images not working in teh vscode for me. Below are fw examples to refer
#img= Image.open("in.jpeg") to open an image using PIL pillow lib - image
#img.close()

#with Image.open("costume1.gif") as img:
#print(img.size)
#print(img.format)
#img.rotate(180)
##img.save("out.jpeg")
#img.filter(ImageFilter.BLUR)
##img.save("out1.jpeg")
#import numpy as np
