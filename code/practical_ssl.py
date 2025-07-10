import numpy as np
from scipy.io import wavfile


# Main function
def practical_ssl(folder1_files, folder2_files ):
    
    for file1_path, file2_path in zip(folder1_files, folder2_files):
        fs, x1 = wavfile.read(file1_path)
        fs, x2 = wavfile.read(file2_path)

        x1 = np.array(x1)
        x2 = np.array(x2)
    return x1, x2,fs

    # if __name__ == "__main__":
    #   main()