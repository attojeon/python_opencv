import scipy.misc
import numpy as np
from PIL import Image

# Image size
width = 640
height = 480
channels = 3

# Create an empty image
#img = np.zeros((height, width, channels), dtype=np.uint8)
img = Image.new('RGB', (width, height), 255)

# Draw something (http://stackoverflow.com/a/10032271/562769)
xx, yy = np.mgrid[:height, :width]
circle = (xx - 100) ** 2 + (yy - 100) ** 2

# Set the RGB values
for y in range(img.size[1]):
    for x in range(img.size[0]):
        r, g, b = circle[y][x], circle[y][x], circle[y][x]
        img[y][x][0] = r
        img[y][x][1] = g
        img[y][x][2] = b

img.from