# Green Finance Data Analysis

Repositori ini menyajikan serangkaian analisis data yang berfokus pada proyek-proyek energi hijau, khususnya di Indonesia. Analisis ini dirancang untuk memberikan wawasan mendalam kepada para pemangku kepentingan, seperti pemerintah, investor, dan pengembang proyek, sehingga memungkinkan mereka untuk membuat keputusan yang terinformasi dan berbasis data.

**Disusun oleh Kelompok II**

---

|Nama|	No Absen|
|-|-|
|Agus Iskandar Darmawan|	09.000.DB2025|
|Gunawan|	10.005.DB2025|
|M. Sandi Firmansyah|	10.006.DB2025|

---

# 📖Pendahuluan
## 📝Latar Belakang

Sektor energi hijau memainkan peran krusial dalam mitigasi perubahan iklim dan pencapaian pembangunan berkelanjutan. Berbagai inisiatif dan proyek terus digalakkan untuk mengurangi emisi karbon, meningkatkan efisiensi energi, dan mendorong penggunaan sumber energi terbarukan. Namun, keberhasilan proyek-proyek ini sangat bergantung pada pemahaman mendalam tentang berbagai aspek, termasuk dampak lingkungan, kelayakan finansial, dan implikasi sosial di area proyek.

Data yang terfragmentasi seringkali menjadi tantangan dalam pengambilan keputusan yang efektif. Informasi mengenai pengurangan CO2, biaya investasi, tingkat risiko lingkungan, aliran pendapatan, status lahan, dan potensi konflik sosial tersebar di berbagai dataset. Oleh karena itu, diperlukan pendekatan yang sistematis untuk mengintegrasikan dan menganalisis data ini guna memperoleh gambaran komprehensif yang dapat mendukung kebijakan pemerintah dan strategi investasi yang lebih baik.

Proyek ini bertujuan untuk mengatasi tantangan tersebut dengan menyediakan kerangka analisis data yang terstruktur. Fokus utama adalah pada pengintegrasian berbagai dataset untuk mengevaluasi efisiensi proyek, mengidentifikasi pola, mengelola risiko, dan bahkan memprediksi daya tarik investasi.

## 🎯Tujuan

- **Integrasi Data**: Menggabungkan berbagai dataset (lingkungan, keuangan, sosial, ekonomi, dan geospasial) berdasarkan `Project_ID` untuk menciptakan pandangan data yang holistik.

- **Analisis Efisiensi dan Risiko:** Mengevaluasi efisiensi pengurangan CO2 per unit investasi, mengidentifikasi risiko sosial terkait status lahan dan konflik, dan menganalisis faktor-faktor yang memengaruhi daya tarik investasi.

- **Pengembangan Alat Analisis:** Membuat fungsi dan script yang dapat digunakan kembali untuk perhitungan metrik kunci dan pemfilteran data, termasuk implementasi penanganan kesalahan (error handling) untuk kekokohan.

- **Aplikasi Machine Learning:** Membangun model machine learning, khususnya Decision Tree Classifier, untuk memprediksi daya tarik investasi berdasarkan fitur-fitur yang relevan.

## 🔎Ruang Lingkup

Notebook Jupyter dalam repositori ini (`notebooks/Green_Finance_Data-Analysis.ipynb`) terstruktur menjadi beberapa bagian, masing-masing menangani pertanyaan analitis spesifik yang mencakup konsep pemrograman fundamental hingga lanjutan, seperti:

- **Pernyataan Kondisional (If-Else) dan Operasi Aritmatika:** Menghitung efisiensi pengurangan CO2 dan mengkategorikannya.

- **Perulangan `for` dan Daftar (Lists):** Menghitung rata-rata pengurangan CO2 untuk jenis proyek tertentu.

- **Perulangan `while` dan Input Pengguna:** Membangun alat interaktif untuk memeriksa status proyek.

- **Kamus (Dictionaries) dan Pemfilteran Kondisional:** Mengidentifikasi proyek dengan kombinasi daya tarik investasi tinggi dan konflik sosial rendah.

