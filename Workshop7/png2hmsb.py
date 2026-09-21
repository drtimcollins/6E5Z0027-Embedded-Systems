import numpy as np
from PIL import Image

imageName = "mmuOLED.png"

img = np.array(Image.open(imageName).convert("L"))                         # Read png and convert to greyscale
img = (img > (int(np.max(img))+int(np.min(img)))//2).astype(np.uint8)      # Threshold to convert to 1-bit per pixel
height, width = np.shape(img)                                              # HMSB images must have a width that is
if width % 8 != 0:                                                         # a multiple of 8. Pad image if not so.
    img = np.concatenate((img,np.zeros((height,8-(width % 8)),dtype=np.uint8)),axis=1)
    height, width = np.shape(img)
imgByteGrouped = img.reshape(height, width // 8, 8)                        # Convert groups of 8 pixels into bytes
imgHMSB = np.sum(imgByteGrouped * np.array([1, 2, 4, 8, 16, 32, 64, 128], dtype=np.uint8), axis=2, dtype=np.uint8)

print(f"imgHMSB = bytearray({imgHMSB.tobytes()})")
