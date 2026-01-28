import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Load metrics
# =========================

METRICS_PATH = "federated_metrics.csv"

st.title("📊 Federated Learning Training Monitor")

df = pd.read_csv(METRICS_PATH)

# =========================
# Plot accuracy vs rounds
# =========================

st.subheader("Global Accuracy vs Federated Rounds")

fig, ax = plt.subplots()
ax.plot(df["round"], df["global_accuracy"], marker="o")
ax.set_xlabel("Federated Round")
ax.set_ylabel("Global Accuracy (%)")
ax.set_title("Federated Model Performance")

st.pyplot(fig)

# =========================
# Final summary
# =========================

final_round = df["round"].iloc[-1]
final_acc = df["global_accuracy"].iloc[-1]

st.subheader("Final Model Summary")
st.write(f"✅ Final Round: **{final_round}**")
st.write(f"🎯 Final Global Accuracy: **{final_acc:.2f}%**")
