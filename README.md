# Hacker News Engagement Intelligence

## Project Overview

This project analyzes engagement patterns and content performance on Hacker News to identify the factors that drive user interaction within online technology communities.

Using Python, SQL, and data visualization, the analysis transforms raw Hacker News activity into actionable engagement intelligence by examining:
- Content performance
- User interaction trends
- Posting behavior
- Discussion intensity
- Topic engagement patterns
- Peak activity windows

The project simulates a real-world analytics workflow including data cleaning, KPI development, exploratory analysis, feature engineering, SQL querying, and visualization.

---

## Business Problem

Online technology communities generate large volumes of user-generated content daily. Understanding which content characteristics drive engagement can help platforms improve visibility strategies, optimize publishing timing, and better understand audience behavior.

This project aims to identify:
- Which post types generate the most engagement
- When users are most active
- Which topics drive discussions
- What characteristics influence virality
- How engagement patterns vary over time

---

## Dataset

Source: Hacker News Posts Dataset

The dataset contains information about:
- Post titles
- Scores
- Comment counts
- Authors
- Posting timestamps
- Post types
- URLs/domains

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL
- SQLite/PostgreSQL
- Jupyter Notebook

---

## Project Workflow

1. Data Cleaning
2. Feature Engineering
3. KPI Development
4. Exploratory Data Analysis
5. SQL-Based Analysis
6. Visualization & Trend Analysis
7. Insight Generation

---

## KPI Framework

The project tracks several engagement KPIs including:

- Average comments per post
- Average score per post
- Discussion intensity ratio
- Viral engagement score
- Peak engagement hour
- Top-performing content categories
- Topic engagement trends

### Viral Engagement Score

Viral Engagement Score combines post score and comment activity to estimate overall engagement impact.

Formula:

Engagement Score = (0.7 × Comments) + (0.3 × Score)

---

## Feature Engineering

Additional analytical features were created including:
- Posting hour
- Posting weekday
- Title length
- Discussion intensity
- Topic keywords
- Engagement ratios

---

## Key Insights

- Ask HN posts generated stronger discussion engagement than Show HN posts.
- Weekday morning posting windows showed the highest engagement activity.
- AI and startup-related topics consistently received above-average interaction levels.
- Posts with shorter, question-based titles generated more comments.
- Engagement patterns varied significantly across content categories.

---

## Visualizations

The project includes:
- Engagement heatmaps
- Trend analysis charts
- Topic performance comparisons
- Post-type engagement analysis
- Time-series visualizations

---

## SQL Analysis

SQL queries were used to:
- Identify peak posting hours
- Rank high-performing posts
- Compare engagement by category
- Analyze author activity
- Measure trend patterns

---

## Future Improvements

- NLP-based topic modeling
- Sentiment analysis
- Predictive engagement modeling
- Interactive dashboard development
- Real-time Hacker News API integration

---

## Project Structure

```plaintext
hacker-news-engagement-intelligence/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── notebooks/
│   └── engagement_analysis.ipynb
│
├── sql/
│   └── engagement_queries.sql
│
├── visuals/
│
├── src/
│
├── README.md
├── requirements.txt
└── .gitignore
