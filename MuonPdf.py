#Class to implement a random Gaussian generator

import math
import matplotlib.pyplot as plt
import numpy as np
import random

class MuonPdf():

    # initialise muon pdf with lifetime tau

    def __init__(self, tau = 0.0):

        self.tau = tau
        self.normalisation = 1.0/self.tau
        

        # function to evaluate the pdf at point t_point
       
    def evaluateMuonPdf(self, t_point):

        result = self.normalisation * np.exp((-1.0*t_point)/self.tau)
        
        return result

        # function gives the max of pdf 

    def fmax(self):

        fmax = self.evaluateMuonPdf(0.0)

        return fmax
        
        # function to generate random number from exponential pdf. 

    def pullRandMuon(self, upper_bound = 20.0):

        lower_bound = 0.0
        evaluated_random = 0.0
        scaled_random = 0.0
        random_point = 1.0
        
        while (random_point > evaluated_random):

            random_x = np.random.uniform()
            scaled_random_x = lower_bound + (upper_bound - lower_bound)*random_x
            evaluated_random = self.evaluateMuonPdf(scaled_random_x)
        
            random_point = np.random.uniform()*self.fmax()
        

        return scaled_random_x

    
    def integralNumeric(self, lower_limit= -5.0, upper_limit = 5.0):

        #create triangle as area
        #base = upper_limit - lower_limit
        #height = self.fmax() + 1.0
        #area = 0.5*base*height

        #random_point = np.random.uniform()*(upper_limit-lower_limit) + lower_limit

        point_l_x = lower_limit - 1.0
        point_l_y = 0.0
        
        point_c_x = (np.mod(upper_limit)+np.mod(lower_limit))/2.0
        point_c_y = self.fmax() + 1.0

        point_r_x = upper_limit + 1.0
        point_r_y = 0.0

        triangle_point = 0.0
        #if (random_point <= height):
         #   triangle_point = height - np.absolute(random_point)

        # return triangle_point

        #else:
         #   return triangle_point
        

        

        

        




