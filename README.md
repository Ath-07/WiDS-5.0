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

---

### Dataset Overview
- The PlantVillage dataset is available in `color`, `grayscale`, and `segmented` variants.
- Since these variants contain the **same images**, EDA was conducted **only on the `color` dataset** to avoid redundancy.
- Each class follows the naming convention:  
  `PlantName___DiseaseState`

---

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

---

### Methodology
- Images resized to **64×64** and flattened into 1D vectors  
- Features scaled using **StandardScaler**  
- 80–20 train–test split  

Baselines evaluated:
- **Dummy Classifier (most frequent)** — lower-bound sanity check  
- **Random Forest Classifier** — shallow baseline  

---

### Results (Week 2)
- Dummy baseline achieved ~**10% accuracy**, validating correct data handling.
- Random Forest achieved ~**64% accuracy**, defining the upper limit of classical ML on raw pixels.
- Shallow models capture **global color and texture cues** but struggle with **spatial and subtle disease patterns**, especially for minority classes.

---

## Overall Takeaway
Week 1 EDA revealed dataset challenges that directly explain Week 2 baseline performance.  
The shallow baseline establishes a strong benchmark and motivates the use of **CNN-based models** in subsequent weeks.

---

## Repository Structure
- `01_EDA.ipynb` — Exploratory Data Analysis (Week 1)
- `02_Shallow_Baseline.ipynb` — Classical ML baselines (Week 2)
- `learnings.md` — Weekly insights and reflections
