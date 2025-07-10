
import numpy as np
import matplotlib.pyplot as plt

def plot_CDF_vs_time(sorted_times_SRP,  sorted_times_GCC ):

    cdf_SRP = np.arange(1, len(sorted_times_SRP) + 1) / len(sorted_times_SRP)
    cdf_GCC = np.arange(1, len(sorted_times_GCC) + 1) / len(sorted_times_GCC)

    plt.figure(figsize=(8, 6))  # Optional: Set the size of the figure
    plt.plot(sorted_times_GCC, cdf_GCC, color='red',linestyle='--',  marker='x', label='GCC-PHAT')
    plt.plot(sorted_times_SRP, cdf_SRP, color='blue',linestyle='--',  marker='x', label='SRP-PHAT')
    plt.xlabel('Computation Time (seconds)')
    plt.ylabel('CDF')
    plt.title('CDF of Computation Times (real data)')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()




    # # Plot CDF vs. Time
    # plt.figure(figsize=(8, 6))  # Optional: Set the size of the figure
    # #SRP_PHAT
    # plt.subplot(2, 1, 1)  # Create the first subplot (2 rows, 1 column, first plot)
    # plt.plot(sorted_times_SRP, cdf_SRP,color='blue',linestyle='--',  marker='x')
    # plt.xlabel('Computation Time (seconds)')
    # plt.ylabel('CDF')
    # plt.title('CDF of Computation Times For SRP-PHAT')
    # plt.grid(color='gray', linestyle='--', linewidth=0.5)
    # plt.legend()

    # #GCC_PHAT
    # plt.subplot(2, 1, 2)  # Create the first subplot (2 rows, 1 column, first plot)
    # plt.plot(sorted_times_GCC, cdf_GCC, color='red',linestyle='--', marker='o')
    # plt.xlabel('Computation Time (seconds)')
    # plt.ylabel('CDF')
    # plt.title('CDF of Computation Times For GCC-PHAT')
    # plt.grid(color='gray', linestyle='--', linewidth=0.5)
    # # Adjust layout to prevent subplot titles from overlapping
    # plt.tight_layout()
    # plt.show()

