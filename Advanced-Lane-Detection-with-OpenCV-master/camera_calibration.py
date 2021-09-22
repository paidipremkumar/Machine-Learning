# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:47:38 2017

@author: Ashish
"""

import os
import numpy as np
import cv2
import matplotlib.image as mpimg
import pickle

dir_ =  "camera_cal\\"
cal_imgs  = os.listdir('camera_cal')

        
 # Empty Arrays to store object (3D) and image (2D) points 
objpts = []
imgpts = []
mtx = []
dist = []
nx = 9
ny = 6

#Zero Object Points based on nx and ny
objp = np.zeros((nx*ny,3), np.float32)
#Generate "Known" Coordinates
objp[:,:2] =  np.mgrid[0:nx,0:ny].T.reshape(-1,2)

# get corners and Object Points
for imgs in cal_imgs:
    img = mpimg.imread(dir_+imgs)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
    if ret == True:
        imgpts.append(corners)
        objpts.append(objp)

# Undistort
def cal_undistort(img, objpoints, imgpoints):
    global mtx, dist
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    dst = cv2.undistort(img, mtx, dist, None, mtx)
    return dst

# Runs through multiple images and undistorts
# For Demo purposes
def cal_list(imgs, objpts, imgpts):
    dir_ =  "camera_cal\\"
    nImgs = []
    for i in range(0,len(imgs)):
        img = mpimg.imread(dir_+imgs[i])
        dst = cal_undistort(img, objpts, imgpts)
        nImgs.append(dst)
        mpimg.imsave('./chessboard_undist/output'+str(i)+'.png',dst)
    return nImgs

c = cal_list(cal_imgs, objpts, imgpts)
    
calibration_data_pickle = {}
calibration_data_pickle["mtx"] = mtx
calibration_data_pickle["dist"] = dist
pickle.dump( calibration_data_pickle, open("./calibration_pickle.p", "wb"))
