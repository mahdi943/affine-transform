import cv2 as cv
import numpy as np

# Loading image
src = cv.imread('input.jpg')
if src is None:
    print('Could not open or find the image input.jpg')
    exit(0)
    
# Reading Scale Affine matrix
warp_mat = np.loadtxt('matrix.txt')
warp_mat = np.float32(warp_mat.flatten()[:6].reshape(2,3))

# Affine Transforming
warp_dst = cv.warpAffine(src, warp_mat, (src.shape[0], src.shape[1]))

# Defining Rotating Affine matrix after Scale Warp
center = (warp_dst.shape[1]//2, warp_dst.shape[0]//2)
angle = -30
scale = 0.9
rot_mat = cv.getRotationMatrix2D( center, angle, scale )
warp_rotate_dst = cv.warpAffine(warp_dst, rot_mat, (warp_dst.shape[1], warp_dst.shape[0]))

# Showing and saving outputs
cv.imshow('Source image', src)
cv.imshow('Warp', warp_dst)
cv.imshow('Warp + Rotate', warp_rotate_dst)
cv.imwrite('output.jpg', warp_rotate_dst)
cv.waitKey(0)
