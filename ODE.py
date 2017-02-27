import numpy as np
import math

# This module contains classes that define functions as ODEs so they can be integrated.
# Contains classes for exponentials, polynomials, sinusoidals, top hats, Heavisides, discrete functions, and one-offs!

# Class for dealing with exponential ODEs of the form y= exp(kx), such that dy/dx= ky



class ExponentialODE():

    def __init__(self, _k = 1.0):

        self.k = _k

        self.initial_x = 0.0

        self.initial_coordinate = [self.initial_x, self.exact_solution(self.initial_x)]


    # Calculate numerical value of the first derivative

    def first_derivative(self, coordinates):
        return self.k * coordinates[1]


    def initial_value(self):
        return self.initial_coordinate


    def exact_solution(self, x):
        return np.exp(self.k*x)


# Class for dealing with polynomial ODEs of the form y = a + bx + cx^2 + ...

class PolynomialODE():

    def __init__(self, _coefficients):

        self.coefficients = _coefficients
        self.initial_x = 0.0
        self.initial_coordinate = [self.initial_x, self.exact_solution(self.initial_x)]

    # Calculate numerical value of derivative at given x

    def first_derivative(self, coordinates):

        derivative = 0.0

        # Calculate derivative by looping through coefficients.
        # Ignore zeroth power using power+1, and do n-1 interations as a result.
        # Calcaulte n*x^(n-1)

        for power in range(len(self.coefficients)-1):
            derivative += (power+1)*self.coefficients[power+1]*np.power(coordinates[0], float(power))

        return derivative

    # Function to return the initial value

    def initial_value(self):
        return self.initial_coordinate


    # Function to calculate the exact solution.
    # Uses similar method to first_derivative.
    # Loops over powers of and increments derivative value, starting with zeroth power.

    def exact_solution(self, x):

        value = 0.0

        for power in range(len(self.coefficients)):

            value += self.coefficients[power] * np.power(x, float(power))

        return value


# Class to handle sinusoidal ODEs of the form y = sin(kx)

class SinusoidalODE():

    def __init__(self, _k = 1.0):

        self.k = _k
        self.initial_x = 0.0
        self.initial_coordinate = [self.initial_x, self.exact_solution(self.initial_x)]

    def first_derivative(self, coordinates):
        return self.k * math.cos(self.k * coordinates[0])


    def initial_value(self):
        return self.initial_coordinate


    def exact_solution(self, x):
        return math.sin(self.k * x)

# Class to handle top hat functions

class TopHatODE():

    # Initialise with given height, width, and center point.
    # If no arguments, defaults to 1,1,0

    def __init__(self, _height = 1.0, _width = 1.0, _center = 0.0):

        self.height = _height
        self.width = _width
        self.center = _center


        self.initial_x = 0.0
        self.initial_coordinate = [self.initial_x, 0.0]


    # Define the first derivative as the function, using piecewise funtions.

    def first_derivative(self, coordinates):

        half_width = self.width/2.0
        x = coordinates[0] # Get the x component from the coordinate in the form [x,y]

        #tophat = 0.0 # Value of y at given x

        # Returns 0 if outside tophat region
        # Returns height if within tophat region
        # Returns half the height if at the discontinuity

        if ((x > self.center-half_width) and (x < self.center+half_width)):
            return  self.height
        else:
            return 0.0

        if (x < self.center-half_width):
            tophat = 0.0
        if ((x >= self.center-half_width) and (x < self.center+half_width)):
            tophat = self.height
        if (x >= self.center+half_width):
            tophat = 0.0

        if ((x == self.center-half_width) or (x == self.center+half_width)):
            tophat = self.height/2.0



        #return tophat

    # Function to return the initial coordinates of the function (boundary cond.)

    def initial_value(self):
        return self.initial_coordinate


    # Function to set initial coordinate if required.

    def set_initial_coordinate(self, point):
        self.initial_x = point[0]
        self.initial_coordinate = [self.initial_x, point[1]]


    # Function to evaluate the tophat function.
    # Useful for drawing the original function or testing how it looks.

    def evaluate(self, x):

        half_width = self.width/2.0

        if ((x > self.center-half_width) and (x < self.center+half_width)):
            tophat = self.height


        else:
            tophat = 0.0


        return tophat


    # Function to return the exact solution of the integral of the top hat.

    def exact_solution(self, x):

        half_width = self.width/2.0

        y = 0

        # Return constant (0) if x < top hat region
        # Return appropriate ramp function within top hat region
        # Return constant (height) if x > top hat region

        if (x < self.center - half_width):
            y = 0

        if ((x > self.center - half_width) and (x < self.center + half_width)):
            y = self.height*x - (self.height*(self.center-half_width))

        if (x >= self.center + half_width):
            y = self.height


        return y

