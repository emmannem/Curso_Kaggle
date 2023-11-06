import pandas as pd
reviews = pd.read_csv("data\winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

print(reviews[pd.isnull(reviews.country)])

print(reviews.region_2.fillna("Unknown"))

print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))