import pandas as pd

wine_reviews = pd.read_csv("data\winemag-data-130k-v2.csv")
print(wine_reviews.shape)
print(wine_reviews.head())

wine_reviews2 = pd.read_csv("data\winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews2.shape)
print(wine_reviews2.head())
