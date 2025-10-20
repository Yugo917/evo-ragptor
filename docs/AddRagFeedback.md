# Feedback Loop Workflow

**Objectif :**
Le workflow **Feedback Loop** a pour but de collecter et traiter le retour utilisateur sur les réponses générées par un agent connecté à une base RAG. Il permet de mesurer la qualité des réponses et de produire des données utilisables pour enrichir la base vectorielle ou pour un futur entraînement/fine-tuning.

---

```
Generated Response
       │
       ▼
  Asking Feedback
       │
       ▼
 Deducing Feedback
       │
       ▼
 QA Feedback Storage
       │
       ▼
    Data Sanitizer
```

💡 **Explication rapide :**

1. **Generated Response**

   * L’agent RAG produit une réponse à partir de la question posée par l’utilisateur.
   * Cette réponse constitue le point de départ pour l’évaluation.

2. **Asking Feedback**

   * L’utilisateur évalue la réponse fournie par l’agent.
   * Notation possible : **Bonne**, **Mauvaise**, **Neutre**.
   * Le feedback peut être explicite (boutons, choix) ou implicite (interactions, clics).

3. **Deducing Feedback**

   * Analyse automatique ou semi-automatique du feedback reçu.
   * Déduction du niveau de qualité de la réponse : pertinence, exactitude, clarté.
   * Génération de métadonnées associées au feedback (timestamp, utilisateur, type de question).

4. **QA Feedback Storage**

   * Stockage structuré de chaque Q/R avec son feedback et ses métadonnées.
   * Préparation des données pour une éventuelle augmentation, réinjection dans la base vectorielle ou pour des sessions de fine-tuning.

5. **Data Sanitizer**

   * Nettoyage et normalisation des données collectées.
   * Suppression des doublons, correction des typographies et formatage uniforme.
   * Préparation des chunks pour être intégrés dans le pipeline RAG ou LoRA.

---

**Avantages :**

* Permet de créer un **cycle d’amélioration continue** de la base RAG.
* Collecte des données réelles d’usage pour **enrichir la base vectorielle**.
* Constitue un dataset de qualité pour **un futur entraînement ou fine-tuning**.
* Assure des données propres et cohérentes grâce au Data Sanitizer.
