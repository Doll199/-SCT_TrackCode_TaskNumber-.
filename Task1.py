import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Age_Group": ["0-18", "19-35", "36-50", "51-65", "65+"],
    "Population": [500, 800, 600, 300, 200]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,5))

bars = plt.bar(df["Age_Group"], df["Population"])

# add values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, yval, ha='center')

plt.title("Population Distribution by Age Group", fontsize=14)
plt.xlabel("Age Group", fontsize=12)
plt.ylabel("Population", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()