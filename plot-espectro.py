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


import matplotlib.pyplot as plt
from astropy.io import fits
'''
rascunhos e lembretes:
matriz[linha][coluna]
plt.plo(x, y)

NGC5548: z = 0.01627
SDSSJ1430+2303: z = 0.08105
NGC6264: z = 0.03384
NGC3259: z = 0.00560
NGC3982: z = 0.00371
arquivo fit NGC5548 --> 'spec-2127-53859-0085.fits'
arquivo fit SDSSJ1430+2303 --> 'spec-2132-53493-0002.fits'
arquivo fit NGC6264 --> 'spec-1691-53260-0620.fits'
arquivo fit NGC3259 --> 'spec-0489-51930-0193.fits'
arquivo fit NGC3982 --> 'spec-1018-52672-0359.fits'
'''
z = 0.00371  # redshift da galáxia usada
with fits.open('spec-1018-52672-0359.fits') as hdul:
    # hdul.info() # informações sobre o documento.fit
    # specobj = hdul[2].data
    coadd = hdul[1].data

flux = []
wlen = []
em_lines = []
for i in range(len(coadd)):
    flux.append(coadd[i][0]*1e-17)
    wlen.append((10**coadd[i][1])/(z+1))

plt.figure(figsize=(12,4))
plotlines(3.5e3, 9e3, 2.5e-14)
plt.plot(wlen, flux, 'black')
'''
A função plotlines recebe três valores:
- um limite mínimo e um máximo para o x;
    linhas fora desses valores não são plotadas no gráfico.
- e outro valor máximo para o y;
    define a altura máxima das legendas.
'''
plt.xlabel('Wavelength [$\AA$]')
plt.ylabel('Flux Density [erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$]')
plt.title('Galaxy NGC3982 - Seyfert 2 - starburst')
plt.show()
