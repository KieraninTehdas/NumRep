import numpy as np
import sys

class Linear:

    # set initial parameter values

    def __init__(self,  m = 1.0, c = 1.0):
        self.m = m
        self.c = c


    # method to set parameters from a matrix
    def setParameters(self,parameters):

        if (len(parameters) != 2):

            print("WARNING: TOO MANY PARAMETERS, PARAMETERS NOT SET!")

        elif (type(parameters) is list):

            self.m = parameters[0]
            self.c = parameters[1]

        elif (type(parameters) is np.matrix):

            self.m = parameters.item(0)
            self.c = parameters.item(1)

        else :
            raise TypeError("Unexpected parameter type, parameters not set.")



    # evaluate function for given parameters
    def Evaluate(self, x):

        return((self.m*x)+self.c)
