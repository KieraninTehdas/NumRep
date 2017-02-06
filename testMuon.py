import math
import matplotlib.pyplot as plt
import numpy as np
from MuonPdf import MuonPdf
import pylab

def main():


    n_points = 1000
    n_repeats = 500

    
    muon_pdf = MuonPdf()
    average_tau= []

    for i in range (n_repeats):

        muon_t = [muon_pdf.pullRandMuon() for j in range(n_points)]
        average_tau.append(np.mean(muon_t))

    
    print("Mean muon lifetime: ", np.mean(average_tau), "\n")
   
    plt.hist(average_tau, 10)
    plt.xlabel("Lifetime (ms)")
    plt.ylabel("Counts")
    plt.show()
    



main()
