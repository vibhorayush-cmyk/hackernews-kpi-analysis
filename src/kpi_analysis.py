def generate_kpis(df):

    print("\n--- KPI SUMMARY ---")

    print(
        f"Average Points: "
        f"{df['points'].mean():.2f}"
    )

    print(
        f"Highest Points: "
        f"{df['points'].max()}"
    )

    print(
        f"Average Performance Score: "
        f"{df['performance_score'].mean():.2f}"
    )

    print(
        f"Viral Posts: "
        f"{df['is_viral'].sum()}"
    )

    print(
        f"Average Title Length: "
        f"{df['title_length'].mean():.2f}"
    )