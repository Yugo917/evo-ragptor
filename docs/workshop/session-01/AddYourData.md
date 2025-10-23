
# Add your data workflow (For RAG purpose)

**Objectif :**
La add your data workflow a pour but de préparer et structurer des documents multilingues afin de les rendre consultables efficacement via des recherches vectorielles et de les utiliser dans des systèmes RAG (Retrieval-Augmented Generation).

Le workflow comprend cinq étapes principales : **Document Storage**, **Data Sanitizer**, **Data Chunking**, **Data Augmentation**, et **Indexation Vectorielle**.

---

```
Document Storage
       │
       ▼
   Data Sanitizer
       │
       ▼
   Data Chunking
       │
       ▼
  Data Augmentation
       │
       ▼
Indexation Vectorielle
```

💡 **Explication rapide :**

1. **Document Storage** : sauvegarde des documents originaux + métadonnées.
2. **Data Sanitizer** : nettoyage et normalisation du texte selon type MIME et type de document (technique, FAQ, narratif, etc.).
3. **Data Chunking** : découpage en morceaux cohérents pour traitement.
4. **Data Augmentation** : traduction, glossaire, synonymes → plusieurs versions par chunk.
5. **Indexation Vectorielle** : génération des embeddings et stockage dans la base pour recherche rapide.

---

## 1️⃣ Document Storage

**But :**
Stocker les documents originaux et leurs métadonnées pour référence et traçabilité.

**Actions :**

* Sauvegarder le texte complet des documents dans la base de données.
* Conserver les métadonnées pertinentes : titre, source, langue, date, tags.
* Permet de lier chaque chunk et ses embeddings à son document d’origine.

**Avantages :**

* Possibilité de retrouver le texte exact pour QA ou génération par LLM.
* Facilite la recherche filtrée selon métadonnées.

---

## 2️⃣ Data Sanitizer

**But :**
Nettoyer et normaliser les documents selon leur type MIME et type de contenu.

**Actions :**

* Nettoyage des balises HTML, caractères spéciaux et contenu inutile.
* Normalisation du texte selon le type de document :

  * **Technique** : standardiser unités, supprimer code/commentaires inutiles.
  * **FAQ** : uniformiser questions/réponses, retirer décorations.
  * **Narratif** : corriger typographies et retours à la ligne.
* Préparer le texte pour un chunking et une augmentation efficaces.

**Avantages :**

* Assure que chaque chunk contient un texte propre et cohérent.
* Réduit les erreurs lors de la traduction et des reformulations.
* Optimise la qualité des embeddings générés.

---

## 3️⃣ Data Chunking

**But :**
Découper les documents en morceaux gérables pour générer des embeddings précis.

**Actions :**

* Diviser les documents en chunks de 50‑100 lignes en moyenne.
* Ajouter un recouvrement (overlap) de 10 % pour ne pas perdre de contexte.
* Préparer chaque chunk pour les étapes suivantes de transformation.

**Avantages :**

* Assure que chaque vecteur représente un contexte cohérent.
* Optimise la taille des chunks pour les modèles d’embeddings et LLM.

---

## 4️⃣ Data Augmentation

**But :**
Enrichir chaque chunk avec des variantes pour améliorer la recherche vectorielle.

**Actions pour chaque chunk :**

* Traduction si nécessaire pour harmoniser la langue.
* Application du glossaire ou dictionnaire de synonymes pour normaliser les termes.
* Génération de versions alternatives : original, traduite, reformulée avec synonymes.

**Avantages :**

* Améliore la robustesse des embeddings face à la variation linguistique ou terminologique.
* Permet de couvrir plusieurs langues et formulations pour chaque concept.

---

## 5️⃣ Indexation Vectorielle

**But :**
Convertir les chunks en vecteurs et les rendre consultables rapidement.

**Actions :**

* Génération des embeddings pour chaque version de chunk.
* Stockage dans PostgreSQL ou moteur vectoriel (pgvector, Milvus, etc.).
* Création d’un index vectoriel pour accélérer la recherche par similarité (cosine, dot-product, etc.).

**Avantages :**

* Recherche rapide et pertinente basée sur la signification sémantique du texte.
* Prépare les chunks pour une utilisation efficace dans les systèmes RAG et LLM.

---

Si tu veux, je peux te **faire un diagramme workflow mis à jour** avec le Data Sanitizer inclus pour ton README, façon visuel clair et professionnel. Veux‑tu que je fasse ça ?
