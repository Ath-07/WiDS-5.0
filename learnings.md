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

## Overall Takeaway

- Week 1 EDA revealed structural challenges in the dataset that directly influenced Week 2 model performance.
- Shallow baselines provide a strong yet limited benchmark, scientifically motivating the transition to **CNN-based architectures** in subsequent weeks.
- Together, these weeks establish a rigorous foundation for evaluating the true impact of deep learning models on plant disease classification.
