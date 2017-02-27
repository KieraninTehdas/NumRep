#Integrator.py:
# Module of functions that can be used to numerically integrate functions.
# Contains functions to integrate using Euler, Runge-Kutta 2 & 4 as well as
# function to do the actual integration.
from ODE import *

# Euler method of integration.
# Derivative evaluated at start.
# Returns change as list.

def euler_method(ODE, point, dx):

    dy = ODE.first_derivative(point) * dx

    #print("Point in euler: {0}".format(point))

    return [dx,dy]

# RK2 integration method. Uses midpoint gradient.
# Returns change as list.

def rk2_method(ODE, point, dx):


    mid_point = [point[0] + (dx/2.0), point[1] + (dx/2.0)* ODE.first_derivative(point)]
    dy = ODE.first_derivative(mid_point) * dx

    #print("Point in rk2: {0}".format(point))

    return [dx,dy]

# RK4 integration method. Uses gradients at several points.
# Returns change as list.

def rk4_method(ODE, point, dx):

    x = point[0]
    y = point[1]

    k1 = ODE.first_derivative(point)
    k2 = ODE.first_derivative([x + (dx/2.0), y + (dx*k1)/2.0])
    k3 = ODE.first_derivative([x + (dx/2.0), y + (dx*k2)/2.0])
    k4 = ODE.first_derivative([x + dx, y + (dx*k3)])

    #print("Point in rk4: {0}".format(point))
    #print("k1 = {0}, k2 = {1}, k3 = {2}, k4 = {3}".format(k1,k2,k3,k4))
    dy = dx*(k1/6.0 + k2/3.0 + (k3/3.0) + k4/6.0)
    #print("dy = {0}".format(dy))
    return [dx, dy]


# Function to actually do the numerical integration.
# Integration method is supplied as an argument.


def integrate(ODE, n_steps, dx, integration_method):

    results = [] # Create a list to hold the integrated points.
    results.append(ODE.initial_value()) # Add the initial value to the list.

    # Do the integration numerically.
    # Given a starting point from the last element of the list, calculate change
    # according to given integration method, calculate next point and add to list.

    for i in range (n_steps):
        starting_point = results[i]
        #print("Starting point: {0} Step: {1}".format(starting_point,i))
        change = integration_method(ODE, starting_point, dx)
        #print("Change: {0}".format(change))
        end_point = [a + b for a,b in zip(starting_point, change)]
        #print("End point: {0}".format(end_point))
        results.append(end_point)

    return results
