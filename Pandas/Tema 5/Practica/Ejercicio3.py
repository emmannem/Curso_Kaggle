
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
n_missing_prices = reviews.price.isnull().sum()

n_missing_prices = pd.isnull(reviews.price).sum()

# Check your answer
q3.check()
