#Integrator.py:
from ODE import *

def euler_method(ODE, point, dx):

    dy = ODE.first_derivative(point) * dx

    return [dx,dy]

def rk2_method(ODE, point, dx):


    mid_point = [point[0] + (dx/2.0), point[1] + (dx/2.0)* ODE.first_derivative(point)]
    dy = ODE.first_derivative(mid_point) * dx

    return [dx,dy]

def rk4_method(ODE, point, dx):

    k1 = ODE.first_derivative(point)
    k2 = ODE.first_derivative([point[0] + (dx/2.0), point[1] + (dx*k1)/2.0])
    k3 = ODE.first_derivative([point[0] + (dx/2.0), point[1] + (dx*k2)/2.0])
    k4 = ODE.first_derivative([point[0] + dx, point[1] + (dx*k3)])

    #print("Point: {0}".format(point))

    dy = dx*(1.0/6.0)*(k1 + (2.0*k2) + (2.0*k3) + k4)

    return [dx, dy]

def integrate(ODE, n_steps, dx, integration_method):

    results = []
    results.append(ODE.initial_value())

    for i in range (n_steps):
        starting_point = results[i]
        #print("Starting point: {0} Step: {1}".format(starting_point,i))
        change = integration_method(ODE, starting_point, dx)
        #print("Change: {0}".format(change))
        end_point = [a + b for a,b in zip(starting_point, change)]
        #print("End point: {0}".format(end_point))
        results.append(end_point)

    return results

def discrete_integration(discrete_points):

    for i in range(len(discrete_points)-1):
        print(len(discrete_points))
        dy = discrete_points[i+1][1] - discrete_points[i][1]
        print("dy {0}".format(dy))
        dx = discrete_points[i+1][0] - discrete_points[i][0]
        print("dx {0}".format(dx))

        return(dy/dx)
