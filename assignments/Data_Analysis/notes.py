import pandas as pd # Our data manipulation library
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods


players = pd.read_csv("basketball_players.csv")
print(players.rebounds.min())
print(players.rebounds.max())
print(players.rebounds.mean())
print(players.rebounds.median())
print(players.sort_values("rebounds", ascending = False).head(10))
print(players[["playerID", "year", "tmID", "rebounds"]].sort_values("rebounds", ascending = False).head(10))


master = pd.read_csv("basketball_master.csv")
nba = pd.merge(players,
               master,
               how = "left",
               left_on = "playerID",
               right_on = "bioID")
print(nba.columns)

print(nba[["year", "useFirst", "lastName", "tmID", "rebounds"]].sort_values("rebounds", ascending = False).head(10))

nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
nba = nba[nba.GP > 0]
print(nba[["year", "useFirst", "lastName", "GP", "reboundsPerGame"]].sort_values("reboundsPerGame", ascending = False).head(10))

#sns.boxplot(data=nba.reboundsPerGame)
#plt.show()
#sns.boxplot(data=nba[["rebounds", "oRebounds", "dRebounds"]])
#plt.show()

eighties = nba[(nba.year >= 1980) & (nba.year < 1990)]
#sns.boxplot(eighties["reboundsPerGame"], orient = "v")
#plt.show()

#grid = sns.FacetGrid(eighties, col="year")
#grid.map(sns.boxplot, "reboundsPerGame", orient="v")
#plt.show()

nba_grouped_year = nba[["reboundsPerGame", "year"]].groupby("year").median()
print(nba_grouped_year.head())

nba_grouped_year = nba_grouped_year.reset_index()
nba_grouped_year = nba_grouped_year[nba_grouped_year.reboundsPerGame > 0]
sns.regplot(data = nba_grouped_year,
            x="year",
            y = "reboundsPerGame").set_title("Median rebounds per Year")
plt.show()

# Get the top 10 rebounders per year
nba_topRebounders_perYear = nba[["reboundsPerGame", "year"]].groupby("year")["reboundsPerGame"].nlargest(10)

# Get the median of these 10
nba_topRebounders_median_perYear = nba_topRebounders_perYear.groupby("year").median()

# Put year back in as a column
nba_topRebounders_median_perYear = nba_topRebounders_median_perYear.reset_index()

# Again no zeros...
nba_topRebounders_median_perYear_noZeros = nba_topRebounders_median_perYear[nba_topRebounders_median_perYear["reboundsPerGame"] > 0]

# Now plot
sns.regplot(data=nba_topRebounders_median_perYear_noZeros, x="year", y="reboundsPerGame").set_title("Median of Top 10 Rebounders Each Year")
plt.show()