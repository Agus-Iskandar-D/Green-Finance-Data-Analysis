# Bonus Question: Machine Learning/AI with Decision Tree
Description: The government aims to predict investment attractiveness ("High", "Medium", "Low") for new projects based on features like GDP_Growth, CO2_Reduction, and Investment_Cost.

📌Task:

- Merge Economic_Dataset.xlsx, Environmental_Dataset.xlsx, and Financial_Dataset.xlsx
- Use scikit-learn to build a Decision Tree Classifier with Daya_Tarik_Investasi as the target.
- Train the model, evaluate its accuracy, and predict the attractiveness of a new project (e.g., GDP_Growth=5.0, CO2_Reduction=70000, Investment_Cost=150).

✔️Jawaban:

Pertanyaan bonus ini membahas dasar-dasar machine learning. Ini melibatkan:

- Persiapan Data: Menggabungkan beberapa dataset dan memilih fitur yang relevan serta variabel target.
- Pelatihan Model: Menggunakan `DecisionTreeClassifier` dari `scikit-learn` untuk melatih model. Ini biasanya melibatkan pembagian data menjadi set pelatihan dan pengujian, penanganan fitur kategorikal (misalnya, dengan one-hot encoding), dan pemasangan model.
- Evaluasi: Menilai kinerja model (misalnya, menggunakan skor akurasi).
- Prediksi: Menggunakan model yang telah dilatih untuk memprediksi daya tarik investasi dari proyek baru yang belum pernah dilihat.

Berikut skripnya:

```

import pandas as pd
Bonus-Question-Sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
import os

df_econ = pd.read_excel('Data/Economic_Dataset.xlsx')
df_env = pd.read_excel('Data/Environmental_Dataset.xlsx')
df_fin = pd.read_excel('Data/Financial_Dataset.xlsx')

merged_df = pd.merge(df_econ, df_env, on='Project_ID', how='inner')
merged_df = pd.merge(merged_df, df_fin, on='Project_ID', how='inner')

print("Merged Data Head:\n", merged_df.head())
print("\nMerged Data Info:\n")
merged_df.info()

# Define features (X) and target (y)
features = ['GDP_Growth', 'CO2_Reduction', 'Investment_Cost']
target = 'Daya_Tarik_Investasi'

# Select relevant columns and drop rows with any missing values in these columns
# This ensures a clean dataset for model training.
df_ml = merged_df[features + [target]].dropna()

# Encode the categorical target variable ('High', 'Medium', 'Low') into numerical format.
# LabelEncoder assigns numerical labels alphabetically by default.
# For example: High=0, Low=1, Medium=2
le = LabelEncoder()
df_ml['Daya_Tarik_Investasi_Encoded'] = le.fit_transform(df_ml[target])

print(f"\nLabelEncoder classes (numerical mapping): {list(le.classes_)}")
print(f"Example of encoded target values:\n{df_ml[[target, 'Daya_Tarik_Investasi_Encoded']].head()}")

X = df_ml[features]
y = df_ml['Daya_Tarik_Investasi_Encoded']

# 2. Splitting: Use train_test_split to divide data into training (80%) and testing (20%) sets.
# random_state ensures reproducibility of the split.
# stratify=y ensures that the proportion of target classes is maintained in both train and test sets,
# which is important for imbalanced datasets.
try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
except ValueError as e:
    # This might occur if one of the classes has too few samples to be split proportionally
    print(f"\nWarning: Could not use stratify due to small class sizes or single instance class. Splitting without stratification. Error: {e}")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


print(f"\nTraining set shape (X_train): {X_train.shape}")
print(f"Testing set shape (X_test): {X_test.shape}")
print(f"Training target distribution:\n{pd.Series(y_train).value_counts(normalize=True)}")
print(f"Testing target distribution:\n{pd.Series(y_test).value_counts(normalize=True)}")


# 3. Training: Fit the Decision Tree model using the training data.
dt_classifier = DecisionTreeClassifier(random_state=42) # random_state for reproducibility
dt_classifier.fit(X_train, y_train)

print("\nDecision Tree Classifier trained successfully.")

# 4. Evaluation: Compute accuracy on the test set using accuracy_score.
y_pred = dt_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Set: {accuracy:.2f}")

# 5. Prediction: Predict the class for new data.
new_project_data = pd.DataFrame([{
    'GDP_Growth': 5.0,
    'CO2_Reduction': 70000,
    'Investment_Cost': 150
}])

# Predict the encoded label for the new project
predicted_attractiveness_encoded = dt_classifier.predict(new_project_data)

# Inverse transform the encoded label to get the original categorical label
predicted_attractiveness = le.inverse_transform(predicted_attractiveness_encoded)

print(f"\nFeatures of new project for prediction: {new_project_data.iloc[0].to_dict()}")
print(f"Predicted Investment Attractiveness: {predicted_attractiveness[0]}")

```

📈Output:

![output bonus](https://github.com/Agus-Iskandar-D/Green-Finance-Data-Analysis/blob/main/Asset/output%20bonus.png)

💡Analisis:

Hasil Machine menunjukan bahwa datasetnya terlalu sedikit, namun jika tetap dilakukan training dihasilkan tingkat akurasi 0.5, dengan prediksi tingat kemenarikan untuk berinvestasi medium.

Ketika akurasi model Decision Tree pada data pengujian adalah 0.5 (atau 50%), itu berarti setengah dari prediksi model tersebut benar, dan setengahnya lagi sala akurasi 0.5 berarti model tidak lebih baik dari tebakan acak dan membutuhkan perbaikan signifikan.


