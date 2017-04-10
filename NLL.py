import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize
from SimulateLifetime import *

# This code can be used to find the best fit parameters of a function of three parameters.
# The parameter estimation is calculated using negative log likelihood (NLL).
# Also has functionality to simulate the lifetime measurements.

# Function to return negative log likelihood of given data, with given parameters

def NLL(data, parameters):

    f = parameters[0]
    tauOne = parameters[1]
    tauTwo = parameters[2]

    # Take the negative log of the pdf
    #L = [-math.log(f*(1.0/tauOne)*np.exp(-t/tauOne) + (1-f)*(1.0/tauTwo)*(np.exp(-t/tauTwo))) for t in data]

    NLL = 0

    for i in range(len(data)):

        t = data[i]
        pdf = f*(1.0/tauOne)*np.exp(-t/tauOne) + (1-f)*(1.0/tauTwo)*(np.exp(-t/tauTwo))

        if (pdf > 0.0):
            NLL += -math.log(pdf)


    return NLL


# Function which varies a given parameter by an amount, stat_error, from the best value.
# The parameter to vary is defined as an integer, which is the index of the desired parameter in the
# list params.

def vary_parameter(data, params, param_num_to_vary, stat_error):

    param_value = []
    temp_param = list(params) # Copies the list parameters
    NLL_value = []

    # Varies the chosen parameter by +/- the input statistical error.
    # Returns the value of the NLL for a given paramter value.

    for i in range(-100, 100):

        # Temporary variable to allow variation of single best fit parameter
        temp_param[param_num_to_vary] = params[param_num_to_vary] + (i*(stat_error[param_num_to_vary]/100))
        param_value.append(temp_param[param_num_to_vary])

        NLL_value.append(NLL(data, temp_param))

    return (param_value, NLL_value)

# Function returns the error from varying the parameter.
# Find an x value where the pdf has increased by 0.5 from the minimum

def error_from_parameter_vary(x_list, y_list):

    # Find the index of the value of NLL that is closest to the minimum NLL + 0.5
    index_of_min_y_error = min(range(len(y_list)), key=lambda i: abs(y_list[i]-(min(y_list)+0.5)))

    # Find the index of the minimum NLL.
    index_of_min_y = min(range(len(y_list)), key=lambda i: abs(y_list[i]))

    # Both x and y lists are ordered and correspond as (x1, y1), (x2,y2).
    # Use indexes calculated above for y to find x distance between minimum y
    # and minimum y + 0.5.
    error = abs(x_list[index_of_min_y_error]-x_list[index_of_min_y])

    return error

#######################################################################
############################################################################################

