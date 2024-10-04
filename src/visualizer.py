import matplotlib.pyplot as plt
import numpy as np

def visualize_stream(data, anomalies):
    plt.figure(figsize=(12, 6))
    plt.plot(data, label='Data Stream')
    plt.scatter(np.where(anomalies)[0], data[anomalies], color='red', label='Anomalies')
    plt.legend()
    plt.title('Data Stream with Detected Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()