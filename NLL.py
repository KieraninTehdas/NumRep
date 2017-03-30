import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize


def NLL(data, parameters):

    f = parameters[0]
    tauOne = parameters[1]
    tauTwo = parameters[2]

    L = [-math.log(f*(1.0/tauOne)*np.exp(-t/tauOne) + (1-f)*(1.0/tauTwo)*(np.exp(-t/tauTwo))) for t in data]

        
        
    return np.sum(L)


def vary_parameter(data, params, param_num_to_vary, stat_error):

    param_value = []
    temp_param = list(params)
    NLL_value = []

    for i in range(-100, 100):

        temp_param[param_num_to_vary] = params[param_num_to_vary] + (i*(stat_error[param_num_to_vary]/100))
        param_value.append(temp_param[param_num_to_vary])

        NLL_value.append(NLL(data, temp_param))

    return (param_value, NLL_value)

def main():


    filename = "DecayTimesData.txt"
    
    data = np.loadtxt(filename)

    #print(data)



    tauOne = 0.4
    tauTwo = 0.5
    f = 1

    parameters = [f, tauOne, tauTwo]
    
    

    lNLL = lambda args: NLL(data, args)
    
    bnds = ((0.001,1), (0.001, None), (0.001, None))

    method = 'L-BFGS-B'

    r = minimize(lNLL, parameters, bounds = bnds)
    print(r)
    #r.hess        

    f_best = r.x[0]
    tau_1_Best = r.x[1] 
    tau_2_Best = r.x[2]

    best_params = [f_best, tau_1_Best, tau_2_Best]

        
    samples = 5
    range_number = 5
    
    estimate_sd = []

    for i in range(0,range_number):
        step_size = int(len(data)/samples)
        i_min = step_size*i
        i_max = step_size*(i+1)
        
        lNLL = lambda args: NLL(data[i_min:i_max], args)
        #print("max {0} min {1} \n".format(i_max, i_min))
        res = minimize(lNLL, best_params, bounds = bnds)

        estimate_sd.append([res.x[0], res.x[1], res.x[2]])

    average = np.average(estimate_sd, axis = 0)
    sd = np.std(estimate_sd, axis = 0)
    print("Averages {0} \n".format(average))
    print("SD {0} \n".format(sd))

    sd_f = sd[0]/np.sqrt(samples)
    sd_tau_1 = sd[1]/np.sqrt(samples)
    sd_tau_2 = sd[2]/np.sqrt(samples)

    # For plotting
    g = [r.x[0]*(1.0/r.x[1])*np.exp(-t/r.x[1]) + (1-r.x[0])*(1.0/r.x[2])*(np.exp(-t/r.x[2])) for t in data]

  

    # Vary the parameters to estimate error.

    f_sigma_test, f_sigma_NLL = vary_parameter(data, average, 0, sd)
    tau_1_sigma_test, tau_1_sigma_NLL = vary_parameter(data, average, 1, sd)
    tau_2_sigma_test, tau_2_sigma_NLL = vary_parameter(data, average, 2, sd)

    plt.figure(1)
    plt.subplot(211)
    plt.hist(data, 100)
    plt.subplot(212)
    plt.scatter(data, g)
    plt.show()

    plt.subplot(311)
    plt.scatter(f_sigma_test, f_sigma_NLL)
    plt.subplot(312)
    plt.scatter(tau_1_sigma_test, tau_1_sigma_NLL)
    plt.subplot(313)
    plt.scatter(tau_2_sigma_test, tau_2_sigma_NLL)
    plt.show()

main()
