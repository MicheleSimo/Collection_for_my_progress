import spacy

nlp = spacy.load("it_core_news_sm")

testo = "Maria Rossi, nata il 10/05/1985 a Milano, lavora come ingegnere presso Google a Londra."

doc = nlp(testo)

informazioni = {}

for ent in doc.ents:
    if ent.label_ == "PER":
        informazioni["persona"] = ent.text
    elif ent.label_ == "DATE":
        informazioni["data_nascita"] = ent.text
    elif ent.label_ == "LOC":
        # Distinguiamo tra luogo di nascita e luogo di lavoro
        if "nata a" in str(ent.sent):
            informazioni["luogo_nascita"] = ent.text
        else:
            informazioni["luogo_lavoro"] = ent.text
    elif ent.label_ == "ORG":
        informazioni["azienda"] = ent.text

# Estrai la professione usando le dipendenze sintattiche
for token in doc:
    if token.dep_ == "nsubj" and token.head.lemma_ == "lavorare":
        informazioni["professione"] = token.head.text

print(informazioni)