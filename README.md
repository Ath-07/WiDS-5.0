# Plant Disease Classification — WiDS 5.0  
## PlantVillage Dataset

This repository contains the **All deliverables** for the Plant Disease Classification project under **WiDS 5.0**, following a progressive approach from data understanding to baseline modeling.

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

## Week 4 — Federated Learning with CNNs

### Objective  
Simulate decentralized training using federated learning and analyze model behavior under non-IID data distributions.

### Methodology  
- Implemented federated learning using the Flower framework  
- Simulated three clients with disjoint, non-IID data splits  
- Trained a shared CNN using the FedAvg algorithm across multiple rounds  

### Results  
- Initial federated round achieved high accuracy (~91%)  
- Subsequent rounds showed accuracy degradation due to client drift  
- Demonstrated known limitations of FedAvg under heterogeneous data  

---

## Week 5 — Saving, Visualizing, and Deploying the Federated Model (MLOps)

### Objective  
Transition from experimentation to system-level thinking by persisting models, logging metrics, and visualizing training behavior.

### Methodology  
- Saved the final global federated model to disk  
- Logged per-round global accuracy to a CSV file  
- Built a Streamlit app to visualize federated training performance  

### Results  
- Enabled post-training inspection without retraining  
- Visualizations revealed federated convergence issues clearly  
- Demonstrated reproducibility and separation of training from analysis

---

## Overall Takeaway

This project follows a progressive and structured approach to plant disease classification, moving from data understanding to model development, distributed training, and system-level deployment considerations.

Weeks 1–3 established a strong foundation for modeling by emphasizing the importance of **data characteristics** and **model choice**. Exploratory data analysis in Week 1 revealed significant class imbalance and high visual similarity between disease categories within the same plant, framing the problem as a fine-grained classification task. Week 2 demonstrated that classical machine learning models operating on raw pixel features are inherently limited in capturing such subtle spatial patterns, achieving only moderate performance despite careful preprocessing. Week 3 showed that convolutional neural networks substantially improve performance by learning hierarchical spatial representations, and that transfer learning with a pretrained MobileNetV2 backbone provides robust generalization even under severe class imbalance.

Building on this foundation, Week 4 extended the problem to a **federated learning setting**, highlighting challenges that arise when training models across decentralized, non-IID data sources. While the federated model achieved strong initial performance when initialized from centralized weights, training became unstable in later rounds due to client drift and heterogeneous data distributions. These results underscore that federated learning is not a drop-in replacement for centralized training, but a paradigm that requires careful optimization, architectural constraints, and algorithmic choices.

Finally, Week 5 shifted the focus from experimentation to **machine learning system design**. By saving trained models, persisting training metrics, and visualizing federated behavior using a lightweight Streamlit application, the project adopted an MLOps-oriented mindset. This separation of training, analysis, and deployment reflects real-world workflows, where reproducibility, observability, and usability are as critical as raw model performance.

Overall, the project demonstrates that effective plant disease classification requires not only accurate models, but also a deep understanding of data properties, appropriate learning paradigms for the deployment context, and sound engineering practices to turn experiments into reliable systems.

---

## Repository Structure
- `01_EDA.ipynb` — Exploratory Data Analysis (Week 1)
- `02_Shallow_Baseline.ipynb` — Classical ML baselines (Week 2)
- `03_deeplearning.ipynb` - CNNs and Transfer Learning (Week 3)
- `04_fedretead_learning.ipynb` - Federated Models (Week 4)
- `app.py` - Strealit script for visualizing (Week 5)
- `federated_metrics.csv` - Result metrices
- `federated_global_model.pth` - final federated model weights
- `learnings.md` — Weekly insights and reflections
