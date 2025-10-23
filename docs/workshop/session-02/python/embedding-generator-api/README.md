# 🧩 Embedding Generator API

## 📌 Purpose

The **Embedding Generator API** is a microservice specialized in generating high-quality vector embeddings from text inputs.
It supports converting raw text into fixed-size vector representations.

---

## 🚀 Responsibilities

* Generate vector embeddings from input text using specified embedding models

---

## ⚙️ Core Functionalities

| Functionality            | Description                                           |
| ------------------------ | ----------------------------------------------------- |
| **Embedding Generation** | Convert text inputs into fixed-size vector embeddings |

---

## 🔌 API Overview

| Endpoint | Method | Description                         |
| -------- | ------ | ----------------------------------- |
| `/embed` | `POST` | Generate embeddings from input text |

---

## 🔄 Example Usage

```bash
curl -X POST "http://localhost:8000/embed" -H "Content-Type: application/json" -d '{
  "text": "This is a sample text to embed.",
  "model": "openai-text-embedding-ada-002"
}'
```

---

## Request Schema

```json
{
  "text": "string",
  "model": "string"  // optional: specify embedding model
}
```

---

## Response Schema

```json
{
  "embedding": [0.123, 0.456, ...]  // float array of embedding vector
}
```
