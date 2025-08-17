# Heart Disease Prediction Project

##  Overview
This project aims to predict the likelihood of heart disease using machine learning models. The dataset is based on the Cleveland Heart Disease dataset, a well-known benchmark in healthcare analytics.

##  Features Implemented
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Principal Component Analysis (PCA)
- Supervised Learning (Logistic Regression, Random Forest, SVM, Naive Bayes, KNN)
- Unsupervised Learning (K-Means, Hierarchical Clustering)
- Model Evaluation (Accuracy, Precision, Recall, F1 Score, ROC & AUC)
- Hyperparameter Tuning (GridSearchCV, RandomizedSearchCV)
- Model Export (`.pkl` file using joblib)
- Streamlit Web App for real-time prediction
- Ngrok Deployment for public access

##  Dataset
- Source: Cleveland Heart Disease Dataset
- Rows: 303
- Features: Age, Sex, Chest Pain, Blood Pressure, Cholesterol, etc.
- Target: `num` (converted to binary `target` → 1: Heart Disease, 0: No Disease)

##  Tech Stack
- Python (pandas, numpy, scikit-learn, matplotlib, seaborn)
- Streamlit (for UI)
- Pyngrok (for deployment)
- Joblib (model persistence)

## ▶ How to Run the App
1. Clone this repository:
git clone <your-repo-link>
cd heart-disease-prediction

2. Install dependencies:
pip install -r requirements.txt

3. Run the Streamlit app:
streamlit run app.py

4. (Optional) Deploy via Ngrok:
python ngrok_tunnel.py

## 📊 Evaluation Metrics
See [evaluation_metrics.txt](evaluation_metrics.txt) for full details.

## 🌐 Deployment
Ngrok provides a temporary public URL for accessing the app.

---

### Author
Passant Shaaban Elsherif
