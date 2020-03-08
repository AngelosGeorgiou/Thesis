from nltk.corpus import gutenberg
from printModule import *
import inspect
from collections import defaultdict
from nltk.corpus import wordnet as wn
from nltk.corpus import PlaintextCorpusReader
from functools import reduce
# printList(nltk.corpus.gutenberg.fileids())
# emma = gutenberg.words('austen-emma.txt')
# print(len(emma))

# emma = nltk.Text(emma)
# printList(emma.concordance("surprize"))



# for fileid in gutenberg.fileids():
# 	num_chars = len(gutenberg.raw(fileid))
# 	num_words = len(gutenberg.words(fileid))
# 	num_sents = len(gutenberg.sents(fileid))
# 	num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
# 	print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

def content_fraction(text):
	stopwords = nltk.corpus.stopwords.words('english')
	content = [w for w in text if w.lower() not in stopwords]
	return len(content) / len(text)


file_pattern = '*.txt'
corpus_root = '/home/angelos/thesis/OntologyRelated/Criteria/Sjogren-Criteria'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
# printList(wordlists.fileids())
# ['OntologyRelatedEADME', 'connectives', 'propernames', 'web2', 'web2a', 'words']
# for fileid in wordlists.fileids():
# 	print(fileid)
# 	print("\tSentences:",len(wordlists.sents(fileid)))
# 	print("\tWords:",len(wordlists.words(fileid)))
# 	print("\tVocabulary: ", len(set(w.lower() for w in wordlists.words(fileid))))
# 	print()
# ['the', 'of', 'and', 'to', 'a', 'in', 'that', 'is', ]


# print(wn.synsets("monstrous"))
entVoc = load_obj('EntitiesVocabulary')
# print(wn.synsets(list(entVoc.keys())[0]))
owlEnt = defaultdict()

for key in entVoc.keys():
	owlEnt[key] = reduce(lambda x, y: x + y, entVoc[key][1:])
# print(owlEnt)
printToFile(owlEnt,"/home/angelos/thesis/output/owlEnt")


for key, values in list(owlEnt.items())[:1]:
	print('----------',key)
	for value in values:
		print(value)
		# synsets = wn.synsets(str(value))
		# printList(map(lambda x: x.lemma_names(), wn.synsets(value)))
		printList(map(lambda x: [x.name()] + [x.definition()] + [x.lemma_names()], wn.synsets(value)))
		# printList(wn.synsets(value))
