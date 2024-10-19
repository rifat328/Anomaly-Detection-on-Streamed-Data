import ZScore_anomaly_detector as zScoreClass
import numpy as np 
import random
import matplotlib.pyplot as plt

# Function to simulate the continuous data stream
def data_stream():
    t = 0  # Initialize time counter
    while True:
        time_value = t  # Use as the time value
        seasonal = 10 * np.sin(time_value)  # Seasonal variation
        anomaly = random.choices([0, random.uniform(10, 20)], [0.99, 0.01])[0]  # 1% chance of anomaly
        noise = random.uniform(-1, 1)  # Small random noise
        yield seasonal + noise + anomaly  # Yield the sum of seasonal, noise, and any anomaly
        
        t += 0.1  # Increment time value

# Anomaly detection function
def anomaly_detection(stop_threshold=1000):
    """Detect anomalies in a continuous data stream using Z-score and visualize results."""
    detector = zScoreClass.ZScoreAnomalyDetector()  # Initialize the anomaly detector
    stream = data_stream()  # Get the data stream

    # Initialize lists for plotting
    data_points = []
    z_scores = []
    anomaly_points = []

    # Set up the plot
    plt.ion()  # Turn on interactive mode for real-time plotting
    fig, ax = plt.subplots()
    line, = ax.plot([], [], label='Data Stream')
    scatter_anomaly = ax.scatter([], [], color='red', label='Anomalies')
    ax.set_xlim(0, stop_threshold)
    ax.set_ylim(-20, 30)
    ax.set_xlabel('Time Steps')
    ax.set_ylabel('Data Value')
    ax.legend()

    for i, data_point in enumerate(stream):
        detector.update(data_point)  # Update mean and variance
        z = detector.z_score(data_point)  # Calculate Z-score
        
        # Append to data lists
        data_points.append(data_point)
        z_scores.append(z)
        
        # Plot update
        line.set_data(range(len(data_points)), data_points)

        # Check for anomaly
        if abs(z) > 3:
            print(f"Anomaly detected: {data_point}, Z-score: {z}")
            anomaly_points.append((i, data_point))  # Store anomaly points

        # Update scatter plot for anomalies
        if anomaly_points:
            ax.scatter(*zip(*anomaly_points), color='red')

        # Redraw plot
        ax.set_xlim(0, max(10, len(data_points)))
        fig.canvas.draw()
        fig.canvas.flush_events()

        # Stop after a set number of iterations
        if i >= stop_threshold:
            break

    plt.ioff()  # Turn off interactive mode
    plt.show()

# Run the anomaly detection function

anomaly_detection()
























"""
small scale Algorithm Test

# data = [1, 2, 2, 2, 3, 1, 1, 15, 2, 2, 2, 3, 1, 1, 2]
# mean = np.mean(data)
# std = np.std(data)
# print('mean of the dataset is', mean)
# print('std. deviation is', std)

threshold = 3
outlier = []
for i in data:
	z = (i-mean)/std
	if z > threshold:
		outlier.append(i)
print('outlier in dataset is', outlier)

"""


# For Z-Score Calculation:
# To calculate the Z-score of a data point in a stream, you'll need:

# The mean of the data stream up to the current point.
# The standard deviation of the data stream up to the current point.

# for continious data stream intremental Mean calculation
#! new_mean= old_mean + (x - old_mean)/n

# Incremental Variance and Standard Deviation:
# The standard deviation can be calculated incrementally by first updating the variance 
# (because standard deviation is just the square root of variance).

#! new_variance=old_variance + (x-old_mean) * (x-new-mean) / n 
# where x= new data_point and n is number of data point.
# then 
#! new_standerd_deviation = root_over(new_variance)

# !Z-Score:
#!  Z = x - U / sigma   where x = new current data point , u is the mean of the data stream so far ,
# !  sigma is the standard_deviation in data stream so far.  