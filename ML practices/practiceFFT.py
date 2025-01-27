import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2,fftshift
from skimage import data, color

image = color.rbg2gray(data.astronaut())

imageFFT = fft2(image)
imageFFTshifted = fftshift(imageFFT)