import cv2
import matplotlib.pyplot as plt
import os

# Image paths
infected_path = "../dataset/Parasitized"
uninfected_path = "../dataset/Uninfected"

# Pick first image from each folder
infected_img = os.listdir(infected_path)[0]
uninfected_img = os.listdir(uninfected_path)[0]

# Read images
img1 = cv2.imread(os.path.join(infected_path, infected_img))
img2 = cv2.imread(os.path.join(uninfected_path, uninfected_img))

# Convert BGR → RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Display side by side
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img1)
plt.title("Parasitized Cell")

plt.subplot(1,2,2)
plt.imshow(img2)
plt.title("Uninfected Cell")

plt.show()