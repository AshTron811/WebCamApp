# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:47:47 2021

@author: DELL
"""

import cv2
cap=cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow('Img', img)
    cv2.waitKey(1)
