
import numpy as np
from sim_ssl import sim_ssl
import time  
from SRP import SRP_updated 
import matplotlib.pyplot as plt
from GCC_PHAT import GCC_PHAT
from utils import TDOA_to_DOA
from plot_doa_polar import plot_doa_polar 
import random
from plot_CDF import plot_CDF_vs_time
from plot_accuracy import accuracy
from scipy.io import wavfile
from CSV import save_to_csv


fs = 44100  
mic_seperation = 0.707106782  


folder1_files = [
        'data\S-30_1\XM4_RIR.wav','data\S-45_1\XM4_RIR.wav','data\S-60_1\XM4_RIR.wav',
        'data\S-90_1\XM4_RIR.wav','data\S0_1\XM4_RIR.wav','data\S30_1\XM4_RIR.wav',
        'data\S45_1\XM4_RIR.wav','data\S60_1\XM4_RIR.wav','data\S90_1\XM4_RIR.wav'
    ]

folder2_files = [
        'data\S-30_1\XM5_RIR.wav','data\S-45_1\XM5_RIR.wav','data\S-60_1\XM5_RIR.wav',
        'data\S-90_1\XM5_RIR.wav','data\S0_1\XM5_RIR.wav','data\S30_1\XM5_RIR.wav',
        'data\S45_1\XM5_RIR.wav','data\S60_1\XM5_RIR.wav','data\S90_1\XM5_RIR.wav'
    ]



et_thetas_SRP = []  # estimated thetas
et_thetas_GCC  = []  # estimated thetas
computation_times_SRP= []  # To store computation times for each iteration
computation_times_GCC = []  # To store computation times for each iteration

gt_thetas=[-30, -45, -60, -90,  0, 30, 45, 60, 90]

for file1_path, file2_path in zip(folder1_files, folder2_files):
    fs, x1 = wavfile.read(file1_path)
    fs, x2 = wavfile.read(file2_path)

    x1 = np.array(x1)
    x2 = np.array(x2)

    #GCC-PHAT
    start_time_GCC = time.time()
    cc, tdoa = GCC_PHAT(x1, x2, fs)  ## GCC_PHAT(signal_received_first, signal_received_last, fs)
    end_time_GCC = time.time()
    elapsed_time_GCC = end_time_GCC - start_time_GCC #Calculate elapsed time for the current iteration and store it
    computation_times_GCC.append(elapsed_time_GCC)
    doa_GCC = TDOA_to_DOA(tdoa, mic_seperation) 
    print(f'GT-DoA={file1_path}        ET-DoA-GCC={doa_GCC}')
    et_thetas_GCC.append(doa_GCC)


    #SRP-PHAT
    start_time_SRP= time.time() #for computation time
    doa_SRP=SRP_updated(x1, x2, fs, mic_seperation)
    end_time_SRP = time.time()
    elapsed_time_SRP = end_time_SRP - start_time_SRP #Calculate elapsed time for the current iteration and store it
    computation_times_SRP.append(elapsed_time_SRP)
    print(f'                              ET-DoA-SRP={doa_SRP}')
    et_thetas_SRP.append(doa_SRP)




# Save gt_thetas, et_thetas_SRP, and et_thetas_GCC to the same CSV file
save_to_csv('et_thetas_practical.csv', gt_thetas, et_thetas_SRP, et_thetas_GCC)


# Plot the estimations now on polar plot
plot_doa_polar(gt_thetas, et_thetas_GCC, et_thetas_SRP)   

#CDF
sorted_times_SRP = np.sort(computation_times_SRP)
sorted_times_GCC = np.sort(computation_times_GCC)
plot_CDF_vs_time(sorted_times_GCC,sorted_times_SRP )

# accuracy comparaison
accuracy(gt_thetas,  et_thetas_GCC ,et_thetas_SRP )









