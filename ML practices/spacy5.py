import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Ensure you have the necessary NLTK data files
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('averaged_perceptron_tagger_eng')

# Testo da elaborare
text = "Mario Rossi lavora a Roma per Google."

# Tokenizzazione delle parole
tokens = word_tokenize(text)

# Assegnazione dei tag di parte del discorso
tagged = pos_tag(tokens)

# Riconoscimento delle entità nominate
entities = ne_chunk(tagged)

# Stampa le entità nominate
print(entities)