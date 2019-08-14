#????????
# -*- coding: utf-8 -*-

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread('ClearImg.jpg')
plt.imshow(img)

# Parameters 
f = 3
n_H = img.shape[0]
n_W = img.shape[1] 
n_C = img.shape[2]
stride = 1
padding = 1

# filter
blur_filter = np.ones((f,f,n_C), np.float)/(f*f*n_C)

def zero_pad(input_img, pad):
    """    
    Argument:
    input_image -- python numpy array of shape (n_H, n_W, n_C)
    pad -- integer, amount of padding around each image on vertical and horizontal dimensions
    
    Returns:
    input_padded_img -- padded image of shape (n_H + 2*pad, n_W + 2*pad, n_C)
    """

    input_padded_img = np.pad(input_img, ((pad,pad),(pad,pad),(0,0)), 'constant', constant_values=(0,0))
    
    return input_padded_img

'''
blur = zero_pad(img, 1500)
plt.imshow(blur)
'''
 
def conv_single_step(img_slice, blur_filter):
    """  
    Arguments:
    img_slice -- slice of input data of shape (f, f, n_C)
    blur_filter -- filter contained in a window - matrix of shape (f, f, n_C)
    
    Returns:
    Z -- a scalar value, result of convolving the sliding window on a slice x of the input data
    """

    # Element-wise product then sum between img_slice and blur_filter 
    Z = np.sum(np.multiply(img_slice, blur_filter))
    
    return Z
    
def conv_forward(input_img, blur_filter):
    """
    Arguments:
    input_padded_img -- numpy array of shape (n_H, n_W, n_C)
    blur_filter -- filter, numpy array of shape (f, f, n_C)
        
    Returns:
    Z -- conv output, numpy array of shape (n_H, n_W, n_C)
    """ 
        
    # Initialize the output volume Z with zeros. 
    Z = np.zeros(shape=(n_H, n_W, n_C))
    
    # Create A_prev_pad by padding A_prev
    input_padded_img = zero_pad(input_img, 1)

    for h in range(n_H):                            # loop over vertical axis of the output volume
        for w in range(n_W):                        # loop over horizontal axis of the output volume
            for c in range(n_C):                    # loop over channels (= #filters) of the output volume
                
                # Find the corners of the current "slice" (≈4 lines)
                vert_start = h*stride
                vert_end = vert_start+f
                horiz_start = w*stride
                horiz_end = horiz_start+f
                
                # Use the corners to define the (3D) slice of a_prev_pad (See Hint above the cell). 
                a_slice = A[vert_start:vert_end, horiz_start:horiz_end,:]
                
                # Convolve the (3D) slice with the correct filter W and bias b, to get back one output neuron. 
                Z[h, w, c] = conv_single_step(a_slice, W[:,:,:,c])
                                        
    
    # Making sure your output shape is correct
    assert(Z.shape == (n_H, n_W, n_C))
    
    return Z

blur = conv_forward(img, blur_filter)
