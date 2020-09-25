# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:11:40 2019

@author: Varad Srivastava
"""

import os
import glob

import cv2

source_directory = 'F:/WORK/PROJECTS/IITJodhpur/ProjectHumanDetection/SlimYOLOimplementation/Dataset/VisDrone2019-DET-val/VisDrone2019-DET-val/images'

image_filenames = glob.glob(os.path.join(source_directory, '*.jpg'))
for img_fname in image_filenames:
    annotation_fname = img_fname.replace('.jpg', '.txt')
    img = cv2.imread(img_fname, cv2.IMREAD_COLOR)
    height, width, chans = img.shape
    # read the initial lines in the txt
    with open(annotation_fname, 'r') as f:
        annotations = f.read().strip().split('\n')
    # split them on commas ','
    annotations = [x.split(',') for x in annotations]
    annotations = [x[0:8] for x in annotations ]
    with open(annotation_fname.replace('.txt', '.txt'), 'w') as f:
        for ann in annotations:
            xmin, ymin, xwidth, yheight, score, cat, trunc, occ = ann
            x_ctr = (int(xmin) + (int(xwidth) / 2)) / width
            y_ctr = (int(ymin) + (int(yheight) / 2)) / height
            f.write('{cat} {x_ctr} {y_ctr} {width} {height}'.format(cat=cat, x_ctr=x_ctr, y_ctr=y_ctr, width=(int(xwidth) / float(width)), height=(int(yheight)/float(height))))
            f.write('\n')