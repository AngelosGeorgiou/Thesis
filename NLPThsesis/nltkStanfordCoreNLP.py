from nltk.parse import CoreNLPParser
from nltk.corpus import treebank
from printModule import *

sentence1 = "Patient with HGM value greater than 55 g/L"
sentence = "When did princes Diana die?"

# Lexical Parser
parser = CoreNLPParser(url='http://localhost:9000')

# Parse tokenized text.
print("\nParse tokenized text")
# print(list(parser.parse('What is the airspeed of an unladen swallow ?'.split())))
print(list(parser.parse(sentence.split())))
# [Tree('ROOT', [Tree('SBARQ', [Tree('WHNP', [Tree('WP', ['What'])]), Tree('SQ', [Tree('VBZ', ['is']), Tree('NP', [Tree('NP', [Tree('DT', ['the']), Tree('NN', ['airspeed'])]), Tree('PP', [Tree('IN', ['of']), Tree('NP', [Tree('DT', ['an']), Tree('JJ', ['unladen'])])]), Tree('S', [Tree('VP', [Tree('VB', ['swallow'])])])])]), Tree('.', ['?'])])])]

print("\nRaw string")
# Parse raw string.
print(list(parser.raw_parse(sentence)))
# [Tree('ROOT', [Tree('SBARQ', [Tree('WHNP', [Tree('WP', ['What'])]), Tree('SQ', [Tree('VBZ', ['is']), Tree('NP', [Tree('NP', [Tree('DT', ['the']), Tree('NN', ['airspeed'])]), Tree('PP', [Tree('IN', ['of']), Tree('NP', [Tree('DT', ['an']), Tree('JJ', ['unladen'])])]), Tree('S', [Tree('VP', [Tree('VB', ['swallow'])])])])]), Tree('.', ['?'])])])]

# Neural Dependency Parser
print("\nNeural Dependency Parser")
from nltk.parse.corenlp import CoreNLPDependencyParser
dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
parses = dep_parser.parse(sentence.split())
# [[(governor, dep, dependent) for governor, dep, dependent in parse.triples()] for parse in parses]
# [[(('What', 'WP'), 'cop', ('is', 'VBZ')), (('What', 'WP'), 'nsubj', ('airspeed', 'NN')), (('airspeed', 'NN'), 'det', ('the', 'DT')), (('airspeed', 'NN'), 'nmod', ('swallow', 'VB')), (('swallow', 'VB'), 'case', ('of', 'IN')), (('swallow', 'VB'), 'det', ('an', 'DT')), (('swallow', 'VB'), 'amod', ('unladen', 'JJ')), (('What', 'WP'), 'punct', ('?', '.'))]]


# Tokenizer
parser = CoreNLPParser(url='http://localhost:9000')
print("\nTokenizer")
print(list(parser.tokenize(sentence)))
# ['What', 'is', 'the', 'airspeed', 'of', 'an', 'unladen', 'swallow', '?']

# POS Tagger
print("\nPOS Tagger")
pos_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='pos')
print(list(pos_tagger.tag(sentence.split())))
# [('What', 'WP'), ('is', 'VBZ'), ('the', 'DT'), ('airspeed', 'NN'), ('of', 'IN'), ('an', 'DT'), ('unladen', 'JJ'), ('swallow', 'VB'), ('?', '.')]

# NER Tagger
print("\nNER Tagger")
ner_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='ner')
print(list(ner_tagger.tag((sentence.split()))))
# [('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'), ('studying', 'O'), ('at', 'O'), ('Stony', 'ORGANIZATION'), ('Brook', 'ORGANIZATION'), ('University', 'ORGANIZATION'), ('in', 'O'), ('NY', 'STATE_OR_PROVINCE')]