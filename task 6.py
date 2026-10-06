import numpy as np

def analyze_distribution(seed):
    rng = np.random.default_rng(seed)
    measurements = rng.normal(loc=0, scale=1, size=1000)
    
    mean_val = np.mean(measurements)
    median_val = np.median(measurements)
    std_val = np.std(measurements)
    min_val = np.min(measurements)
    max_val = np.max(measurements)
    
    lower_bound = mean_val - std_val
    upper_bound = mean_val + std_val
    inside_1_std = np.sum((measurements >= lower_bound) & (measurements <= upper_bound))
    percentage = (inside_1_std / 1000) * 100
    
    return mean_val, median_val, std_val, min_val, max_val, percentage

mean1, med1, std1, min1, max1, pct1 = analyze_distribution(42)
mean2, med2, std2, min2, max2, pct2 = analyze_distribution(99)

print(f"Seed 42 -> Mean: {mean1:.4f}, Median: {med1:.4f}, Std: {std1:.4f}, Min: {min1:.4f}, Max: {max1:.4f}, Inside 1 Std: {pct1}%")
print(f"Seed 99 -> Mean: {mean2:.4f}, Median: {med2:.4f}, Std: {std2:.4f}, Min: {min2:.4f}, Max: {max2:.4f}, Inside 1 Std: {pct2}%")
