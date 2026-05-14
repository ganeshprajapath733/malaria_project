import cv2
import os

path="../dataset/Parasitized"

img_name=os.listdir(path)[0]

img=cv2.imread(os.path.join(path,img_name))

# grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# resize smaller for easy simulation
gray=cv2.resize(gray,(64,64))

# output file
output_path="../hex_output/image.hex"

with open(output_path,"w") as f:

    for row in gray:

        for pixel in row:

            hex_value=format(pixel,'02x')

            f.write(hex_value+"\n")

print("HEX file generated successfully")