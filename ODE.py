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
        
