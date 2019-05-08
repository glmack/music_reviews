def vectorize(corpus):
    """learns vocab dictionary and returns feature names and term-document matrix"""
    vectorizer = CountVectorizer(lowercase=False)
    X = vectorizer.fit_transform(documents)
    return vectorizer.get_feature_names(), X.toarray()