### 🧠 1. Central API: `CorpusApi`

The system is structured around the central `CorpusApi`, which orchestrates the management of textual data based on the business domain. It serves as the unified entry point for feeding, processing, and querying the corpus by coordinating the various submodules.

---

### 📚 2. `BaseCorpus`: Generic Linguistic Resources

The `BaseCorpus` module centralizes domain-independent linguistic assets, such as:

* **Glossary**
* **Synonym dictionary**
* **Paraphrase dictionary**

Each resource is stored in its raw form to support regeneration (e.g., for multilingual use), ensuring the corpus remains consistent and reusable over time.

---

### 🏭 3. `DomainCorpus`: Domain-Specific Content

The `DomainCorpus` module handles textual data specific to a business domain, including:

* FAQs
* Support tickets
* Conversations
* Written documents (Word, Markdown, PDF…)
* Visual documents (PNG, Draw\.io…)
* Technical specifications (OpenAPI, etc.)

It segments documents into chunks, manages translation and code-switching, then generates embeddings enriched with metadata for intelligent indexing and querying.

---

### 📝 4. `DomainDocument`: Raw Document Ingestion

Raw documents are first saved through the `DomainDocument` module, which stores their content along with a unique identifier. These documents are then processed by `DomainCorpus` for structuring and enrichment.

---


### 💬 5. `ChatLogger`: Storage of User-Agent Interactions

`ChatLogger` is responsible solely for **storing conversations** between the user and the agent.

#### Responsibilities:

* Log each user query and agent response
* Tag entries with metadata (timestamp, validation, model, etc.)
* Support export for analytics or fine-tuning (`.jsonl`)

#### Storage Structure:

* **Raw Chat DB**: stores full text logs with metadata
* **Vectorized Chat DB**: stores embeddings of validated Q/A pairs (populated externally)

---

### 🔁 6. Interdependence and Synergy

Interactions between `BaseCorpus` and `DomainCorpus` allow dynamic enrichment of business content using foundational linguistic resources, while maintaining a robust, extensible, and coherent infrastructure.
This modular design supports scalability and enables precise contextualization of responses through AI models or semantic search engines.

