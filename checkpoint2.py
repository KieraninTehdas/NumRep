from ODE import *
from Coordinates import *
import matplotlib.pyplot as plt
import numpy as np
from Integrator import *

def main():

    top_hat = TopHatODE(1, 1, 1.5)
    top_hat2 = TopHatODE(-1,1, 2.5)

    x1 = [i*0.1 for i in range (0,20)]
    y1 = [top_hat.evaluate(x1[i]) for i in range (len(x1))]
    #print("{0}, {1}".format(x,y))

    x2 = [i*0.1 for i in range (20,40)]
    y2 = [top_hat2.evaluate(x2[i]) for i in range (len(x2))]

    x = x1+x2
    y = y1+y2
    charge_distribution = zip(x,y)

    #electric_field1 = integrate(top_hat, ) 

    plt.figure(1)

    #plt.subplot(311)
    plt.scatter(*zip(*charge_distribution))
    plt.show()
main()
