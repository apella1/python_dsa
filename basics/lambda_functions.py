# add_two = lambda x: x + 2
import pandas as pd


def add_two(x):
    return x + 2


df = pd.DataFrame({
    'name': ['Amy', 'Jackie', 'Sue'],
    'grades': [90, 84, 76]
})

# use the lambda function to multiply bump up the values
# in the grades column by 1.2!
df['grades'] = df['grades'].apply(lambda x: x * 1.2)

print(df)
