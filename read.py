# Testing best configuration to read the data
import os
import duckdb

con = duckdb.connect(database=":memory:")

####
#### VIDEO INFO
####


# Print the raw line count first
with open("sb-mirror/videoInfo.csv", "r") as f:
    count = len(f.readlines())
print(f"Total raw lines: {count}")

# Connect to DuckDB


# Try reading with more permissive options
video_info = con.read_csv(
    "sb-mirror/videoInfo.csv",
    header=True,
    columns={
        "videoID": "VARCHAR",
        "channelID": "VARCHAR",
        "title": "VARCHAR",
        "published": "DOUBLE",
    },
    ignore_errors=True,
    quotechar=None,
)

# Show the count
print("\nCount from DuckDB:")
con.sql("SELECT COUNT(*) as row_count FROM video_info").show()


####
#### SponsorTimes
####

# # Print the raw line count first
# with open("sb-mirror/sponsorTimes.csv", "r") as f:
#     count = len(f.readlines())
# print(f"\nSponsorTimes - Total raw lines: {count}")

# # Try reading with efficient options for large files
sponsor_times = con.read_csv(
    "sb-mirror/sponsorTimes.csv",
    header=True,
    columns={
        "videoID": "VARCHAR",
        "startTime": "DOUBLE",
        "endTime": "DOUBLE",
        "votes": "INTEGER",
        "locked": "INTEGER",
        "incorrectVotes": "INTEGER",
        "UUID": "VARCHAR",
        "userID": "VARCHAR",
        "timeSubmitted": "DOUBLE",
        "views": "INTEGER",
        "category": "VARCHAR",
        "actionType": "VARCHAR",
        "service": "VARCHAR",
        "videoDuration": "DOUBLE",
        "hidden": "INTEGER",
        "reputation": "DOUBLE",
        "shadowHidden": "INTEGER",
        "hashedVideoID": "VARCHAR",
        "userAgent": "VARCHAR",
        "description": "VARCHAR",
    },
    ignore_errors=True,
    quotechar="",
)

# # Show just basic stats to avoid heavy queries
# print("\nCount from DuckDB:")
# con.sql("SELECT COUNT(*) as row_count FROM sponsor_times").show()

# # Sample just a few rows instead of heavy analysis
# print("\nSampling 5 rows:")
# con.sql("SELECT * FROM sponsor_times LIMIT 5").show()
