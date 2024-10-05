Anomaly Detection in Data Streams
This project implements a real-time anomaly detection system for continuous data streams. It uses a simple statistical approach based on Z-scores to identify unusual patterns or exceptionally high values in the data.
Features

Real-time anomaly detection in continuous data streams
Adaptive algorithm that can handle concept drift and seasonal variations
Data stream simulation with trend, seasonality, and random noise
Visualization of the data stream and detected anomalies

![Figure_1](https://github.com/user-attachments/assets/d11d2f81-66a2-4615-8d38-719647391f5d)


Requirements

Python 3.10,
NumPy,
Matplotlib,
SciPy,

Installation

Clone this repository:
Copygit clone https://github.com/yildizahmethakan0/anomaly-detection-project.git
cd anomaly-detection-project

Install the required packages:
Copypip install -r requirements.txt


Usage
Run the main script:
Copypython main.py
This will generate a simulated data stream, perform anomaly detection, and display a graph showing the data stream and detected anomalies.
Project Structure

src/anomaly_detector.py: Contains the AnomalyDetector class implementing the detection algorithm
src/data_generator.py: Includes functions for generating simulated data streams
src/visualizer.py: Contains functions for visualizing the data and anomalies
main.py: The main script that ties everything together

How It Works
The anomaly detection algorithm uses a sliding window approach with Z-score calculation. It continuously updates the mean and standard deviation of the data within the window and flags a data point as an anomaly if its Z-score exceeds a specified threshold.
Limitations

Assumes the data follows a normal distribution
May not be as effective for detecting subtle or gradual anomalies
The fixed threshold might need tuning for different datasets
