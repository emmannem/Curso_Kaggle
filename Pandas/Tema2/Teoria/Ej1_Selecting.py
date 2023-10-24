import pandas as pd
reviews = pd.read_csv("data\winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows',5)

print('reviews')
print(reviews)

print('reviews.country')
print(reviews.country)

print('reviews[country]')
print(reviews['country'])

print('reviews[country][0]')
print(reviews['country'][0])