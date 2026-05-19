import pandas as pd


def engineer_features(df):

    # Title length
    df['title_length'] = df['title'].str.len()

    # Word count
    df['word_count'] = (
        df['title']
        .str.split()
        .str.len()
    )

    # Question-style titles
    df['is_question'] = (
        df['title']
        .str.contains(r'\?')
        .astype(int)
    )

    # Viral flag
    df['is_viral'] = (
        df['engagement_level'] == 'Viral'
    ).astype(int)

    return df