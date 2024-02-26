import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Part 1 Prepare the data
df = pd.read_csv('./data/IMDB-Movie-Data.csv')
columns = ['Title','Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)']
colData = df[columns]
npData = colData.to_numpy()

# Select the last column and cast to float to account for strings such as nan to not break any manipulations.
revenueCol = npData[:, -1].astype(float)
meanRev = np.nanmean(revenueCol.astype(float))
revenueCol[np.isnan(revenueCol)] = meanRev
print("Revenue mean: \n", revenueCol)

# Part 2 Statistical Analysis with Numpy
# Calculate the average rating of the films.
avgRating = np.mean(npData[:, 3].astype(float))
print("Average rating: \n", str(avgRating))

# Find movie with the longest duration
longestMovie = npData[np.argmax(npData[:, 2].astype(int))]
print("Longest Movie: \n", str(longestMovie[0]) + " with " + str(longestMovie[2]) + " minutes.")

# Determine the average and median revenue of the films.
avgRevenue = np.mean(revenueCol.astype(float))
print("Average revenue: \n", str(avgRevenue))
medianRevenue = np.median(revenueCol[~np.isnan(revenueCol)].astype(float))
print("Revenue median: \n", str(round(medianRevenue, 2)))

# Part 3 Data Manipulation
# Create a subset of data with movies released in the last 10 years.
moviesLast10Y = npData[npData[:, 1].astype(int) >= 2014]
print("Movie from the last 10 years: \n", str(moviesLast10Y))
# Calculate the average number of votes for this subset.
avgVotes = np.mean(moviesLast10Y[:, 4].astype(int))
print("Average vote for recent films (>= 10y): \n", str(round(avgVotes, 2)))

# Correlation
# Evaluate whether there is a correlation between IMD rating and movie revenues. Represent it with matplotlib.pyplot
correlation = np.corrcoef(npData[:, 3].astype(float), revenueCol.astype(float))[0,1]
print("Correlation between average rating and average revenue: \n", round(correlation, 2))