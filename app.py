from flask import Flask
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Connect database
engine = create_engine('sqlite:///trading_journal.db')

@app.route('/')
def dashboard():
    df = pd.read_sql("SELECT * FROM trades", engine)

    total_trades = len(df)
    win_trades = len(df[df['profit'] > 0])
    loss_trades = len(df[df['profit'] < 0])

    win_rate = (win_trades / total_trades) * 100 if total_trades > 0 else 0
    total_profit = df['profit'].sum()

    return f"""
    <h1>📊 Trading Journal Dashboard</h1>
    <p>Total Trades: {total_trades}</p>
    <p>Win Trades: {win_trades}</p>
    <p>Loss Trades: {loss_trades}</p>
    <p>Win Rate: {win_rate:.2f}%</p>
    <p>Total Profit: {total_profit}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)