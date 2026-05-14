import cv2
import matplotlib.pyplot as plt
import os

path="../dataset/Parasitized"

img_name=os.listdir(path)[0]

img=cv2.imread(os.path.join(path,img_name))

original=img.copy()

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,binary=cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY+cv2.THRESH_OTSU
)

# invert so parasite becomes white
binary=cv2.bitwise_not(binary)

# find regions
contours,_=cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for c in contours:

    area=cv2.contourArea(c)

    if area>10:

        x,y,w,h=cv2.boundingRect(c)

        cv2.rectangle(
            original,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.imshow(binary,cmap='gray')
plt.title("Detected Region")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(original,cv2.COLOR_BGR2RGB))
plt.title("Bounding Box")

plt.show()