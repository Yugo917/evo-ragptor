# 🧩 Inference API

## 📌 Purpose

The **Inference API** is a dedicated microservice that handles requests to perform text generation, completions, and chat responses using Large Language Models (LLMs).
It acts as the endpoint to query LLMs—whether hosted locally or accessed via external providers—enabling flexible and efficient model inference.

---

## 🚀 Responsibilities

* Accept inference requests with prompts and parameters
* Communicate with local or remote LLMs to generate responses
* Support multiple types of inference (completion, chat, instruction-following)
* Manage inference parameters such as temperature, max tokens, and stop sequences
* Provide scalable and reliable inference service for downstream applications

---

## ⚙️ Core Functionalities

| Functionality             | Description                                      |
| ------------------------- | ------------------------------------------------ |
| **Text Completion**       | Generate text completions based on input prompts |
| **Chat Response**         | Support conversational chat-style interactions   |
| **Instruction Following** | Generate outputs following user instructions     |

---

## 🔌 API Overview

| Endpoint     | Method | Description                            |
| ------------ | ------ | -------------------------------------- |
| `/inference` | `POST` | Generate text output from input prompt |

---

## 🔄 Example Usage

```bash
curl -X POST "http://localhost:8000/inference" -H "Content-Type: application/json" -d '{
  "model": "fine-tuned-llm-model",
  "prompt": "Explain the concept of retrieval-augmented generation.",
  "parameters": {
    "temperature": 0.7,
    "max_tokens": 150,
    "stop": ["\n"]
  }
}'
```

---

## Request Schema

```json
{
  "model": "string",         // Identifier of the model to use for inference
  "prompt": "string",        // Input text prompt to generate a response
  "parameters": {            // Optional parameters to control generation
    "temperature": "number",
    "max_tokens": "integer",
    "top_p": "number",
    "frequency_penalty": "number",
    "presence_penalty": "number",
    "stop": ["string"]
  }
}
```

---

## Response Schema

```json
{
  "generated_text": "string"   // Generated output text from the model
}
```
