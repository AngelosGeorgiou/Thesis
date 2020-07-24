from nltk.book import *
from printModule import *

# print(text1.concordance("monstrous"))

# print(text1.similar("monstrous"))
# print(text2.similar("monstrous"))

# print(text2.common_contexts(["monstrous","very"]))

# print(len(text3))

# print(sorted(set(text3)))
# print(len(text3))

#Fine-grained Selections of Words

V = set(text1)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))

fdist5 = FreqDist(text5)
print(sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7))

#Collocations and Bigrams

print(text4.collocations())
print(text8.collocations())

# dir(text1)
# _CONTEXT_RE
# _COPY_TOKENS
# __class__
# __delattr__
# __dict__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __getitem__
# __gt__
# __hash__
# __init__
# __init_subclass__
# __le__
# __len__
# __lt__
# __module__
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __setattr__
# __sizeof__
# __str__
# __subclasshook__
# __unicode__
# __weakref__
# _context
# _train_default_ngram_lm
# collocation_list
# collocations
# common_contexts
# concordance
# concordance_list
# count
# dispersion_plot
# findall
# generate
# index
# name
# plot
# readability
# similar
# tokens
# unicode_repr
# vocab

# dir()
# FreqDist
# Text
# __annotations__
# __builtins__
# __doc__
# __loader__
# __name__
# __package__
# __spec__
# bigrams
# genesis
# gutenberg
# inaugural
# nps_chat
# printList
# printToFile
# printVars
# print_function
# sent1
# sent2
# sent3
# sent4
# sent5
# sent6
# sent7
# sent8
# sent9
# sents
# text1
# text2
# text3
# text4
# text5
# text6
# text7
# text8
# text9
# texts
# treebank
# webtext
# wordnet
