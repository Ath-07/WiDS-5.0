# Week 1 — Exploratory Data Analysis  
## Plant Disease Classification (PlantVillage Dataset)

This repository contains the **Week 1 deliverables** for the Plant Disease Classification project under **WiDS 5.0**.  
The focus of this week is on **understanding the dataset through structured Exploratory Data Analysis (EDA)** before proceeding to model development.

---

## Objective
The goal of Week 1 is to:
- Understand the structure and composition of the PlantVillage dataset
- Identify class and plant-level imbalance
- Examine image quality and visual similarity between disease classes
- Derive insights that inform preprocessing and modeling decisions

No model training is performed in this week.

---

## Dataset Description
**PlantVillage Dataset (Kaggle)**  
- The original dataset contains three variants:
  - `color`
  - `grayscale`
  - `segmented`
- Since these variants contain the **same images in different representations**, EDA was conducted **only on the `color` dataset** to avoid redundancy and skewed statistics.
- Each class follows the naming convention:  
  `PlantName___DiseaseState`

---

## EDA Tasks Performed
The following analyses were carried out in `01_EDA.ipynb`:

- Dataset loading and dataframe construction from folder structure
- Extraction of plant and disease state from class labels
- Overall image count and class count analysis
- Class-wise and plant-wise image distribution
- Plant × disease state count analysis
- Visualization of plant-wise disease distribution using grid pie charts
- Visual inspection of image quality (blur, lighting, background)
- Visual comparison of disease classes to assess similarity

---

## Key Findings
- The dataset shows **significant class imbalance**, especially for certain plants such as Tomato.
- Disease distributions are also **imbalanced at the plant level**, not just globally.
- Many disease classes within the same plant show **high visual similarity**, making the task fine-grained.
- Image quality is generally good, but lighting and background variations exist.
- Color information is important for disease identification, justifying the use of RGB images.

Detailed observations are documented in `learnings.md`.

---
