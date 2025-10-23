# 🧩 Fine-Tuning API

## 📌 Purpose

The **Fine-Tuning API** is a microservice focused on advanced model tuning using LoRA (Low-Rank Adaptation) techniques.
It enables the creation, training, and fusion of LoRA adapters to efficiently fine-tune base LLM models and produce improved versions.

---

## 🚀 Responsibilities

* Create and train LoRA adapters for base LLM models
* Fuse LoRA adapters with base models to generate fine-tuned enhanced models
* Manage fine-tuned and fused model lifecycle for downstream use

---

## ⚙️ Core Functionalities

| Functionality                | Description                                                      |
| ---------------------------- | ---------------------------------------------------------------- |
| **LoRA Creation & Training** | Generate and fine-tune LoRA adapters for base LLM models         |
| **Model Fusion**             | Merge LoRA adapters with base models to create fine-tuned models |

---

## 🔌 API Overview

| Endpoint         | Method | Description                           |
| ---------------- | ------ | ------------------------------------- |
| `/lora-finetune` | `POST` | Create and train a LoRA adapter       |
| `/lora-fuse`     | `POST` | Fuse a LoRA adapter with a base model |

---

## 🔄 Example Usage

```bash
# Create and fine-tune a LoRA adapter
curl -X POST "http://localhost:8000/lora-finetune" -H "Content-Type: application/json" -d '{
  "base_model": "base-llm-model",
  "training_data": ["Fine-tuning example sentence 1", "Example 2"],
  "parameters": {
    "learning_rate": 0.001,
    "epochs": 3
  }
}'

# Fuse LoRA adapter with base model
curl -X POST "http://localhost:8000/lora-fuse" -H "Content-Type: application/json" -d '{
  "base_model": "base-llm-model",
  "lora_adapter": "lora-adapter-id"
}'
```

---

## Request Schemas

### LoRA fine-tune request

```json
{
  "base_model": "string",
  "training_data": ["string"],
  "parameters": {
    "learning_rate": "number",
    "epochs": "integer"
  }
}
```

### LoRA fuse request

```json
{
  "base_model": "string",
  "lora_adapter": "string"
}
```

---

## Response Schema

```json
{
  "status": "success",
  "model_id": "string", // ID of the fine-tuned or fused model
  "message": "string"
}
```

---
