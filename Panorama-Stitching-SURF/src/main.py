"""
Final Project of Computer Vision Class 1551534 Yunxin Sun
Implementation of SURF
Please refer to https://link.springer.com/content/pdf/10.1007/11744023_32.pdf
Usage: python main.py [-h] [--help] [-s] [--show] img1 img2 [dest]
"""

import argparse
import sys
import os.path
import cv2
import matplotlib.pyplot as plt
import numpy as np


def parseArgs():
    """
    parse Args
    Usage: [-h] [--help] [-s] [--show] img1 img2 [dest]
    """
    parser = argparse.ArgumentParser(
        description='This program can stitch two images together using SURF algorithm.')
    parser.add_argument("img1", help="the first image file url you want to stitch together")
    parser.add_argument("img2", help="the second image file url you want to stitch together")
    parser.add_argument("--show", "-s", help="show the result immediately",
                        action="store_true")
    parser.add_argument("dest",
                        help="the result image file url you want to save,\
                        the default value is dest.png",
                        default="dest.png", nargs='?', const=1)
    return parser.parse_args()


def findKPandDES(image):
    """
    find keypoints and features of an image
    """
    surf = cv2.xfeatures2d.SURF_create(400)
    return surf.detectAndCompute(image, None)


def match(descrip1, descrip2):
    """
    Match two sets of interesting points
    """
    FLANN_INDEX_KDTREE = 0
    indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    searchParams = dict(checks=50)
    flann = cv2.FlannBasedMatcher(indexParams, searchParams)
    match = flann.knnMatch(descrip1, descrip2, k=2)
    good_match = []
    for _, (m, n) in enumerate(match):
        if m.distance < 0.75 * n.distance:
            good_match.append(m)
    return good_match


def stitch(kp1, kp2, img1, img2, good_match):
    """
    Stitch two Images together
    """
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_match]).reshape(-1, 1, 2)
    dest_pts = np.float32([kp2[m.trainIdx].pt for m in good_match]).reshape(-1, 1, 2)
    M, _ = cv2.findHomography(src_pts, dest_pts, cv2.RANSAC, 5.0)
    warpImg = cv2.warpPerspective(img2, np.linalg.inv(M),
                                  (img1.shape[1] + img2.shape[1],
                                   max(img1.shape[0], img2.shape[0])))
    warpImg[0:img1.shape[0], 0:img1.shape[1]] = img1
    return warpImg


def main():
    """
    Main Function
    """
    args = parseArgs()
    if (not os.path.isfile(args.img1) or not os.path.isfile(args.img2)):
        print("Image Read Error!")
        sys.exit(1)
    img1 = cv2.imread(args.img1)
    img2 = cv2.imread(args.img2)
    kp1, descrip1 = findKPandDES(img1)
    kp2, descrip2 = findKPandDES(img2)
    MIN = 10
    good_match = match(descrip1, descrip2)
    if len(good_match) > MIN:
        result = stitch(kp1, kp2, img1, img2, good_match)
        cv2.imwrite(args.dest, result)
        if args.show:
            plt.imshow(result)
            plt.show()
    else:
        print("Not enough matches!")
        sys.exit(1)
main()
