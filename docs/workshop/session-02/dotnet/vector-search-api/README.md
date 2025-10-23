# 🧩 Vector Search API

## 📌 Purpose

The **Vector Search API** is a core retrieval service in the RAG architecture.
It receives a user’s initial question from the chat, performs a semantic similarity search over precomputed embeddings, and returns the most relevant embeddings along with links to their raw source documents.

Additionally, it provides the content of embeddings on demand to build enriched preprompts for downstream LLM consumption.

---

## 🚀 Responsibilities

* Receive a **query** (initial chat question) and find the most semantically relevant embeddings
* Return embeddings metadata with links to their raw documents
* Provide the full **text content** of requested embeddings
* Generate a concatenated, formatted **preprompt snippet** ready to be injected in the LLM prompt
* Serve as a lightweight and fast retrieval API for preprompt enrichment in chatbots or RAG pipelines

---

## ⚙️ Workflow Overview

```
User Question
       │
       ▼
Vector Search API (search embeddings)
       │
       ▼
Relevant Embeddings + Raw Document Links
       │
       ▼
Text Retrieval (embedding content)
       │
       ▼
Preprompt Enrichment for LLM
```

🧭 The **Vector Search API** acts as the semantic retrieval layer:
it bridges user queries and raw document context through embeddings.

---

## 🔌 API Overview

| Endpoint           | Method | Description                                                                                                     |
| ------------------ | ------ | --------------------------------------------------------------------------------------------------------------- |
| `/search`          | `POST` | Find relevant embeddings by query                                                                               |
| `/embeddings/text` | `POST` | Retrieve full text for specified embeddings                                                                     |
| `/preprompt`       | `POST` | Get concatenated and formatted preprompt text; optionally include raw document links (via `include_links` flag) |
| `/health`          | `GET`  | Check API status and readiness                                                                                  |

---

## 🔄 Example Usage

```bash
# Search embeddings by user question
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" -d '{
  "query": "How to configure database connection?",
  "top_k": 5
}'

# Fetch full text content of embeddings by IDs
curl -X POST "http://localhost:8000/embeddings/text" -H "Content-Type: application/json" -d '{
  "embedding_ids": ["abc123", "def456"]
}'

# Get concatenated preprompt snippet directly
curl -X POST "http://localhost:8000/preprompt" -H "Content-Type: application/json" -d '{
  "query": "How to configure database connection?",
  "top_k": 5
}'
```

### Example response from `/preprompt`

```json
{
  "preprompt": "Document 1:\n[Texte complet du document 1]\n\nSource: https://docs.mycompany.com/config-db.md\n\n---\nDocument 2:\n[Texte complet du document 2]\n\nSource: https://wiki.mycompany.com/database-connection\n\n---"
}
```
