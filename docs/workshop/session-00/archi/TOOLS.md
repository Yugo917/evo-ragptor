### 🧠 1. Central API: `DataToolApi`

The `DataToolApi` component centralizes all data transformation and enrichment operations. 
It is composed of different modules: `DataConverter` for format transformation and `EmbeddingsCreator` for semantic vectorization.

---

### 🧱 2. `EmbeddingsCreator`: Embedding Generation

The `EmbeddingsCreator` module transforms enriched textual data into vector embeddings that can be used by AI models.
Example input types:

* `datachunk-to-embeddings`
* `faq-to-embeddings`

Each input is vectorized along with rich metadata (document ID, section, language, tags, timestamp...) for optimal use in semantic search engines or chatbots.

```json
{
  "text": "Make sure your computer meets the minimum requirements...",
  "embedding": [0.123, 0.456, 0.789, ...],
  "metadata": {
    "document_id": "doc-001",
    "chunk_id": "doc-001-chunk-003",
    ...
  }
}
```

---

### 🔁 3. `DataConverter`: Data Transformation

This module converts raw data sources (Markdown, Word, images, conversations) into usable segments (`datachunks` or FAQs). It can also generate training datasets from the same sources.

---

### 🔗 4. Synergy and Pipeline

Together, the components form a fully functional processing chain:

1. `DataConverter` transforms raw sources into `datachunks`.
2. `EmbeddingsCreator` enriches these chunks with vectors and metadata.
3. `DataToolApi` orchestrates the process and ensures pipeline consistency.

This modular setup ensures a reusable, scalable architecture that’s ready to power AI-assisted search or query systems.
