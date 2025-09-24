## 📊 **Tableau récapitulatif — Modèles vs max tokens (contexte)**

| Modèle / API                        | Type         | Fenêtre max (tokens)  | Notes principales                    |
| ----------------------------------- | ------------ | --------------------- | ------------------------------------ |
| **GPT-3.5 Turbo** (`gpt-3.5-turbo`) | OpenAI       | 16 385                | Très utilisé pour chat & embeddings  |
| **GPT-4 Turbo** (`gpt-4-turbo`)     | OpenAI       | 128 000               | Ultra grande fenêtre, tarif réduit   |
| **Claude 3 Opus**                   | Anthropic    | 200 000               | Excellente compréhension longue      |
| **Claude 3 Sonnet / Haiku**         | Anthropic    | 200 000               | Moins cher, même contexte            |
| **Mistral 7B**                      | Open source  | 8 192                 | Modèle dense très performant         |
| **Mixtral 8x7B** (MoE)              | Open source  | 32 768                | MoE performant, coût optimisé        |
| **Gemini 1.5 Pro**                  | Google       | 1 000 000 (streaming) | Ultra large, mais accès limité       |
| **LLaMA 2 (7B/13B/65B)**            | Open source  | 4 096                 | Standard chez Meta                   |
| **LLaMA 3 (8B/70B)**                | Open source  | 8 192                 | Plus grand contexte, plus efficace   |
| **Command R / R+ (Reka)**           | Open source  | 128 000               | Optimisé pour RAG                    |
| **TinyLLaMA 1.1B**                  | Open source  | 2 048                 | Ultra léger, peu de contexte         |
| **Phi-2 (1.5B)**                    | Microsoft    | 2 048                 | Très compact, rapide à fine-tuner    |
| **BGE (embedding models)**          | Hugging Face | 512 – 8192            | `bge-large-en-v1.5` = 512 tokens max |
| **text-embedding-3-large**          | OpenAI       | 8 192                 | Embedding performant multi-langue    |
| **text-embedding-ada-002**          | OpenAI       | 8 192                 | Embedding rapide et pas cher         |

---

## 📌 Notes techniques

* 🧠 **Fenêtre de contexte = limite de tokens** que le modèle peut traiter **en une requête**.
* ⚙️ **Tokens ≠ mots** : 1 token ≈ 4 caractères en anglais, 0.75 mot en moyenne.
* 🔁 Pour les **modèles d’embedding**, la fenêtre max détermine la **taille du chunk que tu peux vectoriser**.

---

## 📊 **Modèles LLM utilisables localement — Fenêtre de contexte**

| Modèle                      | Taille (paramètres) | Fenêtre max (tokens) | Type d’usage principal            | Notes techniques                            |
| --------------------------- | ------------------- | -------------------- | --------------------------------- | ------------------------------------------- |
| **TinyLLaMA**               | 1.1B                | 2 048                | Chat léger / embedded LLM         | Parfait en CPU / edge                       |
| **Phi-2**                   | 1.5B                | 2 048                | Bon pour dev, raisonnant bien     | Moins bon en génération longue              |
| **LLaMA 2 (7B)**            | 7B                  | 4 096                | Génération générale               | Qualité correcte, vite obsolète             |
| **LLaMA 3 (8B)**            | 8B                  | 8 192                | Chat + tâche générale             | 🔥 Nouveau standard local                   |
| **Mistral 7B**              | 7B                  | 8 192                | Modèle dense, rapide              | Excellent en CPU/GPU local                  |
| **Mixtral 8x7B (MoE)**      | 12.9B (active)      | 32 768               | Performant et économe (2 experts) | Context ultra-large                         |
| **OpenChat 3.5 / 4**        | 7B – 8B             | 8 192                | Style GPT, dialogue/chat          | Très fluide, entraîné sur partages sociaux  |
| **Command R / R+ (Reka)**   | \~35B eq. (MoE)     | 128 000              | 🔍 Optimisé RAG et retrieval      | Disponible via vLLM, pas encore dans Ollama |
| **Nous Hermes 2 (LLaMA 3)** | 7B – 8B             | 8 192                | Chat / généraliste                | Fine-tuned roleplay et multitâche           |
| **Code LLaMA 7B / 13B**     | 7B – 13B            | 16 384               | Génération de code                | Très fort pour devs, en local via llama.cpp |
| **WizardLM 2 / Dolphin**    | 7B – 13B            | 8 192                | Chat affiné style assistant       | Très apprécié en local                      |
| **BGE Small / Base**        | 110M – 1.5B         | 512 – 8192           | Embedding uniquement              | Parfait pour vector store local             |

---

## 🧠 Recommandations par cas d’usage local

| Cas d’usage                              | Modèles recommandés                     |
| ---------------------------------------- | --------------------------------------- |
| Chat local rapide (CPU)                  | TinyLLaMA, Phi-2, Mistral 7B            |
| Chat local de qualité (GPU)              | LLaMA 3 (8B), Mixtral, Nous Hermes 2    |
| Embedding local                          | BGE Small / Large, E5, Instructor XL    |
| Chat multi-docs avec long contexte (RAG) | Mixtral, Command R+, LLaMA 3 fine-tuné  |
| Génération de code locale                | Code LLaMA, Deepseek Coder, WizardCoder |
