#import pandas and requests libraries
import pandas as pd
import requests as rq
from dotenv import load_dotenv
import os
import pyplotlib as plt

load_dotenv()
# Variables
baseUrl = os.getenv("BASE_URL")
key = os.getenv("API_KEY")

userInput = input ("Which movie should we search for? \n")
url = f"{baseUrl}{key}&t={userInput}"

# Make the request and search for a movie
movieResult = rq.get(url)

# Send the response to pandas and print the columns
data = pd.DataFrame(movieResult.json())
print(data.columns)

# Print the column values for Title, Year, Poster, and BoxOffice
print(data.get(["Title", "Year", "Poster", "BoxOffice"]))

# Get the poster with pyplotlib
poster_url = data["Poster"].iloc[0]