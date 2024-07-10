import subprocess

# Step 1: Enrich the dataset and generate BBAs for both sources
subprocess.run(["Rscript", "__main.R"])

# Step 2: Load BBAs and combine using CWAC method
# Implement the CWAC method in Python
import numpy as np
import pandas as pd

# Load BBAs
bba_source1 = pd.read_rds("bba_source1.rds")
bba_source2 = pd.read_rds("bba_source2.rds")

# Implement the CWAC combination (this is a placeholder, implement your method)
def combine_cwac(bba1, bba2):
    combined_bba = (bba1 + bba2) / 2  # Simplified example, replace with actual CWAC logic
    return combined_bba
    
combined_bba = combine_cwac(bba_source1, bba_source2)

# Step 3: Calculate pignistic probabilities from combined BBA
def calculate_betp(bba):
    # Placeholder for BetP calculation
    betp = bba / np.sum(bba, axis=1, keepdims=True)
    return betp

betp = calculate_betp(combined_bba)

# Save the results
np.save("combined_bba.npy", combined_bba)
np.save("betp.npy", betp)
