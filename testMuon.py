import math
import matplotlib.pyplot as plt
import numpy as np
from MuonPdf import MuonPdf
import pylab

def main():


    #muon_pdf = MuonPdf(2.2)
    #print(gauss.max())
    muon_x_data = []
    n_points = 1000

    #muon_t = [muon_pdf.pullRandMuon() for i in range(n_points)]
    
    #average_tau = np.mean(muon_t)
    #print(average_tau)

    average_tau= []

    for i in range (500):
        muon_pdf = MuonPdf(2.2)
        muon_t = [muon_pdf.pullRandMuon() for j in range(n_points)]
        average_tau.append(np.mean(muon_t))

    #print(average_tau)

    #muon_y_data = [muon_pdf.evaluateMuonPdf(muon_x_data[i]) for i in range(len(muon_x_data))]
    
    
   #plt.hist(muon_t, bins=30)
    plt.hist(average_tau, 10)
    plt.show()
    



main()
