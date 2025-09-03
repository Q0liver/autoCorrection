from sentence_transformers import SentenceTransformer, util

# Modell laden (klein, schnell, gut für Freitext)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Zwei Texte zum Vergleich
text1 = " Eine Datenbank ist eine Sammlung nicht-redundanter Daten, die von mehreren Applikationen benutzt werden."
text2 = "Eine Datenbank ist ein System für Daten austausch."

# Embeddings erzeugen
emb1 = model.encode(text1, convert_to_tensor=True)
emb2 = model.encode(text2, convert_to_tensor=True)

# Kosinus-Ähnlichkeit berechnen
similarity = util.cos_sim(emb1, emb2)

print(f"Semantische Ähnlichkeit: {similarity.item():.4f}")
