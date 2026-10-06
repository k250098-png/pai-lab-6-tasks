import numpy as np

features = np.random.rand(10, 4) * 100
feature_means = np.mean(features, axis=0)
feature_stds = np.std(features, axis=0)
standardized_features = (features - feature_means) / feature_stds

print("Original Features:\n", features)
print("Feature Means:", feature_means)
print("Feature Standard Deviations:", feature_stds)
print("Standardized Features:\n", standardized_features)
print("Verification - Means (should be ~0):", np.mean(standardized_features, axis=0))
print("Verification - Std Devs (should be ~1):", np.std(standardized_features, axis=0))
