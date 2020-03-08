from stanfordcorenlp import StanfordCoreNLP
from printModule import *

nlp = StanfordCoreNLP(r'/home/angelos/stanford-corenlp-full-2018-10-05')
nlp = StanfordCoreNLP('http://localhost', port=9000)

sentenceOld = 'Guangdong University of Foreign Studies is located in Guangzhou.'
sentence = "Patient with HGM value greater than 55 g/L"
print( 'Tokenize:', nlp.word_tokenize(sentence))
print( 'Part of Speech:', nlp.pos_tag(sentence))
print( 'Named Entities:', nlp.ner(sentence))
print( 'Constituency Parsing:', nlp.parse(sentence))
print( 'Dependency Parsing:', nlp.dependency_parse(sentence))

nlp.close()