# -*- coding: utf-8 -*-
# Correctly Blurring png file but not jpg file

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread('sample.jpg')
plt.imshow(img)

# Parameters 
f = 3
n_H = img.shape[0]
n_W = img.shape[1] 
n_C = img.shape[2]
stride = 1
pad = int((f-1)/2) 

# filter
blur_filter = np.ones((f,f), np.float)/(f*f)
#vertical_edge_detector = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
#vertical_edge_detector = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
#horizontal_edge_detector = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

def conv_forward(input_img, blur_filter):
    """
    Arguments:
    input_img -- numpy array of shape (n_H, n_W, n_C)
    blur_filter -- filter, numpy array of shape (f, f, n_C)
        
    Returns:
    Z -- conv output, numpy array of shape (n_H, n_W, n_C)
    """ 
        
    # Initialize the output volume Z with zeros. 
    Z = np.zeros(shape=(n_H, n_W, n_C))
    
    # Create input_padded_img by padding input_img
    input_padded_img = np.pad(input_img, ((pad,pad),(pad,pad),(0,0)), 'constant', constant_values=(0,0))

    for h in range(n_H):                            # loop over vertical axis of the output volume
        for w in range(n_W):                        # loop over horizontal axis of the output volume
            for c in range(n_C):                    # loop over channels (= #filters) of the output volume
                
                # Find the corners of the current "slice" (≈4 lines)
                vert_start = h*stride
                vert_end = vert_start+f
                horiz_start = w*stride
                horiz_end = horiz_start+f
                
                # Use the corners to define the (2D) slice of a_prev_pad. 
                img_slice = input_padded_img[vert_start:vert_end, horiz_start:horiz_end,c]
                
                # Convolve the (2D) slice with the blur filter to get back one output neuron. 
                # Single step convolution step
                Z[h, w, c] = np.sum(np.multiply(img_slice, blur_filter))
                                        
    return Z

blur = conv_forward(img, blur_filter)
plt.imshow(blur)
mpimg.imsave('sampleBlur.jpg', blur)
