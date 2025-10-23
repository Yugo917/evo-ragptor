# RagptorApi

## 🚀 Overview

**RagptorApi** is the **Backend For Frontend (BFF)** service designed to serve as the main API gateway and orchestrator for the **EvoRagptor** system.

It provides a streamlined interface that handles client requests, communicates with underlying services, and manages data flows for an optimized Retrieval-Augmented Generation (RAG) experience.

---

## 🎯 Purpose

* Act as the centralized API layer for EvoRagptor clients.
* Aggregate and coordinate calls to microservices such as data ingestion, processing, vector search, and model inference.
* Simplify client interaction by exposing a clean, well-defined API.
* Manage authentication, request validation, and response formatting.
* Ensure scalable and maintainable integration between frontend and backend components.

---

## 🛠️ Features

* Unified API endpoint for RAG workflows.
* Request routing and orchestration across multiple backend services.
* Handling of semantic search queries and response aggregation.
* Support for real-time model inference requests.
* Centralized error handling and logging.
* Extensible architecture to add new endpoints and integrations.

---

## 🧩 Architecture Overview

```
Client
  │
  ▼
RagptorApi (BFF - .NET)
  │
  ├──> data-store-api (.NET) (document storage & metadata management)
  ├──> data-creator-api (.NET) (data transformation pipelines: sanitizer, chunking, augmentation)
  ├──> data-tool-api (Python) (utilities: chunk sanitizer, cleaning, helpers)
  ├──> llm-tool-api (Python) (embedding generation, LoRA fine-tuning, model inference)
  ├──> vector-search-api (vector indexing & semantic search)
```

---
