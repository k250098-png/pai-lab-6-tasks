import numpy as np

sensors = np.random.uniform(10.0, 100.0, size=(4, 6))
sensor_means = np.mean(sensors, axis=1)
sensor_mins = np.min(sensors, axis=1)
sensor_maxs = np.max(sensors, axis=1)
sensor_stds = np.std(sensors, axis=1)

top_sensor_idx = np.argmax(sensor_means)
threshold = 75.0
high_readings = sensors[sensors > threshold]

print("Sensor Data Matrix:\n", sensors)
print("Per-Sensor Means:", sensor_means)
print("Per-Sensor Mins:", sensor_mins)
print("Per-Sensor Maxs:", sensor_maxs)
print("Per-Sensor Stds:", sensor_stds)
print(f"Sensor with Highest Average: Sensor {top_sensor_idx}")
print(f"Readings above {threshold}:", high_readings)
