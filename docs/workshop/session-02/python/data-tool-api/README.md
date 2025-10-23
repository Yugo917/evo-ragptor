# 🧩 Data Tool API

## 📌 Purpose

The **Data Tool API** is a utility microservice providing essential text processing tools.
It supports the preparation and enrichment of textual data through sanitization, chunking, augmentation, and language detection.

---

## 🚀 Responsibilities

* Sanitize and normalize raw text inputs according to their `mymetype` and `DataContentType`
* Split text into semantically coherent chunks based on content type
* Augment text via translation, reformulation, or enrichment
* Detect the language of provided text

---

## ⚙️ Core Functionalities

| Functionality       | Description                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Sanitize**        | Clean and normalize text by removing noise and formatting issues, adapted to `mymetype` and `DataContentType` |
| **Chunk**           | Split text into meaningful segments suitable for downstream processing, respecting content type constraints   |
| **Augment**         | Translate, paraphrase, or enrich text to improve coverage and clarity                                         |
| **Language Detect** | Identify the language of the input text                                                                       |

---

## 🔌 API Overview

| Endpoint           | Method | Description                                                                            |
| ------------------ | ------ | -------------------------------------------------------------------------------------- |
| `/sanitize`        | `POST` | Clean and normalize input text with context on `mymetype` and `DataContentType`        |
| `/chunk`           | `POST` | Split sanitized text into coherent chunks, respecting `mymetype` and `DataContentType` |
| `/augment`         | `POST` | Generate augmented variants of input text                                              |
| `/language-detect` | `POST` | Detect the language of provided text                                                   |

---

## 🔄 Example Usage

```bash
# Sanitize text with type info
curl -X POST "http://localhost:8000/sanitize" -H "Content-Type: application/json" -d '{
  "text": "Raw text with noise, HTML tags, and weird formatting!!!",
  "mymetype": "code",
  "DataContentType": "sourcecode"
}'

# Chunk text with type info
curl -X POST "http://localhost:8000/chunk" -H "Content-Type: application/json" -d '{
  "text": "Sanitized and clean text that needs to be split into chunks.",
  "mymetype": "chat",
  "DataContentType": "conversation"
}'

# Augment text (e.g., translate or paraphrase)
curl -X POST "http://localhost:8000/augment" -H "Content-Type: application/json" -d '{
  "text": "Original sentence to be enriched or translated."
}'

# Detect language
curl -X POST "http://localhost:8000/language-detect" -H "Content-Type: application/json" -d '{
  "text": "Bonjour, comment ça va?"
}'
```
