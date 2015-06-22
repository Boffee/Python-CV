from PIL import Image
from pylab import *
from random import randint
import parentpath
import os

file_path = os.path.join(parentpath.DATA_DIR, 'empire.jpg')

# read image to array
im = array(Image.open(file_path).convert('L'))

# plot the image
imshow(im)

# size of image
y, x = im.shape

# set plot size
ylim([y-1, 0])
xlim([0, x-1])

print 'Please click 3 points'
coord = ginput(3)
print 'you clicked:', coord

# plot the points with red pentagon-markers with dashed lines
plot(coord, '--rp')

# add title and show the plot
title ('Plotting: "empire.jpg"')

# create a new grayscale figure
figure()
gray()

# countour map
contour(im, origin='image')
axis('equal')
axis('off')

# histogram of the pixels with 128 bins
figure()
hist(im.flatten(), 128)

# show all figures
show()

