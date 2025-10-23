Voici un tableau comparatif complet des principales méthodes de **PEFT (Parameter-Efficient Fine-Tuning)** pour les LLMs : **LoRA**, **QLoRA**, **D-LoRA**, **AdaLoRA**, etc., avec leurs **avantages**, **inconvénients**, **benchmarks typiques** et **cas d’usage privilégiés**.

---

### 🔍 Comparatif des méthodes PEFT pour LLMs

| Méthode                        | Description courte                                                                              | Avantages                                                                                                        | Inconvénients                                                                                                                       | Benchmarks (ex.)                                                                           | Cas d’usage idéaux                                                      |
| ------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **LoRA** (Low-Rank Adaptation) | Injecte des matrices low-rank dans les poids de l’attention ou MLP                              | - Très peu de paramètres à fine-tuner<br>- Facilement adaptable<br>- Compatible avec Hugging Face                | - Pas de quantization<br>- Moins efficace en mémoire que QLoRA                                                                      | - GPT-3.5 avec LoRA atteint des scores proches du full fine-tuning avec <1% des paramètres | - Déploiement en prod<br>- Fine-tuning avec peu de RAM (ex. 24–32GB)    |
| **QLoRA** (Quantized LoRA)     | Combine quantization (4-bit) et LoRA pour un fine-tuning à coût ultra faible                    | - RAM minimale (\~24GB pour 65B)<br>- S’entraîne sur un GPU consumer<br>- Très peu d’impact sur les performances | - Temps de training plus long<br>- Incompatible avec certains accelerateurs (ex. XLA)<br>- Moins efficace si full precision requise | - Alpaca-QLoRA (7B) atteint des performances proches de LLaMA-7B full-tune                 | - LLMs > 7B sur machines grand public<br>- Fine-tuning full corpus      |
| **D-LoRA** (Decomposed LoRA)   | Ajoute une séparation entre LoRA statique (training) et dynamique (inférence)                   | - Réduction significative du temps d'inférence<br>- Optimisé pour serving                                        | - Implémentation plus complexe<br>- Support encore limité                                                                           | - D-LoRA 13B \~30% plus rapide en inférence vs LoRA classique                              | - API temps réel<br>- Applications embarquées                           |
| **AdaLoRA** (Adaptive LoRA)    | Alloue dynamiquement la capacité LoRA aux couches les plus sensibles                            | - Meilleure efficacité que LoRA classique<br>- Optimise l’allocation mémoire                                     | - Hyperparamètres difficiles à régler<br>- Moins supporté dans les lib standards                                                    | - GPT2 + AdaLoRA > GPT2 + LoRA (en BLEU sur tâches NLG)                                    | - Fine-tuning long ou sélectif<br>- Quand la perf. prime sur simplicité |
| **LoRA + LLaMA-Adapter**       | Injecte LoRA dans les couches spécifiques d’un backbone (ex. LLaMA) avec alignement instruction | - Parfait pour instruction tuning<br>- Léger & rapide                                                            | - Moins générique<br>- Besoin d’un dataset bien aligné                                                                              | - Vicuna, Alpaca, etc. utilisent ce mécanisme                                              | - Agents conversationnels<br>- Chatbots spécialisés                     |
| **Full Fine-tuning**           | Re-train de tous les poids                                                                      | - Meilleure performance possible<br>- Compatible avec tous les downstream tasks                                  | - Coût énorme (RAM, stockage, temps)<br>- Pas scalable                                                                              | - OpenChat, LLaMA2 full fine-tune = top perf                                               | - Labs R\&D<br>- Très gros budgets                                      |

---

### 📌 Remarques importantes

* **QLoRA est aujourd’hui le meilleur compromis pour le fine-tuning local sur GPU limités** (A100, RTX 3090, 4090…).
* **LoRA** reste plus simple à déployer en production et compatible avec ONNX / accélérateurs.
* **D-LoRA** est intéressant quand on veut combiner **fine-tuning efficace + déploiement rapide**.
* **AdaLoRA** brille dans des scénarios exigeant **performance fine-grained + contrôle avancé**.
* Tous ces outils font partie de la famille **PEFT**, portée notamment par la lib `peft` de Hugging Face.

---

