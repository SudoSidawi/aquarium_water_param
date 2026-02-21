#importing pandas library to read data from google sheet
import pandas as pd
import matplotlib.pyplot as plt

#Importing from google sheet URL
spreadsheet_id = "104BzVJoxskDc4tqmh2YoNQAHY7g3p8yTRQW98stTAVQ"
gid = "1664117972"
url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&gid={gid}"
df = pd.read_csv(url)


df["Date"] = pd.to_datetime(df["Date"])

# Set Date as index (handy for time series plots)
df = df.set_index("Date")

# Choose the parameter columns you want to plot
cols = ["Ammonia", "Nitrite", "Nitrate", "PH"]  # rename to your exact headers

# Single line chart with one line per parameter
plt.figure(figsize=(10, 6))
for col in cols:
    plt.plot(df.index, df[col], marker="o", label=col)

plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Water Parameters Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
