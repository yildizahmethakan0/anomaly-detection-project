import numpy as np
from src.anomaly_detector import AnomalyDetector
from src.data_generator import generate_data_stream
from src.visualizer import visualize_stream

def main():
    n_points = 1000
    data_stream = generate_data_stream(n_points)
    detector = AnomalyDetector()
    anomalies = np.zeros(n_points, dtype=bool)

    for i, value in enumerate(data_stream):
        detector.update(value)
        if detector.is_anomaly(value):
            anomalies[i] = True
        
        # Simulate real-time processing
        if i % 100 == 0:
            print(f"{i} data points processed...")

    print("Anomaly detection completed.")
    visualize_stream(data_stream, anomalies)

if __name__ == "__main__":
    main()