# 🏀 NBA Shot Prediction - Kobe Bryant Shot Success Classifier

An interactive Machine Learning web app that predicts whether Kobe Bryant's shot will be **Made** or **Missed**, using actual NBA shot data.

✅ **Trained on real match data**  
✅ **Multiple ML models compared**  
✅ **Best model deployed with Streamlit**  
✅ **Live Prediction Interface**

---

## 🚀 Live Demo

🔗 **Deployed Here**:  
👉 [nba-shot-prediction.streamlit.app](https://nba-shot-prediction.streamlit.app)

---

## 📌 Project Description

Using 20+ years of NBA shot data, we built and deployed a model to predict shot outcomes based on game context like:

- Shot distance  
- Shot type  
- Game period  
- Clutch situations  
- Home/away  
- Zone and range of the court  
- Playoff match or not  
- Season information

All engineered into **16 meaningful features** with categorical encoding and time-based transformations.

---

## 📊 Model Comparison

| Model                | Accuracy | F1 Score | ROC AUC | Best Trait                     |
|---------------------|----------|----------|---------|-------------------------------|
| Logistic Regression | 0.6806   | 0.5708   | 0.6967  | Simplicity, interpretable     |
| K-Nearest Neighbors | 0.6070   | 0.5347   | 0.6267  | Local patterns, fast prototype |
| Decision Tree       | 0.6833   | 0.5806   | 0.6978  | Interpretable non-linear rules |
| Random Forest       | 0.6615   | 0.5643   | 0.6904  | Robust ensemble, stable       |
| **XGBoost ✅**        | **0.6806** | **0.5714** | **0.7091** | Best generalization, boosted performance |

---

### ✅ Why XGBoost?

- ⏱️ Efficient training with boosting  
- 📈 Highest **ROC AUC (0.7091)**, showing best ranking performance  
- ✅ Handles class imbalance using `scale_pos_weight`  
- 🧠 Regularized, prevents overfitting  
- 🚀 Easy deployment with `.pkl` serialization  

---

## 🛠️ Tech Stack

| Tool            | Use                            |
|-----------------|---------------------------------|
| Python          | Core language                  |
| Pandas / NumPy  | Data cleaning & transformation |
| Scikit-learn    | ML models & evaluation         |
| XGBoost         | Final classifier               |
| Streamlit       | Web app framework              |
| GitHub          | Version control                |
| Streamlit Cloud | Deployment                     |

---

## 🧪 Features Used

- `shot_distance`, `is_3pt`, `is_clutch`, `home_game`, `period`, `time_remaining`, `playoffs`, `season_start`
- One-hot encoded:  
  - `shot_zone_basic`: `'Restricted Area'`, `'Mid-Range'`, `'Left Corner 3'`  
  - `shot_zone_range`: `'<8 ft.'`, `'8-16 ft.'`, `'24+ ft.'`  
  - `combined_shot_type`: `'Jump Shot'`, `'Layup'`

---

## 🗂 Project Structure

nba-shot-prediction/
├── app.py # Streamlit app
├── xgboost_model.pkl # Final XGBoost model
├── X_test.pkl # Test set features
├── y_test.pkl # Test set targets
├── data.csv # Cleaned dataset
├── requirements.txt # Python dependencies
├── README.md # Project documentation

🌐 Deployment
✅ Hosted on Streamlit Cloud

🔗 Live App : https://nba-shot-prediction.streamlit.app

📂 GitHub: [nba-shot-prediction](https://github.com/SuyogDeepMind/Nba-Shot-Prediction)

### 👨‍💻 Author  
**Suyog Manke**  
💼 Aspiring Data Scientist  
📫 Email: suyogmanke4@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/suyogmanke/)  
🔗 [GitHub](https://github.com/SuyogDeepMind?tab=repositories)  

---

### 📢 Credits  
Dataset: [data.csv]


Powered by ❤️ and 🐍 Python
