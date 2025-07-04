# Bonus Question: Machine Learning/AI with Decision Tree
Description: The government aims to predict investment attractiveness ("High", "Medium", "Low") for new projects based on features like GDP_Growth, CO2_Reduction, and Investment_Cost.

📌Task:

- Merge Economic_Dataset.xlsx, Environmental_Dataset.xlsx, and Financial_Dataset.xlsx
- Use scikit-learn to build a Decision Tree Classifier with Daya_Tarik_Investasi as the target.
- Train the model, evaluate its accuracy, and predict the attractiveness of a new project (e.g., GDP_Growth=5.0, CO2_Reduction=70000, Investment_Cost=150).

✔️Jawaban:

```

import pandas as pd
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

Merged Data Head:
        Project_ID  GDP_Growth  Interest_Rate  Bond_Yield  \
0    PLTS-NTT-001         4.5            4.2         5.1   
1  PLTM-SUMUT-001         5.2            3.8         4.8   
2  PLTS-JATIM-001         6.0            0.0         5.0   
3   PLTM-KALB-001         4.8            4.1         5.2   
4   PLTS-SULS-001         5.5            0.0         4.9   

                               Konteks_Ekonomi Daya_Tarik_Investasi  \
0  Sumba: pertumbuhan rendah, pariwisata hijau          Medium: 💵💵💵   
1               Tapanuli: ekonomi agro, stabil           High: 💵💵💵💵   
2         Surabaya: pasar besar, industri kuat          High: 💵💵💵💵💵   
3    Kalbar: ekonomi perkebunan, sedang tumbuh          Medium: 💵💵💵   
4     Makassar: hub ekonomi, pendidikan tinggi           High: 💵💵💵💵   

   CO2_Reduction  Energy_Output  Environmental_Risk_Index  \
0          75000          25000                        45   
1          30000          10000                        60   
2          90000          30000                        30   
3          35000          12000                        55   
4          60000          20000                        40   

                                 Konteks_Lingkungan Peringkat_Dampak  \
0  Sumba: radiasi matahari tinggi, rawan kekeringan       High: 🌿🌿🌿🌿   
1        Tapanuli: banjir musiman, debit air stabil      Medium: 🌿🌿🌿   
2         Surabaya: risiko rendah, efisiensi tinggi      High: 🌿🌿🌿🌿🌿   
3         Kalbar: rawan banjir, hutan lindung dekat      Medium: 🌿🌿🌿   
4             Makassar: cuaca stabil, risiko sedang       High: 🌿🌿🌿🌿   

   Investment_Cost  Revenue_Stream  Debt_Ratio  Payment_Delay  \
0           150.00            12.5        0.65             30   
1            80.00             6.8        0.55             15   
2           200.23            18.0        0.70             45   
3            90.00             7.2        0.60             20   
4           125.50            10.0        0.50             10   

                                      Konteks_Proyek    Status_Rank  
0  PLTS di Sumba, biaya logistik tinggi, pendanaa...  Medium: ★★★☆☆  
1      PLTM di Tapanuli, akses mudah ke jaringan PLN     Low: ★★☆☆☆  
2    PLTS besar di Surabaya, permintaan pasar tinggi    High: ★★★★☆  
3     PLTM di Kalimantan Barat, tantangan lahan adat  Medium: ★★★☆☆  
4      PLTS di Makassar, efisiensi tinggi distribusi     Low: ★☆☆☆☆  

Merged Data Info:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 17 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Project_ID                10 non-null     object 
 1   GDP_Growth                10 non-null     float64
 2   Interest_Rate             10 non-null     float64
 3   Bond_Yield                10 non-null     float64
 4   Konteks_Ekonomi           10 non-null     object 
 5   Daya_Tarik_Investasi      10 non-null     object 
 6   CO2_Reduction             10 non-null     int64  
 7   Energy_Output             10 non-null     int64  
 8   Environmental_Risk_Index  10 non-null     int64  
 9   Konteks_Lingkungan        10 non-null     object 
 10  Peringkat_Dampak          10 non-null     object 
 11  Investment_Cost           10 non-null     float64
 12  Revenue_Stream            10 non-null     float64
 13  Debt_Ratio                10 non-null     float64
 14  Payment_Delay             10 non-null     int64  
 15  Konteks_Proyek            10 non-null     object 
 16  Status_Rank               10 non-null     object 
dtypes: float64(6), int64(4), object(7)
memory usage: 1.5+ KB

LabelEncoder classes (numerical mapping): ['High: 💵💵💵💵', 'High: 💵💵💵💵💵', 'Low: 💵💵', 'Medium: 💵💵💵']
Example of encoded target values:
  Daya_Tarik_Investasi  Daya_Tarik_Investasi_Encoded
0          Medium: 💵💵💵                             3
1           High: 💵💵💵💵                             0
2          High: 💵💵💵💵💵                             1
3          Medium: 💵💵💵                             3
4           High: 💵💵💵💵                             0

Warning: Could not use stratify due to small class sizes or single instance class. Splitting without stratification. Error: The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2.

Training set shape (X_train): (8, 3)
Testing set shape (X_test): (2, 3)
Training target distribution:
Daya_Tarik_Investasi_Encoded
3    0.500
0    0.250
2    0.125
1    0.125
Name: proportion, dtype: float64
Testing target distribution:
Daya_Tarik_Investasi_Encoded
1    0.5
0    0.5
Name: proportion, dtype: float64

Decision Tree Classifier trained successfully.

Model Accuracy on Test Set: 0.50

Features of new project for prediction: {'GDP_Growth': 5.0, 'CO2_Reduction': 70000.0, 'Investment_Cost': 150.0}
Predicted Investment Attractiveness: Medium: 💵💵💵
'
💡Analisis:
