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


    # Single test run to check exponential distribution statistics.

    muon_t_test = [muon_pdf.pullRandMuon() for j in range(n_points)]
    print("Single run mean lifetime: {0:6.3f}".format(
        np.mean(muon_t_test)))
    print("Single run standard deviation: {0:6.4f}".format(
        np.std(muon_t_test)))
    print("Single run error on mean: {0:6.4f}".format(
        np.std(muon_t_test)/np.sqrt(n_points)))

    plt.hist(muon_t_test, 50)
    plt.xlabel("Lifetime (ms)")
    plt.ylabel("Counts")
    plt.show()



    # Perform 500 runs of 1000 events each. Average each run and add to average list.

    for i in range (n_repeats):

        print("Run {0} begins!".format(i))
        muon_t = [muon_pdf.pullRandMuon() for j in range(n_points)]
        average_tau.append(np.mean(muon_t))
        print("Run {0} ends!".format(i))

    # Output the relevant information to the user.

    standard_deviation = np.std(average_tau)
    std_err_mean = standard_deviation/np.sqrt(n_points)


    print("Mean muon lifetime: {0:6.3f}".format(np.mean(average_tau)))
    print("Standard deviation: {0:6.3f}".format(standard_deviation))
    print("Standard error on mean: {0:6.4f}".format(std_err_mean))

    # Plot and show a histogram of the data.

    plt.hist(average_tau, 10)
    plt.xlabel("Lifetime (ms)")
    plt.ylabel("Counts")
    plt.show()


# Run main.

main()
