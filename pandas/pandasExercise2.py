import os
from dotenv import load_dotenv
import pandas as pd

# Load the CSV into a Dataframe
URL = "https://drive.google.com/uc?export=download&id=1-zKKm5aEEabJS01n4vZhE8iiacnXYWGg"
df = pd.read_csv(URL)

# Show the first and last 5 rows of the Dataframey
print(df.head(), "\n")
print(df.tail(), "\n")

# Show general information about the Dataframe like number of rows, columns, and type of data
print(df.info(), "\n")
print(df.describe(), "\n")

# Convert the Height values from inches to cm
heightCmDf = df['Height'] * 2.54
print(heightCmDf)