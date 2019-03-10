import pandas
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np

pandas.set_option('display.max_columns', 10)

# Part 1
players = pd.read_csv("basketball_players.csv")
print(players.columns)

players["fgSuccessPercent"] = players["fgMade"] / players["fgAttempted"]
players = players[(players.fgAttempted > 0) & (players.fgSuccessPercent <= 1)]

players["ftSuccessPercent"] = players["ftMade"] / players["ftAttempted"]
players = players[(players.ftAttempted > 0) & (players.ftSuccessPercent <= 1)]

players["threeSuccessPercent"] = players["threeMade"] / players["threeAttempted"]
players = players[(players.threeAttempted > 0) & (players.threeSuccessPercent <= 1)]

sns.boxplot(data=players[["fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent"]])
plt.show()


#2 Part
newdat = players[(players.points > 150)]

newdat = players[(players.ftSuccessPercent > .6) & (players.fgSuccessPercent > .6) & (players.threeSuccessPercent > .6)]
print(newdat[["playerID", "fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent", "assists", "rebounds"]])



# Part 3
grouped = players.groupby('year')
three_stats = grouped['threeMade'].agg([np.mean, np.median])
three_stats = three_stats.reset_index()
three_stats = pd.melt(three_stats, id_vars=["year"], var_name="stat")
print(three_stats)

sns.relplot(data=players, x="year", y="threeMade", hue = "lgID")
plt.show()
sns.relplot(data=three_stats, x="year", y="value", hue = "stat")
plt.show()


