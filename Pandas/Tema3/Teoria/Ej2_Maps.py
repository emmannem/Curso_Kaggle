import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("data\winemag-data-130k-v2.csv", index_col=0)


review_points_mean = reviews.points.mean()

print(reviews.points.map(lambda p: p - review_points_mean))

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

print(reviews.apply(remean_points, axis='columns'))

print(reviews.head(1))

review_points_mean = reviews.points.mean()
print(reviews.points - review_points_mean)

print(reviews.country + " - " + reviews.region_1)