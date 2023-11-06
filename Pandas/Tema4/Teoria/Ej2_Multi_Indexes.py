import pandas as pd
reviews = pd.read_csv("data\winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)

mi = countries_reviewed.index
print(type(mi))

print(countries_reviewed.reset_index())