- **Fungsi dan Aritmatika:** Menghitung total investasi berdasarkan kriteria efisiensi lokasi.

- **Modul dan Penanganan Kesalahan:** Mengembangkan fungsi yang dapat digunakan kembali dengan penanganan ZeroDivisionError.

- **Penanganan Kesalahan dalam Perulangan:** Mengelola data yang hilang atau tidak valid saat menghitung rata-rata energy output.

- **Machine Learning (Bonus):** Memprediksi daya tarik investasi menggunakan Decision Tree Classifier.

Melalui analisis ini, diharapkan dapat memberikan fondasi yang kuat untuk evaluasi proyek energi hijau yang lebih efektif dan mendukung transisi Indonesia menuju masa depan energi yang lebih berkelanjutan.

# ✍🏻 Pembahasan
## Question 1: Conditional Statements (If-Else) and Arithmetic Operations 

Description: The government seeks to identify PLTS projects with high CO2 reduction efficiency per unit of investment, calculated as CO2 reduction per million rupiah.

📌Task:

- Merge Environmental_Dataset.xlsx and Financial_Dataset.xlsx using Project_ID.
- For PLTS projects (Project_ID starts with "PLTS"), compute the ratio: CO2_Reduction / (Investment_Cost * 1_000_000).
- Use if-else to classify the ratio as "High" (≥ 0.5 tons CO2e/million Rp) or "Low"(< 0.5).
- Display results as: "Project_ID: Ratio (Category)" using f-strings.

✔️Jawaban:

```

# import pandas ibrary
import pandas as pd

# read the Environmental_Dataset
df_Env = pd.read_excel('Data/Environmental_Dataset.xlsx')

# read the Financial_Dataset
df_Fin = pd.read_excel('Data/Financial_Dataset.xlsx')

# merge the datasets by Project_Id field and merge all the columns
df_merged = pd.merge( df_Env, df_Fin, on='Project_ID', how='outer' )

# call the row to use
for index, row in df_merged.iterrows():

    # calculate the CO2 reduction efficiency per million investment the PLTS Project
    if row['Project_ID'].startswith('PLTS'):
        ratio = (row['CO2_Reduction']) / (row['Investment_Cost'] * 1000000)

        # print the ratio category
        if ratio >= 0.5:
            print(f'{row['Project_ID']}: {ratio} (High)')
        else:
            print(f'{row['Project_ID']}: {ratio} (Low)')

```

📈 Output:

