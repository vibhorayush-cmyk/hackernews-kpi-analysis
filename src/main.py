import os
import pandas as pd

from data_cleaning import clean_data
from feature_engineering import engineer_features
from kpi_analysis import generate_kpis
from visualization import (
    create_top_posts_chart,
    create_engagement_distribution
)

# Load dataset
df = pd.read_csv(
    r'C:\Users\nehad\OneDrive\news-kpi\data\raw\hackernews_final.csv'
)

# Run pipeline
df = clean_data(df)

df = engineer_features(df)

generate_kpis(df)

create_top_posts_chart(df)

create_engagement_distribution(df)

# Save cleaned data


os.makedirs(
    'data/cleaned',
    exist_ok=True
)

df.to_csv(
    'data/cleaned/hackernews_cleaned.csv',
    index=False
)

print("Pipeline completed successfully.")
