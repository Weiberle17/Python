import pandas as pd

movies = pd.read_csv("IMDb-movies.csv")
movies.head()

print("Übung 2: \n{}".format(movies["duration"].max()))
print("Übung 3: \n{}".format(movies["duration"].max() // 60))
print("Übung 4: \n{}".format(movies["title"].loc[movies["duration"] == movies["duration"].max()]))
print("Übung 5: \n{}".format(movies["title"].loc[movies["actors"].str.contains("Stephen Fry", na=False)]))
print("Übung 6: \n{}".format(movies["duration"].loc[movies["actors"].str.contains("Stephen Fry", na=False)].mean()))
selection = int(sum(movies[["reviews_from_users", "reviews_from_critics"]].loc[pd.to_numeric(movies["year"] >= 1960) & (movies["language"] == "German")].sum()))
print("Übung 7: {}".format(selection))