![output 1](https://github.com/Agus-Iskandar-D/Green-Finance-Data-Analysis/blob/main/Asset/output%201.png)

💡 Analisis:

Projek PLTS memiliki efisiensi pengurangan karbon (CO2 Reduction) per satu juta nilai investasi (per unit investasi) rendah (low). Artinya perlu ada peningkatan pengurangan karbon setiap unit investasi agar projek bisa menjadi projek hijau.

## Question 2: For Loop and Lists

Description: The government needs the average CO2 reduction across PLTM projects to assess their collective environmental impact.

📌Task:

- Use Environmental_Dataset.xlsx.
- Create a list of CO2_Reduction values for PLTM projects (Project_ID starts with "PLTM").
- Use a for loop to calculate the total CO2 reduction and count of PLTM projects.
- Compute and display the average.

✔️Jawaban:

```

import pandas as pd


df_Env = pd.read_excel('Data/Environmental_Dataset.xlsx')

# make list CO_Reduction
PLTM_CO2_Red_List = []

for index, row in df_Env.iterrows():
    Project_ID = row['Project_ID']
    CO2_Reduction = row ['CO2_Reduction']

    # make list value Project_ID starts with "PLTM"
    if isinstance(Project_ID, str) and Project_ID.startswith("PLTM"):
        PLTM_CO2_Red_List.append(CO2_Reduction)
    
# calculate the average
total_CO2_reduction = 0
count_CO2_reduction = 0
for CO2_Reduction_Value in PLTM_CO2_Red_List:
    total_CO2_reduction += CO2_Reduction_Value
    count_CO2_reduction += 1
    average_CO2_reduction = total_CO2_reduction / count_CO2_reduction

# print the average
print(f"Average CO2 Reduction for PLTM Projects:{average_CO2_reduction} tons CO2e")

```

📈 Output:

![output 2](https://github.com/Agus-Iskandar-D/Green-Finance-Data-Analysis/blob/main/Asset/output%202.png)

💡 Analisis:

Projek PLTM memiliki Rata-rata CO2 Reduction sebesar 34.600 ton CO2e. 

## Question 3: While Loop and User Input

Description: The government requires a tool to check land status and social conflict levels by entering Project_IDs.

📌Task:

- Use Social_Dataset.xlsx.
- Write a program using a while loop to prompt for Project_ID until "DONE" is entered.
- For valid Project_IDs, display Land_Status and Tingkat_Konflik.
- For invalid Project_IDs, show "Project not found".

✔️Jawaban:

```

import pandas as pd

# Load the dataset
df_Soc = pd.read_excel('Data/Social_Dataset.xlsx')

# Make a dictionary to store project data for quick lookup
social_data_dict = {}

# Populate the dictionary from the DataFrame
for index, row in df_Soc.iterrows():
    # Ensure Project_ID is stripped, converted to string, and uppercase for consistent lookup
    project_id = row['Project_ID']
    social_data_dict[project_id] = {
        # Use consistent key names for dictionary access (matching the DataFrame column names)
        'Land_Status': row['Land_Status'],
        'Tingkat_Konflik': row['Tingkat_Konflik']
    }

# Start the while loop to continuously prompt for Project_ID
while True:
    # Get input from the user
    # This makes the input case-insensitive for 'DONE' and Project_IDs
    project_id_input = input("\nEnter Project_ID (or DONE to finish): ").strip().upper()
    # Check if the user wants to exit
    if project_id_input == "DONE":
        print("Done, goodbye!")
        break # Exit the while loop

    # Check if the entered Project_ID exists in the dictionary
    # Corrected: Use social_data_dict for lookup, not Project_ID variable
    if project_id_input in social_data_dict:
        # Retrieve the Land_Status and Tingkat_Konflik from the dictionary
        # Corrected: Access data from social_data_dict
        data = social_data_dict[project_id_input]
        land_status = data["Land_Status"]
        tingkat_konflik = data["Tingkat_Konflik"]

        # Display the retrieved information
        print(f"{project_id_input} - Land Status: {land_status} - Tingkat Konflik: {tingkat_konflik}")
    else:
        # Inform the user if the Project_ID is not found
        print(f"Project '{project_id_input}' not found.")

```

📈 Output:

![output 3](https://github.com/Agus-Iskandar-D/Green-Finance-Data-Analysis/blob/main/Asset/output%203.png)

💡 Analisis:

Dengan aplikasi command prompt ini bisa diketahui status lahan dan tingkat konflik dari projek, dengan memasukan `Project_ID`.

## Question 4: Dictionary and Conditional Filtering

Description: The government seeks projects with high investment attractiveness and low social conflict to minimise risks.

📌Task:

- Merge Economic_Dataset.xlsx and Social_Dataset.xlsx using Project_ID.
- Create a dictionary with Project_ID as keys and a tuple (Daya_Tarik_Investasi,Tingkat_Konflik) as values.
- Use a for loop with if to filter projects where Daya_Tarik_Investasi == "High" and Tingkat_Konflik == "Low".
- Display the filtered Project_IDs

  
✔️Jawaban:

```

import pandas as pd

# Load the datasets
df_econ = pd.read_excel('Data/Economic_Dataset.xlsx')
df_soc = pd.read_excel('Data/Social_Dataset.xlsx')

# Merge the two DataFrames on 'Project_ID'
# A 'left' merge ensures all projects from the economic dataset are considered,
# and social data is added if available.
# 'inner' merge would only include projects present in BOTH datasets.
merged_df = pd.merge(df_econ, df_soc, on='Project_ID', how='inner')
# Create a dictionary with Project_ID as keys and (Daya_Tarik_Investasi, Tingkat_Konflik) as values
project_attractiveness_conflict = {}
for index, row in merged_df.iterrows():
    project_id = row['Project_ID']
    daya_tarik_investasi = row['Daya_Tarik_Investasi']
    tingkat_konflik = row['Tingkat_Konflik']
    project_attractiveness_conflict[project_id] = (daya_tarik_investasi, tingkat_konflik)

# List to store filtered Project_IDs
filtered_project_ids = []

# Filter projects where Daya_Tarik_Investasi == "High" and Tingkat_Konflik == "Low"
for project_id, (daya_tarik, tingkat_konflik) in project_attractiveness_conflict.items():
    if daya_tarik.startswith("High") and tingkat_konflik.startswith("Low"):
        filtered_project_ids.append(project_id)
# Display the filtered Project_IDs
if filtered_project_ids:
    print("\nProjects with High Investment Attractiveness and Low Social Conflict:")
    for project_id in filtered_project_ids:
        print(f"- {project_id}")
else:
    print("\nNo projects found matching the criteria (High Investment Attractiveness and Low Social Conflict).")

```

📈 Output:

![output 4](https://github.com/Agus-Iskandar-D/Green-Finance-Data-Analysis/blob/main/Asset/output%204.png)

💡 Analisis:

Menampilkan projek dengan tingkat kemenarikan investasi tinggi dengan social konflik yang rendah. Dari data ini, kita akan tahu projek mana yang berpotensi untuk mendatangkan investor.

## Question 5: Functions and Arithmetic

Description: The government needs to calculate the total investment for projects with high location efficiency.

📌Task:

- Define a function calculate_total_investment that takes a list of Project_IDs and merged data from Geospatial_Dataset.xlsx and Financial_Dataset.xlsx.
- Use a for loop to sum Investment_Cost for projects where Efisiensi_Lokasi == "High".
- Return and display the total

✔️Jawaban:

```

import pandas as pd

# Load the new datasets
df_geo = pd.read_excel('Data/Geospatial_Dataset.xlsx')
df_fin = pd.read_excel('Data/Financial_Dataset.xlsx')

# Merge the geospatial and financial DataFrames on 'Project_ID'
# An 'inner' merge is used to ensure we only consider projects present in both datasets
merged_df_geo_fin = pd.merge(df_geo, df_fin, on='Project_ID', how='inner')

def calculate_total_investment(merged_df_geo_fin) -> float:
    total_investment = 0.0
    high_efficiency_projects_found = False

    # Iterate through the rows of the merged DataFrame
    for index, row in merged_df_geo_fin.iterrows():
        # Ensure 'Efisiensi_Lokasi' is treated as a string and stripped for comparison
        efficiency = str(row['Efisiensi_Lokasi']).strip()
        
        # Ensure 'Investment_Cost' is a numeric type for summation
        # 'errors='coerce'' will turn non-numeric values into NaN
        investment_cost = pd.to_numeric(row['Investment_Cost'], errors='coerce')

        # Check if Efisiensi_Lokasi is "High" and Investment_Cost is a valid number
        if efficiency.startswith("High"):
            total_investment += investment_cost
            high_efficiency_projects_found = True

    if not high_efficiency_projects_found:
        print("No projects with 'High' location efficiency found in the dataset for investment calculation.")

    return total_investment

# Calculate the total investment for projects with high location efficiency
total_investment_high_efficiency = calculate_total_investment(merged_df_geo_fin)

# Display the total investment
print(f"\nTotal Investment for Projects with High Location Efficiency: {total_investment_high_efficiency} billion rupiah")

```

📈 Output:

![output 5](https://github.com/Agus-Iskandar-D/Green-Finance-Data-Analysis/blob/main/Asset/output%205.png)

💡 Analisis:
Hasil perhitungan menunjukan jumlah investasi dari projek yang memiliki efisiensi lokasi yang tinggai sebesar 955,73 miliar rupiah.

## Question 6: Modules and Error Handling

Description: The government requires a reusable tool to compute CO2 reduction efficiency with error handling.

📌Task:

- Create a module green_analysis.py with a function compute_co2_efficiency that takes CO2_Reduction and Investment_Cost as parameters.
- Use try-except to handle ZeroDivisionError (if Investment_Cost is 0), returning "Cannot compute" if an error occurs.
- Otherwise, compute and return the ratio: CO2_Reduction / (Investment_Cost * 1_000_000).
- In the main script, import the module and test it on three projects.

✔️Jawaban:

- modul yang berisi fungsi untuk menghitung efisiensi CO2 

```

def compute_co2_efficiency(co2_reduction: float, investment_cost: float) -> float | str:
    try:
        # Ensure investment_cost is treated as a number.
        # Convert to float and handle potential non-numeric inputs gracefully.
        numeric_investment_cost = float(investment_cost)

        if numeric_investment_cost == 0:
            # Explicitly handle division by zero for clarity
            return "Cannot compute: Investment Cost is zero."
        else:
            # Compute the ratio. Investment_Cost is assumed to be in millions,
            # so multiply by 1,000,000 to get the actual cost in the denominator.
            efficiency = co2_reduction / (numeric_investment_cost * 1000000)
            return efficiency
    except ValueError:
        # Handle cases where investment_cost cannot be converted to a float
        return "Cannot compute: Invalid Investment Cost (not a number)."
    except Exception as e:
        # Catch any other unexpected errors during computation
        return f"Cannot compute: An unexpected error occurred - {e}"

```

- Menggunakan module untuk tiga projek dan data sintetis dengan data invalid dan negatif

```

from green_analysis import compute_co2_efficiency
import pandas as pd

# load dataset
df_env = pd.read_excel('Data/Environmental_Dataset.xlsx')
df_fin = pd.read_excel('Data/Financial_Dataset.xlsx')

# Merge the two DataFrames on 'Project_ID'
# Use an 'inner' merge to ensure we only consider projects present in both datasets
merged_projects_df = pd.merge(df_env, df_fin, on='Project_ID', how='inner')

# Create a dictionary with Project_ID as keys and (CO2_Reduction, Investment_Cost) as values
# This will be used to test the compute_co2_efficiency function
projects_for_testing = {}
selected_projects_df = merged_projects_df.head(3) 

for index, row in selected_projects_df.iterrows():
    project_id = str(row['Project_ID']).strip().upper() # Standardize Project_ID
    co2_reduction = row['CO2_Reduction']
    investment_cost = row['Investment_Cost']
    projects_for_testing[project_id] = (co2_reduction, investment_cost)

# Add synthetic projects for testing the error handling
projects_for_testing["TEST_ZERO_INV"] = (100000.0, 0.0)
projects_for_testing["TEST_INVALID_INV"] = (50000.0, "N/A")
projects_for_testing["TEST_NEGATIVE_CO2"] = (-10000.0, 50000.0) # Added for new error handling test

print("\nProjects selected for testing (including synthetic cases):")
for project_id, data in projects_for_testing.items():
    print(f"  {project_id}: CO2_Reduction={data[0]}, Investment_Cost={data[1]}")

# Iterate through the created dictionary and test the function for each project
if not projects_for_testing:
    print("\nNo projects available for testing after merging datasets and selection.")
else:
    print("\n--- Testing CO2 Efficiency for Selected Projects ---")
    for project_id, (co2_red, inv_cost) in projects_for_testing.items():
        print(f"\nTesting {project_id} (CO2 Red: {co2_red}, Inv Cost: {inv_cost}):")
        efficiency = compute_co2_efficiency(co2_red, inv_cost)

        # Format output based on whether the result is a float or a string (error message)
        if isinstance(efficiency, float):
            print(f"  CO2 Reduction Efficiency: {efficiency:.10f}")
        else:
            print(f"  CO2 Reduction Efficiency: {efficiency}")

```

📈 Output:

![output 6](https://github.com/Agus-Iskandar-D/Green-Finance-Data-Analysis/blob/main/Asset/output%206.png)

💡 Analisis:

Fungsi dan modul yang digunakan memperpendek skrip. Modul dan fungsi yang dibuat bisa digunakan kembali kapan pun.

## Question 7: Error Handling in Loops

Description: The government needs to calculate the average energy output of selected projects, handling missing data.

📌Task:

- Create a list of Project_IDs to analyse.
- Use a for loop with try-except to process Energy_Output from Environmental_Dataset.xlsx, catching KeyError for missing Project_IDs.
- Sum valid Energy_Output values and count valid projects.
- Compute and display the average.

✔️Jawaban:

```

import pandas as pd

# load dataset
df_Env = pd.read_excel('Data/Environmental_Dataset.xlsx')

# create a list of Project_ID
Project_ID_List = []

for index, row in df_Env.iterrows():
    Project_ID = row['Project_ID']
    Project_ID_List.append(Project_ID)


# Make first value for iteration
total_energy_output = 0
valid_projects_count = 0
missing_projects = []
invalid_outputs = []

print("Processing energy output for selected projects:\n")

# Use a for loop with try-except to process Energy_Output
for project_id in Project_ID_List:
    try:
        # Attempt to find the project ID in the DataFrame
        # Use .loc for more explicit row and column selection
        # This will return a Series if found, or an empty Series if not
        project_row = df_Env.loc[df_Env['Project_ID'] == project_id]

        if not project_row.empty:
            # Project ID found, now get the energy output
            energy_output = project_row['Energy_Output'].iloc[0] # .iloc[0] to get the scalar value

            # Check for NaN values (missing data within existing projects)
            if pd.isna(energy_output):
                print(f"Warning: Project ID '{project_id}' found, but has missing (NaN) energy output. Skipping.")
                invalid_outputs.append(project_id)
                continue # Skip to the next project in the loop
            else:
                total_energy_output += energy_output
                valid_projects_count += 1
                print(f"Project ID '{project_id}': Energy Output = {energy_output}")
        else:
            # Project ID not found in the DataFrame
            print(f"Error: Project ID '{project_id}' not found in the dataset. Skipping.")
            missing_projects.append(project_id)

    except Exception as e:
        # Catch any other unexpected errors during processing
        print(f"An unexpected error occurred for Project ID '{project_id}': {e}. Skipping.")

print("\n--- Summary ---")

# Compute and display the average.
if valid_projects_count > 0:
    average_energy_output = total_energy_output / valid_projects_count
    print(f"Total valid energy output: {total_energy_output} kWh")
    print(f"Number of valid projects processed: {valid_projects_count}")
    print(f"Average energy output: {average_energy_output} kWh")
else:
    print("No valid projects were processed to calculate an average.")

```

📈 Output:

![output 7](https://github.com/Agus-Iskandar-D/Green-Finance-Data-Analysis/blob/main/Asset/output%207.png)

💡 Analisis:
Rata-rata energy yang dikeluar atau digunakan adalah sebesar 19.600 kWh

## Bonus Question: Machine Learning/AI with Decision Tree

Description: The government aims to predict investment attractiveness ("High", "Medium", "Low") for new projects based on features like GDP_Growth, CO2_Reduction, and Investment_Cost.

📌Task:

- Merge Economic_Dataset.xlsx, Environmental_Dataset.xlsx, and Financial_Dataset.xlsx
- Use scikit-learn to build a Decision Tree Classifier with Daya_Tarik_Investasi as the target.
- Train the model, evaluate its accuracy, and predict the attractiveness of a new project (e.g., GDP_Growth=5.0, CO2_Reduction=70000, Investment_Cost=150).


✔️Jawaban:

Klik: [Jawaban Bonus Question bisa baca disini](https://github.com/Agus-Iskandar-D/Green-Finance-Data-Analysis/blob/Bonus-Question-Sklearn/README.md)

