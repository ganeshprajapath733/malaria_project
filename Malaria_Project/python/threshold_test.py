import cv2
import matplotlib.pyplot as plt
import os

# Select one infected image
path="../dataset/Parasitized"

img_name=os.listdir(path)[0]

img=cv2.imread(os.path.join(path,img_name))

# convert RGB -> Gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold
_,binary=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(gray,cmap='gray')
plt.title("Gray")

plt.subplot(1,3,3)
plt.imshow(binary,cmap='gray')
plt.title("Threshold Output")

plt.show()