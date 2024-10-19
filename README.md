# Anomaly Detection on Streamed Data 🌐

Welcome to the **Efficient Data Stream Anomaly Detection** project! This repository provides a framework for detecting anomalies in real-time data streams using the Z-score method. It includes data simulation, anomaly detection, and real-time visualization.

## 📌 What is Anomaly Detection?

Anomaly detection identifies unusual patterns or outliers that deviate from the expected behavior in data. These anomalies often represent critical incidents such as fraud, system failures, or unusual system behavior.

## 🔥 Why is Anomaly Detection Important?

- **Proactive Risk Management**: Early detection of anomalies helps mitigate risks.  
  _Example_: Detecting fraudulent transactions in real-time prevents financial losses.
- **Enhanced Security**: Spotting unusual activity in real-time strengthens cybersecurity.  
  _Example_: Identifying an unusual spike in login attempts signals a possible intrusion.
- **Quality Control**: Detecting defects ensures that products meet required standards.  
  _Example_: Identifying abnormal measurements in manufacturing improves quality assurance.
- **Improved Insights**: Anomalies may offer insights that lead to better decisions and strategies.  
  _Example_: Discovering unusual patterns in customer behavior to adjust marketing or sales strategies.

---

## 🚀 Project Features:

1. **Continuous Data Stream Simulation**: A function generates synthetic data with seasonal variation, noise, and rare anomalies.
2. **Z-Score Anomaly Detection**: Efficiently detects outliers based on the Z-score formula.
3. **Real-time Visualization**: Continuously updates a plot to visualize the data stream and mark detected anomalies.
4. **Interactive Plot**: Red markers indicate anomalies in the live-updating plot for easy identification.
5. **Robust Error Handling and Data Validation**: Ensures that the data points are valid and checks for potential issues in processing. This keeps the algorithm stable and avoids crashes in production environments.

---

## 🛠 How to Run the Code on Your System:

1. Clone the repository:

   ```bash
   git clone https://github.com/rifat328/Anomaly-Detection-on-Streamed-Data.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Anomaly-Detection-on-Streamed-Data
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python main.py
   ```

---

## 📐 Theory and Formula:

### Z-Score Formula:

The Z-score of a data point measures how far it is from the mean, relative to the standard deviation. The formula is:

Z = (x - μ) / σ

Where:

- `x` = current data point
- `μ` = mean of the data stream so far
- `σ` = standard deviation of the data stream so far

If the absolute value of the Z-score exceeds 3, the point is flagged as an anomaly.

### Incremental Mean and Variance:

The Z-score calculation depends on real-time updates to the mean and variance of the data stream:

- **Mean update**:
  ```
  new_mean = old_mean + (x - old_mean) / n
  ```
- **Variance update**:
  ```
  new_variance = old_variance + ((x - old_mean) * (x - new_mean)) / n
  ```

These updates allow the algorithm to efficiently handle continuous data without storing the entire dataset.

### **Effectiveness of the Z-Score Algorithm**:

- **Simplicity**: Z-score is an effective statistical method for detecting anomalies, particularly in continuous data streams, as it identifies points significantly deviating from the mean.
- **Real-time Efficiency**: The incremental calculation of mean and variance ensures that the algorithm performs efficiently even on large data streams without storing all past data.
- **Adaptability**: The Z-score method can be easily tuned by adjusting the threshold (default: Z > 3) to suit different data environments and anomaly detection needs.

---

## 📂 Inner Structure of Code:

1. **Streamed Data Generator**: Simulates a continuous stream with seasonal variation, random noise, and rare anomalies.
2. **Z-Score Based Anomaly Detector**: Tracks the mean and variance of the data stream and flags points with a Z-score greater than 3 as anomalies.
3. **Visualization**: Real-time plotting of the data stream with anomalies highlighted in red.
4. **Error Handling and Data Validation**: Ensures that only valid data is passed through the anomaly detection algorithm and that the process handles unexpected data smoothly.

---

## 🧑‍💻 Code Explanation:

### Streamed Data Generator:

This function simulates data as a combination of:

- Seasonal variations (`sin` wave pattern).
- Random noise.
- Anomalies generated with a 1% probability.

```python
def data_stream():
    while True:
        seasonal = 10 * np.sin(time_value)
        anomaly = random.choices([0, random.uniform(10, 20)], [0.99, 0.01])[0]
        noise = random.uniform(-1, 1)
        yield seasonal + noise + anomaly
```

## Z-Score Based Anomaly Detection:

The ZScoreAnomalyDetector class calculates the Z-score for each point and flags anomalies in real-time.

```python
if abs(z) > 3:
print(f"Anomaly detected: {data_point}, Z-score: {z}")
```

## Real-time Visualization:

Uses matplotlib to plot the data stream and anomalies dynamically. Anomalies are highlighted with red scatter points.

## Robust Error Handling:

The code checks for potential invalid data points (like NaN values or extremely large/small numbers). If detected, it will handle the error gracefully, either by skipping the problematic point or issuing a warning, ensuring that the detection process remains stable.

## ✅ Small-scale Algorithm Test:

A small static test is included in the comments to validate the Z-score calculation on a predefined dataset.

**Example static data test**

```python
data = [1, 2, 2, 2, 3, 1, 1, 15, 2, 2]
```

🔍 Example Command to Run:

```bash
pip install -r requirements.txt
python main.py
```

## 🌱 Future Improvements:

Add dynamic thresholds that adjust based on long-term trends in the data stream.
Extend anomaly detection to handle multivariate data streams.
Incorporate advanced error detection and recovery mechanisms for a more robust system

### **⭐Feel free to contribute or fork this project for your own needs! and give a Star ⭐**
