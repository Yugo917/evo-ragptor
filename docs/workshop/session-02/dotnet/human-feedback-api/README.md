⚠️ WIP - Work In Progress

# 🧩 Human Feedback API

## 📌 Purpose

The **Human Feedback API** is a microservice dedicated to collecting, storing, and managing both explicit and implicit user feedback on AI-generated responses.
It enables capturing validated, corrected, or inferred user satisfaction during conversational interactions to support continuous model improvement.

---

## 🚀 Responsibilities

* Collect explicit user feedback on AI-generated responses
* Capture implicit feedback signals such as user inactivity or lack of follow-up questions
* Store and manage all types of feedback securely and efficiently
* Provide endpoints to retrieve, filter, and export feedback for analysis and model retraining

---

## ⚙️ Core Functionalities

| Functionality          | Description                                                                         |
| ---------------------- | ----------------------------------------------------------------------------------- |
| **Explicit Feedback**  | Receive and store direct user validations, corrections, or comments on AI responses |
| **Implicit Feedback**  | Infer user satisfaction from interaction patterns (e.g., no further questions)      |
| **Feedback Retrieval** | Query and filter collected feedback data                                            |
| **Feedback Export**    | Export feedback datasets for training or auditing                                   |

---

## 🔌 API Overview

| Endpoint           | Method | Description                                   |
| ------------------ | ------ | --------------------------------------------- |
| `/feedback`        | `POST` | Submit new explicit or implicit user feedback |
| `/feedback/{id}`   | `GET`  | Retrieve specific feedback entry              |
| `/feedback`        | `GET`  | List or filter feedback entries               |
| `/feedback/export` | `GET`  | Export feedback data for external use         |

---

## 🔄 Example Usage

```bash
# Submit explicit feedback after user confirmation
curl -X POST "http://localhost:8000/feedback" -H "Content-Type: application/json" -d '{
  "userId": "user123",
  "question": "What is RAG architecture?",
  "response": "RAG stands for Retrieval-Augmented Generation...",
  "feedbackType": "explicit",
  "isCorrect": true,
  "comments": "Clear and accurate explanation."
}'

# Submit implicit feedback inferred from no follow-up questions
curl -X POST "http://localhost:8000/feedback" -H "Content-Type: application/json" -d '{
  "userId": "user123",
  "feedbackType": "implicit",
  "reason": "no_followup_question",
  "timestamp": "2025-10-23T15:30:00Z"
}'
```

---

## Request Schema

```json
{
  "userId": "string",
  "question": "string",            // optional if implicit feedback
  "response": "string",            // optional if implicit feedback
  "feedbackType": "string",       // "explicit" or "implicit"
  "isCorrect": "boolean",         // required if explicit
  "comments": "string",           // optional
  "reason": "string",             // required if implicit, e.g., "no_followup_question"
  "timestamp": "string"           // ISO8601 datetime
}
```

---

## Response Schema

```json
{
  "feedbackId": "string",
  "status": "success",
  "message": "Feedback recorded successfully"
}
```

---

## Benefits

* Facilitates collection of comprehensive user feedback
* Enables improved training data through explicit and implicit signals
* Reduces user effort in providing feedback
* Supports continuous improvement of AI models based on real interactions

