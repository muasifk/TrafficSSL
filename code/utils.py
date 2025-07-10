
import random, torch
import numpy as np
import scipy
import scipy.io
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import math


''' SEED Everything '''
def seed_everything(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = True
    return None
    

def plot_audio(path):
    ''' Plot audio signal'''
    fs, x      = wavfile.read(path)
    N  = x.shape[0]  # num_samples
    C  = x.shape[0]    # num_channels
    D  = x.shape[0] / fs  # duration
    fig, [ax1,ax2] =  plt.subplots(1,2, figsize=(8,3))
    ## Time domain
    t  = np.arange(N) / fs
    # x  = x[:,0]
    ax1.plot(t, x, color='k', alpha=0.9)  # plotting only one channel
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Amplitude")
    ax1.set_title('Time domain')
    ## Frequency domain
    xf = fft(x)
    f = fftfreq(N, 1/fs)
    ax2.plot(f, xf, color='b', alpha=0.9)
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Amplitude")
    ax2.set_title('Frequnecy domain')
    plt.show()
    print(f'\nSampling rate  : {fs}')
    print(f'n_samples      : {N} ')
    # print(f'n_channels     : {C}')
    print(f'Duration (s)     : {D}')
    return None


def propagation_time(d):
    ''' calculate propagation time from distance '''
    e    = 0          # e is measurement error
    c    = 343        # Speed of sound in meter/second
    time = (d/c) + e  # propagation time in second
    return time


def TDOA_to_DOA(tdoa, mic_distance):
    '''
    Calculate the direction of arrival (DOA) in degrees based on the time delay
    between two microphones and the known distance between them.
    We use the inverse cosine function as arccos(x), x should be in the range [-1, 1], otherwise it returns ValueError.
    arcos calculates the angle whose cosine equals the input value.
    arccos(0)   = 90 degrees
    arccos(0.5) = 60 degrees
    arccos(1)   = 0 degrees
    Note:
    =====
    A limitation is that the angle of arrival estimated from a single mic pair has front-back ambiguity. For instance an angle at θ = 30 degrees
    would have the same time difference of arrival as θ = 150 degrees. You can think of the sin⁻¹ inverse function as multivalued to represent
    this ambiguity.
    
    Parameters:
        tdoa (float): Time delay between the two microphones in seconds.
        mic_distance (float): Distance between the two microphones in meters.
        speed_of_sound (float): Speed of sound in the medium in meters per second.
    
    Returns:
        doa (float): Direction of arrival (DOA) in degrees.
        A DOA=90 degree means the source is in front of the mic array (making 90 degree angle with positive x-axis)
    '''
    speed_of_sound = 343 # mps
    max_tdoa = mic_distance / speed_of_sound
    tdoa = np.clip(tdoa, -max_tdoa, max_tdoa)  # TDOA must be within the range [-max_tdoa, max_tdoa]
    x    = speed_of_sound*tdoa/mic_distance
    # doa  = np.degrees(np.arccos(x))    # https://github.com/JSerwatka/Acoustic-Source-Localization-System
    doa  = int(np.degrees(np.arcsin(x)))      # https://stackoverflow.com/questions/64919158/sound-source-localization-with-matlab
    
    
    ##### For my own use
    ## For mic_distance=0.15, see below calculations
    ## TDOA/x/doa, 0.0001/0.228/76, 0.0002/0.457/62,0.0003/0.685/46,0.0004/0.914/23
    ## TDOA/x/doa, -0.0001/-0.228/103, -0.0002/-0.457/117,-0.0003/0.685/46,-0.0004/0.914/23
    return doa



