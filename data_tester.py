import pandas as pd

# Load dataset
file_path = 'transfers_history.csv'
df = pd.read_csv(file_path)

print("--- Data Analysis Report ---")

# 1. Total records check
print(f"Total Transfers Processed: {df.shape[0]}")

# 2. Position distribution
print("\n--- Top 5 Playing Positions ---")
print(df['position'].value_counts().head(5))

# 3. Average transfer fee
avg_fee = df['fee_eur_m'].mean()
print(f"\nAverage Transfer Fee: {avg_fee:.2f} Million Euro")

# 4. Top 5 Leagues receiving players
print("\n--- Top 5 Leagues Receiving Players ---")
print(df['to_league'].value_counts().head(5))

print("\n--- Analysis Complete ---")

