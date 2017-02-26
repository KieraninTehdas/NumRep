from ODE import *
import matplotlib.pyplot as plt
import numpy as np
from Integrator import *
from operator import add

def main():


    t1 = TopHatODE(1.0, 1.0, 1.5)
    t2 = TopHatODE(-1.0, 1.0, 2.5)

    x = [i*0.1 for i in range (0, 40)]
    y1 = [t1.evaluate(x[i]) for i in range (0,40)]
    y2 = [t2.evaluate(x[i]) for i in range (0,40)]

    y = map(add, y1, y2)


    exact1 = [t1.exact_solution(x[i]) for i in range(len(x))]
    exact2 = [t2.exact_solution(x[i]) for i in range(len(x))]

    #print(exact1)
    #print(exact2)
    exact_y = map(add, exact1, exact2)



    #t2.set_initial_coordinate([0.0, 0.0])

    h1 = integrate(t1, 20, 0.2, euler_method)
    h2 = integrate(t2, 20, 0.2, euler_method)


    h1x, h1y = zip(*h1)
    h2x, h2y = zip(*h2)

    hx = h1x + h2x

    hy = map(add, h1y, h2y)
    h = zip(h1x, hy)



    rk2_1 = integrate(t1, 20, 0.2, rk2_method)
    rk2_2 = integrate(t2, 20, 0.2, rk2_method)

    rk2_1x, rk2_1y = zip(*rk2_1)
    rk2_2x, rk2_2y = zip(*rk2_2)

    rk2_y = map(add, rk2_1y, rk2_2y)
    rk2 = zip(rk2_1x, rk2_y)

    rk4_1 = integrate(t1, 40, 0.1, rk4_method)
    rk4_2 = integrate(t2, 40, 0.1, rk4_method)

    #print(rk4_1)
    #print(rk4_2)

    rk4_1x, rk4_1y = zip(*rk4_1)
    rk4_2x, rk4_2y = zip(*rk4_2)

    rk4_y = map(add, rk4_1y, rk4_2y)
    rk4 = zip(rk4_1x, rk4_y)

    discrete1 = DiscreteFunction(h)


    #print(h)
    #print(h[0])
    VE_neg_euler = integrate(discrete1, 21, 0.2, euler_method)


    VE_neg_euler_x, VE_neg_euler_y = zip(*VE_neg_euler)

    print("TOTAL:{0}".format(VE_neg_euler_y))
    V_euler = [-1.0 * i for i in VE_neg_euler_y]
    print("V = {0}".format(V_euler))


    discrete_rk2 = DiscreteFunction(rk2)
    VE_neg_rk2 = integrate(discrete_rk2, 21, 0.2, rk2_method)


    VE_neg_rk2_x, VE_neg_rk2_y = zip(*VE_neg_rk2)


    print("TOTAL:{0}".format(VE_neg_rk2_y))
    V_rk2 = [-1.0 * i for i in VE_neg_rk2_y]
    print("V = {0}".format(V_rk2))


    discrete_rk4 = DiscreteFunction(rk4)
    VE_neg_rk4 = integrate(discrete_rk4, 21, 0.2, rk4_method)


    VE_neg_rk4_x, VE_neg_rk4_y = zip(*VE_neg_rk4)



    print("TOTAL:{0}".format(VE_neg_rk4_y))
    V_rk4 = [-1.0 * i for i in VE_neg_rk4_y]
    print("V = {0}".format(V_rk4))

    plt.figure(1)

    plt.subplot(411)
    plt.scatter(x,y)

    plt.subplot(412)
    plt.scatter(*zip(*h))
    plt.plot(x, exact_y)

    plt.subplot(413)
    plt.scatter(*zip(*rk2))
    plt.plot(x, exact_y)

    plt.subplot(414)
    plt.scatter(*zip(*rk4))
    plt.plot(x, exact_y)

    plt.show()

    plt.figure(1)
    plt.subplot(411)
    #plt.scatter(*zip(*VE_neg_euler))
    #plt.scatter(*zip(*VE_neg_rk2), marker = 'x', color='r')
    #plt.scatter(*zip(*VE_neg_rk4), marker = 'v', color = 'y')
    plt.scatter(VE_neg_euler_x, V_euler, marker = 'v', color = 'b')
    plt.scatter(VE_neg_rk2_x, V_rk2, marker = 'v', color = 'g')
    plt.scatter(VE_neg_rk4_x, V_rk4, marker = 'v', color = 'y')

    plt.show()
main()
