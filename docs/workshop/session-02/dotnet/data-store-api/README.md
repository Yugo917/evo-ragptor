# 🧠 Data Store API

## 📌 Purpose

The **Data Store API** acts as the **persistence layer** of the RAG ecosystem.
It is responsible for **storing, indexing, and exposing** all data generated throughout the document transformation workflow.

It ensures **traceability**, **consistency**, and **efficient retrieval** of data across all processing stages handled by the **Data Creator API**.

---

## 🚀 Responsibilities

* Store original documents, chat logs, and their metadata
* Manage all transformation stages: sanitized text, chunks, augmented data, and embeddings
* Expose APIs for:

  * Uploading new raw data
  * Reading or updating document states
  * Searching data semantically through embeddings
* Handle **vector indexation** for RAG systems (using pgvector, Milvus, or Qdrant)

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

Each transformation step is stored and versioned, allowing downstream services to retrieve or reuse intermediate states (sanitized, chunked, augmented…).

---

## 🧩 Core Data Entities

| Entity                | Description                                                          |
| --------------------- | -------------------------------------------------------------------- |
| **RawDocuments**      | Stores the original uploaded documents (binary or text) and metadata |
| **RawChatLog**        | Stores chat or conversation logs for contextual use                  |
| **ReadableDocuments** | Extracted readable text from raw sources                             |
| **SanitizedData**     | Cleaned and normalized data                                          |
| **ChunkedData**       | Split text into coherent, context-preserving chunks                  |
| **EmbededData**       | Vector embeddings generated from chunks                              |

Each entity is linked to the previous step for full traceability.

---

Voici ta section **API Overview** entièrement **reformatée** pour ton README, dans un style professionnel, clair et cohérent avec le reste de ta documentation 👇

---

## 🔌 API Overview

### 📍 Endpoints Summary

| Endpoint             | Method | Description                                              |
| -------------------- | ------ | -------------------------------------------------------- |
| **`/documents`**     | `POST` | Upload a new raw document with metadata and content type |
| **`/documents/:id`** | `GET`  | Retrieve a stored document and its metadata              |
| **`/sanitized`**     | `POST` | Store sanitized (cleaned and normalized) text            |
| **`/chunked`**       | `POST` | Store chunked data derived from sanitized text           |
| **`/augmented`**     | `POST` | Store augmented (translated or reformulated) data        |
| **`/embeddings`**    | `POST` | Store generated embeddings vectors                       |
| **`/search`**        | `POST` | Perform semantic search on stored embeddings             |

---

### 🧾 `/documents` — Upload a New Raw Document

**Purpose:**
Upload a document or data source to initialize a new RAG data workflow.
The document is stored in the **Data Store API** and becomes available for transformation by the **Data Creator API**.

#### 📥 Request Body (JSON or Multipart)

```json
{
  "filename": "api_reference.pdf",
  "mimetype": "application/pdf",
  "dataContentType": "technical",
  "metadata": {
    "source": "internal_doc_portal",
    "author": "John Doe",
    "language": "en",
    "tags": ["api", "reference", "v1.2"]
  },
  "metadatatype": "document",
  "blob": "<base64-encoded-file>"
}
```

#### 📤 Example Response

```json
{
  "id": "dcbf5120-73b4-45ab-8d2c-f5c8a3a7b7a1",
  "status": "stored",
  "createdAt": "2025-10-23T14:12:00Z"
}
```

---

### 🧱 Enum — `DataContentType`

Defines the **semantic nature** of the uploaded content to determine the appropriate processing pipeline.

| Enum Value         | Code          | Description                               |
| ------------------ | ------------- | ----------------------------------------- |
| **TECHNICAL**      | `"technical"` | Code, configuration files, specifications |
| **CONVERSATIONAL** | `"chat"`      | Chat logs, transcripts, or emails         |
| **DOCUMENTATION**  | `"doc"`       | Official or internal documentation        |
| **KNOWLEDGE**      | `"knowledge"` | Articles, blogs, or wiki content          |
| **META**           | `"meta"`      | Commits, issues, or tracking data         |

