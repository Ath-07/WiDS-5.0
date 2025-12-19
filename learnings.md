# Week 1 Learnings — Plant Disease Classification (PlantVillage)

## Dataset Understanding
- The PlantVillage dataset is structured as folder-based image data, where each folder represents a **Plant–Disease combination**.
- Multiple representations of the same images exist (color, grayscale, segmented).  
  For EDA, only the **color dataset** was used to avoid duplication and biased statistics.

---

## Key Observations

### 1. Class and Plant Imbalance
- The dataset contains **38 disease classes across 14 plants**.
- Certain plants, especially **Tomato**, dominate the dataset with multiple disease states and a high number of images.
- Some disease classes have significantly fewer samples.
- Imbalance exists both **globally** and **within individual plants**.
- Class imbalance must be handled carefully during training using augmentation, sampling strategies, or class-weighted losses.

---

### 2. Plant-wise Disease Distribution
- Plant-level analysis shows that some plants are dominated by one or two disease states.
- Other plants have a more balanced distribution of disease classes.
- This indicates that imbalance is not uniform across plants.

---

### 3. Image Quality Analysis
- Most images are clear and well-focused.
- Variations exist in lighting conditions, including overexposed and underexposed images.
- Backgrounds are mostly clean but occasionally include noise such as soil or other leaves.

---

### 4. Visual Similarity Between Disease Classes
- Disease classes within the same plant often show **subtle visual differences**.
- Differences are mainly in texture, spot patterns, and color intensity.
- In many cases, diseases are difficult to distinguish even by human inspection.
- This is a **fine-grained image classification problem**, requiring strong feature extraction and careful evaluation.

---

## Overall Takeaways
- Dataset understanding reveals that performance will depend heavily on data handling rather than model complexity alone.
- Addressing imbalance and visual similarity will be critical for downstream success.
- Week 1 EDA provides a strong foundation for informed modeling decisions in future weeks.

---

## Reflection
This exploratory analysis emphasized the importance of deeply understanding dataset characteristics before model training. The challenges observed in class balance, image quality, and disease similarity closely reflect real-world agricultural diagnosis problems.
