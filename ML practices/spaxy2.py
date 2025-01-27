import spacy
from transformers import pipeline

# Carica un modello di Question Answering pre-addestrato per l'italiano
qa_pipeline = pipeline(
    "question-answering", 
    model="dbmdz/bert-base-italian-cased", 
    top_k=5  # Aumenta top_k a 5 (o un valore maggiore)
)

# Testo di contesto
context = """
SpaCy è una libreria open-source in Python per l'elaborazione del linguaggio naturale (NLP) avanzata. 
È progettata per essere veloce, efficiente e facile da usare, rendendola ideale sia per la ricerca che per le applicazioni in produzione.
"""

# Domanda
question = "Cos'è SpaCy?"

# Estrai la risposta dal contesto
result = qa_pipeline({"question": question, "context": context})
print(result)