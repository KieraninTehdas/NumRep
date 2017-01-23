import numpy as np

class Linear:

    #set initial parameter values

    def __init__(self,  m, c):
        self.m = m
        self.c = c


    #method to set parameters from a matrix
    @staticmethod
    def setParameters(self, *param):

        m = param[0]
        c = param[1]

    
    #evaluate function for given parameters
    def evaluate(self, x):

        return((self.m*x)+self.c)
        

    #evaluate function for given matrix
    #def evaluateMatrix(*vector)
