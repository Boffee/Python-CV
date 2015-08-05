from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
import parentpath

STD = 4

im = array(Image.open(parentpath.DATA_DIR + '/empire.jpg'))
im2 = zeros(im.shape)

for i in range(3):
	im2[:,:,i] = filters.gaussian_filter(im[:,:,i], STD)
im2 = uint8(im2)

figure()
subplot(1,2,1)
imshow(im)
subplot(1,2,2)
imshow(im2)
show()