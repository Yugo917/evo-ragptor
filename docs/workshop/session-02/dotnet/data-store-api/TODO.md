# TODO

## 🧰 TODO

* [ ] Create PostgreSQL database
* [ ] Implement API endpoints for each workflow step

  * `/upload` → store raw document
  * `/sanitize` → clean and normalize
  * `/chunk` → create chunks
  * `/augment` → perform data augmentation
  * `/embed` → generate and store embeddings
* [ ] Integrate pgvector or Milvus
* [ ] Add authentication and role-based access
* [ ] Build semantic search endpoint

---

## 🧩 Example Workflow

```bash
# 1. Upload document
POST /upload

# 2. Sanitize document
POST /sanitize/:id

# 3. Chunk data
POST /chunk/:id

# 4. Augment content
POST /augment/:id

# 5. Embed and index
POST /embed/:id
```

---

### 🧱 Table Definitions

```sql
CREATE TABLE RawDocuments (
  id SERIAL PRIMARY KEY,
  metadata JSONB,
  metadatype VARCHAR(255),
  blob BYTEA,
  creationDate TIMESTAMP DEFAULT NOW()
);

CREATE TABLE RawChatLog (
  id SERIAL PRIMARY KEY,
  text TEXT,
  metadata JSONB,
  metadatype VARCHAR(255),
  creationDate TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ReadableDocuments (
  id SERIAL PRIMARY KEY,
  rawDocumentId INTEGER REFERENCES RawDocuments(id),
  text TEXT,
  metadata JSONB,
  metadatype VARCHAR(255),
  version VARCHAR(50),
  creationDate TIMESTAMP DEFAULT NOW()
);

CREATE TABLE SanitizedData (
  id SERIAL PRIMARY KEY,
  readableDocumentId INTEGER REFERENCES ReadableDocuments(id),
  text TEXT,
  metadata JSONB,
  metadatype VARCHAR(255),
  version VARCHAR(50),
  creationDate TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ChunkedData (
  id SERIAL PRIMARY KEY,
  sanitizedDataId INTEGER REFERENCES SanitizedData(id),
  text TEXT,
  metadata JSONB,
  metadatype VARCHAR(255),
  version VARCHAR(50),
  creationDate TIMESTAMP DEFAULT NOW()
);

CREATE TABLE EmbededData (
  id SERIAL PRIMARY KEY,
  chunkedDataId INTEGER REFERENCES ChunkedData(id),
  vector VECTOR(1536), -- for example, OpenAI embedding size
  metadata JSONB,
  metadatype VARCHAR(255),
  version VARCHAR(50),
  creationDate TIMESTAMP DEFAULT NOW()
);
```