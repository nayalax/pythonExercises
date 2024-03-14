# %%
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import utilities.utils as tools
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI, ChatCompletion
from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
import utilities.PushToAstra as pta


load_dotenv()
openaiApiKey = os.getenv("OPENAI_API_KEY")
engine = "gpt-3.5-turbo"
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")

# %%
load_dotenv()

dataSource = "../data/rotten_tomatoes_movies.csv"
df = pd.read_csv(dataSource)

# Clean up the data for processing
columns = ['movie_title','movie_info', 'genres', 'directors', 'tomatometer_rating']
df = tools.clean_dataset(columns, df)
df['summary'] = str(df['movie_title'].astype(str) + ": " + df['directors'].astype(str) + ": " + df['movie_info'].astype(str)).lower()
df['processed'] = df['summary'].apply(tools.preprocess())

# %%
# Add the summary data to AstraDB
astra = pta(api_key=openaiApiKey, model="text-embedding-3-large", token=ASTRA_DB_APPLICATION_TOKEN, api_endpoint=ASTRA_DB_API_ENDPOINT)
astra.push(df)

# %%
# Get the TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['processed'])

# Get the cosine similarity matrix
cosineSim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# %%
openai = OpenAI(api_key=openaiApiKey)
st.title("Rotten Tomatoes Movie Recommendations")

userInput = st.text_input("Enter a movie you recently watched and enjoyed:")
num_recommendations = st.slider("Number of recommendations:", min_value=1, max_value=15, value=5)

if userInput:
    st.write("You might also enjoy these movies:")
    recommendations = tools.get_recommendations(df, cosineSim, userInput)[:num_recommendations]
    
    movie_data = []    
    st.write("Here are the rotton tomatoes scores and descriptions for each movie.")
    for movie in recommendations:
        prompt = f"Write a description for the movie {movie} and it's rotten tomatoes score"
        response = openai.ChatCompletion.create (
            model=engine,
            messages= [
                {"role": "system", "content": "You are a movie critic."},
                {"role": "user", "content": prompt}
            ]
        )
        movie_data.append([movie, response['choices'][0]['message']['content']])
        
    st.table(pd.DataFrame(movie_data, columns=["Movie", "Description & Score"]))


