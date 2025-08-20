# 🔥 Calories Prediction App

A professional **Machine Learning + Streamlit web app** that predicts the number of **calories burned** based on user’s personal and physical activity details.  

This project demonstrates the **end-to-end ML pipeline** including data preprocessing, model training, evaluation, and deployment using **Streamlit**.

---

## 🚀 Features
- Interactive **Streamlit UI** with sidebar inputs.  
- Predicts calories burned based on:
  - Gender  
  - Age  
  - Height & Weight  
  - Exercise Duration  
  - Heart Rate  
  - Body Temperature  
- Machine Learning models (Linear Regression, Decision Tree, Random Forest, Gradient Boosting).  
- Visualization of prediction results.  
- Saved and loaded models using **Joblib**.  

---

## 🧑‍💻 Tech Stack
- **Python 3.11+**  
- **Pandas / NumPy** → Data handling  
- **Matplotlib / Seaborn** → Visualization  
- **Scikit-learn** → ML models & preprocessing  
- **Streamlit** → Web app deployment  
- **Joblib** → Model persistence  

---

## 📂 Project Structure
```
├── calories.csv              # Dataset
├── calories_model.pkl        # Trained model
├── scaler.pkl                # StandardScaler
├── app.py                    # Streamlit app
├── notebook.ipynb            # Jupyter notebook (training & analysis)
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/calories-prediction-app.git
cd calories-prediction-app
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App
```bash
streamlit run app.py
```

Then open 👉 [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📊 Model Training
The dataset (`calories.csv`) was used to train multiple regression models.  
Cross-validation and hyperparameter tuning were performed.  
Best model was saved as `calories_model.pkl`.  

### Example: Decision Tree Parameters
```python
DecisionTreeRegressor(
    max_depth=10,
    min_samples_split=20,
    min_samples_leaf=10,
    random_state=42
)
```

---

## 🎯 Sample Prediction
Example input:  
- Male, Age: 25, Height: 170 cm, Weight: 70 kg  
- Duration: 30 min, Heart Rate: 120 bpm, Body Temp: 38°C  

**Output → Estimated Calories Burned: ~140 kcal**

---

## 📸 Screenshots
### App Interface
![App Screenshot](https://via.placeholder.com/800x400.png?text=Calories+App+Screenshot)

---

## 🤝 Contributing
Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.  

---

## 🧑 Author
👨‍💻 **Ahmed Hamdy**  
- Data Science & AI Enthusiast 🚀  
- [LinkedIn](https://www.linkedin.com/in/ahmed-hamdy/) | [GitHub](https://github.com/ahmedhub2005)  

---
