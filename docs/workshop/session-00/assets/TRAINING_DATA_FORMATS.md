# Training data formats
----------------------------------------------------------------------------------------------------


## 📘 Résumé

| Format                  | Type modèle     | Pros                          | Cons                | LoRA compatible | **LargeLLM (5)**                                                             | **LightLLM (5)**                                                         |
| ----------------------- | --------------- | ----------------------------- | ------------------- | --------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **SFT (prompt-output)** | Tous            | Simple, efficace              | Peu contextuel      | ✅               | GPT-J, LLaMA-1, Falcon-40B, Pythia-12B, MPT-30B                              | GPT-2, GPT-Neo-1.3B, TinyLLaMA, Pythia-1B, Phi-1.5                       |
| **ChatML**              | Chat            | Riche, rôles distincts        | Format lourd        | ✅               | GPT-4, GPT-3.5, LLaMA-2-Chat, Mistral-7B-Instruct, DeepSeek-Chat             | Mistral-7B, LLaMA-2-7B-Chat, Zephyr-7B, OpenChat-3.5-7B, DeepSeek-Coder  |
| **Prompt-Completion**   | Base LLM        | Ultra simple                  | Pas conversationnel | ✅               | Pythia-12B, MPT-30B, LLaMA-1-13B, Falcon-40B, GPT-J                          | GPT-Neo-1.3B, GPT-2, TinyLLaMA, Pythia-1.4B, Phi-2                       |
| **Instruction**         | Instruction     | Données faciles à générer     | Biais possible      | ✅               | WizardLM-13B, Alpaca-13B, LLaMA-2-13B, Vicuna-13B, Baize-13B                 | Alpaca-7B, Vicuna-7B, Zephyr-7B, TinyLLaMA, OpenHermes-2.5-Mistral       |
| **Multi-turn Dialogue** | Chatbot         | Simule des conversations      | Difficile à générer | ✅               | Claude-2, ChatGLM3-6B, Yi-34B-Chat, OpenAssistant-12B, Mistral-Instruct-v0.2 | Zephyr-7B, OpenChat-3.5-7B, Mistral-7B-Instruct, MythoMax-L2-13B, Phi-2  |
| **Preference (DPO)**    | Alignement RLHF | Apprentissage des préférences | Coûteux à annoter   | ⚠️              | GPT-4, Claude-2, Mistral-7B-DPO, LLaMA-2-Chat-70B, Zephyr-β                  | Zephyr-7B, OpenHermes-2.5-Mistral, DeepSeek-7B-DPO, TinyLLaMA-DPO, Phi-2 |

---

### 📌 Légende

* **LargeLLM** : Modèles puissants, souvent utilisés pour inference cloud ou fine-tuning sur GPU haut de gamme.
* **LightLLM** : Parfaits pour fine-tuning local (QLoRA/LoRA), training rapide et évaluation low-cost.
* **LoRA compatible** : tous les formats ici sont adaptés à des fine-tunings LoRA.

---


## 📚 Catalogue des Formats de Données pour Entraînement LLM & LoRA
----------------------------------------------------------------------------------------------------

Ce guide réunit les formats d'entraînement principaux utilisés pour les LLMs (grands ou légers), avec :

* Description du format
* Exemple de données (thème : jeux vidéo)
* Tableau synthétique des avantages / inconvénients
* Compatibilité LoRA
* Modèles célèbres (LargeLLM vs LightLLM)

---

### 🔹 1. **SFT — Supervised Fine-Tuning**

**Format :**

```json
{
  "prompt": "...",
  "completion": "..."
}
```

**Utilisation :** apprentissage supervisé (Dolly, Pythia)

**Exemple :**

```json
{
  "prompt": "Quels sont les meilleurs jeux coopératifs sur PC ?",
  "completion": "It Takes Two, Deep Rock Galactic, Valheim, Left 4 Dead 2."
}
```

| Avantages                          | Inconvénients              |
| ---------------------------------- | -------------------------- |
| Simple, clair, facile à construire | Peu de gestion de contexte |
| Bonne base pour comportement ciblé | Risque d'overfitting       |
| Compatible avec tous les LLMs      | Structure rigide           |

**LoRA :** ✅ Parfaitement compatible

**LargeLLM :** LLaMA-1, Falcon-40B, GPT-J, MPT-30B, Pythia-12B
**LightLLM :** GPT-2, GPT-Neo, TinyLLaMA, Pythia-1.4B, Phi-1.5

---

### 🔹 2. **ChatML / OpenAI Chat Format**

**Format :**

```json
[
  {"role": "user", "content": "..."},
  {"role": "assistant", "content": "..."}
]
```

**Utilisation :** agents conversationnels (ChatGPT-like)

**Exemple :**

```json
[
  {"role": "user", "content": "Peux-tu me recommander un RPG ?"},
  {"role": "assistant", "content": "Je recommande Divinity: Original Sin 2."}
]
```

