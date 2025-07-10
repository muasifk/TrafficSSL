import numpy as np

def SRP_updated(x1, x2, fs, mic_seperation):

    # Normalize both signals before proceeding
    x1 = x1 / np.linalg.norm(x1)
    x2 = x2 / np.linalg.norm(x2)

    results = []

    for angle in range (-90, 90):
        delay_samples = int(fs * mic_seperation * np.cos(np.radians(90) - np.radians(angle)) / 345)
        x_delayed = np.roll(x2, delay_samples)
 

        # because they're both np array you can do matrix operation on them directly 
        # Comapre x_delayed with x1 (as x2 is the earlier signal (for positive degrees), we delay it)
        addition = x_delayed + x1
        power = np.sum(addition ** 2)



# list composition, doing the operation on each element of both lists
#         # Comapre x_delayed with x1 (as x2 is the earlier signal (for positive degrees), we delay it)
#         addition = [x_delayed[i] + x1[i] for i in range (len (x1))]  
#         power = sum([x ** 2 for x in addition]) # building the results with the power of the addition of both signals element by elem


        results.append(power)
        # print(f"Angle: {angle},\tDelay Samples: {delay_samples},\tPower Comparison Score: {power}")

    return np.argmax(results) - 90




#slowww
# import numpy as np
# import matplotlib.pyplot as plt

# def beamforming_search(x1, x2, fs, mic_seperation):

#     # Normalize both signals before proceeding
#     x1 = x1 / np.linalg.norm(x1)
#     x2 = x2 / np.linalg.norm(x2)

#     results = []

#     for angle in range (-90, 90):
#         delay_samples = int(fs * mic_seperation * np.cos(np.radians(90) - np.radians(angle)) / 345)
#         x_delayed = np.roll(x2, delay_samples)
#         # list composition, doing the operation on each element of both lists
#         # Comapre x_delayed with x1 (as x2 is the earlier signal (for positive degrees), we delay it)
#         addition = [x_delayed[i] + x1[i] for i in range (len (x1))]  
#         power = sum([x ** 2 for x in addition]) # building the results with the power of the addition of both signals element by elem

#         results.append(power)
#         #print(delay_samples, angle, power)
#         doa=np.argmax(results) - 90

#     return doa

