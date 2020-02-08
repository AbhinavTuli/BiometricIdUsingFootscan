import random
from PIL import Image
from PIL import ImageFilter
img = Image.open('0000215_L_01.tif').convert('L')
threshold=80
img = img.point(lambda p: p > threshold and 255) 
cordinate = x, y = 151, 200
pixels=img.load()
# print(pixels[0,0])

#sort the boundary
for i in range(img.size[0]): 
    for j in range(img.size[1]):
        if i<10 or j<10:
            pixels[i,j]=0

l = []


img = img.filter(ImageFilter.MedianFilter(size = 3))
img = img.filter(ImageFilter.MedianFilter(size = 3))
img = img.filter(ImageFilter.MedianFilter(size = 3))

img = img.filter(ImageFilter.FIND_EDGES())
pixels=img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i,j] == 255:
            l.append([i,j])
#        if i<img.size[0] and i>=0 & j<img.size[1] and j>=0 and pixels([i][j])==255:

# img = img.filter(ImageFilter.FIND_EDGES)

img.save('greyscale2.png')