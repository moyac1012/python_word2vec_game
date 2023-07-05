from gensim.models import KeyedVectors


model_dir = '../entity_vector/entity_vector.model.bin'
model: KeyedVectors = KeyedVectors.load_word2vec_format(model_dir, binary=True)


def parsing(formula: str):
    pos, neg = []
    formula = formula.split('+')
    formula = list(map(lambda x: x.split('-'), formula))
    for x in formula:
        if len(x) == 1:
            pos += [x]
        else:
            pos += [x[0]]
            neg += [x[1:]]
    return pos, neg
# while True:
formula = input('式を入力')
print(formula)
print(parsing(formula))
# print(model.most_similar(positive=['東京', 'イギリス'], negative=['日本']))

