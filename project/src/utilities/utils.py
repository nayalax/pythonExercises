import pandas as pd
import zipfile
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Utils():
    def __init__(self):
        pass
        
def extract_zip_file(filePath, extractPath):
    with zipfile.ZipFile(filePath, 'r') as zip_ref:
        zip_ref.extractall(extractPath)
    return extractPath

def get_avg_rating (df: pd.DataFrame):
    avg = pd.DataFrame(df.groupby('directors', as_index=False)['tomatometer_rating'].mean())
    return avg
    
def clean_dataset (columns: list, df: pd.DataFrame):
    df = df[columns]
    df.columns = [column.strip() for column in df.columns]
    df.dropna(axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def preprocess(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    return ' '.join(lemmatizer.lemmatize(word) for word in text.lower().split() if word not in stop_words)

def get_recommendations(df: pd.DataFrame, cosineSim, title):
    idx = df[df['movie_title'] == title].index[0]
    simScores = list(enumerate(cosineSim[idx]))
    simScores = sorted(simScores, key=lambda x: x[1], reverse=True)
    simScores = simScores[1:16]
    movieIndices = [i[0] for i in simScores]
    return df['movie_title'].iloc[movieIndices]