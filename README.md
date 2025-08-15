# 🍎 Food Wastage Prediction

> **Predict. Prevent. Preserve.**  
> A machine learning project using **XGBoost** to forecast potential food wastage and provide actionable insights for reduction.

---

## 📌 Overview  
Food wastage is a massive global issue — and a solvable one.  
This project predicts wastage based on **days until expiry** and **perishability status**, helping organizations:

- 📦 Optimize **redistribution**
- 💰 Reduce **operational losses**
- 🌱 Support **sustainability goals**

**Core Tech:** `Python`, `XGBoost`, `Streamlit`

---

## 📁 Dataset  
The dataset includes:

| Feature               | Description                           |
|-----------------------|---------------------------------------|
| Days until expiry     | Number of days before item spoils     |
| Perishability status  | 0 = Non-perishable, 1 = Perishable    |
| Quantity              | Target variable (units)               |

📥 **Download:** [Food Wastage Dataset – Dropbox](https://www.dropbox.com/scl/fo/0akkaed1rqsyx6d70xj2i/AKzd4tXvmPZ-fYgntpo_Zmc?rlkey=zjpep1spz5iaedwqe3zrgruy1&st=x389pjef&dl=0)  
➡ Place files in a `data/` folder in your project directory.

---

## ⚙ Installation  

1️⃣ **Clone Repository**
```bash
git clone https://github.com/yourusername/food-wastage-prediction.git
cd food-wastage-prediction
```

2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Prepare Dataset**
```bash
mkdir data
# Place downloaded CSV files in /data
```

---

## 🚀 Usage  

**Train the Model**
```bash
python train_model.py
```
✔ Loads dataset → Trains XGBoost model → Saves as `xgboost_food_wastage_model.pkl`

**Run Web App**
```bash
streamlit run app.py
```
🌐 Opens at `http://localhost:8501` where you can:
- Input food item details  
- Get wastage predictions  
- Receive actionable recommendations  

---

## 📂 Project Structure  
```
├── app.py                         # Streamlit web app
├── train_model.py                 # Model training script
├── data/                          # Dataset folder
│   ├── food_data1.csv
│   └── food_data2.csv
├── xgboost_food_wastage_model.pkl # Trained model
├── requirements.txt               # Dependencies
├── README.md
└── .gitignore
```

---

## 🔧 Requirements  
- Python 3.8+  
- Libraries:  
```txt
pandas==1.3.5  
numpy==1.21.5  
scikit-learn==1.0.2  
xgboost==1.6.2  
streamlit==1.12.0  
joblib==1.1.0  
```

---

## 📊 Model Performance  
| Metric   | Score          |
|----------|---------------|
| R² Score | ~0.90          |
| MAE      | ~8.5 units     |
| MSE      | ~120           |

**Key Insights:**  
- Days until expiry = strongest predictor  
- Perishable items → 2–3× higher wastage risk  
- High-risk items flagged for prioritization  

---

## 🎯 Business Impact  
- 📉 Reduce waste by 15–30%  
- 💰 Save costs via better inventory control  
- 🌱 Support sustainability & CSR goals  
- 🚚 Improve logistics planning  

---

## 🔮 Future Improvements  
- Add storage temperature, humidity, packaging type  
- Mobile app for field teams  
- IoT-based real-time tracking  
- Optimal redistribution route prediction  

---

## 🤝 Contributing  
Pull requests welcome. Open issues for suggestions or bugs.
