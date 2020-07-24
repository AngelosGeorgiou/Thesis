import spacy 
import scispacy
from printModule import *

nlp = spacy.load('en_core_web_sm')
nlpmd = spacy.load('en_ner_bionlp13cg_md')
nlpdc = spacy.load('en_ner_bc5cdr_md')


# wikiText = """The Turkish invasion of Cyprus[29] (Turkish: Kıbrıs Barış
# Harekâtı, lit. 'Cyprus peace operation' and Greek: Τουρκική εισβολή στην
# Κύπρο), code-named by Turkey as Operation Atilla,[30][31] (Turkish: Atilla
# Harekâtı) was a Turkish military invasion of the island country of Cyprus. It
# was launched on 20 July 1974, following the Cypriot coup d'état on 15 July
# 1974."""
criteriaOld = "MPA patients with no poor prognosis factor;"
criteria = """ Patients aged over 18 years-old with newly diagnosed
systemic Wegener'sgranulomatosis, - microscopic polyangitis with at least one
factor of poor prognosis according to the five factors score (proteinuria > 1
g/day, renal insufficiency defined as a serum creatininemia > 140 µmol/L,
specific cardiomyopathy, gastrointestinal tract and/or CNS involvement)."""

criteriaNlp = nlp(criteria)
criteriaBio = nlpmd(criteria) 
criteriaDc = nlpdc(criteria)



for word in criteriaNlp.ents:     
	# print(word.text, word.label_,'\t\t\t\t',spacy.explain(word.label_))
	print(word.text,'\t\t\t\t', word.label_)

print(list(criteriaNlp.sents))

print("\nBio results\n")
for word in criteriaBio.ents:     
	# print(word.text, word.label_,'\t\t\t\t',spacy.explain(word.label_))
	print(word.text,'\t\t\t\t', word.label_)
print("\nDisease and Chemical results\n")
for word in criteriaDc.ents:     
	# print(word.text, word.label_,'\t\t\t\t',spacy.explain(word.label_))
	print(word.text,'\t\t\t\t', word.label_)



# from spacy import displacy

# displacy.render(wikitext,style = "ent",jupyter = True )


