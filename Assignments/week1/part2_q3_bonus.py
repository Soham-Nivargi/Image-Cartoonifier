import pandas as pd

df = pd.read_csv('/Users/sohamnivargi/Desktop/Code/week1/Data - STOCK_US_XNYS_CSV.csv')
#print(df)
df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

avg_closing_prices = df.groupby("Month")["Close"].mean()

#print(avg_closing_prices)

df = df.sort_values("Date")

df.write_to_csv('/Users/sohamnivargi/Desktop/Code/week1/Data - STOCK_US_XNYS_CSV.csv')
print(df)
df["Rolling Average"] = df["Close"].rolling(window=30).mean()

df = df[df["Rolling Average"] > df["Close"] * 1.05]

#for index, row in df.sort_values("Date").iterrows():
   # print(row["Date"].strftime("%Y-%m-%d"), row["Close"])