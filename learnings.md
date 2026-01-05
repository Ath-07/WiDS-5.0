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
While the transfer learning model achieves very high validation accuracy on the PlantVillage dataset, these results reflect the controlled acquisition conditions of the dataset. Real-world agricultural images are significantly more complex, and performance is expected to degrade under domain shift. Therefore, the reported metrics should be interpreted as an upper bound rather than a realistic deployment benchmark.
---

## Overall Takeaway (Weeks 1–3)

- Week 1 established that PlantVillage is a **large, imbalanced, and fine-grained image classification dataset**, requiring models capable of capturing subtle visual patterns.
- Week 2 showed that **classical machine learning methods**, while useful as scientific baselines, are fundamentally limited by their reliance on flattened pixel representations.
- Week 3 demonstrated that **convolutional neural networks** effectively address spatial complexity, and that **transfer learning is critical** for achieving robust and scalable performance under class imbalance.
- Together, these weeks illustrate a clear progression from data understanding to baseline modeling and finally to high-performing deep learning solutions, forming a strong foundation for further optimization, interpretability, and real-world deployment.
