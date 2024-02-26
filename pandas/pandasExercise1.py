import pandas as pd

data = pd.read_csv("./data/Titanic-Dataset.csv")
ageSeries = pd.Series(data.Age)
print("Original series: \n", ageSeries)

# Add new data to the series
ageSeries = pd.concat([ageSeries, pd.Series([22, 18])], ignore_index=True)
print("Add new data to the series (22 and 18): \n", ageSeries)

#Remove an element from the series
ageSeries = ageSeries.drop_duplicates()
print("Removing all duplicate ages from the series: \n", ageSeries)

#Perform basic arithmetic operations
sumTotal = ageSeries + 3
print("Sum total (series + 3): \n", sumTotal)

subtractionTotal = ageSeries - 1
print("Subtraction total (series - 3): \n", subtractionTotal)

multTotal = ageSeries * 4
print("Multiplication total (series * 3): \n", multTotal)

divTotal = ageSeries / 2
print("Division total (series / 3): \n", divTotal)