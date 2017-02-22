import numpy as np
import math

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

    def __init__(self, _height = 1.0, _width = 1.0, _center = 0.0):

        self.height = _height
        self.width = _width
        self.center = _center


        self.initial_x = self.center - (self.width/2.0)
        self.initial_coordinate = [self.initial_x, 0.0]

    def first_derivative(self, coordinates):

        half_width = self.width/2.0

        boxcar = self.height * (0.5*(1+np.sign(coordinates[0]-(self.center-half_width)))
        - 0.5*(1+np.sign(coordinates[0]-(self.center+half_width))))

        return boxcar

    def initial_value(self):
        return self.initial_coordinate


    def set_boundary_point(self, point):
        self.initial_x = point[0]
        self.initial_coordinate = [self.initial_x, point[1]]
        

    def evaluate(self, x):

        half_width = self.width/2.0

        boxcar = self.height * 0.5*((1+np.sign(x-(self.center-half_width)))
        - 1.5*(1+np.sign(x-(self.center+half_width))))
       
    
        return boxcar


class pn_junction(): 

    def __init__(self, _height= 1.0, _width = 2.0, _center = 2.0):


        self.height = _height
        self.width = _width
        self.center = _center


        self.initial_coordinate = [0.0,0.0]

    def first_derivative(self, coordinates):

        half_width = self.width/2.0

        print("Centre = {0}, width = {1}, height = {2}".format(self.center, self.width, self.height))

        charge_distribution = 0
        #x = coordinates[0]
        x = coordinates
        print("Point: {0}".format(x))
        if ((x > (self.center-half_width)) and (x < self.center)):
            charge_distribution = self.height
            print("1-2: {0}".format(charge_distribution))
        if ((x > self.center) and (x < (self.center+half_width))):
            charge_distribution = -1.0*self.height
            print("2-3: {0}".format(charge_distribution))
            
        return charge_distribution


    def initial_value(self):
        return self.initial_coordinate
