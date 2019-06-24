import spacy
import re
import itertools
import numpy as np
from spacy import displacy
from common import produce_sns_plot


def top_pos(doc, pos, n):
    """Finds the top n spaCy pos

    Parameters:
    doc: spaCy's doc
    pos: pos we are interesting in finding; one of "VERB", "NOUN", "ADJ" or "ADV"
    n: how many pos
    """

    pos_count = {}
    for token in doc:
        # ignore stop words
        if token.is_stop:
            continue

        if token.pos_ == pos:
            if token.lemma_ in pos_count:
                pos_count[token.lemma_] += 1
            else:
                pos_count[token.lemma_] = 1

    # sort by values, but before get only those keys where value > 1;
    # I want lemmas that appear more than one
    # lastly, get the first n results
    result = sorted({k: v for (k, v) in pos_count.items() if v > 1}.items(),
                    key=lambda kv: kv[1], reverse=True)[:n]

    print("top {} {} {}".format(n, pos, result))
    produce_sns_plot(result, pos)


def top_entities(doc, n):
    """Finds the top n spaCy entities

    Parameters:
    doc: spaCy's doc
    n: how many entities
    """
    
    entities = {}
    # named entities
    for ent in doc.ents:
        # Print the entity text and its label
        if ent.text in entities:
            entities[ent.text] += 1
        else:
            entities[ent.text] = 1
    result = sorted(entities.items(), key=lambda kv: kv[1], reverse=True)[:n]
    print("top {} entities {}".format(n, result))

    produce_sns_plot(result, "entitie")


if __name__ == "__main__":
    nlp = spacy.load("en_core_web_md")
    with open('cleaned_tweets.txt', 'r') as file:
        text = file.read()

    doc = nlp(text)
    top_pos(doc, 'VERB', 20)
    top_pos(doc, 'NOUN', 20)
    top_pos(doc, 'ADJ', 20)
    top_pos(doc, 'ADV', 20)
    top_entities(doc, 30)
