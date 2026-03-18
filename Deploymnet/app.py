# app.py

from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
from pathlib import Path
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import logging

# ----------------------------
# 1. Initialize FastAPI app
# ----------------------------
app = FastAPI(title="Plant Disease Detector API")

# ----------------------------
# 2. Setup Logging
# ----------------------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------------
# 3. Define Model Architecture
# ----------------------------
class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()

        # Convolution layers
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)

        self.pool = nn.MaxPool2d(2, 2)

        # Fully connected layers
        self.fc1 = nn.Linear(64 * 56 * 56, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))

        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# ----------------------------
# 4. Load Model Weights
# ----------------------------
MODEL_PATH = Path(__file__).resolve().parent / "model" / "federated_global_model.pth"
device = torch.device("cpu")

try:
    model = SimpleCNN(num_classes=38)
    model.load_state_dict(
        torch.load(MODEL_PATH, map_location=device, weights_only=True)
    )
    model.to(device)
    model.eval()
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")


# ----------------------------
# 5. Image Preprocessing
# ----------------------------
def preprocess_image(image: Image.Image) -> torch.Tensor:
    image = image.resize((224, 224))
    image_array = np.asarray(image, dtype=np.float32) / 255.0
    image_array = np.transpose(image_array, (2, 0, 1))
    return torch.from_numpy(image_array).unsqueeze(0)


# ----------------------------
# 6. Class Names (38 Classes)
# ----------------------------
class_names = [
    "Orange___Haunglongbing_(Citrus_greening)",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Soybean___healthy",
    "Peach___Bacterial_spot",
    "Tomato___Bacterial_spot",
    "Tomato___Late_blight",
    "Squash___Powdery_mildew",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Apple___healthy",
    "Tomato___healthy",
    "Blueberry___healthy",
    "Pepper,_bell___healthy",
    "Tomato___Target_Spot",
    "Grape___Esca_(Black_Measles)",
    "Corn_(maize)___Common_rust_",
    "Grape___Black_rot",
    "Corn_(maize)___healthy",
    "Strawberry___Leaf_scorch",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Cherry_(including_sour)___Powdery_mildew",
    "Tomato___Early_blight",
    "Potato___Late_blight",
    "Potato___Early_blight",
    "Pepper,_bell___Bacterial_spot",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Tomato___Leaf_Mold",
    "Cherry_(including_sour)___healthy",
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Strawberry___healthy",
    "Grape___healthy",
    "Tomato___Tomato_mosaic_virus",
    "Raspberry___healthy",
    "Peach___healthy",
    "Apple___Cedar_apple_rust",
    "Potato___healthy"
]


# ----------------------------
# 7. Routes
# ----------------------------

@app.get("/")
def home():
    return {
        "status": "Online",
        "message": "Send POST request to /predict 🌿"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Read image
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGB")

    # Preprocess
    tensor = preprocess_image(image).to(device)

    # Inference
    with torch.no_grad():
        outputs = model(tensor)
        probabilities = torch.softmax(outputs[0], dim=0)
        confidence, predicted_class = torch.max(probabilities, 0)

    result = class_names[predicted_class.item()]

    # Log prediction
    logging.info(
        f"Prediction: {result} | Confidence: {confidence.item():.4f}"
    )

    return {
        "class": result,
        "confidence": float(confidence.item())
    }
