import pandas as pd
import joblib

# 1. Load pipeline
pipeline = joblib.load('final_attrition_pipeline.pkl')

# 2. Load data (attrition_cleaned.csv digunakan sebagai contoh)
data_baru = pd.read_csv('attrition_cleaned.csv')

# 3. Siapkan X
X_new = data_baru.drop(columns=['Attrition', 'EmployeeId'])

# 4. Prediksi
prediksi = pipeline.predict(X_new)
probabilitas = pipeline.predict_proba(X_new)[:, 1]

# 5. Gabung hasil ke data asli
hasil = data_baru.copy()
hasil['PredictedAttrition'] = prediksi
hasil['AttritionProbability'] = probabilitas

# 6. Simpan ke file
hasil.to_csv('hasil_prediksi.csv', index=False)
print("✅ Prediksi selesai dan disimpan di hasil_prediksi.csv")
