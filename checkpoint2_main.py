from ODE import *
import matplotlib.pyplot as plt
import numpy as np
from Integrator import *
from operator import add

# This main function is used to find the electric field of a hetero pn junction.
# This discrete function is then integrated to find the potential.

def main():

        # Initialise two top hat objects to represent the charge distribution

    # TopHatODE(height, width, center)

    charge_distribution = pn_junction()

    # Evaluate the top hat functions in the range 0-4 to show charge distribution

    x = [i*0.1 for i in range (0, 40)]
    y = [charge_distribution.evaluate(x[i]) for i in range (0,40)] 


    # Use the analytical integral of the junction to get the exact electric field
    E_exact = [charge_distribution.exact_solution(x[i]) for i in range (0,40)]


    # Do the numerical integrations with the different methods

    # integrate(function to integrate, number of steps, step size, integration method)
    # Integration methods available are euler_method, rk2_method, rk4_method.



    number_of_steps = 20 # Must be int!!!
    step_size = 0.2

    #Euler method

    E_euler = integrate(charge_distribution, number_of_steps, step_size, euler_method)

    #RK2 method
    E_rk2 = integrate(charge_distribution, number_of_steps, step_size, rk2_method)

    #RK4 method
    E_rk4 = integrate(charge_distribution, number_of_steps, step_size, rk4_method)


    #Create discrete function so hold data
    discrete_euler_V = DiscreteFunction(E_euler)
    discrete_rk2_V = DiscreteFunction(E_rk2)
    discrete_rk4_V = DiscreteFunction(E_rk4)

    # Find the negative potential from the discrete function.
    # Note!!!
    # The rk2 and rk4 discrete integrals will not be accurate, as the first_derivative
    # function is called more than once per step.

    V_euler_neg = integrate(discrete_euler_V, number_of_steps, step_size, euler_method)
   # V_rk2_neg = integrate(discrete_rk2_V, number_of_steps, step_size, rk2_method)
   # V_rk4_neg = integrate(discrete_rk4_V, number_of_steps, step_size, rk4_method)

    # Split up the potential coordinates.

    V_euler_neg_x, V_euler_neg_y = zip(*V_euler_neg)
   # V_rk2_neg_x, V_rk2_neg_y = zip(*V_rk2_neg)
   # V_rk4_neg_x, V_rk4_neg_y = zip(*V_rk4_neg)

    # Multiply the y coordinates by -1 to get the actual potential

    V_euler_y = [-1.0 * i for i in V_euler_neg_y]
   # V_rk2_y = [-1.0 * i for i in V_rk2_neg_y]
   # V_rk4_y = [-1.0 * i for i in V_rk4_neg_y]


    # Plot everything

    plt.figure(1)

    plt.subplot(411)
    plt.scatter(x,y)

    
    plt.subplot(412)
    plt.scatter(x, E_exact)
    plt.scatter(*zip(*E_euler), marker = 'x', color = 'r')

    plt.subplot(413)
    plt.scatter(x, E_exact)
    plt.scatter(*zip(*E_rk2), marker = 'x', color = 'g')
    

    plt.subplot(414)
    plt.scatter(x, E_exact)
    plt.scatter(*zip(*E_rk4), marker = 'x', color = 'y')

    plt.show()

    plt.figure(1)

    plt.subplot(111)
    plt.scatter(V_euler_neg_x, V_euler_y)
    
   # plt.subplot(312)
   # plt.scatter(V_rk2_neg_x, V_rk2_y)
    

    #plt.subplot(313)
    #plt.scatter(V_rk4_neg_x, V_rk4_y)
    

    plt.show()


main()
