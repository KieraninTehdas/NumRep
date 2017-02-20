from ODE import *
from Coordinates import *
import matplotlib.pyplot as plt
import numpy as np
from Integrator import *

def main():

    exponential_ode = ExponentialODE()



    print(exponential_ode.first_derivative([0.0, 5.0]))
    print(exponential_ode.initial_value())
    print(exponential_ode.exact_solution(0))

    exponentials = [[i, exponential_ode.exact_solution(i)] for i in range(0,3)]

    print("Value of function at {0} is {1}".format(exponentials[0][0], exponentials[0]))


    polynomial_ode = PolynomialODE([1.0, -6.0, 3.0])


    #print(polynomial_ode.first_derivative([1.0,1.0]))
    print(polynomial_ode.initial_value())

    polynomials = [[i,polynomial_ode.exact_solution(i)] for i in range(0,5)]
    #print(polynomials)

    print("Value of function at {0} is {1}".format(polynomials[1][0], polynomials[1]))

    print(polynomial_ode.exact_solution(0))

    sinusoidal_ode = SinusoidalODE()

    print(sinusoidal_ode.first_derivative([1.0,1.0]))
    print(sinusoidal_ode.initial_value())
    print(sinusoidal_ode.exact_solution(1.56))

    sins = [[i, sinusoidal_ode.exact_solution(i)] for i in range(0,21)]

    #Integrator.integrate(polynomial_ode, 100, Integrator.euler_method(polynomial_ode, polynomial_ode.initial_value, 1.0))
    integrated = integrate(polynomial_ode, 160, 0.025, euler_method)
    integrated_exp = integrate(exponential_ode, 10, 0.2, euler_method)
    integrated_sins = integrate(sinusoidal_ode, 400, 0.05, euler_method)

    plt.figure(1)
    plt.subplot(311)
    plt.plot(*zip(*polynomials))
    plt.plot(*zip(*integrated), linestyle = '', marker = 'x')


    plt.subplot(312)
    plt.plot(*zip(*exponentials))
    plt.plot(*zip(*integrated_exp), linestyle = '', marker = 'x')
    #plt.show()

    plt.subplot(313)
    plt.plot(*zip(*sins))
    plt.plot(*zip(*integrated_sins), linestyle = '', marker = 'x')
    plt.show()

main()
