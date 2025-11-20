import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../dataset/sales.csv")

# Line chart
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
