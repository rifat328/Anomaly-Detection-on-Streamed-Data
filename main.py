import numpy as np 
import random
#Anomaly: variable
#random.choices(population , weights ) choses population based on provided weight,
# The weights determine the likelihood of each item being chosen.
#anomaly = random.choices([0, random.uniform(10, 20)], [0.99, 0.01])[0]    last 0 represent arrey index
                        #    population part              Weight Part which is 99% normal & 1% anomaly



def data_stream():
    t = 0  # Initialize time counter
    while True:
        time_value = t  # Use as the time value intiger
        seasonal = 10 * np.sin(time_value)  # Seasonal variation, sin simulating cyclic behavior
        anomaly = random.choices([0, random.uniform(10, 20)], [0.99, 0.01])[0]  # Rare anomaly 1% chance of anomaly
        noise = random.uniform(-1, 1)  #Small random noise
        yield seasonal + noise + anomaly  #Yield the sum of seasonal, noise, and any anomaly
        
        t += 0.1  # Will Incriment time value over time like real world




def anomaly_detection(stop_threshold=20): # This stop_hreshold serves as a stoping point so we can stop the program rather then infinite loop 
    stream= data_stream()
    for data_point in stream:
        print(f"Data Point: {data_point}")


anomaly_detection()
# anomaly detection algorithm , from stream data , show flaged data in visiulised way + documentation Update<< Work left tomorrow




















# data = [1, 2, 2, 2, 3, 1, 1, 15, 2, 2, 2, 3, 1, 1, 2]
# mean = np.mean(data)
# std = np.std(data)
# print('mean of the dataset is', mean)
# print('std. deviation is', std)


# threshold = 3
# outlier = []
# for i in data:
# 	z = (i-mean)/std
# 	if z > threshold:
# 		outlier.append(i)
# print('outlier in dataset is', outlier)

