#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 mjirik <mjirik@hp-mjirik>
#
# Distributed under terms of the MIT license.

"""

"""

import logging
logger = logging.getLogger(__name__)
import argparse

import model
import tracker
import sys
import os.path as op
import numpy as np
import matplotlib.pyplot as plt
import glob


def loop(gray_img, bm, tr):
    """
    Tato funkce je prováděna v každém cyklu
    """
    # 1.část
    bm.add_frame(gray_img)
    model = bm.get_model()
    img_without_background = gray_img - model
    
    # 2.část
    tr.track_in_frame(img_without_background)


def main():
    """
    Metoda spustí sledování kvasinek. Na začátku rozhodne, zda je na vstupu
    soubor s videem, nebo adresář s obrázky s příponou .jpg. Podle toho je pak
    zařízeno načítání jednotlivých framů.
    """

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "../../kvasinky1.avi"

    debug = False
    if len(sys.argv) > 2:
        debug = True


    # prostor pro inicializaci
    # 1.část
    bm = model.BackgroundModel()
    # 2.část
    tr = tracker.Tracker()



    if op.isfile(filename):
        # Nacitani videa pomoci opencv
        import cv2
        cap = cv2.VideoCapture(filename)
        while(cap.isOpened()):

            ret, frame = cap.read()
            if ret:
                gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                loop(gray_img, bm, tr)
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        # Nacitani jpg pomoci scipy
        import scipy
        import scipy.misc
        import skimage
        import skimage.color

        files = files = sorted(glob.glob(op.join(filename, '*.jpg')))
        for filename in files:
            img = scipy.misc.imread(filename)
            gray_img = skimage.color.rgb2gray(img)
            loop(gray_img, bm, tr)

    tr.saveCsvFile()


if __name__ == "__main__":
    main()
