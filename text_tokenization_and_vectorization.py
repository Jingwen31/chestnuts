import re, string
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

print (f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')

# basic text tokenization
re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')
def tokenize(s):
    return re_tok.sub(r" \1 ", s).split()

vec = TfidfVectorizer(ngram_range=(1, 2), tokenizer=tokenize,
min_df=3, max_df=0.9, strip_accents="unicode", use_idf=1,
smooth_idf=1, sublinear_tf=1)

train_term_doc = vec.fit_transform(train[text])
test_term_doc = vec.transform(test[text])