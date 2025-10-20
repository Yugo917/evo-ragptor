1. **Data Ingestion & Storage Service**

   * Document Storage
   * Metadata Management

2. **Data Processing Service**

   * Data Sanitizer
   * Data Chunking
   * Data Augmentation

3. **Vector Search / RAG Service**

   * Indexation Vectorielle
   * Query / Retrieval API

4. **Fine-Tuning / Model Service**

   * Data Tokenisation
   * LoRA Fine-Tuning
   * Fusion LoRA + Model

5. **Feedback Service**

   * Asking Feedback
   * Deducing Feedback
   * QA Feedback Storage
   * Data Sanitizer (réutilisé ici pour nettoyage post-feedback)

6. **Serving / API Layer**

   * FastAPI / GGUF / ONNX
   * Inference Endpoint

---

Le diagramme montrerait **les flux entre les services**, par exemple :

```
[Ingestion] --> [Processing] --> [Vector Search / RAG] --> [Fine-tuning / Model] --> [Serving]
                                   ^                                  |
                                   |                                  v
                               [Feedback Service] <------------------
```

* Les étapes **mutualisées** comme Data Sanitizer apparaissent dans plusieurs services.
* Chaque service peut être représenté par un bloc coloré autour du dino pour rester cohérent avec ton style néo-pop.

---

Si tu veux, je peux te **générer directement une image vectorielle / diagramme complet** dans le style et les couleurs exactes de ton logo, avec flèches et labels pour tous les services et étapes.

Veux‑tu que je fasse ça ?
