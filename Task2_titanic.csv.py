import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("titanic.csv")

# -------------------------------
# 1. Basic Info
# -------------------------------
print("First 5 Rows:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())

# -------------------------------
# 2. Survival Count
# -------------------------------
plt.figure(figsize=(6,4))
df['Survived'].value_counts().plot(kind='bar')

plt.title("Survival Count", fontweight='bold')
plt.xlabel("0 = Not Survived, 1 = Survived")
plt.ylabel("Count")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("task2_survival.png")
plt.show()

# -------------------------------
# 3. Age Distribution
# -------------------------------
plt.figure(figsize=(6,4))
df['Age'].dropna().plot(kind='hist', bins=20)

plt.title("Age Distribution", fontweight='bold')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("task2_age.png")
plt.show()

# -------------------------------
# 4. Passenger Class Distribution
# -------------------------------
plt.figure(figsize=(6,4))
df['Pclass'].value_counts().plot(kind='bar')

plt.title("Passenger Class Distribution", fontweight='bold')
plt.xlabel("Class (1=High, 3=Low)")
plt.ylabel("Count")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("task2_class.png")
plt.show()

# -------------------------------
# 5. Survival by Gender (IMPORTANT 🔥)
# -------------------------------
plt.figure(figsize=(6,4))
df.groupby('Sex')['Survived'].mean().plot(kind='bar')

plt.title("Survival Rate by Gender", fontweight='bold')
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("task2_gender.png")
plt.show()