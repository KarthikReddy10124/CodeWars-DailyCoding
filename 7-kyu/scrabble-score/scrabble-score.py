def scrabble_score(word):
    return sum(dict_scores.get(char.upper(), 0) for char in word)
​