def main():

    # Load the data file and read the text.

    filename = "DecayTimesData.txt"

    data = np.loadtxt(filename)

    #print(data)

    # Provide initial best fit parameters and cast as list.

    tauOne = 0.5
    tauTwo = 0.5
    f = 1.0

    parameters = [f, tauOne, tauTwo]

    # Use lambda function to calculate NLL from data, supplying a number of additional arguments.

    lNLL = lambda args: NLL(data, args)

    # Don't let any of the parameters be < 0!
    # Don't let f > 1!

    bnds = ((0.001,1), (0.001, None), (0.001, None))

    #method = 'L-BFGS-B'

    # Minimize the NLL using scipy.optimize.

    r = minimize(lNLL, parameters, bounds = bnds)
    #print(r)


    f_best = r.x[0]
    tau_1_Best = r.x[1]
    tau_2_Best = r.x[2]

    best_params = [f_best, tau_1_Best, tau_2_Best]

    print("Best fit parameters: f = {0}, t1 = {1}, t2 = {2} \n".format(f_best, tau_1_Best, tau_2_Best))

    # Estimate the standard deviation on the parameters by splitting the data up into samples.
    # Find best fit parameters for each sample of data to find stanard deviation.

    samples = 5


    estimate_sd = []

    for i in range(0, samples):
        step_size = int(len(data)/samples)
        i_min = step_size*i
        i_max = step_size*(i+1)

        lNLL = lambda args: NLL(data[i_min:i_max], args)
        #print("max {0} min {1} \n".format(i_max, i_min))
        res = minimize(lNLL, best_params, bounds = bnds)

        estimate_sd.append([res.x[0], res.x[1], res.x[2]])

    # Calculate average of different best fit parameters and standard deviations.

    average = np.average(estimate_sd, axis = 0)
    sd = np.std(estimate_sd, axis = 0)
    #print("Average parameters from sampling data: f, t1, t2 {0} \n".format(average))
    #print("Standard deviation in sample parameters: f, t1, t2 {0} \n".format(sd))

    sd_f = sd[0]/np.sqrt(samples)
    sd_tau_1 = sd[1]/np.sqrt(samples)
    sd_tau_2 = sd[2]/np.sqrt(samples)

    # For plotting the pdf.
    g = [r.x[0]*(1.0/r.x[1])*np.exp(-t/r.x[1]) + (1-r.x[0])*(1.0/r.x[2])*(np.exp(-t/r.x[2])) for t in data]



    # Vary the parameters to estimate error.

    # Value of parameters and value of NLL at given parameters returned.
    # Integer indicates which parameter is being varied.

    f_sigma_test, f_sigma_NLL = vary_parameter(data, best_params, 0, sd)
    tau_1_sigma_test, tau_1_sigma_NLL = vary_parameter(data, best_params, 1, sd)
    tau_2_sigma_test, tau_2_sigma_NLL = vary_parameter(data, best_params, 2, sd)


    error_f = error_from_parameter_vary(f_sigma_test, f_sigma_NLL)
    error_tau1 = error_from_parameter_vary(tau_1_sigma_test, tau_1_sigma_NLL)
    error_tau2 = error_from_parameter_vary(tau_2_sigma_test, tau_2_sigma_NLL)

    print("Error f = {0}, t1 = {1}, t2 = {2} \n".format(error_f, error_tau1, error_tau2))

    ################################################################################################

    # Simulate the lifetime measurement experiments using Monte-Carlo random number generation.
    # Can then be compared with actual measured values.


    # Number of data points per run and number of runs.
    n_points = 10000
    n_repeats = 10


    # Initialise a lifetime simulation with best fit parameters.
    simulation_pdf = LifetimePdf(best_params[0], best_params[1], best_params[2])




    simulated_params = []
    simulated_data = []
    simulated_errors = []

    # Conduct the experiment a number of times and calculate errors/best fits etc.

    for i in range(0, n_repeats):

        # Simulate the measurements by pulling at random from pdf.
        simulated_lifetimes = [simulation_pdf.pull_rand_lifetime() for j in range(n_points)]
        simulated_data = simulated_data + simulated_lifetimes

        lNLL = lambda args: NLL(simulated_lifetimes, args)

        r = minimize(lNLL, parameters, bounds = bnds)
        # print(r)

        simulated_params.append([r.x[0], r.x[1], r.x[2]])

        estimate_sim_sd = []

        for k in range(0, samples):
            step_size = int(len(simulated_lifetimes)/samples)
            k_min = step_size*k
            k_max = step_size*(k+1)

            lNLL = lambda args: NLL(simulated_lifetimes[k_min:k_max], args)
            #print("max {0} min {1} \n".format(i_max, i_min))
            res = minimize(lNLL, [r.x[0], r.x[1], r.x[2]], bounds = bnds)

            estimate_sim_sd.append([res.x[0], res.x[1], res.x[2]])

        #print("Run {3} Simulated f = {0}, tau1 = {1}, tau2 = {2}".format(r.x[0], r.x[1], r.x[2], i))

        sim_sd = np.std(estimate_sim_sd, axis = 0)

        f_vary, f_vary_NLL = vary_parameter(simulated_lifetimes, [r.x[0], r.x[1], r.x[2]], 0, sim_sd)
        tau_1_vary, tau_1_vary_NLL = vary_parameter(simulated_lifetimes, [r.x[0], r.x[1], r.x[2]], 1, sim_sd)
        tau_2_vary, tau_2_vary_NLL = vary_parameter(simulated_lifetimes, [r.x[0], r.x[1], r.x[2]], 2, sim_sd)


        error_f_sim = error_from_parameter_vary(f_vary, f_vary_NLL)
        error_tau1_sim = error_from_parameter_vary(tau_1_vary, tau_1_vary_NLL)
        error_tau2_sim = error_from_parameter_vary(tau_2_vary, tau_2_vary_NLL)

        #print("{0} errors: {1}, {2}, {3} \n".format(i,error_f_sim, error_tau1_sim, error_tau2_sim))

        simulated_errors.append([error_f_sim, error_tau1_sim, error_tau2_sim])

    simulated_averages = np.average(simulated_params, axis = 0)
    simulated_error = np.average(simulated_errors, axis = 0)
    #simulated_sd = np.std(simulated_params, axis = 0)

    print("Average simulated f = {0}, t1 = {1}, t2 = {2} \n".format(simulated_averages[0], simulated_averages[1], simulated_averages[2]))

    print("Average simulated error f = {0}, t1 = {1}, t2 = {2} \n".format(simulated_error[0], simulated_error[1], simulated_error[2]))
    #print("Simulated sd = f, t1, t2 {0}".format(simulated_sd/np.sqrt(n_repeats)))
    #print(len(simulated_data))

    plt.figure(1)
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    plt.subplot(211)
    ax = plt.subplot(211)
    ax.set_title("Lifetime measurements")
    ax.set_xlabel("Decay Time (s)")
    ax.set_ylabel("Frequency")
    plt.hist(data, 100)
    plt.subplot(212)
    ax = plt.subplot(212)
    ax.set_title("Probability Distribution Function")
    ax.set_xlabel("Decay Time (s)")
    ax.set_ylabel("Relative Likelihood")
    plt.scatter(data, g)
    plt.show()

    plt.figure(1)
    plt.subplot(311)
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    ax = plt.subplot(311)
    ax.set_xlabel("Parameter f value")
    ax.set_ylabel("Negative Log Likelihood")
    plt.scatter(f_sigma_test, f_sigma_NLL)
    plt.subplot(312)
    ax = plt.subplot(312)
    ax.set_xlabel("Parameter tau 1 value")
    ax.set_ylabel("Negative Log Likelihood")
    plt.scatter(tau_1_sigma_test, tau_1_sigma_NLL)
    plt.subplot(313)
    ax = plt.subplot(313)
    ax.set_xlabel("Parameter tau 2 value")
    ax.set_ylabel("Negative Log Likelihood")
    plt.scatter(tau_2_sigma_test, tau_2_sigma_NLL)
    plt.show()

    plt.figure(1)
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    plt.subplot(211)
    ax = plt.subplot(211)
    ax.set_title("Lifetime measurements")
    ax.set_xlabel("Decay Time (s)")
    ax.set_ylabel("Frequency")
    plt.hist(data, 100)
    plt.subplot(212)
    ax = plt.subplot(212)
    ax.set_title("Simulated Lifetime measurements")
    ax.set_xlabel("Decay Time (s)")
    ax.set_ylabel("Frequency")
    plt.hist(simulated_lifetimes, 100)
    plt.show()

main()
