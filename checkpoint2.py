from ODE import *
import matplotlib.pyplot as plt
import numpy as np
from Integrator import *

def main():

    top_hat1 = TopHatODE(1, 1, 1.5)
    top_hat2 = TopHatODE(-1,1, 2.5)
    top_hat2.set_boundary_point([2,0])

    junction = pn_junction()

    x1 = [i*0.1 for i in range (0,20)]
    y1 = [top_hat1.evaluate(x1[i]) for i in range (len(x1))]
    #print("{0}, {1}".format(x,y))

    x2 = [i*0.1 for i in range (20,40)]
    y2 = [top_hat2.evaluate(x2[i]) for i in range (len(x2))]

    x = x1+x2
    y = y1+y2
    charge_distribution = zip(x,y)
    #print(charge_distribution)
    
    xp = [i*0.1 for i in range (0,40)]
    yp = [junction.first_derivative(xp[i]) for i in range (len(xp))]
    

    electric_field1 = integrate(top_hat1, 40, 0.1, euler_method)
    electric_field2 = integrate(top_hat2, 40, 0.1, euler_method)
    #print(electric_field1)
    #print(electric_field2)
    electric_field = electric_field1 + electric_field2
    #print(electric_field)

    e_field = integrate(junction, 400, 0.01, euler_method)




    plt.figure(1)

    plt.subplot(411)
    plt.scatter(*zip(*charge_distribution))

    plt.subplot(412)
    plt.scatter(*zip(*electric_field))

    plt.subplot(413)
    plt.scatter(xp,yp)

    plt.subplot(414)
    plt.scatter(*zip(*e_field))

    plt.show()
main()
