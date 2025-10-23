⚠️ WIP - Work In Progress

# 🧩 Inference Cache API

## 📌 Purpose

The **Inference Cache API** is a microservice designed to improve the efficiency of LLM inference workflows by caching responses to repeated or similar queries.
It minimizes redundant calls to LLM models by storing and serving cached answers, reducing latency and compute costs.

---

## 🚀 Responsibilities

* Store and retrieve cached inference results based on input queries
* Match new queries against cached entries using similarity metrics or exact matching
* Manage cache lifecycle with configurable expiration and invalidation policies
* Provide fast response retrieval to improve user experience and reduce load on LLM models

---

## ⚙️ Core Functionalities

| Functionality           | Description                                                     |
| ----------------------- | --------------------------------------------------------------- |
| **Cache Storage**       | Save inference results associated with input queries            |
| **Cache Retrieval**     | Retrieve cached responses for repeated or similar queries       |
| **Similarity Matching** | Support approximate matching to find semantically close queries |
| **Cache Management**    | Handle expiration, invalidation, and cache size policies        |

---

## 🔌 API Overview

| Endpoint        | Method | Description                                   |
| --------------- | ------ | --------------------------------------------- |
| `/cache`        | `POST` | Store a new inference result in the cache     |
| `/cache/search` | `POST` | Search for a cached response matching a query |
| `/cache/{id}`   | `GET`  | Retrieve a cached entry by ID                 |
| `/cache/clear`  | `POST` | Clear cache entries based on criteria         |

---

## 🔄 Example Usage

```bash
# Store a new cache entry
curl -X POST "http://localhost:8000/cache" -H "Content-Type: application/json" -d '{
  "query": "What is RAG architecture?",
  "response": "RAG stands for Retrieval-Augmented Generation...",
  "embedding": [0.123, 0.456, ...],
  "metadata": {
    "userId": "user123",
    "timestamp": "2025-10-23T15:00:00Z"
  }
}'

# Search for a cached response similar to a query
curl -X POST "http://localhost:8000/cache/search" -H "Content-Type: application/json" -d '{
  "query": "Explain RAG architecture",
  "embedding": [0.124, 0.459, ...]
}'

# Retrieve a cache entry by ID
curl -X GET "http://localhost:8000/cache/abc123"

# Clear all cache entries older than a specific date
curl -X POST "http://localhost:8000/cache/clear" -H "Content-Type: application/json" -d '{
  "beforeDate": "2025-01-01T00:00:00Z"
}'
```

---

## Request Schemas

### Cache store request

```json
{
  "query": "string",
  "response": "string",
  "embedding": [0.0],
  "metadata": {
    "userId": "string",
    "timestamp": "string"
  }
}
```

### Cache search request

```json
{
  "query": "string",
  "embedding": [0.0]
}
```

---

## Response Schemas

### Cache store response

```json
{
  "cacheId": "string",
  "status": "success",
  "message": "Cache entry stored successfully"
}
```

### Cache search response

```json
{
  "cacheId": "string",
  "response": "string",
  "similarityScore": 0.95
}
```

### Cache retrieval response

```json
{
  "cacheId": "string",
  "query": "string",
  "response": "string",
  "embedding": [0.0],
  "metadata": {}
}
```

---

## Benefits

* Reduces latency by serving cached inference results
* Decreases computational costs by avoiding redundant LLM calls
* Improves user experience with faster responses
* Supports semantic similarity for approximate query matching

