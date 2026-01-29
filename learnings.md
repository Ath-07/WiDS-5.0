# Plant Disease Classification — Week-wise Learnings (PlantVillage)

## Week 1: Dataset Understanding & Exploratory Analysis

- The PlantVillage dataset is organized as **folder-based image data**, where each folder represents a **Plant–Disease combination**.
- It contains **38 disease classes across 14 plants**, with significant **class imbalance** both globally and within individual plants.
- Certain plants, especially **Tomato**, dominate the dataset with multiple disease categories and large sample sizes, while some classes have very limited data.
- For EDA, only the **color image dataset** was used to avoid duplication from grayscale and segmented versions.

**Key Observations**
- Image quality is generally high, but variations in **lighting, exposure, and background noise** are present.
- Disease classes within the same plant often exhibit **subtle visual differences** in texture, spot patterns, and color intensity.
- The task represents a **fine-grained image classification problem**, where distinguishing diseases can be challenging even for human observers.
- Effective modeling will require careful handling of imbalance and strong feature extraction.

---

## Week 2: Shallow Baseline Modeling (Classical ML)

- A **Dummy Classifier (most frequent)** achieved ~**10% accuracy**, establishing a valid lower-bound baseline and confirming correct data preprocessing.
- A **Random Forest model trained on flattened 64×64 RGB images** achieved ~**64% accuracy**, defining the **upper limit of classical machine learning performance** on raw pixels.
- Classical models captured **global color and texture patterns** but struggled with **spatial and fine-grained disease characteristics**.
- Minority and visually similar disease classes showed low recall, exposing the limitations of flattened representations.

---

## Week 3: Deep Learning with CNNs & Transfer Learning

- A **custom CNN trained from scratch** achieved high training accuracy but showed a noticeable generalization gap, highlighting the risk of overfitting on imbalanced and fine-grained datasets.
- The CNN performed well on visually distinct and high-support classes but struggled with minority classes and subtle disease variations.
- **Transfer learning using a pretrained MobileNetV2 backbone** significantly improved performance, achieving strong precision, recall, and F1-scores across almost all classes.
- Fine-tuning higher-level convolutional layers further improved generalization, demonstrating the value of pretrained representations for plant disease recognition.
- Confusion matrix analysis confirmed a substantial reduction in inter-class confusion compared to both shallow models and the custom CNN.

**Note on Reported Accuracy**  
 - While the transfer learning model achieves very high validation accuracy on the PlantVillage dataset, these results reflect the controlled acquisition conditions of the dataset. Real-world agricultural images are significantly more complex, and performance is expected to degrade under domain shift. Therefore, the reported metrics should be interpreted as an upper bound rather than a realistic deployment benchmark.
---

## Week 4: Federated Learning & Decentralized Training Dynamics

Week 4 extended the plant disease classification problem from centralized training to a federated learning (FL) setting, simulating collaboration across multiple decentralized clients without sharing raw data.

Using the Flower framework, a federated setup was created with multiple simulated clients, each training locally on a disjoint subset of the PlantVillage dataset. The global model was initialized using the centrally trained CNN from Week 3 and updated across several federated rounds using the FedAvg aggregation algorithm.

Key Observations

- The federated model achieved strong performance in the initial round, reflecting the quality of centralized pretraining.
- As training progressed, global accuracy steadily degraded across rounds, despite all clients participating consistently.
- This behavior highlighted the sensitivity of FedAvg to non-IID data distributions, as each client’s local data exhibited different plant and disease compositions.
- Client updates drifted toward local optima, and naive averaging of these updates resulted in loss of globally useful features.
- The large fully connected layers of the CNN amplified divergence, making the model particularly unstable under federated aggregation.

Week 4 demonstrated that federated learning introduces new challenges beyond model accuracy, including optimization stability, client heterogeneity, and aggregation robustness. These challenges are not visible in centralized training and require dedicated strategies to address.

---

## Week 5: Model Persistence, Visualization, and MLOps Thinking

Week 5 shifted the focus from model training to system-level considerations, emphasizing what happens *after* federated training completes.

Rather than improving accuracy, this week treated the federated model as a production artifact. The final global model was saved to disk, and training metrics were persisted for offline analysis. A lightweight Streamlit application was built to visualize global accuracy across federated rounds, separating training from evaluation and monitoring.

Key Observations

- Persisting models enables reuse for inference, fine-tuning, or deployment without retraining.
- Logging per-round metrics allows post hoc inspection of federated training behavior, which is critical for debugging distributed systems.
- Visualization made the instability observed in Week 4 immediately apparent, reinforcing the importance of observability in federated learning.
- Separating training (GPU-intensive, batch-oriented) from analysis (lightweight, interactive) mirrors real-world MLOps workflows.

Week 5 emphasized that even when training outcomes are suboptimal, properly saved artifacts and metrics preserve their value by enabling diagnosis, comparison, and iteration.

---

## Overall Takeaway (Weeks 1–3)

- Week 1 established that PlantVillage is a **large, imbalanced, and fine-grained image classification dataset**, requiring models capable of capturing subtle visual patterns.
- Week 2 showed that **classical machine learning methods**, while useful as scientific baselines, are fundamentally limited by their reliance on flattened pixel representations.
- Week 3 demonstrated that **convolutional neural networks** effectively address spatial complexity, and that **transfer learning is critical** for achieving robust and scalable performance under class imbalance.
- Week 4 revealed that moving from centralized to federated learning introduces a new class of challenges unrelated to model expressiveness. Non-IID data distributions, client drift, and aggregation instability can significantly degrade performance, even when starting from a strong pretrained model. This highlights that federated learning is not merely a privacy-preserving alternative to centralized training, but a paradigm that requires careful algorithmic and architectural choices.
- Week 5 completed the transition from experimentation to engineering by emphasizing model persistence, metric logging, and visualization. By decoupling training from analysis and treating models as reusable artifacts, the project adopted an MLOps-oriented mindset essential for real-world deployment.

Overall, these weeks demonstrate that effective plant disease classification is not solely about achieving high accuracy, but about building reliable, interpretable, and deployable machine learning systems that account for data characteristics, training paradigms, and operational constraints.
