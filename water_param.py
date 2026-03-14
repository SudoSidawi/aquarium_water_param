#source venv/bin/activate

import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
#import tkinter as tk
#from tkinter import filedialog

#Importing from google sheet URL
spreadsheet_id = "104BzVJoxskDc4tqmh2YoNQAHY7g3p8yTRQW98stTAVQ"
gid = "1664117972"
url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&gid={gid}"
df = pd.read_csv(url)

# --- Step 3: Create the Plot ---
columns_to_plot = ['Ammonia', 'Nitrite']
fig, ax = plt.subplots(figsize=(14, 8))

for column in columns_to_plot:
    if column in df.columns:
        ax.plot(df.index, df[column], label=column, marker='o', linestyle='-')

# --- Step 4: Add Vertical Lines for 'Dose' Events ---
if 'Dose' in df.columns:
    dose_dates = df[df['Dose'] == 1].index
    v_line_plotted = False
    for date in dose_dates:
        label = 'Ammonia Dose' if not v_line_plotted else ""
        ax.axvline(x=date, color='r', linestyle='--', linewidth=2, label=label)
        v_line_plotted = True
else:
    print("FYI: 'Dose' column not found. Skipping event markers.")

#---- Step 4.5: Add verticle line for when fish are added to the tank
if 'Dose' in df.columns:
    fish_dates = df[df['New_Fish'] == 1].index
    v_line_plotted = False
    for date in fish_dates:
        label = 'Fish Introduction' if not v_line_plotted else ""
        ax.axvline(x=date, color='b', linestyle='--', linewidth=2, label=label)
        v_line_plotted = True
else:
    print("FYI: 'Fish' column not found. Skipping event markers.")


# --- Step 5 & 6: Customize and Show Plot ---
ax.set_title('Tank Water Parameters Over Time', fontsize=16)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Concentration / PH', fontsize=12)
ax.legend()
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
fig.autofmt_xdate()

plt.tight_layout()
plt.show()