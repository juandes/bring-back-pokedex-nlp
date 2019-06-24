import re

with open('tweets.txt', 'r') as file:
        text = file.read()

# remove RT mentions
text = re.sub('RT @[\w_]+:', '', text)

text = re.sub(r'é', 'e', text)

text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)

text = re.sub(r'[^\w\s]', '', text)

with open('cleaned_tweets.txt', 'w') as file:
    file.write(text)
