# Plant Disease Classification - WiDS 5.0

## PlantVillage Dataset

This repository contains the deliverables for a Plant Disease Classification project under WiDS 5.0. The work progresses from data understanding to baseline modeling, deep learning, federated learning, and deployment.

---

## Week 1 - Exploratory Data Analysis

### Objective
- Understand the structure and composition of the PlantVillage dataset
- Identify class-level and plant-level imbalance
- Examine image quality and visual similarity between disease classes

No model training is performed in this week.

### Key Findings
- The dataset contains 38 disease classes across 14 plants
- There is significant imbalance both globally and within plants
- Tomato dominates the dataset with multiple disease categories
- Disease classes within the same plant are visually similar, making this a fine-grained classification task

Detailed observations are documented in `learnings.md`.

---

## Week 2 - Shallow Baseline Modeling

### Objective
Establish a scientific baseline using traditional machine learning methods before introducing deep learning models.

### Methodology
- Images resized to 64x64 and flattened into 1D vectors
- Features scaled using `StandardScaler`
- 80-20 train-test split
- Baselines evaluated: Dummy Classifier and Random Forest

### Results
- Dummy baseline achieved about 10% accuracy
- Random Forest achieved about 64% accuracy
- Shallow models captured global color and texture cues but struggled with spatial and subtle disease patterns

---

## Week 3 - Deep Learning With CNNs And Transfer Learning

### Objective
Apply convolutional neural networks to learn fine-grained disease patterns and compare them with transfer learning.

### Models
- Custom CNN trained from scratch on 224x224 images
- MobileNetV2 with transfer learning and fine-tuning

### Results
- Custom CNN reached 98.64% training accuracy and 85.89% validation accuracy
- MobileNetV2 reached 98.76% validation accuracy with strong macro and weighted F1 scores
- Transfer learning generalized much better under class imbalance

---

## Week 4 - Federated Learning With CNNs

### Objective
Simulate decentralized training and analyze model behavior under non-IID data distributions.

### Methodology
- Federated learning implemented with Flower
- Three simulated clients with disjoint, non-IID data splits
- Shared CNN trained with FedAvg across multiple rounds

### Results
- Initial federated round achieved high accuracy
- Later rounds degraded due to client drift
- The experiment highlighted the limitations of FedAvg under heterogeneous data

---

## Week 5 - Saving, Visualizing, And Deploying The Federated Model

### Objective
Move from experimentation to system-level thinking by persisting models, logging metrics, and exposing the model for inference.

### Outputs
- Final global federated model saved to disk
- Per-round accuracy logged to CSV
- Streamlit visualization for federated metrics
- FastAPI inference service packaged with Docker

---

## Deployment API

The repository includes a FastAPI inference service in `Deploymnet/` for serving the trained plant disease classifier over HTTP.

### Files
- `Deploymnet/Dockerfile` - Docker image definition for the API
- `Deploymnet/.dockerignore` - Docker build context exclusions
- `Deploymnet/app.py` - FastAPI app for inference
- `Deploymnet/requirements.txt` - Python dependencies for the API
- `Deploymnet/model/federated_global_model.pth` - model weights used at inference time

### Build And Run With Docker

From the repository root:

```powershell
docker build -t wids-api .\Deploymnet
docker run --rm -p 8000:8000 wids-api
```

The API will be available at:
- `http://localhost:8000`
- `http://localhost:8000/docs`

### API Endpoints
- `GET /` returns a simple health response
- `POST /predict` accepts an image upload and returns predicted class and confidence

Example request:

```powershell
curl.exe -X POST "http://localhost:8000/predict" -F "file=@C:\path\to\leaf.jpg"
```

Example response:

```json
{
  "class": "Tomato___Late_blight",
  "confidence": 0.94
}
```

### Pulling The Prebuilt Image

If a prebuilt image has been pushed to Docker Hub, others can run:

```powershell
docker pull <dockerhub-username>/wids-api:latest
docker run --rm -p 8000:8000 <dockerhub-username>/wids-api:latest
```

---

## Repository Structure
- `01_eda_plantvillage.ipynb` - Exploratory Data Analysis
- `02-baseline-model.ipynb` - Classical ML baseline
- `03_deeplearning.ipynb` - CNNs and transfer learning
- `04_fedretead_learning.ipynb` - Federated learning experiments
- `stream_app.py` - Streamlit visualization
- `federated_metrics.csv` - Logged federated metrics
- `Deploymnet/` - Dockerized FastAPI inference service
- `learnings.md` - Weekly insights and reflections
