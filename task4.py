import pandas as pd
import matplotlib.pyplot as plt

# sample data
data = {
    "Weather": ["Clear","Rain","Fog","Clear","Rain","Fog","Clear"],
    "Accidents": [10,25,15,12,30,18,14]
}

df = pd.DataFrame(data)

# count accidents
df.groupby("Weather")["Accidents"].sum().plot(kind='bar')

plt.title("Accidents by Weather Condition")
plt.xlabel("Weather")
plt.ylabel("Number of Accidents")

plt.show()