import pandas as pd

# Netflix dataset
data = {
    "Title": ["Stranger Things", "Money Heist", "Wednesday", "Dark", "Narcos"],
    "Type": ["TV Show", "TV Show", "TV Show", "TV Show", "TV Show"],
    "Year": [2016, 2017, 2022, 2017, 2015],
    "Rating": [8.7, 8.2, 8.1, 8.8, 8.8]
}

df = pd.DataFrame(data)

print("Netflix Dataset")
print(df)

print("\nAverage Rating:")
print(df["Rating"].mean())

print("\nHighest Rated Show:")
print(df.loc[df["Rating"].idxmax()]
