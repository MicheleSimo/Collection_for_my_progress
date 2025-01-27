import spacy

nlp = spacy.load("it_core_news_sm")

# Crea un oggetto Doc elaborando un testo
text = "This is a sentence about spaCy."
doc = nlp(text)

# Accedi ai token nel Doc
print("Token nel Doc")
for token in doc:
    print(token.text, token.pos_, token.dep_)

# Estrai le entità nominate
print("Entita'nel doc")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Accedi alle caratteristiche linguistiche dei token
print("Catatteristiche:")
for token in doc:
    print(token.text, token.lemma_, token.is_stop)

# Esegui la lemmatizzazione
print("risultato Lemmatizzazione")
for token in doc:
    print(token.text, token.lemma_)

# Esegui il Part-of-Speech tagging
for token in doc:
    print(token.text, token.pos_)

# Esegui il riconoscimento delle dipendenze
for token in doc:
    print(token.text, token.dep_)

# Esegui la segmentazione delle frasi
for sent in doc.sents:
    print(sent.text)

# Calcola la similarità tra due documenti
doc1 = nlp("This is a sentence about cats.")
doc2 = nlp("This is another sentence about dogs.")
similarity = doc1.similarity(doc2)
print(similarity)