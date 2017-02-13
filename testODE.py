from ODE import *

def main():

    exponential_ode = ExponentialODE()

    
        
    print(exponential_ode.first_derivative([0.0, 5.0]))
    print(exponential_ode.initial_value())
    print(exponential_ode.exact_solution(0))

    
    polynomial_ode = PolynomialODE([5.0, 2.0, 3.0, 4.0])

    print(polynomial_ode.first_derivative([1.0,1.0]))
    print(polynomial_ode.initial_value())
    print(polynomial_ode.exact_solution(0))

    sinusoidal_ode = SinusoidalODE()

    print(sinusoidal_ode.first_derivative([1.0,1.0]))
    print(sinusoidal_ode.initial_value())
    print(sinusoidal_ode.exact_solution(1.56))

main()
