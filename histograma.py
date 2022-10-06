import matplotlib.pyplot as plt
import tifffile as tf
import numpy as np

im = tf.imread('Cassino.tif')
nbin = 8
tam_im = (len(im), len(im[0]))
tx_am = 1

hstg_r = np.zeros(2**nbin)
hstg_g = np.zeros(2**nbin)
hstg_b = np.zeros(2**nbin)

for i in range(0,tam_im[0],tx_am):
    for j in range(0,tam_im[1],tx_am):
        hstg_r[im[i][j][0]] = hstg_r[im[i][j][0]] + 1
        hstg_g[im[i][j][1]] = hstg_g[im[i][j][1]] + 1
        hstg_b[im[i][j][2]] = hstg_b[im[i][j][2]] + 1

x = np.array(range(1,2**nbin))

fig, (axs) = plt.subplots(nrows = 2, ncols = 3) 

axs[0, 0].plot(hstg_r, color='red')
axs[0, 1].plot(hstg_g, color='green')
axs[0, 2].plot(hstg_b, color='blue')

p01 = axs[1,0].imshow(im[:,:,0], interpolation='bilinear', cmap='gray')
p02 = axs[1,1].imshow(im[:,:,1], interpolation='bilinear', cmap='gray')
p03 = axs[1,2].imshow(im[:,:,2], interpolation='bilinear', cmap='gray')


plt.show()
