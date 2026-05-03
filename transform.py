import pandas as pd

# Load your raw data
df = pd.read_csv("hackernews_raw.csv")

# -------------------------
# CLEAN POINTS
# -------------------------
df["points"] = df["points"].str.replace(" points", "", regex=False)
df["points"] = pd.to_numeric(df["points"], errors="coerce")

# -------------------------
# FIX TIME (IMPORTANT PART)
# -------------------------
def convert_time(x):
    if "minute" in x:
        return 1
    elif "hour" in x:
        return int(x.split()[0])
    elif "day" in x:
        return int(x.split()[0]) * 24
    else:
        return None

# 🔥 THIS LINE REPLACES YOUR OLD hours_ago
df["hours_ago"] = df["published_time"].apply(convert_time)

# -------------------------
# FEATURE ENGINEERING
# -------------------------
df["engagement_level"] = pd.cut(
    df["points"],
    bins=[0, 50, 150, 500, 10000],
    labels=["Low", "Medium", "High", "Viral"]
)

# 🔥 RECALCULATE (VERY IMPORTANT)
df["performance_score"] = df["points"] / (df["hours_ago"] + 1)

# -------------------------
# SAVE FINAL FILE
# -------------------------
df.to_csv("hackernews_final.csv", index=False)

# -------------------------
# CHECK OUTPUT
# -------------------------
print(df[["published_time", "hours_ago"]].tail())