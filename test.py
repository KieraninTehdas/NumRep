import math
import matplotlib.pyplot as plt
import numpy as np
from GaussianPdf import GaussianPdf
import pylab

def main():


    gauss = GaussianPdf(0.0, 1.0)
    #print(gauss.max())
    gauss_x_data = []
    n_points = 10000

    gauss_x_data = [gauss.pullRandGauss() for i in range(n_points)]
    
    gauss_y_data = [gauss.evaluateGaussian(gauss_x_data[i]) for i in range(len(gauss_x_data))]
    #triangle_data = [gauss.integralNumeric() for i in range(n_points)]

    #print([gauss_data[i] for i in range (0, 1000)])

    tri_x = [-6.0,0.0,6.0]
    tri_y = [0.0,gauss.fmax()+1.0,0]
    random_x = []
    random_y =[]

    for i in range(n_points):
        r1 = np.random.uniform()
        r2 = np.random.uniform()
        
        
        a = (1-np.sqrt(r1))*tri_x[0] + (np.sqrt(r1)*(1-r2))*tri_x[1] + (r2*np.sqrt(r1))*tri_x[2]
        b = (1-np.sqrt(r1))*tri_y[0] + (np.sqrt(r1)*(1-r2))*tri_y[1] + (r2*np.sqrt(r1))*tri_y[2]

        random_x.append(a)
        random_y.append(b)

        



    plt.scatter(tri_x, tri_y)
    plt.scatter(gauss_x_data, gauss_y_data)
    #plt.scatter(random_x, random_y)
    #plt.show()
    #plt.hist(gauss_data, bins = 50)
    plt.show()


main()
