import matplotlib.pyplot as plt
import numpy as np


def absorption():
    abslines = np.loadtxt('absorptionLines.txt', dtype=('str', 'str'), usecols=(0, 3), unpack=True)
    abs_w = []
    abs_n = []
    for i in range(len(abslines[0])):
        abs_w.append(float(abslines[0][i]))
        abs_n.append(abslines[1][i])
    return abs_w, abs_n


def emission():
    emslines = np.loadtxt('emissionLines.txt', dtype=('str', 'str'), usecols=(0, 3), unpack=True)
    ems_w = []
    ems_n = []
    for i in range(len(emslines[0])):
        ems_w.append(float(emslines[0][i]))
        ems_n.append(emslines[1][i])
    return ems_w, ems_n


def sky():
    skylines = np.loadtxt('skyLines.txt', dtype=('str', 'str'), usecols=(0, 3), unpack=True)
    sky_w = []
    sky_n = []
    for i in range(len(skylines[0])):
        sky_w.append(float(skylines[0][i]))
        sky_n.append(skylines[1][i])
    return sky_w, sky_n


def plotlines(xlimmin, xlimmax, ymax):
    ems_lines = emission()
    abs_lines = absorption()
    c = 0.5
    for k in range(len(ems_lines[0])):
        if ems_lines[0][k] >= xlimmin:
            if c == 2.5: c = 0.5
            plt.axvline(x=ems_lines[0][k], color='gray', linestyle=':')
            plt.text(ems_lines[0][k], ymax-0.15*c*ymax, ems_lines[1][k], color='red')#, rotation='vertical')#, backgroundcolor='white')
            c += 0.5
    c = 3.5
    for j in range(len(abs_lines[0])):
        if xlimmin <= abs_lines[0][j] <= xlimmax:
            if c == 5.5: c = 3.5
            plt.axvline(x=abs_lines[0][j], color='gray', linestyle=':')
            plt.text(abs_lines[0][j], ymax-0.1*c*ymax, abs_lines[1][j], color='blue')#, rotation='vertical')#, backgroundcolor='white')
            c += 0.5
    return
