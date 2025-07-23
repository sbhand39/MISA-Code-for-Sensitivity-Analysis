import os
import numpy as np
import pandas as pd
from scipy.stats import wasserstein_distance

# === STEP 1: Read input from Excel ===
input_path = r"Input excel file path"                                    #CHANGE HERE!!!
df = pd.read_excel(input_path, sheet_name='sheet name')                  #CHANGE HERE!!!

# === STEP 2: Simulate lognormal variables ===
n = 10000
np.random.seed(0)

input_names = df['INPUT'].tolist()
input_values = {}
for _, row in df.iterrows():
    name = row['INPUT']
    mu1, sigma1 = row['AM_m'], row['AM_sd']
    mu2, sigma2 = row['IMPACT CATEGORY_m'], row['IMPACT CATEGORY_sd']    #CHANGE HERE!!!
    samples = np.exp(
        np.random.normal(mu1, sigma1, n) +
        np.random.normal(mu2, sigma2, n)
    )
    input_values[name] = samples

# === STEP 3 & 4: Stack inputs and compute total output Y ===
X = np.column_stack(list(input_values.values()))
Y = X.sum(axis=1)

# === STEP 5: Compute MISA Delta Index per input ===
quantiles = [10, 30, 50, 70, 90]
mean_deltas = []
for xi in X.T:
    delta_vals = []
    for q in quantiles:
        val = np.percentile(xi, q)
        mask = np.abs(xi - val) < 0.05 * xi.ptp()
        if mask.sum() > 200:
            delta_vals.append(wasserstein_distance(Y, Y[mask]))
    mean_deltas.append(np.mean(delta_vals))

# === STEP 6: Write results to Excel ===
out_df = pd.DataFrame({
    'INPUT': input_names,
    'MISA Delta Index': mean_deltas
})

# your desired folder:
output_dir = r"Output file path"                                         #CHANGE HERE!!!
os.makedirs(output_dir, exist_ok=True)                          

# desired filename (with .xlsx extension)
filename = "Output file name.xlsx"                                       #CHANGE HERE!!!
output_path = os.path.join(output_dir, filename)

out_df.to_excel(output_path, index=False)
print(f"Results written to:\n{output_path}")
