from ODE import *
from Coordinates import *
import matplotlib.pyplot as plt
import numpy as np

def main():

    exponential_ode = ExponentialODE()



    print(exponential_ode.first_derivative([0.0, 5.0]))
    print(exponential_ode.initial_value())
    print(exponential_ode.exact_solution(0))

    exponentials = [[i, exponential_ode.exact_solution(i)] for i in range(-50,50)]

    print("Value of function at {0} is {1}".format(exponentials[0][1], exponentials[1]))


    polynomial_ode = PolynomialODE([1.0, -2.0, -3.0, -4.0])

    print(polynomial_ode.first_derivative([1.0,1.0]))
    print(polynomial_ode.initial_value())

    polynomials = [[i,polynomial_ode.exact_solution(i)] for i in range(-50,50)]
    print(polynomials)

    print("Value of function at {0} is {1}".format(polynomials[0][1], polynomials[1]))

    print(polynomial_ode.exact_solution(0))

    sinusoidal_ode = SinusoidalODE()

    print(sinusoidal_ode.first_derivative([1.0,1.0]))
    print(sinusoidal_ode.initial_value())
    print(sinusoidal_ode.exact_solution(1.56))

    plt.figure(1)
    plt.subplot(211)
    plt.plot(*zip(*polynomials))

    plt.subplot(212)
    plt.plot(*zip(*exponentials))
    plt.show()

main()
