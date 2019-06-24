from common import produce_sns_plot

pokemon = {}

with open('cleaned_tweets.txt', 'r') as file:
    text = file.read()

with open('pokemon.csv') as file:
    for line in file:
        pokemon[line.rstrip('\n').lower()] = 0

for word in text.split():
    if word.lower() in pokemon:
        pokemon[word.lower()] += 1


# remove wingull because it was mentioned way too many times in a retweet
pokemon.pop('wingull')

top_mentioned_pokemon = sorted({k: v for (k, v) in pokemon.items()}.items(),
                               key=lambda kv: kv[1], reverse=True)[:20]

produce_sns_plot(top_mentioned_pokemon, "mentioned Pokemon")