| Avantages                                   | Inconvénients                              |
| ------------------------------------------- | ------------------------------------------ |
| Format adapté aux dialogues naturels        | Lourd à générer / structurer               |
| Permet de spécifier les rôles (system/user) | Requiert un tokenizer avec `chat_template` |

**LoRA :** ✅ Compatible avec tous les LLMs modernes (Mistral, DeepSeek)

**LargeLLM :** GPT-3.5, GPT-4, LLaMA-2-Chat, DeepSeek-Chat, Mistral-Instruct
**LightLLM :** Zephyr, OpenChat, Mistral-7B, LLaMA2-7B, DeepSeek-Coder

---

### 🔹 3. **Prompt-Completion (legacy OpenAI)**

**Format :**

```
Question: ...
Answer: ...
```

**Utilisation :** anciens modèles ou base (GPT-2, GPT-Neo)

**Exemple :**

```
Q: C'est quoi un roguelike ?
A: Un jeu avec mort permanente, niveaux générés et forte rejouabilité.
```

| Avantages                  | Inconvénients                      |
| -------------------------- | ---------------------------------- |
| Simple, rapide à créer     | Pas adapté aux interactions riches |
| Peu de formatage à prévoir | Moins pertinent pour chatbots      |

**LoRA :** ✅ Compatible (surtout avec petits modèles)

**LargeLLM :** MPT-30B, Pythia-12B, GPT-J, Falcon-40B, LLaMA-1-13B
**LightLLM :** GPT-2, GPT-Neo-1.3B, TinyLLaMA, Phi-2, Pythia-1.4B

---

### 🔹 4. **Instruction Tuning (Alpaca-like)**

**Format :**

```json
{
  "instruction": "...",
  "input": "...",
  "output": "..."
}
```

**Utilisation :** modèles orientés instruction (Alpaca, WizardLM)

**Exemple :**

```json
{
  "instruction": "Explique ce qu’est un MMORPG.",
  "input": "",
  "output": "Un MMORPG est un jeu de rôle massivement multijoueur..."
}
```

| Avantages                           | Inconvénients          |
| ----------------------------------- | ---------------------- |
| Parfait pour les tâches spécifiques | Moins fluide pour chat |
| Facile à générer avec GPT-3.5       | Peut induire des biais |

**LoRA :** ✅ Idéal pour QLoRA / PEFT ciblé

**LargeLLM :** WizardLM, Alpaca-13B, LLaMA-2-13B, Vicuna-13B, Baize
**LightLLM :** Alpaca-7B, Vicuna-7B, Zephyr-7B, OpenHermes, TinyLLaMA

---

### 🔹 5. **Multi-turn Dialogue**

**Format :**

```json
[
  {"speaker": "user", "text": "..."},
  {"speaker": "assistant", "text": "..."},
  ...
]
```

**Utilisation :** simulateur de conversation, chatbot FAQ

**Exemple :**

```json
[
  {"speaker": "user", "text": "Je veux jouer avec ma copine, une idée ?"},
  {"speaker": "assistant", "text": "It Takes Two : coopératif, drôle, excellent !"}
]
```

| Avantages                                  | Inconvénients                            |
| ------------------------------------------ | ---------------------------------------- |
| Réaliste, naturel, simule un vrai dialogue | Demande une structure claire et propre   |
| Permet l'apprentissage de contexte         | Contexte limité par la taille de fenêtre |

**LoRA :** ✅ Compatible (attention au context window)

**LargeLLM :** ChatGLM3, Yi-34B-Chat, Claude, OpenAssistant-12B, Mistral-Instruct
**LightLLM :** Zephyr, Mistral-7B, OpenChat-3.5, Phi-2, MythoMax

---

### 🔹 6. **Preference Format (DPO / RLHF)**

**Format :**

```json
{"prompt": "...", "chosen": "...", "rejected": "..."}
```

**Utilisation :** alignement par préférence humaine (DPO)

**Exemple :**

```json
{
  "prompt": "Donne une astuce dans Elden Ring.",
  "chosen": "Utilise les cendres de guerre pour faciliter les boss.",
  "rejected": "Utilise toujours l’attaque sautée, c’est la meilleure."
}
```

| Avantages                               | Inconvénients                       |
| --------------------------------------- | ----------------------------------- |
| Renforce qualité et pertinence          | Coûteux à annoter / comparer        |
| Indispensable pour affiner l’alignement | Nécessite déjà un modèle SFT aligné |

**LoRA :** ⚠️ Possible **après** un SFT préalable

**LargeLLM :** GPT-4, Claude-2, Mistral-DPO, LLaMA-2-70B, Zephyr-β
**LightLLM :** Zephyr-7B, DeepSeek-7B-DPO, TinyLLaMA-DPO, Phi-2, OpenHermes-DPO

