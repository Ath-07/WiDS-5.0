# Plant Disease Classification — WiDS 5.0  
## PlantVillage Dataset

This repository contains the **Week 1 and Week 2 deliverables** for the Plant Disease Classification project under **WiDS 5.0**, following a progressive approach from data understanding to baseline modeling.

---

## Week 1 — Exploratory Data Analysis (EDA)

### Objective
- Understand the structure and composition of the PlantVillage dataset  
- Identify class-level and plant-level imbalance  
- Examine image quality and visual similarity between disease classes  

> No model training is performed in this week.

### Dataset Overview
- The PlantVillage dataset is available in `color`, `grayscale`, and `segmented` variants.
- Since these variants contain the **same images**, EDA was conducted **only on the `color` dataset** to avoid redundancy.
- Each class follows the naming convention:  
  `PlantName___DiseaseState`

### Key Findings (Week 1)
- The dataset contains **38 disease classes across 14 plants**, with significant imbalance both globally and within plants.
- Certain plants, especially **Tomato**, dominate the dataset with multiple disease categories.
- Disease classes within the same plant show **high visual similarity**, making this a fine-grained classification task.
- Image quality is generally good, with some variation in lighting and background conditions.

Detailed observations are documented in `learnings.md`.

---

## Week 2 — Shallow Baseline Modeling (Classical ML)

### Objective
Establish a **scientific baseline** using traditional machine learning methods before introducing deep learning models.


### Methodology
- Images resized to **64×64** and flattened into 1D vectors  
- Features scaled using **StandardScaler**  
- 80–20 train–test split  

Baselines evaluated:
- **Dummy Classifier (most frequent)** — lower-bound sanity check  
- **Random Forest Classifier** — shallow baseline  


### Results (Week 2)
- Dummy baseline achieved ~**10% accuracy**, validating correct data handling.
- Random Forest achieved ~**64% accuracy**, defining the upper limit of classical ML on raw pixels.
- Shallow models capture **global color and texture cues** but struggle with **spatial and subtle disease patterns**, especially for minority classes.

---

## Week 3 — Deep Learning with CNNs & Transfer Learning

### Objective
Move beyond shallow baselines by applying convolutional neural networks to learn spatial and fine-grained disease patterns, and evaluate the impact of transfer learning.

### Methodology
Two models were trained and compared:

- **Custom CNN (from scratch)**  
  - Input resolution: 224×224  
  - Two convolutional layers followed by fully connected layers  
  - Trained for 10 epochs with data augmentation and Adam optimizer  

- **MobileNetV2 (transfer learning)**  
  - ImageNet-pretrained backbone  
  - Classifier head trained first, followed by fine-tuning of the last convolutional blocks  
  - Lower learning rate used during fine-tuning  

### Results (Week 3)
- **Custom CNN**:
  - Training accuracy: **98.64%**  
  - Validation accuracy: **85.89%**  
  - Macro F1-score: **0.81**, Weighted F1-score: **0.86**  
  - Exhibits overfitting and reduced recall on minority and visually similar disease classes  

- **MobileNetV2**:
  - Validation accuracy: **98.76%**  
  - Macro F1-score: **0.98**, Weighted F1-score: **0.99**  
  - Strong precision and recall across all classes, with minimal confusion even under class imbalance  

---

## Overall Takeaway
 A progressive evaluation of the PlantVillage dataset highlights the importance of aligning modeling complexity with dataset characteristics.  
Week 1 EDA revealed significant class imbalance and high visual similarity between disease categories within the same plant, establishing this as a fine-grained classification problem.  
Week 2 classical machine learning baselines demonstrated that shallow models relying on raw pixel features are limited in their ability to capture subtle disease patterns, achieving moderate performance despite careful preprocessing.  
Week 3 deep learning experiments confirmed that convolutional neural networks substantially improve performance by learning spatial representations, while transfer learning with a pretrained MobileNetV2 backbone delivers near-optimal generalization even under class imbalance.  

Together, these results show that effective plant disease classification requires both domain-aware data understanding and modern CNN architectures, with transfer learning emerging as the most reliable and scalable approach for real-world deployment.

---

## Repository Structure
- `01_EDA.ipynb` — Exploratory Data Analysis (Week 1)
- `02_Shallow_Baseline.ipynb` — Classical ML baselines (Week 2)
- `03_deeplearning.ipynb` - CNNs and Transfer Learning
- `learnings.md` — Weekly insights and reflections
