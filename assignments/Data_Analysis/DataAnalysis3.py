import pandas as pd
import pandas
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np

# display more columns in the shell
pandas.set_option('display.max_columns', 10)

# Part 1

# load the data
players = pd.read_csv("basketball_players.csv")
# The "master" data (basketball_master.csv) has names, biographical information, etc.
master = pd.read_csv("basketball_master.csv")

#  merging the two data sets together
players = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")
print(players.columns)

# create the throw success rates like I did in analysis 2. 
players["fgSuccessPercent"] = players["fgMade"] / players["fgAttempted"]
players = players[(players.fgAttempted > 0) & (players.fgSuccessPercent <= 1)]
players["ftSuccessPercent"] = players["ftMade"] / players["ftAttempted"]
players = players[(players.ftAttempted > 0) & (players.ftSuccessPercent <= 1)]
players["threeSuccessPercent"] = players["threeMade"] / players["threeAttempted"]
players = players[(players.threeAttempted > 0) & (players.threeSuccessPercent <= 1)]

# THE GOAT needs to have scored a lot of points.
# He needs great accuracy
# He needs to be a team player, so
# he needs assists, rebounds blocks, and steals
# Im looking for the best well rounded player
# This player also needs to do this consistently
# I did not sum up the players stats or find an average.
# The GOAT needs to be consistent, but a bad season or
# injury should not totally cut him out. 
newdat = players[(players.points > 2000) & (players.assists > 400) & (players.steals > 200)]
newdat = newdat[newdat.fgSuccessPercent > .5]
print(newdat[["playerID", "firstName", "lastName", "points", "assists", "steals", "blocks", "fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent"]].sort_values("points", ascending=False))

# this is why I chose Michael Jordan.
# He was consitently the best in all categories. 

# Part 2

# this more exploratory than anything.
# I first found how many players are from each state
print(players["birthState"].value_counts())

# then I looked at californias cities
CAdat = players[players.birthState == "CA"]
print(CAdat["birthCity"].value_counts())

# there was a lot from Los Angeles 
LAdat = players[players.birthCity == "Los Angeles"]
# I don't see much of a correlation
print(LAdat[["firstName", "lastName", "points", "assists", "steals", "blocks", "fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent"]].sort_values("points", ascending=False))

# I looked at a state with a lot less players
WYdat = players[players.birthState == "WY"]
print(WYdat["birthCity"].value_counts())
# I still don't see much of a correlation
print(WYdat[["playerID", "birthCity", "points", "assists"]].sort_values("points", ascending=False)) 

# looking a little deeper at LAs data
LAdat = players[players.birthCity == "Los Angeles"]
print(LAdat[["firstName", "lastName", "points", "assists", "steals", "blocks", "fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent"]].sort_values("points", ascending=False)) 

# I tried one more state
# but this time I eanted to see
# if there are any correlation with which college they went to.
AZdat = players[players.birthState == "AZ"]
print(AZdat["birthCity"].value_counts())
# there is a lot of variability 
print(AZdat[["playerID", "birthCity", "college", "points", "assists"]].groupby("playerID").max())

# trying something out here. Still not producing much
# but it was interesting to see what schools had the higher
# mean points
print(players[["playerID", "birthState", "college", "points"]].groupby(["college"]).mean().sort_values("points", ascending=False))

# Part 3

# I wanted to see if time in the game had any correlation with points
# After seeing the correlation I decided to add games played
# into the mix.
# this is also a positive correlation there. 
newdat = players[players.minutes >= 0]
sns.relplot(data=newdat, x="minutes", y="points", hue = "GP")
plt.show()

# I took one of the top schools that I found earlier
# and I wanted to see if year was correlated with points
# but it appears that points from that school are
# very random.
newdat = players[players.college == "North Carolina"]
sns.relplot(data=newdat, x="year", y="points")
plt.show()

# next I wanted to see how top players and how they fair
# over the years.
# I see that I lot of players drop in points as their season
# progresses. 
newdat = players[(players.playerID == "jordami01") | (players.playerID == "ervinju01") | (players.playerID == "bryanko01") | (players.playerID == "mcadobo01")]
sns.lineplot(data=newdat, x="year", y="points", hue = "playerID")
plt.show()
