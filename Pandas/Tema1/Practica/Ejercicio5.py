
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=[
                       'Year 1', 'Year 2'])
animals

# Your code goes here
animals.to_csv("cows_and_goats.csv")
# Check your answer
q5.check()
