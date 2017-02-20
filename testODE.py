from ODE import *
from Coordinates import *
import matplotlib.pyplot as plt
import numpy as np
from Integrator import *

def main():

    exponential_ode = ExponentialODE()



#    print(exponential_ode.first_derivative([0.0, 5.0]))
#    print(exponential_ode.initial_value())
#    print(exponential_ode.exact_solution(0))

    exponentials = [[i, exponential_ode.exact_solution(i)] for i in range(0,21)]

#    print("Value of function at {0} is {1}".format(exponentials[0][0], exponentials[0]))


    polynomial_ode = PolynomialODE([1.0, -6.0, 3.0])


    #print(polynomial_ode.first_derivative([1.0,1.0]))
    #print(polynomial_ode.initial_value())

    polynomials = [[i,polynomial_ode.exact_solution(i)] for i in range(0,21)]
    #print(polynomials)

    #print("Value of function at {0} is {1}".format(polynomials[1][0], polynomials[1]))

    #print(polynomial_ode.exact_solution(0))

    sinusoidal_ode = SinusoidalODE()

    #print(sinusoidal_ode.first_derivative([1.0,1.0]))
    #print(sinusoidal_ode.initial_value())
    #print(sinusoidal_ode.exact_solution(1.56))

    sins = [[i, sinusoidal_ode.exact_solution(i)] for i in range(0,21)]

    #Integrator.integrate(polynomial_ode, 100, Integrator.euler_method(polynomial_ode, polynomial_ode.initial_value, 1.0))
    integrated = integrate(polynomial_ode, 40, 0.5, euler_method)
    integrated_exp = integrate(exponential_ode, 20, 1., euler_method)
    integrated_sins = integrate(sinusoidal_ode, 20, 1., euler_method)

    rk_integrated_poly = integrate(polynomial_ode, 40, 0.5, rk2_method)
    rk_integrated_exp = integrate(exponential_ode, 20, 1.0, rk2_method)
    rk_integrated_sin = integrate(sinusoidal_ode, 20, 1.0, rk2_method)

    rk4_integrated_poly = integrate(polynomial_ode, 40, 0.5, rk4_method)
    rk4_integrated_exp = integrate(exponential_ode, 20, 1.0, rk4_method)
    rk4_integrated_sin = integrate(sinusoidal_ode, 20, 1.0, rk4_method)

#    print(rk2_method(polynomial_ode, [0,0], 2))


    plt.figure(1)
    plt.subplot(311)
    plt.scatter(*zip(*polynomials))
    plt.plot(*zip(*integrated), linestyle = '', marker = 'x')
    plt.plot(*zip(*rk_integrated_poly), linestyle = '', marker = 'x', c = 'r')
    plt.plot(*zip(*rk4_integrated_poly), linestyle = '', marker = 'x', c = 'g')

    plt.subplot(312)
    plt.scatter(*zip(*exponentials))
    plt.plot(*zip(*integrated_exp), linestyle = '', marker = 'x')
    plt.plot(*zip(*rk_integrated_exp), linestyle = '', marker = 'x', c = 'r')
    plt.plot(*zip(*rk4_integrated_exp), linestyle = '', marker = 'x', c = 'g')
    #plt.show()

    plt.subplot(313)
    plt.scatter(*zip(*sins))
    plt.plot(*zip(*integrated_sins), linestyle = '', marker = 'x')
    plt.plot(*zip(*rk_integrated_sin), linestyle = '', marker = 'x', c = 'r')
    plt.plot(*zip(*rk4_integrated_sin), linestyle = '', marker = 'v', c = 'g')
    plt.show()

main()
