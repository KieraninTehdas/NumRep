from ODE import *
import matplotlib.pyplot as plt
import numpy as np
from Integrator import *
from operator import sub

def main():

    charge_distribution = pn_junction()

    coordinates = [[i*0.01,0] for i in range (0,401)]
    x = [i*0.01 for i in range (0,401)]
    y = [charge_distribution.first_derivative(coordinates[i]) for i in range (len(coordinates))]


    electric_field_exact_y = [charge_distribution.exact_solution(x[i]) for i in range (len(x))]
    electric_field_exact = zip(x, electric_field_exact_y)
    #print(electric_field_exact)
    electric_field_euler = integrate(charge_distribution, 20, 0.2, euler_method)
    electric_field_rk2 = integrate(charge_distribution, 20, 0.2, rk2_method)
    electric_field_rk4 = integrate(charge_distribution, 20, 0.2, rk4_method)

    #euler_y = [b for a,b in electric_field_euler]
    #rk2_y = [b for a,b in electric_field_rk2]
    #rk4_y = [b for a,b in electric_field_rk4]
    #residual_euler = [a-b for a,b in zip(electric_field_exact_y, euler_y)]
    #residual_rk2 = [a-b for a,b in zip(electric_field_exact_y, rk2_y)]
    #residual_rk4 = [a-b for a,b in zip(electric_field_exact_y, rk4_y)]



    plt.figure(1)

    plt.subplot(411)
    plt.scatter(x,y)

    plt.subplot(412)
    plt.scatter(*zip(*electric_field_euler))
    plt.plot(*zip(*electric_field_exact))

    plt.subplot(413)
    plt.scatter(*zip(*electric_field_rk2))
    plt.plot(*zip(*electric_field_exact))

    plt.subplot(414)
    plt.scatter(*zip(*electric_field_rk4))
    plt.scatter(*zip(*electric_field_exact), marker = 'x')

    plt.show()
'''
    plt.subplot(515)
    plt.scatter(x,residual_euler, marker ='v')
    plt.scatter(x,residual_rk2, marker ='v', color = 'g')
    plt.scatter(x,residual_rk4, marker ='v', color = 'y')
'''



main()
