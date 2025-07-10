
import numpy as np
import scipy
import scipy.io
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

def GCC_PHAT(x1, x2, fs=1, max_tau=None, interp=16):
    '''
    TDOA is the delay that causes the cross-correlation (CC) between the two signals segments to be maximum.
    To improve robustness against reverberation, we use GCC-PHAT (Generalized Cross Correlation with Phase Transform) instead of CC.
    1) For two signals x1 and x2 (x1 and x2 are signals received first and last respectively)
    G_PHAT = (X1f . [X2f]*) / abs(X1f. [X2f]*)   /////// []* represents conjugate
    G_PHAT = ifft (G_PHAT)
    2) Then delay between two signals received is:
    d = argmax (R_PHAT)
    
    Parameters:
        x1, x2:   audio signals from mic1 and mic2
        fs:       sampling frequency
        max_tau:  max time delay to consider in samples. If not provided, it will be set to half the length of the longer signal.
    
    Return:
        cc:       GCC-PHAT matrix
        tau:      time difference of arrival between x1 and x2 (If tau is negative, it simply means that the sound wave arrives at the second microphone before it arrives at the first microphone.)
            
    '''
    
    # Taking only one channel
    if x1.ndim==2:
        x1 = x1[:,1]
    if x2.ndim==2:
        x2 = x2[:,1]
 
    #####################################  Method 1
    # make sure the length for the FFT is larger or equal than len(x1) + len(x2)
    n = x1.shape[0]  + x2.shape[0]
    
    # Step 1: Convert signals into frequency domain (compute 1D DFT using FFT algorithm)
    x1f = np.fft.rfft(x1, n=n) # equivalent to ==> y[k] = np.sum(x * np.exp(-2j * np.pi * k * np.arange(n)/n))
    x2f = np.fft.rfft(x2, n=n)

    # Step 2: Compute the cross-correlation using GCC-PHAT
    cc       = x1f * np.conj(x2f) # cross correlation
    phat     = 1/np.abs(cc)       # PHAT
    gcc_phat = cc*phat            # GCC-PHAT in frequency domain
    cc       = scipy.fft.irfft(gcc_phat, n=(interp * n))  # GCC-PHAT in time domain
    # Step 3: Compute TDOA 
    max_shift = int(interp * n / 2)
    if max_tau:
        max_shift = np.minimum(int(interp * fs * max_tau), max_shift)
        print('finding max shift', max_shift)
    cc        = np.concatenate((cc[-max_shift:], cc[:max_shift+1]))
    shift     = np.argmax(np.abs(cc)) - max_shift  # find max cross correlation index
    tau       = shift / int(interp * fs)
    return cc, tau