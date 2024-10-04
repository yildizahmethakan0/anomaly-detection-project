import numpy as np
from collections import deque

class AnomalyDetector:
    def __init__(self, window_size=100, threshold=3):
        self.window_size = window_size
        self.threshold = threshold
        self.data_window = deque(maxlen=window_size)
        self.mean = 0
        self.std = 1

    def update(self, value):
        self.data_window.append(value)
        
        if len(self.data_window) == self.window_size:
            self.mean = np.mean(self.data_window)
            self.std = np.std(self.data_window)

    def is_anomaly(self, value):
        if len(self.data_window) < self.window_size:
            return False
        z_score = abs((value - self.mean) / self.std)
        return z_score > self.threshold