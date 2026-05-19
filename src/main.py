import os
import pandas as pd

from data_cleaning import clean_data
from feature_engineering import engineer_features
from kpi_analysis import generate_kpis

from visualization import (
    create_top_posts_chart,
    create_engagement_distribution,
    create_title_length_analysis
)

# Load dataset
df = pd.read_csv(
    r'C:\Users\nehad\OneDrive\news-kpi\data\raw\hackernews_final.csv'
)

# Clean data
df = clean_data(df)

# Feature engineering
df = engineer_features(df)

# KPI analysis
generate_kpis(df)

# Visualizations
create_top_posts_chart(df)

create_engagement_distribution(df)

create_title_length_analysis(df)

# Create cleaned folder if missing
os.makedirs(
    'data/cleaned',
    exist_ok=True
)

# Export cleaned dataset
df.to_csv(
    'data/cleaned/hackernews_cleaned.csv',
    index=False
)

print("\nPipeline completed successfully.")
