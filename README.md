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
