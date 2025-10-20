# Choose your Model Embeddings and Chunk size
```
Tu es un assistant expert en RAG et embeddings. 

Je vais te fournir les informations essentielles suivantes sur mon projet : 

1. contentType : type de contenu principal (code, technique, article, rapport, narratif, etc.)
2. averageDocumentSize : taille moyenne d’un document ou chunk souhaité (nombre de paragraphes, lignes ou tokens)
3. language : langue principale du contenu (FR, EN, Multilingue, etc.)
4. overlapPercent : recouvrement souhaité entre chunks (ex : 10%, 15%, 20%)
5. targetDbEmbeddings : base de données cible pour stocker les embeddings (PostgreSQL, Weaviate, Milvus, Pinecone, etc.)
6. targetLlmHosting : environnement d’hébergement du LLM final (local, Azure, OpenAI API, HuggingFace, etc.)
7. ModelEmbeddings license : (MIT, FreeBSD, OpenSource etc ....)

À partir de ces informations, propose-moi : 

- Les **3 meilleurs modèles d’embeddings** adaptés à ce projet.  
- Pour chaque modèle, indique :
   - **Dimension de l’embedding**
   - **Fenêtre de contexte max**
   - **Qualité sémantique et benchmarks**
   - **Compatibilité avec la langue**
   - **Avantages et inconvénients**
   - **Facilité d’intégration avec la DB cible et l’hébergement LLM**

Réponds sous forme de **tableau comparatif clair** pour faciliter la décision.

```