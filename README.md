# 🏠 House Price Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Overview
This project builds a **House Price Prediction system** using Machine Learning techniques.  
It follows a complete ML workflow including data preprocessing, feature scaling, model training, evaluation, and comparison.

The goal is to identify the best-performing regression model for predicting house prices.

---

## 🎯 Objectives
- Apply **feature scaling** to improve model performance  
- Train and compare multiple regression models  
- Evaluate models using **RMSE and R² Score**  
- Select the best-performing model  
- Visualize model predictions  

---

## 📊 Dataset
- **Dataset:** California Housing Dataset (`housing.csv`)  
- **Target Variable:** `median_house_value`  

### 🔍 Features
- `median_income`  
- `housing_median_age`  
- `total_rooms`  
- `total_bedrooms`  
- `population`  
- `households`  
- `longitude`  
- `latitude`  

> Note: This project uses a **preprocessed dataset** containing only numerical features.  
> The categorical feature `ocean_proximity` is not included.

## 🛠️ Tech Stack
- Python  
- Jupyter Notebook  
- pandas  
- NumPy  
- scikit-learn  
- matplotlib     
---

## 🤖 Models Used
- Linear Regression (Baseline Model)  
- Ridge Regression (Reduces overfitting)  
- Decision Tree Regressor (Handles non-linear patterns)  

---

## 📈 Evaluation Metrics
- **RMSE (Root Mean Squared Error)** → Lower is better  
- **R² Score** → Higher is better  

---

## 🏆 Results
- All models were evaluated on test data  
- The best model was selected based on **lowest RMSE**  
- Ridge Regression showed strong generalization performance  
- Decision Tree showed slight overfitting tendencies  

---

## 📊 Visualizations
- Actual vs Predicted Prices Scatter Plot  
- Model Comparison Bar Chart  

---

## 💾 Model Saving
The best-performing model is saved using:

```python
import joblib
joblib.dump(best_model, "best_model.pkl")

---

## ⚙️ Machine Learning Workflow
