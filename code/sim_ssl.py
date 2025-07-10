

import soundfile as sf
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


# Function to generate a simple sound source (sine wave)
def generate_sound(frequency, duration, sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    return 0.5 * np.sin(2 * np.pi * frequency * t)

# Function to add simulated background noise to a signal
def add_background_noise(signal, noise_level):
    noise = np.random.randn(len(signal))
    return signal + noise_level * noise

# Function to add real background noise to a signal
def overlay_signals(signal, noise):
    signal_len = len(signal)
    noise_len  = len(noise)
    if signal_len >= noise_len:
        # No need to overlay, the signal is longer or equal to the noise
        overlayed_signal = signal[:noise_len] + noise
    else:
        # Randomly select a start position within the noise signal
        start_idx = np.random.randint(0, noise_len - signal_len + 1)
        end_idx = start_idx + signal_len
        # Overlay the signal onto the noise
        overlayed_signal = signal + noise[start_idx:end_idx]
    return overlayed_signal

# Function to simulate a two-microphone array recording
def simulate_microphone_array(signal, mic_distance, angle, sampling_rate):
    '''
    Important: order of mic1_signal and mic2_signal is important. Currently, mic1 is receiving signal first.
    '''
    speed_of_sound = 343.0  # Speed of sound in air (m/s)
    if angle >= 0:
        tau = mic_distance * np.sin(np.radians(angle)) / speed_of_sound  # Malek Try this (But use sin function in TDAO_to_DOA function as well)
    
        #tau = mic_distance * np.cos(np.radians(angle)) / speed_of_sound   # the time delay between the signals recorded by the two microphones.
        time_shift  = int(tau * sampling_rate)   # the number of samples by which one of the microphone signals should be time-shifted.
        mic1_signal = np.pad(signal, (time_shift, 0), 'constant')  # padded with zeros at the end (mic that receive the signal first)
        mic2_signal = np.pad(signal, (0, time_shift), 'constant')  # padded with zeros at the beginning  (mic that receive the signal last)
    else:
        tau = mic_distance * np.sin(np.radians(-angle)) / speed_of_sound  # Malek Try this (But use sin function in TDAO_to_DOA function as well)
        
        #tau = mic_distance * np.cos(np.radians(angle)) / speed_of_sound
        time_shift = int(tau * sampling_rate)
        mic1_signal = np.pad(signal, (0, time_shift), 'constant')
        mic2_signal = np.pad(signal, (time_shift, 0), 'constant')
        
    mic1_signal = mic1_signal[:len(signal)]  # length of mic1 signal is adjusted to match the length of the original signal
    mic2_signal = mic2_signal[:len(signal)]  # length of mic2 signal is adjusted to match the length of the original signal
    return mic1_signal, mic2_signal

# def plot_scene(src_loc, mic1_loc, mic2_loc):
#     # Plot the sound source and microphones
#     fig = plt.figure(figsize=(8, 6))
#     plt.scatter(*src_loc, c='r', marker='o', s=100, label='Sound Source')
#     plt.scatter(*mic1_loc, c='b', marker='^', s=80, label='mic1')
#     plt.scatter(*mic2_loc, c='g', marker='^', s=80, label='mic2')
#     plt.plot([src_loc[0], mic1_loc[0]], [src_loc[1], mic1_loc[1]], 'b', linestyle="--", lw=0.8)
#     plt.plot([src_loc[0], mic2_loc[0]], [src_loc[1], mic2_loc[1]], 'b', linestyle="--", lw=0.8)
#     plt.xlim(-1, 1)
#     plt.ylim(-1, 50)
#     plt.xlabel('X-coordinate (m)')
#     plt.ylabel('Y-coordinate (m)')
#     plt.legend()
#     plt.grid(True)
#     plt.title('SSL Simulation')
#     plt.show()
    


# Main function
def sim_ssl(mic_distance, angle_of_source):
    # Configuration
    sound_file       = "sounds\\honk.wav"
    noise_file       = 'sounds\\urban-ambience.wav'
    # mic_distance     = 0.15  # Microphone distance in meters
    # angle_of_source  = 90  # Angle of the sound source (in degrees)
    bg_noise_level   = 0.1
    
    ## Mics and sound location (currently used for visualization only)
    src_loc          = (0.5, 40)   # Replace with the actual sound source location
    mic1_loc         = (0, 0)  # Replace with the actual location of microphone 1
    mic2_loc         = (0.2, 0) # Replace with the actual location of microphone 
    # plot_scene(src_loc, mic1_loc, mic2_loc)

    # Load the sound files
    fs, sound_source = wavfile.read(sound_file)
    fs, noise_source = wavfile.read(noise_file)
    sound_source     = sound_source[:,1]  # Mono
    noise_source     = noise_source[:,1]  # Mono

    # Add background noise to the sound source
    # sound_with_noise = add_background_noise(sound_source, bg_noise_level)
    sound_with_noise = overlay_signals(sound_source, noise_source)

    # Simulate the two-microphone array recording (reverse order is to avoid an error) 
    mic1_signal, mic2_signal = simulate_microphone_array(sound_with_noise, mic_distance, angle_of_source, fs)
    # plt.plot(mic2_signal)

    # Save microphone recordings as .wav files
    # sf.write('./sim_outputs/mic1.wav', mic1_signal, fs)
    # sf.write('./sim_outputs/mic2.wav', mic2_signal, fs)
    sf.write('./sim_outputs/mic1_' + str(angle_of_source) + '.wav', mic1_signal, fs)
    sf.write('./sim_outputs/mic2_' + str(angle_of_source) + '.wav', mic2_signal, fs)

    # Play the sound source with background noise
    # p = pyaudio.PyAudio()
    # stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sampling_rate, output=True)
    # # stream.write(sound_with_noise.tobytes())
    # stream.write(mic2_signal.tobytes())
    # stream.stop_stream()
    # stream.close()
    # p.terminate()
    #print('Simulation Done ...')
    return mic1_signal, mic2_signal, fs

    # if __name__ == "__main__":
    #   main()