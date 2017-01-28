import numpy as np
import Linear

class ChiSq:

    #initialise with x, y, and error values, plus function

    def __init__(self, xInput, yInput, error, function):

        self.xValues = xInput
        self.yValues = yInput
        self.errorValues = error
        self.function = function

        # check the vectors are correct dimensions
        if (xInput.shape == yInput.shape == error.shape) :

            # make n x n diagonal error matrix
            error_matrix = np.diag(self.errorValues.A1)
            #print(error_matrix)
            error_matrix_squared = np.square(error_matrix)
            #print(error_matrix_squared)
            error_matrix_inverse = np.linalg.inv(error_matrix_squared)
            self.error_matrix_inverse = error_matrix_inverse
            #print(error_matrix_inverse)
        else :
            raise ValueError("Input vector dimensions don't match!")

    # function to enable setting of parameters
    def setParameters(self, parameters):

        self.function.setParameters(parameters)

    # evaluate chi squared
    def evaluateChiSq(self):

        # evaluate the function and calculate the difference vector
        y_calculated = self.function.Evaluate(self.xValues)
        difference = self.yValues - y_calculated
        print(difference)

        # calculate chi squared with matrics
        chi_sq = difference.transpose() * self.error_matrix_inverse *difference

        return chi_sq.item(0)
