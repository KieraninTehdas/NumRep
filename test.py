import math
import matplotlib.pyplot as plt
import numpy as no
from GaussianPdf import GaussianPdf
import pylab

def main():


    gauss = GaussianPdf(0.0, 1.0)
    #print(gauss.max())
    gauss_data = []
    n_points = 10000

    gauss_data = [gauss.pullRandGauss() for i in range(n_points)]

    triangle_data = [gauss.integralNumeric() for i in range(n_points)]
        
    #print([gauss_data[i] for i in range (0, 1000)])
        
    plt.hist(gauss_data, bins = 50)
    plt.show()
    

main()
