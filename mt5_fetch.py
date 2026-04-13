import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

# Connect MT5
if not mt5.initialize():
    print("MT5 connection failed ❌")
    quit()

print("MT5 Connected ✅")

# Get last 30 days trades (safer)
to_date = datetime.now()
from_date = to_date - timedelta(days=30)

# Fetch trades
deals = mt5.history_deals_get(from_date, to_date)

if deals is None or len(deals) == 0:
    print("No trades found ❌")
    mt5.shutdown()
    quit()

# Convert to DataFrame
df = pd.DataFrame(list(deals), columns=deals[0]._asdict().keys())

# Select useful columns
df = df[['time', 'symbol', 'profit', 'volume', 'type']]

# Convert time
df['time'] = pd.to_datetime(df['time'], unit='s')

# Save CSV
df.to_csv("trades.csv", index=False)

print("✅ trades.csv created successfully")

mt5.shutdown()