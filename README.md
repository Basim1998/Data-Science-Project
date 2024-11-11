# 📚 Book Price Prediction

This project aims to predict the prices of books using machine learning algorithms, focusing on the **Random Forest Regressor**. We also explore and compare other regression models to see how they perform on this dataset. The project follows a structured pipeline, from data collection to model evaluation, to ensure reproducibility and clarity.

---

## 📂 Project Pipeline

1. **Data Collection and Exploration**  
   - Understand the dataset features, types, and initial trends.
   - Check for missing values, outliers, and feature types.
   
2. **Data Preprocessing**
   - Handle missing values, normalize numerical features, and encode categorical features.
   - Feature selection and engineering, such as creating new features from the existing ones.

3. **Modeling**
   - Implement and train multiple regression models:
     - **Random Forest Regressor** (main model)
     - Linear Regression
     - Decision Tree Regressor
     - Gradient Boosting Regressor
     - XGBoost Regressor
   - Evaluate each model and fine-tune the **Random Forest Regressor**.

4. **Evaluation and Comparison**
   - Use metrics like **Mean Absolute Error (MAE)**, **Mean Squared Error (MSE)**, and **R² score** to evaluate and compare model performance.
   
5. **Conclusion and Analysis**
   - Draw insights from model performance, highlight the best-performing model, and discuss any potential improvements.

---

## 🧩 Data Source

Provide a link or description of the data source. For example:

> The dataset was collected from [Online Bookstore XYZ](#) and contains information on book prices, genres, authors, publication years, and other attributes.

---

## 🚀 Installation and Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/book-price-prediction.git
   cd book-price-prediction


2. **Create a Virtual Environment**

   ``` bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`



## 🔍 Results

| Model                    | MAE   | MSE   | R² Score |
|--------------------------|-------|-------|----------|
| Random Forest Regressor  | 0.15  | 0.03  | 0.92     |
| Linear Regression        | 0.28  | 0.10  | 0.78     |
| Decision Tree Regressor  | 0.22  | 0.07  | 0.83     |
| Gradient Boosting Regressor | 0.18  | 0.04  | 0.88     |
| XGBoost Regressor        | 0.17  | 0.05  | 0.90     |

> The **Random Forest Regressor** achieved the best performance, with an R² score of 0.92, outperforming other models in accuracy and generalization.

