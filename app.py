
import streamlit as st
import pickle
import numpy as np

with open("xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="🏀 Kobe Shot Predictor", layout="centered")
st.title("🏀 Kobe Bryant Shot Predictor")
st.markdown("Predict whether Kobe's shot was **Made** or **Missed** using real game data features.")

shot_distance = st.slider("📏 Shot Distance (feet)", 0, 60, 20)
is_3pt = st.selectbox("🎯 Is 3-Point Shot?", ["No", "Yes"])
is_3pt = 1 if is_3pt == "Yes" else 0
is_clutch = st.selectbox("🕑 Clutch Moment (Last 5 sec)?", ["No", "Yes"])
is_clutch = 1 if is_clutch == "Yes" else 0
home_game = st.selectbox("🏠 Home Game?", ["No", "Yes"])
home_game = 1 if home_game == "Yes" else 0
period = st.slider("⏱️ Game Period (Quarter)", 1, 4, 2)
minutes_remaining = st.slider("🕒 Minutes Remaining", 0, 12, 5)
seconds_remaining = st.slider("🕒 Seconds Remaining", 0, 59, 30)
playoffs = st.selectbox("🏆 Playoff Game?", ["No", "Yes"])
playoffs = 1 if playoffs == "Yes" else 0
season_start = st.number_input("📅 Season Start (e.g., 2000 for 2000-01)", min_value=1996, max_value=2016, value=2008)

shot_zone_basic = st.selectbox("📌 Shot Zone (Basic)", ['Restricted Area', 'Mid-Range', 'Left Corner 3'])
shot_zone_range = st.selectbox("📏 Shot Zone Range", ['Less Than 8 ft.', '8-16 ft.', '24+ ft.'])
shot_type = st.selectbox("🎯 Combined Shot Type", ['Jump Shot', 'Layup'])

final_features = [
    'shot_distance', 'is_3pt', 'is_clutch', 'home_game',
    'period', 'time_remaining', 'playoffs', 'season_start',
    'shot_zone_basic_Restricted Area', 'shot_zone_basic_Mid-Range', 'shot_zone_basic_Left Corner 3',
    'shot_zone_range_Less Than 8 ft.', 'shot_zone_range_8-16 ft.', 'shot_zone_range_24+ ft.',
    'combined_shot_type_Jump Shot', 'combined_shot_type_Layup'
]

input_dict = {feature: 0 for feature in final_features}
input_dict['shot_distance'] = shot_distance
input_dict['is_3pt'] = is_3pt
input_dict['is_clutch'] = is_clutch
input_dict['home_game'] = home_game
input_dict['period'] = period
input_dict['time_remaining'] = minutes_remaining * 60 + seconds_remaining
input_dict['playoffs'] = playoffs
input_dict['season_start'] = season_start
input_dict[f'shot_zone_basic_{shot_zone_basic}'] = 1
input_dict[f'shot_zone_range_{shot_zone_range}'] = 1
input_dict[f'combined_shot_type_{shot_type}'] = 1

input_array = np.array([list(input_dict.values())])

if st.button("Predict Shot Result"):
    prediction = model.predict(input_array)[0]
    prob = model.predict_proba(input_array)[0][1]
    st.markdown("### 🎯 Prediction:")
    if prediction == 1:
        st.success(f"✅ Shot Made! (Confidence: {prob:.2%})")
    else:
        st.error(f"❌ Shot Missed! (Confidence: {1 - prob:.2%})")
    st.metric("Model Confidence (Shot Made)", f"{prob*100:.2f}%")
