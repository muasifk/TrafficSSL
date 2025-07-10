
import numpy as np
import matplotlib.pyplot as plt

def plot_doa_polar(gt_doa_deg, et_doa_deg,et_doa_deg_2 ):
    # Convert DoA values from degrees to radians
    gt_doa_rad = np.radians(gt_doa_deg)
    et_doa_rad = np.radians(et_doa_deg)
    et_doa_rad_2= np.radians(et_doa_deg_2)
    # Create a polar plot
    plt.figure(figsize=(8, 6))
    ax = plt.subplot(111, projection='polar')
    ax.scatter(gt_doa_rad, np.ones_like(gt_doa_rad), c='black', marker='o', label='Ground Truth')
    ax.scatter(et_doa_rad, 0.9 * np.ones_like(et_doa_rad), c='r', marker='x', label='Estimated GCC')
    ax.scatter(et_doa_rad_2, 0.9 * np.ones_like(et_doa_rad), c='b',marker='x', label='Estimated SRP')

    # Set the angle ticks to degrees
    ax.set_theta_direction(1)  # -1 for Clockwise direction
    ax.set_theta_zero_location('E')  # North as 0 degrees
    ax.legend(loc='upper left')
    plt.title('Ground Truth and Estimated Direction of Arrival (DoA) (real data) ')
    plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# def plot_doa_polar(gt_doa_deg, et_doa_deg ):
#     # Convert DoA values from degrees to radians
#     gt_doa_rad = np.radians(gt_doa_deg)
#     et_doa_rad = np.radians(et_doa_deg)
#     # et_doa_rad_2= np.radians(et_doa_deg_2)
#     # Create a polar plot
#     plt.figure(figsize=(8, 6))
#     ax = plt.subplot(111, projection='polar')
#     ax.scatter(gt_doa_rad, np.ones_like(gt_doa_rad), c='b', marker='o', label='Ground Truth')
#     ax.scatter(et_doa_rad, 0.9 * np.ones_like(et_doa_rad), c='r', marker='x', label='Estimated GCC')
#     # ax.scatter(et_doa_rad_2, 0.9 * np.ones_like(et_doa_rad), c='b',marker='x', label='Estimated SRP')

#     # Set the angle ticks to degrees
#     ax.set_theta_direction(1)  # -1 for Clockwise direction
#     ax.set_theta_zero_location('E')  # North as 0 degrees
#     ax.legend(loc='upper left')
#     plt.title('Ground Truth and Estimated Direction of Arrival (DoA) ')
#     plt.show()














# # # Example usage:
# # ground_truth_doa_deg = np.array([10, 30, 45, 60, 90])  # Replace with your ground truth DoA values
# # estimated_doa_deg = np.array([8, 28, 48, 62, 88])  # Replace with your estimated DoA values
# # plot_doa_polar(ground_truth_doa_deg, estimated_doa_deg)


# import numpy as np
# import matplotlib.pyplot as plt

# def plot_doa_polar(gt_doa_deg, et_doa_deg,et_doa_deg_2 ):
#     # Convert DoA values from degrees to radians
#     gt_doa_rad = np.radians(gt_doa_deg)
#     et_doa_rad = np.radians(et_doa_deg)
#     et_doa_rad_2= np.radians(et_doa_deg_2)
#     # Create a polar plot
#     plt.figure(figsize=(8, 6))
#     ax = plt.subplot(111, projection='polar')
#     ax.scatter(gt_doa_rad, np.ones_like(gt_doa_rad), c='b', marker='o', label='Ground Truth')
#     ax.scatter(et_doa_rad, 0.9 * np.ones_like(et_doa_rad), c='r', marker='x', label='Estimated SRP-PHAT')
#     ax.scatter(et_doa_rad_2, 0.9 * np.ones_like(et_doa_rad), c='b',marker='x', label='Estimated GCC-PHAT')
#     # Set the angle ticks to degrees
#     ax.set_theta_direction(1)  # -1 for Clockwise direction
#     ax.set_theta_zero_location('E')  # North as 0 degrees
#     ax.legend(loc='upper left')
#     plt.title('Ground Truth and Estimated Direction of Arrival (DoA)')
#     plt.show()

# # Example usage:
# ground_truth_doa_deg = np.array([10, 30, 45, 60, 90])  # Replace with your ground truth DoA values
# estimated_doa_deg = np.array([8, 28, 48, 62, 88])  # Replace with your estimated DoA values
# plot_doa_polar(ground_truth_doa_deg, estimated_doa_deg)