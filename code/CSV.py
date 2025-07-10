import csv
import pandas as pd

def save_to_csv(filename, gt_thetas, et_thetas_SRP, et_thetas_GCC):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['gt_thetas', '           ', 'SRP', '                   ', 'GCC']) # Headers
        for gt, et_SRP, et_GCC in zip(gt_thetas, et_thetas_SRP, et_thetas_GCC):
            writer.writerow([gt, '                  ', et_SRP, '                 ', et_GCC])


