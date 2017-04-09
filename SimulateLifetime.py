import numpy as np
import math
import random

class LifetimePdf():

    def __init__(self, fraction, tau1, tau2):

        self.fraction = fraction
        self.tau1 = tau1
        self.tau2 = tau2
        


    def evaluate_pdf(self, t):

        pdf1 = self.fraction*(1.0/self.tau1)*np.exp(-t/self.tau1)
        pdf2 = (1-self.fraction)*(1.0/self.tau2)*np.exp(-t/self.tau2)

        result = pdf1 + pdf2

        return result

    def fmax(self):

        fmax = self.evaluate_pdf(0)

        return fmax


    def pull_rand_lifetime(self, upper_bound = 100.0):

        lower_bound = 0.0
        evaluated_random = 0.0
        scaled_random = 0.0
        random_point = 1.0

        while (random_point > evaluated_random):

            random_x = np.random.uniform()
            scaled_random_x = lower_bound + (upper_bound - lower_bound)*random_x
            evaluated_random = self.evaluate_pdf(scaled_random_x)

            random_point = np.random.uniform()*self.fmax()


        return scaled_random_x
