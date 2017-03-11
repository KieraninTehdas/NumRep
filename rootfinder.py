import numpy as np
from functions import *
import matplotlib.pyplot as plt



def main():



    x_poly = np.linspace(-5.0, 5.0, 20)

    poly1 = Polynomial([10.2, -7.4, -2.1, 1])


    y_poly = [poly1.evaluate(i) for i in x_poly]
    #print(poly1)


    x_exp = np.linspace(-3.0, 3.0, 20)

    exp1 = Exponential(1.0, -2.0)

    y_exp = [exp1.evaluate(i) for i in x_exp]




    x_sinusoidal = np.linspace(-3.0, 3.0, 100)

    sinusoidal1 = SinusoidalProduct()

    y_sinusoidal = [sinusoidal1.evaluate(i) for i in x_sinusoidal]


    #print("Polynomial roots = {0}".format(bisection_find_root(poly1, -10.0, 10.0, 10, 0.000000001)))
    #print("exp bounding regions = {0}".format(find_root_boundaries(exp1, -10, 10, 100)))
    #print("Exponential roots = {0}".format(bisection_find_root(exp1, 3, 10, 10, 0.000000001)))
    #print("Sinusoudal roots = {0}".format(bisection_find_root(sinusoidal1, -3.0, 3.0, 100, 0.000000001)))

    #print(Newton_Raphson_find_root(poly1, -10.0, 10.0, 10, 0.000000001))
    #print(Newton_Raphson_find_root(exp1, -10.0, 10.0, 10, 0.000000001))
    #print(Newton_Raphson_find_root(sinusoidal1, -3.0, 3.0, 2, 0.000000001))

    #print(secant_find_root(poly1, -10.0, 10.0, 10, 0.000000001))
    #print(secant_find_root(exp1, -10.0, 10.0, 10, 0.000000001))
    #print(secant_find_root(sinusoidal1, -3.0, 3.0, 2, 0.000000001))

    plt.subplot(311)
    plt.scatter(x_poly, y_poly)

    plt.subplot(312)
    plt.scatter(x_exp, y_exp)

    plt.subplot(313)
    plt.scatter(x_sinusoidal, y_sinusoidal)
    plt.show()



main()
