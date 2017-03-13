# Tests root finding methods. Can implement, bisection, secant, Newton-Raphson, and Brent methods

import numpy as np
from functions import *
import matplotlib.pyplot as plt



def main():


    # Create linearly spaced points in x
    x_poly = np.linspace(-5.0, 5.0, 20)

    # Create a polynomial with the appropriate coefficients
    poly1 = Polynomial([10.2, -7.4, -2.1, 1])

    # Evaluate for drawing
    y_poly = [poly1.evaluate(i) for i in x_poly]
    #print(poly1)

    # Create linearly spaced points in x
    x_exp = np.linspace(3.0, 6.0, 20)


    # Create appropriate exponential of form exp(k1*x)+k2
    exp1 = Exponential(1.0, -2.0)

    y_exp = [exp1.evaluate(i) for i in x_exp]




    x_sinusoidal = np.linspace(-3.0, 3.0, 100)

    # Create sinusoidal cos(k1x)sin(k2x) with default values of k1 = 1, k2 =3
    # Can add arguments to set k1, k2.
    sinusoidal1 = SinusoidalProduct()

    y_sinusoidal = [sinusoidal1.evaluate(i) for i in x_sinusoidal]

    #oneOver = OneOverX()

    #y_oneOver = [oneOver.evaluate(i) for i in x_poly]

    # Find roots by bisection. Call a particular root finding method, supply a function, lower range, upper range, spacing of points between bounds, and desired accuracy
    
    print("------------------------------------------------------")
    print("Finding roots of polynomial by bisection!")
    print("Polynomial roots = {0}".format(bisection_find_root(poly1, -10.0, 10.0, 10, 0.000000001)))
    print("------------------------------------------------------")
    print("Finding roots of exponential by bisection!")
    #print("exp bounding regions = {0}".format(find_root_boundaries(exp1, -10, 10, 100)))
    print("Exponential roots = {0}".format(bisection_find_root(exp1, -10, 10, 10, 0.000000001)))
    print("------------------------------------------------------")
    print("Finding roots of sinusoidal by bisection!")
    print("Sinusoudal roots = {0}".format(bisection_find_root(sinusoidal1, -3.0, 3.0, 100, 0.000000001)))
    print("------------------------------------------------------")


    # Find roots by N-R. Same function arguments as bisection

    print("Finding roots of polynomial by Newton-Raphson!")
    print(Newton_Raphson_find_root(poly1, -10.0, 10.0, 10, 0.000000001))
    print("------------------------------------------------------")
    print("Finding roots of exponential by Newton-Raphson!")
    print("------------------------------------------------------")
    print(Newton_Raphson_find_root(exp1, -10.0, 10.0, 10, 0.000000001))
    print("------------------------------------------------------")
    print("Finding roots of sinusoidal by Newton-Raphson!")
    print(Newton_Raphson_find_root(sinusoidal1, -3.0, 3.0, 100, 0.000000001))
    print("------------------------------------------------------")

    # Find roots with secant method. Same function arguments as bisection
    print("Finding roots of polynomial by secant!")
    print(secant_find_root(poly1, -10.0, 10.0, 10, 0.000000001))
    print("------------------------------------------------------")
    print("Finding roots of exp by secant!")
    print(secant_find_root(exp1, -10.0, 10.0, 10, 0.000000001))
    print("------------------------------------------------------")
    print("Finding roots of sinusoidal polynomial by secant!")
    print(secant_find_root(sinusoidal1, -3.0, 3.0, 100, 0.000000001))
    print("------------------------------------------------------")


    # Use Brent's hybrid method

    print("Finding roots of polynomial by Brent!")
    print(brent_find_root(poly1, -10.0, 10.0, 10, 0.000000001))
    print("------------------------------------------------------")
    print("Finding roots of exp by Brent!")
    print(brent_find_root(exp1, -10.0, 10.0, 10, 0.000000001))
    print("------------------------------------------------------")
    print("Finding roots of sinusoidal by Brent!")
    print(brent_find_root(sinusoidal1, -3.0, 3.0, 100, 0.000000001))
    print("------------------------------------------------------")

    #print("OneOver roots = ", brent_find_root(oneOver, -10.0, 10.0, 20, 0.00000001))

    plt.subplot(311)
    plt.scatter(x_poly, y_poly)

    plt.subplot(312)
    plt.scatter(x_exp, y_exp)

    plt.subplot(313)
    plt.scatter(x_sinusoidal, y_sinusoidal)
    plt.show()



main()
