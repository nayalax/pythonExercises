import json
from sklearn.model_selection import train_test_split
import pandas as pd
import re
import os

# import openai

df_movies = pd.read_csv('data/TMDB_5000_Movie/tmdb_5000_movies.csv')
df_links = pd.read_csv('data/TMDB_5000_Movie/links.csv')

df_movies = df_movies[['id', 'title']]
df_combined = df_movies.merge(df_links, left_on='id', right_on='tmdbId', how='inner')
df_combined = df_combined.drop(columns=['tmdbId', 'movieId'])

if not os.path.exists('data/movies_con_imdbid.xlsx'):
    df_combined.to_excel('data/movies_con_imdbid.xlsx')
with open('data/qa.json', 'r', encoding='uft-8') as file:
    original_data = json.load(file)

# Transformar cada entrada a formato de fine-tuning de OpenAI
transformed_data = []

for item in original_data:
    # print('Buscando ' + re.sub(r'[a-zA-Z]', '', item['imdb_key']).lstrip('0'))
    # df_combined['imdbId'] = df_combined['imdbId'].astype(str)
    movie_title = df_combined[df_combined['imdbId'] == int(re.sub(r'[a-zA-Z]', '', item['imdb_key']).lstrip('0'))]
    if (not movie_title['title'].empty):
        movie_title_str =  movie_title['title'].iloc[0] # o squeeze()
    else:
        continue
    try:
        transformed_entry = {
            "messages": [
                {
                    "role": "system",
                    "content": "Your are helpful assitant that answers movie-related questions based on specific movie titles."
                },
                {
                    "role": "user",
                    "content": f"Movie: {movie_title_str}: {item['question']}"
                },
                {
                    "role": "assistant",
                    "content": item['answers'][item['correct_index']]
                }
            ]
        }
        transformed_data.append(transformed_entry)
    except TypeError:
        print('No tiene respuesta correcta:', item['imdb_key'])
# Guardar el dataset transformado en un archivo JSON
with open('data/movie_dataset_for_finetuning.jsonl', 'w', encoding='utf-8') as outfile:
    for entry in transformed_data:
        json.dump(entry, outfile)
        outfile.write('\n')
# Load the data from the JSONL file
data = []
with open('data/movie_dataset_for_finetuning.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        data.append(json.loads(line))

# split train vs test
train_data, validation_data = train_test_split(data, test_size=0.2, random_state=42)

# validation data a JSONL file
validation_file_path = '/mnt/data/validation_data.jsonl'
with open('data/movie_validation_for_finetuning.jsonl', 'w', encoding='utf-8') as file:
    for entry in validation_data:
        file.write(json.dumps(entry) + '\n')
   
"""       
status = openai.FineTuningJob.retrieve(job.id).status
start_time = time.time()
while status != "succeeded":
    print(f"Status=[{status}]... {time.time() - start_time:.2f}s", end="\r", flush=True)
    time.sleep(5)
    job = openai.FineTuningJob.retrieve(job.id)
    status = job.status
"""