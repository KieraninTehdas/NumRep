import math
import matplotlib.pyplot as plt
import numpy as np
from MuonPdf import MuonPdf
import pylab

def main():

    # Number of points to sample and number of times to repeat.

    n_points = 1000
    n_repeats = 500

    # Initialise a muon lifetime pdf and a list to hold average lifetimes.

    muon_pdf = MuonPdf()
    average_tau= []

    # Perform 500 runs of 1000 events each. Average each run and add to average list.

    for i in range (n_repeats):

        muon_t = [muon_pdf.pullRandMuon() for j in range(n_points)]
        average_tau.append(np.mean(muon_t))
    

    # Output the relevant information to the user.

    standard_deviation = np.std(average_tau)
    std_err_mean = standard_deviation/np.sqrt(n_repeats)
    

    print("Mean muon lifetime: ", np.mean(average_tau), "\n")
    print("Standard deviation: ", standard_deviation, "\n")
    print("Standard error on mean: ", std_err_mean)
   
    # Plot and show a histogram of the data.

    plt.hist(average_tau, 10)
    plt.xlabel("Lifetime (ms)")
    plt.ylabel("Counts")
    plt.show()
    

# Run main.

main()
