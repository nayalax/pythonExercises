# %%
from astrapy.db import AstraDB
from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
import json
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
dbEndpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
openaiToken = os.getenv("OPENAI_API_KEY")
csvPath = ("../project/data/rotten_tomatoes_movies.csv")
collectionName = "vector_movies"
cleanedCsvPath = ("../project/data/moviesDataSetCleaned.csv")

# Configurar el motor de OpenAI
engine = "gpt-4"
embeddings = OpenAIEmbeddings(api_key=openaiToken, model="text-embedding-3-large")

# Clean the dataset before we try sending it to AstraDB
columns = ['movie_title', 'genres', 'directors', 'tomatometer_rating']
df = pd.read_csv(csvPath)
df = df[columns]
df.columns = [column.strip() for column in df.columns]
df.dropna(axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
df['summary'] = df['movie_title'].astype(str) + ": " + df['directors'].astype(str) + ": " + df['tomatometer_rating'].astype(str)

# Initialize Langchain vector store
vstore = AstraDBVectorStore (
    embedding=embeddings,
    collection_name=collectionName,
    token=token,
    api_endpoint=dbEndpoint
)
vstore.aclear()

# Procesar cada línea y obtener los embeddings
# Leer el documento de texto
documents = []

for index, row in enumerate(df['summary']):
    metadata = {"genres": df['genres'][index]}
    document = Document(page_content=row, metadata=metadata)
    documents.append(document)
    if len(documents) == 15:
        inserted_ids = vstore.add_documents(documents)
        print(f"\nInserted {len(inserted_ids)} documents.")
        documents = []
        inserted_ids = []
        print(f"im at index: {index}")