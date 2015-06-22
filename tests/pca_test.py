from PIL import Image
from numpy import *
from pylab import *
import os
import parentpath
from tools import pca
from tools import imtools

# directory containing font 'a' images
im_dir = os.path.join(parentpath.DATA_DIR, 'a_thumbs')
imlist = imtools.get_imlist(im_dir) # get a list of file names
imlist = imlist[:100]
im = array(Image.open(imlist[0])) # open one image to get size
m,n = im.shape[:2] # get the size of the image
imlist_size = len(imlist) # get the number of images

# store flattened images in a matrix
immatrix = array([array(Image.open(imname)).flatten()
    for imname in imlist], 'f')

# perform PCA
V, S, immean = pca.pca(immatrix)

# show mean and first 15 figures
figure()
gray()
axis('off')
subplot(4, 4, 1)
imshow(immean.reshape(m, n))
for i in range(15):
    subplot(4,4,i+2)
    imshow(V[i].reshape(m, n))

show()
