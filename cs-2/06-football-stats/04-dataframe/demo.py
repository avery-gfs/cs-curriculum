import polars as pl

# Show all rows and columns

pl.Config(tbl_rows=-1, tbl_cols=-1)

# Read CSV data as a dataframe

games = pl.read_csv("games.csv")

print(games)

# Separate each game into two entries, one for the home team and one for away

homeResults = games.select(
    pl.col("home_team").alias("team"),
    pl.col("home_score").alias("scored"),
    pl.col("away_score").alias("allowed"),
)

awayResults = games.select(
    pl.col("away_team").alias("team"),
    pl.col("away_score").alias("scored"),
    pl.col("home_score").alias("allowed"),
)

# Combine the home and away win loss results

combined = pl.concat([homeResults, awayResults])

print(combined)

# Group the stats from each team game into a single row

grouped = combined.group_by("team").agg(
    pl.len().alias("numGames"),
    (pl.col("scored") > pl.col("allowed")).sum().alias("wins"),
    (pl.col("scored") < pl.col("allowed")).sum().alias("losses"),
    (pl.col("scored") == pl.col("allowed")).sum().alias("ties"),
    pl.sum("scored"),
    pl.sum("allowed"),
)

print(grouped)

# Calculate the per-game stats for each team
# Sort the team data by win percentage, highest to lowest

finalStats = grouped.with_columns(
    ((pl.col("wins") + 0.5 * pl.col("ties")) / pl.col("numGames"))
    .round(3)
    .alias("winPct"),
    (pl.col("scored") / pl.col("numGames")).round(1).alias("scoredPerGame"),
    (pl.col("allowed") / pl.col("numGames")).round(1).alias("allowedPerGame"),
).sort("winPct", descending=True)

print(finalStats)
