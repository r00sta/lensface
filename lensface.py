#!/usr/bin/env python3

'''
LensFace Module

Required packages -

python3
opencv (and python bindings)
numpy

'''

import cv2 as cv
import numpy as np


def make_gauss(centre, amp, sig, shapdim):

    '''just makes a Gaussian centred on chosen coordinates to
    use as the grav potential in the field'''

    sidelenx = shapdim[1]
    sideleny = shapdim[0]
    hx = int(sidelenx/2)
    hy = int(sideleny/2)
    l = np.zeros(shapdim)

    ceny = centre[1] * sideleny
    cenx = centre[0] * sidelenx

    for i in range(0, sideleny):

        for j in range(0, sidelenx):

            l[i, j] = np.sqrt((ceny-i)**2+(cenx-j)**2)

    gaussblob = amp*np.exp(-(l**2)/sig)

    iter = 0
    radius = 0
    while (iter < sidelenx) :
        if (gaussblob[hy][hx+iter] < 0.1*gaussblob[hy][hx]) :
            radius = iter
            break
        else :
            iter += 1

    return gaussblob, int(radius)


def calc_tranform(grad, lenx, leny):

    newxpos=np.zeros(lenx*leny, dtype=int)
    newypos=np.zeros(lenx*leny, dtype=int)

    index = 0

    for i in range(0, lenx):

        for j in range(0, leny):

            newxpos[index]=i-int(grad[1][i][j]) % lenx
            newypos[index]=j-int(grad[0][i][j]) % leny
            index+=1

    return (newxpos, newypos)
