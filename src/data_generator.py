import numpy as np


def generate_data_stream(n, seasonality=24, trend=0.1, noise_level=1):
    time = np.arange(n)
    trend_component = trend * time
    seasonal_component = 10 * np.sin(2 * np.pi * time / seasonality)
    noise = np.random.normal(0, noise_level, n)
    data = trend_component + seasonal_component + noise
    
    # Anomalileri ekle
    anomaly_indices = np.random.choice(n, size=int(n*0.05), replace=False)
    data[anomaly_indices] += np.random.uniform(15, 25, size=len(anomaly_indices))
    
    return data
