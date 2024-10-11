##counting stars from the sky picture

from pyexpat import features
import matplotlib.pyplot as plt
import skimage.data as skdata
from skimage import feature 
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

#example_file = glob.glob(r"C:\Users\HP 840 G1\Desktop\wint_sky.gif")[0]
example_file = glob.glob(r"C:\Users\HP 840 G1\Desktop\n_stars.jpg")[0]
im = imread(example_file, as_gray=True)
plt.imshow(im,cmap='gray')
plt.show()

blobs_log = feature.blob_log(im, max_sigma=30, num_sigma=10, threshold=.0000000001)
# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
numrows = len(blobs_log)
print("Number of stars counted : " ,numrows)

fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap='gray')
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='red', linewidth=1, fill=False)
    ax.add_patch(c)
plt.show()