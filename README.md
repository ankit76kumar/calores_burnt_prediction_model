# 🔥 Calories Burnt Prediction Model using XGBoost

This project builds a robust machine learning model to **predict the number of calories burnt** during physical exercises using various physiological and activity-based features. Leveraging the power of **XGBoost (Extreme Gradient Boosting)**, the model delivers high prediction accuracy, making it suitable for use in fitness applications, smart devices, and health tracking systems.

---

## 📌 Project Objective

To accurately predict **calories burnt** based on user demographic and workout features such as age, gender, height, weight, heart rate, body temperature, and workout duration.

---

## 🧠 Machine Learning Technique

- **Algorithm Used**: XGBoost Regressor
- **Why XGBoost?**
  - Handles **non-linear relationships** effectively
  - Performs **exceptionally well with tabular data**
  - Includes **regularization** to reduce overfitting
  - Provides **feature importance**

---

## 📂 Project Structure

```

calories\_burnt\_prediction\_model/
│
├── README.md                          # Project documentation
├── calories burnt predictions.ipynb   # Jupyter notebook with EDA and model building
├── calories.csv                       # Dataset: calories burnt
├── exercise.csv                       # Dataset: user & exercise data
├── predictive\_model.py                # Python script to train the model
├── temp.py                            # Optional temporary/test file
├── tempCodeRunnerFile.py              # Auto-generated temporary file
└── requirements.txt                   # List of required libraries

````

---

## 🧾 Datasets Used

1. **calories.csv**  
   Contains:
   - `User_ID`
   - `Calories` (target variable)

2. **exercise.csv**  
   Contains:
   - `User_ID`, `Gender`, `Age`, `Height`, `Weight`
   - `Duration`, `Heart_Rate`, `Body_Temp`

Datasets are merged using `User_ID` to form a complete training dataset.

---

## 📊 Features Used

| Feature       | Description                        |
|---------------|------------------------------------|
| Gender        | Male or Female                     |
| Age           | Age of the individual              |
| Height        | Height in cm                       |
| Weight        | Weight in kg                       |
| Duration      | Duration of exercise in minutes    |
| Heart_Rate    | Heart rate during exercise         |
| Body_Temp     | Body temperature in Celsius        |

**🎯 Target Variable**: `Calories`

---

## 🔍 Exploratory Data Analysis (EDA)

Performed in the notebook:
- Checked for missing values
- Histograms and KDE plots for distributions
- Correlation heatmap for feature relationships
- Gender-wise analysis
- Feature importance using XGBoost

---

## 🧰 Tools & Technologies Used

- Python 3.x
- Jupyter Notebook
- XGBoost
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

---

## 🚀 How to Run the Project

### 🛠️ Clone the Repository
```bash
git clone https://github.com/yourusername/calories_burnt_prediction_model.git
cd calories_burnt_prediction_model
````

### 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### ▶️ Run the Jupyter Notebook

```bash
jupyter notebook "calories burnt predictions.ipynb"
```

### OR Run the Python Script

```bash
python predictive_model.py
```

---

## 📈 Model Performance

* **Model Used**: XGBoost Regressor
* **Evaluation Metrics**:

  * R² Score
  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)
* **Insights**:

  * Heart rate and duration are strong predictors
  * Gender and weight significantly influence calorie burn
  * XGBoost performed better than basic regression models

---

## ✅ Future Improvements

* Real-time calorie prediction integration via API
* Train on larger and diverse datasets
* Deploy with Flask or Streamlit for web-based interaction
* Include activity type (e.g., running, cycling) as a feature

---

## 📎 Requirements

List of required libraries (included in `requirements.txt`):

```
xgboost
pandas
numpy
scikit-learn
matplotlib
seaborn
jupyter
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 👤 Author

**Ankit Kumar**
🎓 B.Tech – Artificial Intelligence & Data Science
🏫 Truba Institute of Engineering & Information Technology
📍 Bhopal, Madhya Pradesh
📧 \[Add Email or LinkedIn/GitHub link]

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) – feel free to use and modify it.

---

