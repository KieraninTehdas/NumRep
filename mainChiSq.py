from Linear import Linear
from ChiSq import ChiSq
import numpy as np

def main():

    #while True:
        #try:
    filename = str(raw_input("Enter filename (Test data used if blank): "))
    if (filename == ""):
        filename = "testData.txt"
            #break
        #except:
            #ValueError("File not found!")


    input_data = np.loadtxt(filename)

    # load data as vectors by taking transpose
    xValues = np.matrix(input_data[:,0]).transpose()
    yValues = np.matrix(input_data[:,1]).transpose()
    errorValues = np.matrix(input_data[:,2]).transpose()

    chi_sq = ChiSq(xValues, yValues, errorValues, function=Linear())

    parameters = [0.0, 1.0]
    chi_sq.setParameters(parameters)

    chi_sq_value = chi_sq.evaluateChiSq()

    print('Chi squared is: '+ str(chi_sq_value))

main()
