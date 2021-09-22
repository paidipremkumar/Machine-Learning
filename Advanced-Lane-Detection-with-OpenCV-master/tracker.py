# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:04:04 2017

@author: Ashish
"""
import numpy as np
import cv2

class tracker():
    
    def __init__(self, inWindow_width, inWindow_height, inMargin, ym = 1, xm = 1, smoothF = 1):
        self.recent_centers = []
        self.window_width =  inWindow_width
        self.window_height = inWindow_height
        self.margin = inMargin
        self.ym_ = ym
        self.xm_ = xm
        self.smooth = smoothF
        
    def find_windows_centroids(self,warped):
        window_width = self.window_width
        window_height =  self.window_height
        margin = self.margin
        window_centroids = []
        window = np.ones(window_width)
        
        l_sum = np.sum(warped[int(3*warped.shape[0]/4):,:int(warped.shape[1]/2)], axis=0)
        l_center = np.argmax(np.convolve(window,l_sum))-window_width/2
        r_sum = np.sum(warped[int(3*warped.shape[0]/4):,int(warped.shape[1]/2):], axis=0)
        r_center = np.argmax(np.convolve(window,r_sum))-window_width/2+int(warped.shape[1]/2)
        
       
        window_centroids.append((l_center,r_center))
        
        for level in range(1,(int)(warped.shape[0]/window_height)):
            image_layer = np.sum(warped[int(warped.shape[0]-(level+1)*window_height):int(warped.shape[0]-level*window_height),:], axis=0)
            conv_signal = np.convolve(window, image_layer)
    	    # Find the best left centroid by using past left center as a reference
    	    # Use window_width/2 as offset because convolution signal reference is at right side of window, not center of window
            offset = window_width/2
            l_min_index = int(max(l_center+offset-margin,0))
            l_max_index = int(min(l_center+offset+margin,warped.shape[1]))
            l_center = np.argmax(conv_signal[l_min_index:l_max_index])+l_min_index-offset
        	    # Find the best right centroid by using past right center as a reference
            r_min_index = int(max(r_center+offset-margin,0))
            r_max_index = int(min(r_center+offset+margin,warped.shape[1]))
            r_center = np.argmax(conv_signal[r_min_index:r_max_index])+r_min_index-offset
        	  # Add what we found for that layer
            window_centroids.append((l_center,r_center))
        
        self.recent_centers.append(window_centroids)
        
        return np.average(self.recent_centers[-self.smooth:],axis =0)