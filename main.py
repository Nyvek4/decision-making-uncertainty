import subprocess

dataset = 'iris'
# Step 1: Enrich the dataset and generate BBAs for both sources
subprocess.run(["C:\Program Files\R\R-4.4.1\\bin\Rscript.exe", "main.R", dataset])

# Step 2: Load BBAs and combine using CWAC method
import numpy as np
import pandas as pd
from framework import Framework

# Load BBAs
framework = Framework()
framework.set_bbas(dataset)
bbas = framework.get_bbas()

# Implement the CWAC combination
# Placeholder for CWAC combination logic
# combined_bba = ...

# # Step 3: Calculate pignistic probabilities from combined BBA
# def calculate_betp(bba):
#     # Placeholder for BetP calculation
#     betp = bba / np.sum(bba, axis=1, keepdims=True)
#     return betp

# betp = calculate_betp(combined_bba)

# # Save the results
# np.save("combined_bba.npy", combined_bba)
# np.save("betp.npy", betp)