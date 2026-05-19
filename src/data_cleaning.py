import pandas as pd


def clean_data(df):

    # Standardize columns
    df.columns = df.columns.str.lower()

    # Remove duplicates
    df = df.drop_duplicates()

    # Drop missing values
    df = df.dropna(
        subset=[
            'title',
            'points',
            'hours_ago'
        ]
    )

    # Convert numeric columns
    df['points'] = pd.to_numeric(df['points'])
    df['hours_ago'] = pd.to_numeric(df['hours_ago'])

    return df