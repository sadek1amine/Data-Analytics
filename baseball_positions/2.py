import pandas as pd
import matplotlib.pyplot as plt

# Read CSV مباشرة
df = pd.read_csv("baseball_positions.csv")

# Split multiple positions
df["Position"] = df["Position"].str.split("/")

# Expand rows (important step)
df = df.explode("Position")

# Count players per position
position_counts = df["Position"].value_counts()

# Convert to table
result = position_counts.reset_index()
result.columns = ["Position", "Player Count"]

print(result)
