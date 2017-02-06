#Class to implement a random Gaussian generator

import math
import matplotlib.pyplot as plt
import numpy as np
import random

class MuonPdf():

    # Initialise muon pdf with lifetime tau.

    def __init__(self, tau = 2.2):

        self.tau = tau
        self.normalisation = 1.0/self.tau
        

        # Function to evaluate the pdf at point t_point.
       
    def evaluateMuonPdf(self, t_point):

        result = self.normalisation * np.exp((-1.0*t_point)/self.tau)
        
        return result

        # Function gives the max of pdf.

    def fmax(self):

        fmax = self.evaluateMuonPdf(0.0)

        return fmax
        
        # Function to generate random number from exponential pdf. 

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

    

        

        

        

        




