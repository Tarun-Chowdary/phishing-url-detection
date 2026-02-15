# 🔐 Phishing URL Detection System

A Machine Learning–based phishing URL detection system built using **Random Forest**.  
This project allows users to input a URL and receive a prediction indicating whether the URL is **Legitimate** or **Phishing**.

The system is modular, lightweight, and easy to extend into a Web App or REST API.

---

## 📌 Features

- URL-based phishing detection  
- Random Forest classifier  
- Real-time command-line interface  
- Modular project structure  
- Lightweight lexical feature extraction  
- Easily extendable (Streamlit / FastAPI ready)

---

## 📁 Project Structure

```
project_root/
│
├── main.py
│
├── model/
│   └── random_forest_model.pkl
├── notebooks/
├── src/
│   ├── feature_extractor.py
│   └── model_loader.py
├── results/
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/phishing-url-detector.git
cd phishing-url-detector
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

**Mac/Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Setup

Before running the system, you must train and save the model.

If you already have a trained Random Forest model:

```python
import pickle

with open("model/random_forest_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)
```

Ensure the file is saved inside the `model/` directory.

---

## 🚀 Running the Application

From the project root directory:

```bash
python main.py
```

You will see:

```
=== Phishing URL Detection System ===
Enter URL (or type 'exit' to quit):
```

### Example

```
Enter URL: http://secure-login-update.com
⚠️ Phishing URL Detected

Enter URL: https://google.com
✅ Legitimate URL
```

---

## 🔍 How It Works

1. User inputs a URL.
2. Feature extractor converts the URL into numerical features.
3. Trained Random Forest model predicts the class.
4. Prediction is displayed in the terminal.

---

## 🧪 Testing the System

### Legitimate URLs

```
https://google.com
https://github.com
https://wikipedia.org
```

### Suspicious-style URLs

```
http://secure-login-update.com
http://verify-account-paypal-security.net
http://192.168.0.1/login
```

---

## 📦 Dependencies

- numpy  
- scikit-learn  

Manual installation (if required):

```bash
pip install numpy scikit-learn
```

---

## 📊 Model Details

- Algorithm: Random Forest Classifier  
- Feature Type: Lexical URL-based features  
- Output Classes:
  - 0 → Legitimate
  - 1 → Phishing

---

## 📈 Future Improvements

- Add probability confidence score  
- Integrate SHAP for explainability  
- Convert to Web App using Streamlit  
- Deploy REST API using FastAPI  
- Add automated retraining pipeline  
- Perform cross-dataset robustness testing  

---
## 📫 Contact / Support

- For questions, suggestions, or support, please open an issue on the [GitHub repository](https://github.com/Tarun-Chowdary/phishing-url-detection/issues).
- You can also reach out via email: yegi.2992@gmail.com

We welcome feedback and contributions!

