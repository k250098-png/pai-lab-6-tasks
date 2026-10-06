import numpy as np

data = np.array([10.0, 20.0, np.nan, 40.0, np.nan, 60.0])
nan_mask = np.isnan(data)

print("Original Data:", data)
print("NaN Mask:", nan_mask)
print("Indices of NaNs:", np.where(nan_mask)[0])

valid_mean = np.nanmean(data)
print("NaN-aware Mean:", valid_mean)

cleaned_data = np.where(nan_mask, valid_mean, data)
remaining_nans = np.isnan(cleaned_data).sum()

print("Cleaned Data:", cleaned_data)
print("Remaining NaNs Count:", remaining_nans)
