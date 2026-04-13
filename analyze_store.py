import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv("trades.csv")

# Create database
engine = create_engine('sqlite:///trading_journal.db')

# Save to database
df.to_sql('trades', engine, if_exists='append', index=False)

# ---- ANALYSIS ---- #
total_trades = len(df)
win_trades = len(df[df['profit'] > 0])
loss_trades = len(df[df['profit'] < 0])

win_rate = (win_trades / total_trades) * 100 if total_trades > 0 else 0
total_profit = df['profit'].sum()

print("📊 ANALYSIS RESULT")
print("Total Trades:", total_trades)
print("Win Trades:", win_trades)
print("Loss Trades:", loss_trades)
print("Win Rate:", round(win_rate, 2), "%")
print("Total Profit:", round(total_profit, 2))

print("Saved to Database ✅")