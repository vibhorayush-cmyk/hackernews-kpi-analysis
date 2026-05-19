import os
import matplotlib.pyplot as plt

os.makedirs('visuals', exist_ok=True)

import matplotlib.pyplot as plt


def create_top_posts_chart(df):

    top_posts = (
        df.sort_values(
            by='points',
            ascending=False
        )
        .head(10)
    )

    plt.figure(figsize=(12, 6))

    plt.barh(
        top_posts['title'],
        top_posts['points']
    )

    plt.xlabel('Points')

    plt.title(
        'Top Performing Hacker News Posts'
    )

    plt.tight_layout()

    plt.savefig(
        'visuals/top_posts.png'
    )

    plt.close()


def create_engagement_distribution(df):

    plt.figure(figsize=(8, 5))

    df['engagement_level'].value_counts().plot(
        kind='bar'
    )

    plt.title(
        'Engagement Level Distribution'
    )

    plt.xlabel('Engagement Level')
    plt.ylabel('Number of Posts')

    plt.tight_layout()

    plt.savefig(
        'visuals/engagement_distribution.png'
    )

    plt.close()