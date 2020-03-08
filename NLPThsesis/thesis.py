from owlready2 import *
import inspect
from collections import defaultdict
from printModule import *
from functools import reduce

ontPath = "/home/angelos/thesis/OntologyRelated/OWL-Ontology/"
ontologyFileName= "HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.owl"
onto = get_ontology(ontPath+ontologyFileName)
# onto = get_ontology("/home/angelos/Desktop/OntologyRelated/OWL-Ontology/HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.owl")
onto.load()
NamedEntities=["Lymphoma-Organ",
				"Medical-Condition",
				"Symptom-Sign",
				"Drug-Substance",
				"Body-Mass-Index",
				"Education-Level",
				"Ethnicity",
				"Sex",
				"Pregnancy-Outcome",
				"Tobacco-Consumption-Status",
				"Questionnaire-Score",
				"Questionnaire-Element-Value",
				"Questionnaire-Element",
				"Questionnaire-Score-Category",
				"Medical-Imaging-Test"]
# print("ontology vars")
# printVars(onto)
	 # world
	 # _namespaces
	 # ontology
	 # base_iri
	 # name
	 # loaded
	 # _bnodes
	 # storid
	 # _imported_ontologies
	 # metadata
	 # graph
	 # _refactor
	 # _new_numbered_iri
	 # _abbreviate
	 # _unabbreviate
	 # _get_obj_triples_cspo_cspo
	 # _get_obj_triples_spo_spo
	 # _get_obj_triples_sp_co
	 # _get_obj_triples_s_po
	 # _get_obj_triples_po_s
	 # _get_obj_triples_sp_o
	 # _get_obj_triple_sp_o
	 # _get_obj_triple_po_s
	 # _has_obj_triple_spo
	 # _del_obj_triple_raw_spo
	 # _get_obj_triples_spi_o
	 # _get_obj_triples_pio_s
	 # _get_data_triples_spod_spod
	 # _get_data_triples_sp_od
	 # _get_data_triple_sp_od
	 # _get_data_triples_s_pod
	 # _has_data_triple_spod
	 # _del_data_triple_raw_spod
	 # _get_triples_spod_spod
	 # _get_triples_sp_od
	 # _get_triple_sp_od
	 # _get_triples_s_pod
	 # _get_triples_s_p
	 # _get_obj_triples_o_p
	 # _get_obj_triples_transitive_sp
	 # _get_obj_triples_transitive_po
	 # _get_obj_triples_transitive_sym
	 # _get_obj_triples_transitive_sp_indirect
	 # _add_obj_triple_raw_spo
	 # _set_obj_triple_raw_spo
	 # _add_data_triple_raw_spod
	 # _set_data_triple_raw_spod


# print("Base iri:",onto.base_iri)
# # print('\n')
# print("First 10 Classes:", list(onto.classes())[:10])
# print('\n')

# vocabulary.Term, 
# reference-model.Code-System, 
# vocabulary.ESSDAI-Domain, 
# vocabulary.Medical-Test, 
# vocabulary.Units-Expression, 
# vocabulary.Questionnaire-Score, 
# vocabulary.About-Questionnaires, 
# reference-model.ESSDAI-Domain-AL, 
# reference-model.Coded-Value, 
# vocabulary.Activity-Level


# printList(onto.annotation_properties())

 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.acronym,
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.aka,
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.code-System-Organization,
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.code-System-Print-Name,
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.code-System-Unique-ID,
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.essdai-Activity-Level-Exclude,
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.med-Test-Normal-Range-Notes,
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.med-Test-Outcome,
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.med-Test-Outcome-Unit,
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.presentation-Notes
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.quest-Outcome
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.quest-Score-Normal-Range
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.score
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.terminology
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.unit-Expression
 # HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.weight

# /home/angelos/Desktop/OntologyRelated/OWL-Ontology/HarmonicSS-Reference-Model+Vocabularies-v.0.9.1.owl#
# 	 http://www.semanticweb.org/ntua/iccs/harmonicss/terminology#
# 	 http://www.w3.org/2002/07/owl#
# 	 http://www.semanticweb.org/ntua/iccs/harmonicss/terminology/reference-model#


classIter = iter(onto.classes())
firstClass = next(classIter)
referenceModelClass = next(classIter)
# print("\n namespace search")
# printList(onto.search(namespace = list(onto._namespaces)[4]))
# terminologyClass = onto.search(subclass_of = referenceModelClass)[0]

namespaces = set()
classesIRI = defaultdict(str)
classesList = list()
for classes in  onto.classes():
	classesList.append(str(classes))
	classesIRI[str(classes)]=str(classes.iri)
	namespaces.add(classes.namespace)
# for nmspc in namespaces:
# 	print (nmspc.name,nmspc.base_iri)
classesList.sort()
# printList(classesList)

namespaces = list(namespaces)
namespaces.sort(key = str)	
vocabularyNmspc = namespaces[2]
# print("Subclasses of vocabulary.Lymphoma-Organ")
LOClasses = onto.search(subclass_of = vocabularyNmspc["Lymphoma-Organ"])
printToFile(list(onto.search(subclass_of = firstClass)),"/home/angelos/thesis/output/classes")
EntitiesVocabulary = defaultdict(list)
for entity in NamedEntities:
	for element in list(onto.search(subclass_of = vocabularyNmspc[entity])):
		entityAlias = []
		if element.label:
			for lbl in element.label:
				entityAlias.append(lbl) 
		if element.aka:
			for ak in element.aka:
				entityAlias.append(ak)
		if element.acronym:
			for acrnm in element.acronym:
				entityAlias.append(acrnm)
		# print(entityAlias)
		entityIdentifiers = list(reduce(lambda x, y: x+y,map(lambda s: s.split(', '), entityAlias)))
		EntitiesVocabulary[entity].append(entityIdentifiers)
save_obj(EntitiesVocabulary,'EntitiesVocabulary')
printToFile(EntitiesVocabulary.values(),"/home/angelos/thesis/output/EntitiesVocabulary")

# print(firstClass)
# printVars(LOClasses[1])
# for nmspc in namespaces:
# 	print(namespaces)

# print(onto.search(aka = "*"))
# print(len(onto._namespaces))
# printList(onto._namespaces)

# printVars(terminologyClass)
# Class Vars
# 	 namespace
# 	 storid
# 	 _name
# 	 is_a
# 	 _equivalent_to
# 	 __module__
# 	 __doc__


# printVars(vocabularyNmspc)
# Namespace Vars
# 	 ontology
# 	 world
# 	 base_iri
# 	 name


# print(onto.search(base_iri = "http://www.semanticweb.org/ntua/iccs/harmonicss/terminology/vocabulary#"))
# print(dir(vocabularyNmspc))


