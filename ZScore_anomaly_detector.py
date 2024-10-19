import numpy as np 
import random
import math
class ZScoreAnomalyDetector:
    def __init__(self):
        self.n = 0  # Count of data points
        self.mean = 0  # Running mean
        self.M2 = 0  # Running sum of squares of differences from the mean (used to calculate variance)
    
    def update(self, x):
        """Update mean and variance incrementally."""
        self.n += 1
        delta = x - self.mean  # Difference between new data point and current mean
        self.mean += delta / self.n  # Update the mean
        delta2 = x - self.mean  # Difference between new data point and new mean
        self.M2 += delta * delta2  # Update M2 for variance calculation

    def variance(self):
        """Return the variance."""
        if self.n < 2:
            return float('nan')  # Variance is undefined for fewer than 2 data points
        return self.M2 / (self.n - 1)  # Return the unbiased estimate of variance
    
    def std(self):
        """Return the standard deviation."""
        return math.sqrt(self.variance())  # Standard deviation is the square root of variance
    
    def z_score(self, x):
        """Calculate the Z-score of the new data point."""
        if self.n < 2:
            return 0  # Z-score is not meaningful if we have less than 2 data points
        return (x - self.mean) / self.std()  # Z-score formula