# Class to create Heaviside functions for integrtion. Similar to half a top hat.

class HeavisideFunction():

    # Initialise with position of discontinuity and height of step.

    def __init__(self, _discontinuity = 0.0 , _height = 1.0):

        self.discontinuity = _discontinuity
        self.height = _height
        self.initial_coordinate = [0.0,0.0]

    def first_derivative(self, coordinates):

        x = coordinates[0]

        if (x < self.discontinuity):
            return 0.0

        if (x > self.discontinuity):
            return self.height

        if (x == self.discontinuity):
            return self.height/2.0




    def initial_value(self):
        return self.initial_coordinate


    def set_initial_coordinate(self, new_coordinate):
        self.initial_coordinate = new_coordinate

    def evaluate(self, x):


        if (x < self.discontinuity):
            y = 0.0

        if (x > self.discontinuity):
            y = self.height

        if (x == self.discontinuity):
            y = self.height/2.0

        return y


    # Function to return the exact solution of the integral of the top hat.

    def exact_solution(self, x):



        # Return constant (0) if x < top hat region
        # Return appropriate ramp function within top hat region
        # Return constant (height) if x > top hat region

        if (x < self.discontinuity):
            return 0.0

        if (x >= self.discontinuity):
            return (self.height*x) - (self.height*self.discontinuity)



# Class to handle integration of discrete functions.

class DiscreteFunction():

    # Initialise with a list of discrete points in the form [[x1,y1], [x2,y2]...]

    def __init__(self, _points):

        self.points = _points
        #self.initial_coordinate = [0,0]

    # Define the first derivative as the value of y at each x points.
    # Takes argument of coordinates list in form [x,y]
    # Last argument __i[0] is mutable variable to enumerate each set of coordinates
    # and keep track of how many times the function's been called.

    def first_derivative(self, coordinates, __i =[0]):


        #print (__i[0])

        coordinates = self.points # Set coordinates to the list of points.

        #print("COORDINATES: {0}".format(coordinates))
        
        y = coordinates[__i[0]][1] # Get y coordinate from list element
        #print("Y::::{0}".format(y))

       
        __i[0]+=1 # Increase the counter by 1 each call
        #print("CHANGING COUNTER!")

       # print("LEN COORD: {0}".format(len(coordinates)))

        # Reset the counter to zero at the end of the list of coordinates.
        if (__i[0] == len(coordinates)):
            __i[0]=0
           # print("REACHED END")

        return y


    # Return the initial coordinates using the first set of points in the list.

    def initial_value(self):
        return self.points[0]


# Class to hand a charge distribution of a heterogeneous pn junction.

class pn_junction():

    def __init__(self, _height= 1.0, _width = 2.0, _center = 2.0):


        self.height = _height
        self.width = _width
        self.center = _center


        self.initial_coordinate = [0.0,0.0]



    def first_derivative(self, coordinates):

        half_width = self.width/2.0

        #print("Centre = {0}, width = {1}, height = {2}".format(self.center, self.width, self.height))


        x = coordinates[0]

        #print("Point: {0}".format(x))

        if (x < (self.center-half_width)):
            return 0.0

        if ((x >= (self.center-half_width)) and (x < self.center)):
            return self.height


        if ((x > self.center) and (x < (self.center+half_width))):
            return -1.0*self.height

        if (x > (self.center+half_width)):
            return 0.0

        if (x == self.center):
            return 0.0





    def initial_value(self):
        return self.initial_coordinate

    def evaluate(self, x):

        half_width = self.width/2.0

        #print("x = :".format(x))

        y = 0

        if ((x >= (self.center-half_width)) and (x < self.center)):
            y = self.height



        if ((x > self.center) and (x <= (self.center+half_width))):
            y = -1.0*self.height

        return y

    def exact_solution(self, x):

        half_width = self.width/2.0

        y = 0.0

        if ((x >= (self.center-half_width)) and (x < self.center)):

            y = x - (self.center-half_width)

        if (x == self.center):

            y = self.height

        if ((x > self.center) and (x <= self.center + half_width)):

            y = (-1.0 * x) + (self.center+half_width)


        return y
