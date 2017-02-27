from ODE import *
import matplotlib.pyplot as plt
import numpy as np
from Integrator import *
from operator import add

def main():

    # Initialise two top hat objects to represent the charge distribution

    # TopHatODE(height, width, center)

    t1 = TopHatODE(1.0, 1.0, 1.5)
    t2 = TopHatODE(-1.0, 1.0, 2.5)

    # Evaluate the top hat functions in the range 0-4 to show charge distribution

    x = [i*0.1 for i in range (0, 40)]
    y1 = [t1.evaluate(x[i]) for i in range (0,40)]
    y2 = [t2.evaluate(x[i]) for i in range (0,40)]

    # Add the y coordinates of the two top hats to get the total charge distribution

    charge_distribution = map(add, y1, y2)

    # Use the analytical integral of the top hat to get the exact electric field

    exact_E1 = [t1.exact_solution(x[i]) for i in range(len(x))]
    exact_E2 = [t2.exact_solution(x[i]) for i in range(len(x))]

    # Add the y coords of the exact electric fields to get total electric field

    exact_Ey = map(add, exact_E1, exact_E2)



    # Do the numerical integrations with the different methods

    # integrate(function to integrate, number of steps, step size, integration method)
    # Integration methods available are euler_method, rk2_method, rk4_method.

    # Integrate over the two regions, keep nsteps/size of step same for each pair!

    number_of_steps = 20 # Must be int!!!
    step_size = 0.2

    #Euler method

    euler_1 = integrate(t1, number_of_steps, step_size, euler_method)
    euler_2 = integrate(t2, number_of_steps, step_size, euler_method)

    # Unpack the (x,y) integration output into two flat lists, x and y.

    euler_1x, euler_1y = zip(*euler_1)
    euler_2x, euler_2y = zip(*euler_2)

    # Combine the y's for the two regions and rezip into (x,y) list

    euler_Ey = map(add, euler_1y, euler_2y)
    euler_E = zip(euler_1x, euler_Ey)


    # RK2 method

    rk2_1 = integrate(t1, number_of_steps, step_size, rk2_method)
    rk2_2 = integrate(t2, number_of_steps, step_size, rk2_method)

    rk2_1x, rk2_1y = zip(*rk2_1)
    rk2_2x, rk2_2y = zip(*rk2_2)

    rk2_y = map(add, rk2_1y, rk2_2y)
    rk2_E = zip(rk2_1x, rk2_y)


    # RK4 method

    rk4_1 = integrate(t1, number_of_steps, step_size, rk4_method)
    rk4_2 = integrate(t2, number_of_steps, step_size, rk4_method)

    rk4_1x, rk4_1y = zip(*rk4_1)
    rk4_2x, rk4_2y = zip(*rk4_2)

    rk4_y = map(add, rk4_1y, rk4_2y)
    rk4_E = zip(rk4_1x, rk4_y)

    # Plot everything

    plt.figure(1)

    plt.subplot(411)
    plt.scatter(x,charge_distribution)

    plt.subplot(412)
    plt.plot(x, exact_Ey)
    plt.scatter(*zip(*euler_E))

    plt.subplot(413)
    plt.plot(x, exact_Ey)
    plt.scatter(*zip(*rk2_E))

    plt.subplot(414)
    plt.plot(x, exact_Ey)
    plt.scatter(*zip(*rk4_E))

    plt.show()


main()
