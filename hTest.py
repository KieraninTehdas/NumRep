from ODE import *
import matplotlib.pyplot as plt
import numpy as np
from Integrator import *
from operator import add

def main():




    x = [i*0.05 for i in range (0, 80)]

    h1 = HeavisideFunction(1.0, 1.0)
    h2 = HeavisideFunction(2.0, -2.0)
    h3 = HeavisideFunction(3.0, 1.0)
    yh1 = [h1.exact_solution(x[i]) for i in range (0,80)]
    yh2 = [h2.exact_solution(x[i]) for i in range (0,80)]
    yh3 = [h3.exact_solution(x[i]) for i in range (0,80)]
    h1rk2 = integrate(h1, 20, 0.2, rk2_method)
    h1rk4 = integrate(h1, 20, 0.2, rk4_method)
    h2rk2 = integrate(h2, 20, 0.2, rk2_method)
    h2rk4 = integrate(h2, 20, 0.2, rk4_method)
    h3rk2 = integrate(h3, 20, 0.2, rk2_method)
    h3rk4 = integrate(h3, 20, 0.2, rk4_method)

    h1rk2x, h1rk2y = zip(*h1rk2)
    h2rk2x, h2rk2y = zip(*h2rk2)
    h3rk2x, h3rk2y = zip(*h3rk2)

    hrkya = map(add, h1rk2y, h2rk2y)
    hrk2y = map(add, hrkya, h3rk2y)
    hrk2 = zip(h1rk2x, hrk2y)

    h1rk4x, h1rk4y = zip(*h1rk4)
    h2rk4x, h2rk4y = zip(*h2rk4)
    h3rk4x, h3rk4y = zip(*h3rk4)
    hrk4ya = map(add, h1rk4y, h2rk4y)
    hrk4y = map(add, hrk4ya, h3rk4y)
    hrk4 = zip(h1rk4x, hrk4y)

    discreteh1_rk2 = DiscreteFunction(h1rk2)
    vh1 = integrate(discreteh1_rk2, 10, 0.4, rk2_method)

    junction = pn_junction()

    y = [junction.exact_solution(x[i]) for i in range (0,80)]

    yj = [junction.evaluate(x[i]) for i in range (0,80)]

    euler = integrate(junction, 20, 0.2, euler_method)
    rk2j = integrate(junction, 20, 0.2, rk2_method)
    rk4j = integrate(junction, 20, 0.2, rk4_method)

    discrete_rk2 = DiscreteFunction(rk2j)
    V = integrate(discrete_rk2, 20, 0.2, rk2_method)
    discrete_euler = DiscreteFunction(euler)
    VE = integrate(discrete_euler, 20, 0.2, euler_method)
    plt.figure(1)

    plt.subplot(411)
    plt.plot(x, yh1)
    plt.scatter(*zip(*h1rk2), marker = 'x', color = 'g')
    plt.scatter(*zip(*h1rk4), marker = 'x', color = 'r')


    plt.subplot(412)
    plt.plot(x, yh2)
    plt.scatter(*zip(*h2rk2), marker = 'x', color = 'g')
    plt.scatter(*zip(*h2rk4), marker = 'x', color = 'r')


    plt.subplot(413)
    plt.plot(x, yh3)
    plt.scatter(*zip(*h3rk2), marker = 'x', color = 'g')
    plt.scatter(*zip(*h3rk4), marker = 'x', color = 'r')

    plt.subplot(414)
    plt.plot(x,y)
    plt.scatter(*zip(*hrk2), marker = 'x')
    plt.scatter(*zip(*hrk4), marker = 'x', color = 'g')

    plt.show()
main()
