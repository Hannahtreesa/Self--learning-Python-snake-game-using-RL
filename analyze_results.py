import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("model_eval_data.csv")  # Ensure correct filename

# 📊 Basic Statistics
print("📈 Model Performance Summary:")
print(df.describe())  # Shows mean, min, max, std, etc.

# 📉 Plot Score Progression Over Games
plt.figure(figsize=(10, 5))
plt.plot(df["Game"], df["Score"], label="Score per Game", color="blue", alpha=0.6)
plt.xlabel("Game Number")
plt.ylabel("Score")
plt.title("Score Progression Over Games")
plt.legend()
plt.show()

# 📊 Histogram of Scores (How Often a Score Occurs)
plt.figure(figsize=(8, 5))
plt.hist(df["Score"], bins=10, color="purple", edgecolor="black", alpha=0.7)
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Score Distribution")
plt.show()

# 📈 Moving Average to See Performance Trends
df["Moving_Avg"] = df["Score"].rolling(window=10).mean()  # Smooth out fluctuations

plt.figure(figsize=(10, 5))
plt.plot(df["Game"], df["Score"], label="Score per Game", color="blue", alpha=0.4)
plt.plot(df["Game"], df["Moving_Avg"], label="10-Game Moving Average", color="red", linewidth=2)
plt.xlabel("Game Number")
plt.ylabel("Score")
plt.title("Performance Over Time (With Moving Average)")
plt.legend()
plt.show()
