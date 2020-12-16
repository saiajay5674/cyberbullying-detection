import pandas as pd

# Read CSV file
df = pd.read_csv("labelled_tweets.csv")
size = len(df)
train_df = df[:int(0.85 * size)]
test_df = df[int(0.85 * size):]
train_df.to_csv("training.csv", index = False)
test_df.to_csv("testData.csv", index = False)
