import pandas as pd

def get_avg_rating (df: pd.DataFrame):
    avg = pd.DataFrame(df.groupby('directors', as_index=False)['tomatometer_rating'].mean())
    return avg

def clean_dataset (columns: list, df: pd.DataFrame):
    df = df[columns]
    df.columns = [column.strip() for column in df.columns]
    df.dropna(axis=0, inplace=True)
    return df