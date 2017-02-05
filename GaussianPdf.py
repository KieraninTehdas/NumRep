#Class to implement a random Gaussian generator

import math
import matplotlib.pyplot as plt
import numpy as np
import random

class GaussianPdf():

    # initialise with mean and sigma (width)

    def __init__(self, mean = 0.0, sigma = 5.0):

        self.mean = mean
        self.sigma = sigma
        self.normalisation = 1.0/(self.sigma * math.sqrt(2.0*math.pi))
        

       
    def evaluateGaussian(self, x_point):

        result = self.normalisation * np.exp(-0.5 * ((x_point - self.mean)/self.sigma)**2) 
        
    
        return result

    def fmax(self):

        fmax = self.evaluateGaussian(self.mean)

        return fmax

    def pullRandGauss(self, lower_bound = -5.0, upper_bound = 5.0):

        evaluated_random = 0.0
        scaled_random = 0.0
        random_point = 1.0
        
        while (random_point > evaluated_random):

            random_x = np.random.uniform()
            scaled_random_x = lower_bound + (upper_bound - lower_bound)*random_x
            evaluated_random = self.evaluateGaussian(scaled_random_x)
        
            random_point = np.random.uniform()*self.fmax()
        

        return scaled_random_x

    
    def integralNumeric(self, lower_limit= -5.0, upper_limit = 5.0):

        #create triangle as area
        base = upper_limit - lower_limit
        height = self.fmax() + 1.0
        area = 0.5*base*height

        random_point = np.random.uniform()*(upper_limit-lower_limit) + lower_limit
        triangle_point = 0.0
        if (random_point <= height):
            triangle_point = height - np.absolute(random_point)

            return triangle_point

        else:
            return triangle_point
        

        

        

        




