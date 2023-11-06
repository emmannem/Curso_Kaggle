import pandas as pd
reviews = pd.read_csv("data\winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed = countries_reviewed.reset_index()

print(countries_reviewed.sort_values(by='len'))

print(countries_reviewed.sort_values(by='len', ascending=False))

print(countries_reviewed.sort_index())

print(countries_reviewed.sort_values(by=['country', 'len']))