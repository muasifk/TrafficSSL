
import numpy as np
import matplotlib.pyplot as plt

def accuracy(gt_thetas,  et_thetas_GCC ,et_thetas_SRP ):

    # Create the subplot
    plt.figure(figsize=(8, 6))  # Optional: Set the size of the figure
    #SRP_PHAT
    plt.subplot(2, 1, 1)  # Create the first subplot (2 rows, 1 column, first plot)
    plt.plot(gt_thetas, gt_thetas,linestyle='--')
    plt.scatter(gt_thetas,et_thetas_GCC, marker='o', color='red', label='DOA using GCC-PHAT')
    #plt.plot(gt_thetas, et_thetas_SRP, color='blue', label='DOA using SRP-PHAT')
    plt.xlabel('DOA')
    plt.ylabel('Estimated DOA')
    plt.title('Estimated DOA using GCC-PHAT (real data)')
    plt.legend()



    #GCC_PHAT
    plt.subplot(2, 1, 2)  # Create the second subplot (2 rows, 1 column, second plot)
    # plt.plot(gt_thetas, et_thetas_GCC, color='red', label='DOA using SRP-PHAT')
    plt.plot(gt_thetas, gt_thetas,linestyle='--')
    plt.scatter(gt_thetas, et_thetas_SRP, marker='o', color='blue', label='DOA using SRP-PHAT')
    plt.xlabel('DOA')
    plt.ylabel('Estimated DOA')
    plt.title('Estimated DOA using SRP-PHAT (real data)')
    plt.legend()
    # Adjust layout to prevent subplot titles from overlapping
    plt.tight_layout()
    # Show the plot
    plt.show()
