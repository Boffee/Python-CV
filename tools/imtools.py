import os
from PIL import Image
from numpy import *

JPG = '.jpg'
PNG = '.png'


def get_imlist(path):
    """
    Returns a list of filenames for all jpg images in a director.
        :param:  path (string) - directory containing files
    """

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]



def imresize(im, size):
    """
    Resize an image array using PIL.
        :param:  im (NumPy array) - image matrix
                 size ((int, int)) - resize dimension
        :return: resized im
    """
    return array(Image.fromarray(uint8(im)).resize(size))



def histeq(im, nbr_bins=256):
    """
    Histogram equalization of a grayscale image.
        :param:  im (NumPy array) - grayscale image matrix
                 nbr_bins (uint) - number of bins
        :return: im2 (Numpy array) - equalized grayscale image matrix
                 cdf (list) - discrete cumulative distribution
    """

    # get image histogram
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum() # cumlative distribution function
    cdf = 255 * cdf / (cdf[-1]) # normalize

    # use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(), bins[:-1], cdf)
    im2 = uint8(im2.reshape(im.shape))

    return im2, cdf



def compute_average(imlist):
    """
    Compute the average of a list of images.
        :param:  imlist (list of strings) - list of paths to images
        :return: avg_im (NumPy array) - average of im list
    """

    # open first image and make into array of float
    averageim = array(Image.open(imlist[0]), 'f')

    list_size = 1 # number of images used in average image

    # sum the rgb values for each pixel of the images in the list
    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
            avg_size += 1
        except:
            print imname + '...skipped'
    averageim /= list_size

    return uint8(averageim)



def _all2format(path, format):
    """
    Convert all image files in a directory to a given image format.
        :param:  path (string) - directory containing images
                 format (string) - image format (e.g. '.jpg' '.png')
        :return: -
    """
    # list of all files in the given directory
    filelist = os.listdir(path)

    for infile in os.listdir(path):
        outfile = os.path.splitext(infile)[0] + format
        if outfile not in filelist:
            try:
                infile = os.path.join(path, infile)
                outfile = os.path.join(path, outfile)
                Image.open(infile).save(outfile)
            except IOError:
                print "cannot convert", infile



def all2jpg(path):
    """
    convert all image files in a directory to jpg.
        :param:  path (string) - directory containing images
        :return: - 
    """
    _all2format(path, JPG)



def all2png(path):
    """
    convert all image files in a directory to png.
        :param:  path (string) - directory containing images
        :return: - 
    """
    _all2format(path, PNG)

