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

    def first_derivative(self, x):

        derivative = 0.0

        for power in range(len(self.coefficients)-1):
            derivative += (power+1)*self.coefficients[power+1]*np.power(x, float(power))

        return derivative

class Exponential():

    def __init__(self, k = 1.0, c = 1.0):

        self.k = k
        self.c = c


    def evaluate(self, x):

        return np.exp(self.k*x)+self.c

    def first_derivative(self, x):

        return self.k*np.exp(self.k*x)


class SinusoidalProduct():

    def __init__(self, k1 = 1.0, k2 = 3.0):

        self.k1 = k1
        self.k2 = k2


    def evaluate(self, x):

        return np.cos(self.k1*x)*np.sin(self.k2*x)


    def first_derivative(self, x):

        return self.k1*-1.0*np.sin(self.k1*x)*np.sin(self.k2*x) + np.cos(self.k1*x)*self.k2*np.cos(self.k2*x)



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

    max_iterations = 1000000

    if (len(root_boundaries) == 0):
        return "No solutions found in specified range."

    for i in range(len(root_boundaries)):

        iteration_number = 0

        x_lower = root_boundaries[i][0]
        x_upper = root_boundaries[i][1]

        while (iteration_number < max_iterations):

            x_center = x_lower + (x_upper-x_lower)/2.0

            if (function.evaluate(x_center) == 0 or x_upper-x_lower < accuracy):
                roots.append(x_center)
                print("Found root at {0} with bisection after {1} iterations!".format(roots[i], iteration_number))
                break

            iteration_number += 1

            if (np.sign(function.evaluate(x_center)) == np.sign(function.evaluate(x_lower))):
                x_lower = x_center

            else:
                x_upper = x_center


            if (iteration_number == max_iterations-1):
                print("Did not find root in specified range within {0} iterations...".format(max_iterations))

    return roots


def Newton_Raphson_find_root(function, x_lower, x_upper, n_steps, accuracy):

    root_boundaries = find_root_boundaries(function, x_lower, x_upper, n_steps)
    roots = []



    max_iterations = 1000000

    for i in range(len(root_boundaries)):

        x_lower = root_boundaries[i][0]
        x_upper = root_boundaries[i][1]



        x0 = x_lower



        iteration_number = 0

        while (iteration_number < max_iterations):
            y = function.evaluate(x0)
            y_prime = function.first_derivative(x0)

            if (abs(y_prime) < 0.0000001):
                print("Does not converge!")
                break


            x1 = x0 - (y/y_prime)


            if (abs(function.evaluate(x1)) < accuracy):
                print("Found root at {0} with Newton-Raphson after {1} iterations!".format(x1, iteration_number))
                roots.append(x1)
                break



            x0 = x1
            iteration_number += 1

    return roots



def secant_find_root(function, x_lower, x_upper, n_steps, accuracy):

    root_boundaries = find_root_boundaries(function, x_lower, x_upper, n_steps)
    roots = []

    max_iterations = 1000000

    for i in range(len(root_boundaries)):

        x1 = root_boundaries[i][0]
        x2 = root_boundaries[i][1]

        iteration_number = 0

        while (iteration_number < max_iterations):

            y1 = function.evaluate(x1)
            y2 = function.evaluate(x2)

            x3 = x2 - (y2*((x1-x2)/(y1-y2)))

            if (abs(function.evaluate(x3)) < accuracy):
                print("Found root at {0} with Secant after {1} iterations!".format(x1, iteration_number))
                roots.append(x1)
                break

            x1 = x2
            x2 = x3

            iteration_number += 1

    return roots


def brent_find_roots(function, x_lower, x_upper, n_steps, accuracy):

    root_boundaries = find_root_boundaries(function, x_lower, x_upper, n_steps)
    roots = []

    max_iterations = 1000000

    for i in range(len(root_boundaries)):

        x1 = root_boundaries[i][0]
        x2 = root_boundaries[i][1]

        x3 = x1

        iteration_number = 0

        isLastIterationBisection = True

        while (iteration_number < max_iterations):

            y1 = function.evaluate(x1)
            y2 = function.evaluate(x2)
            y3 = function.evaluate(x3)

            if (y1 != y3 and y2 != y3):

                quad1 = (x1*y2*y3)/((y1-y2)*(y1-y3))
                quad2 = (x2*y1*y3)/((y2-y1)*(y2-y3))
                quad3 = (x3*y1*y2)/((y3-y1)*(y3-y2))

                solution = quad1 + quad2 + quad3

            else:

                solution = x2 - (y2*((x2-x1)/(y2-y1)))


            # If current solution isn't in desired range, use bisection method
            if ((solution > ((3*x1+x2)/4)) and (solution < x2)):
                condition1 = False
            else:
                condition1 = True

            if ((isLastIterationBisection) and (abs(solution-x2) >= abs(x2-x3)/2.0)):
                condition2 = True
            else:
                condition2 = False

            if ((isLastIterationBisection == False) and (abs(solution-x2)>=abs(x3-x4)/2.0)):
                condition3 = True
            else:
                condition3 = False

            if ((isLastIterationBisection == True) and (abs(x2-x3)<abs(accuracy))):
                condition4 = True
            else:
                condition4 = False

            if ((isLastIterationBisection == False) and (abs(x3-x4)<abs(accuracy))):
                condition5 = True
            else:
                condition5 = False

            if ((condition1) or (condition2) or (condition3) or (condition4) or (condition5)):

                solution = (x1+x2)/2.0
                isLastIterationBisection = True

            else:

                isLastIterationBisection = False

            y_solution = function.evaluate(solution)

            if(abs(y_solution)<abs(accuracy)):
                print("Root found at {0} with Brent after {1} iterations!".format(solution, iteration_number))
                roots.append(solution)
                break

            x4 = x3
            x3 = x2

            iteration_number += 1

            if (np.sign(y_solution) == y1):
                x1 = solution
            else:
                x2 = solution
