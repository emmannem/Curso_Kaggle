import pandas as pd
reviews = pd.read_csv("data\winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows',5)

print('reviews.iloc[0]')
print(reviews.iloc[0])

print('reviews.iloc[:,0]')
print(reviews.iloc[:,0])

print('reviews.iloc[:3,0]')
print(reviews.iloc[:3,0])

print('reviews.iloc[1:3,0]')
print(reviews.iloc[1:3,0])

print('reviews.iloc[[0, 1, 2],0]')
print(reviews.iloc[[0, 1, 2],0])

print('reviews.iloc[-5:]')
print(reviews.iloc[-5:])