#Integrator.py:
from ODE import *

def euler_method(ODE, point, dx):

    dy = ODE.first_derivative(point) * dx

    return [dx,dy]



def integrate(ODE, n_steps, dx, integration_method):

    results = []
    results.append(ODE.initial_value())

    for i in range (n_steps):
        starting_point = results[i]
        #print("Starting point: {0}".format(starting_point))
        change = integration_method(ODE, starting_point, dx)
        #print("Change: {0}".format(change))
        end_point = [a + b for a,b in zip(starting_point, change)]
        #print("End point: {0}".format(end_point))
        results.append(end_point)

    return results
