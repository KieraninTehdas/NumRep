import numpy as np
import math as mt


class Polynomial():

    def __init__(self, coefficients):
        
        self.coefficients = coefficients

    def evaluate(self, x):
            
        val = 0.
        for power in range(len(self.coefficients)):
            val+= self.coefficients[power]*mt.pow(x,float(power))
        
        return val


class Exponential():

    def __init__(self, k = 1.0, c = 1.0):

        self.k = k
        self.c = c


    def evaluate(self, x):

        return np.exp(self.k*x)+self.c
        

class SinusoidalProduct():

    def __init__(self, k1 = 1.0, k2 = 3.0):

        self.k1 = k1
        self.k2 = k2


    def evaluate(self, x):

        return np.cos(self.k1*x)*np.sin(self.k2*x)






def find_root_boundaries(function, x_lower, x_upper, n_steps):

    points = np.linspace(x_lower, x_upper, n_steps)

    roots = []

    for i in range(len(points)-1):
        
        y1 = function.evaluate(points[i])
        y2 = function.evaluate(points[i+1])

        if (np.sign(y1) != np.sign(y2)):
            
            roots.append([points[i], points[i+1]])

    return roots

    
def bisection_find_root(function, x_lower, x_upper, n_steps, accuracy):


    root_boundaries = find_root_boundaries(function, x_lower, x_upper, n_steps)
    roots = []

    for i in range(len(root_boundaries)):


        

        x_lower = root_boundaries[i][0]
        x_upper = root_boundaries[i][1]

        x_center = x_lower + (x_upper-x_lower)/2.0
            
        while ((x_lower-x_center) < accuracy):

            f_center = function.evaluate(x_center)
            if (f_center <= accuracy):
                roots.append(x_center)
                break

            else:

                if (np.sign(f_center) == np.sign(function.evaluate(x_lower))):
                    x_lower = x_center


                elif (np.sign(f_center) == np.sign(function.evaluate(x_upper))):
                    x_upper = x_center

    return roots
