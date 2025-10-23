# 🧩 Data Creator API

## 📌 Purpose

The **Data Creator API** is the **processing and transformation layer** of the RAG architecture.
It consumes raw documents from users, applies a full pipeline of transformations, and interacts with the **Data Store API** to persist every step.

This service ensures data consistency, modular transformations, and readiness for vector search and LLM-based retrieval.

---

## 🚀 Responsibilities

* Retrieve raw data from **Data Store API**
* Process and transform content through multiple stages:

  1. **Sanitize** → clean and normalize text
  2. **Chunk** → split text into coherent segments
  3. **Augment** → translate, reformulate, or enrich text
  4. **Embed** → generate embeddings for vector storage
* Send results back to **Data Store API** after each step
* Orchestrate the full RAG data preparation workflow

---

## ⚙️ Workflow Overview

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

🧭 The **Data Creator API** acts as the orchestrator:
it transforms data, while **Data Store API** ensures it is saved and indexed properly.

---

## 🧩 Modules

| Module        | Description                                                       |
| ------------- | ----------------------------------------------------------------- |
| **Sanitizer** | Cleans text from noise, HTML, and formatting artifacts            |
| **Chunker**   | Divides text into semantically coherent chunks                    |
| **Augmenter** | Generates enriched variants (translations, synonyms, paraphrases) |
| **Embedder**  | Creates vector embeddings for similarity search                   |

---

## 🔌 API Overview

| Endpoint        | Method | Description                                       |
| --------------- | ------ | ------------------------------------------------- |
| `/process/:id`  | `POST` | Run the complete RAG data workflow for a document |
| `/sanitize/:id` | `POST` | Clean and normalize text                          |
| `/chunk/:id`    | `POST` | Create chunks from sanitized data                 |
| `/augment/:id`  | `POST` | Generate augmented versions                       |
| `/embed/:id`    | `POST` | Generate embeddings                               |
| `/status/:id`   | `GET`  | Check workflow progress                           |

Each endpoint communicates with **Data Store API** to fetch inputs or save outputs.

---

## 🔄 Example Workflow

```bash
# Step 1 — User uploads document to Data Store
POST /data-store-api/documents

# Step 2 — Trigger full processing pipeline
POST /data-creator-api/process/:documentId

# Step 3 — Each transformation is stored through Data Store API
# e.g. POST /data-store-api/sanitized, /chunked, /augmented, /embeddings
```
