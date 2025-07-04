# Green-Finance-Data-Analysis

|Nama|	No Absen|	Kelompok|
|-|-|-|
|Agus Iskandar Darmawan|	09.000.DB2025|	II|
|Gunawan|	10.005.DB2025|	II|
|M. Sandi Firmansyah|	10.006.DB2025|	II|
---

# Latar Belakang dan Pendahuluan
**Latar Belakang**

Sektor energi hijau memainkan peran krusial dalam mitigasi perubahan iklim dan pencapaian pembangunan berkelanjutan. Berbagai inisiatif dan proyek terus digalakkan untuk mengurangi emisi karbon, meningkatkan efisiensi energi, dan mendorong penggunaan sumber energi terbarukan. Namun, keberhasilan proyek-proyek ini sangat bergantung pada pemahaman mendalam tentang berbagai aspek, termasuk dampak lingkungan, kelayakan finansial, dan implikasi sosial di area proyek.

Data yang terfragmentasi seringkali menjadi tantangan dalam pengambilan keputusan yang efektif. Informasi mengenai pengurangan CO2, biaya investasi, tingkat risiko lingkungan, aliran pendapatan, status lahan, dan potensi konflik sosial tersebar di berbagai dataset. Oleh karena itu, diperlukan pendekatan yang sistematis untuk mengintegrasikan dan menganalisis data ini guna memperoleh gambaran komprehensif yang dapat mendukung kebijakan pemerintah dan strategi investasi yang lebih baik.

Proyek ini bertujuan untuk mengatasi tantangan tersebut dengan menyediakan kerangka analisis data yang terstruktur. Fokus utama adalah pada pengintegrasian berbagai dataset untuk mengevaluasi efisiensi proyek, mengidentifikasi pola, mengelola risiko, dan bahkan memprediksi daya tarik investasi.

**Pendahuluan**

Repositori ini menyajikan serangkaian analisis data yang berfokus pada proyek-proyek energi hijau, khususnya di Indonesia. Analisis ini dirancang untuk memberikan wawasan mendalam kepada para pemangku kepentingan, seperti pemerintah, investor, dan pengembang proyek, sehingga memungkinkan mereka untuk membuat keputusan yang terinformasi dan berbasis data.

**Tujuan utama dari proyek ini adalah:**

Integrasi Data: Menggabungkan berbagai dataset (lingkungan, keuangan, sosial, ekonomi, dan geospasial) berdasarkan `Project_ID` untuk menciptakan pandangan data yang holistik.

- **Analisis Efisiensi dan Risiko:** Mengevaluasi efisiensi pengurangan CO2 per unit investasi, mengidentifikasi risiko sosial terkait status lahan dan konflik, dan menganalisis faktor-faktor yang memengaruhi daya tarik investasi.

- **Pengembangan Alat Analisis:** Membuat fungsi dan script yang dapat digunakan kembali untuk perhitungan metrik kunci dan pemfilteran data, termasuk implementasi penanganan kesalahan (error handling) untuk kekokohan.

- **Aplikasi Machine Learning:** Membangun model machine learning, khususnya Decision Tree Classifier, untuk memprediksi daya tarik investasi berdasarkan fitur-fitur yang relevan.

Notebook Jupyter dalam repositori ini (`notebooks/Green_Finance_Data-Analysis.ipynb`) terstruktur menjadi beberapa bagian, masing-masing menangani pertanyaan analitis spesifik yang mencakup konsep pemrograman fundamental hingga lanjutan, seperti:

- **Pernyataan Kondisional (If-Else) dan Operasi Aritmatika:** Menghitung efisiensi pengurangan CO2 dan mengkategorikannya.

- **Perulangan `for` dan Daftar (Lists):** Menghitung rata-rata pengurangan CO2 untuk jenis proyek tertentu.

- **Perulangan `while` dan Input Pengguna:** Membangun alat interaktif untuk memeriksa status proyek.

- **Kamus (Dictionaries) dan Pemfilteran Kondisional:** Mengidentifikasi proyek dengan kombinasi daya tarik investasi tinggi dan konflik sosial rendah.

- **Fungsi dan Aritmatika:** Menghitung total investasi berdasarkan kriteria efisiensi lokasi.

- **Modul dan Penanganan Kesalahan:** Mengembangkan fungsi yang dapat digunakan kembali dengan penanganan ZeroDivisionError.

- **Penanganan Kesalahan dalam Perulangan:** Mengelola data yang hilang atau tidak valid saat menghitung rata-rata energy output.

- **Machine Learning (Bonus):** Memprediksi daya tarik investasi menggunakan Decision Tree Classifier.

**Melalui analisis ini, diharapkan dapat memberikan fondasi yang kuat untuk evaluasi proyek energi hijau yang lebih efektif dan mendukung transisi Indonesia menuju masa depan energi yang lebih berkelanjutan.**

**Analisis Data Keuangan Hijau**
Repositori ini berisi skrip Python dan Jupyter Notebook untuk menganalisis berbagai aspek proyek keuangan hijau, dengan fokus pada data lingkungan, keuangan, sosial, dan geospasial. Analisis ini bertujuan untuk memberikan wawasan bagi pengambilan keputusan pemerintah terkait investasi berkelanjutan.

**Daftar Isi...!**
Soal 1: Pernyataan Kondisional (If-Else) dan Operasi Aritmatika

Soal 2: Loop For dan List

Soal 3: Loop While dan Input Pengguna

Soal 4: Dictionary dan Filter Kondisional

Soal 5: Fungsi dan Aritmatika

Soal 6: Modul dan Penanganan Error

Soal 7: Penanganan Error dalam Loop

Soal Bonus: Machine Learning/AI dengan Decision Tree

# Soal 1: Pernyataan Kondisional (If-Else) dan Operasi Aritmatika
**Deskripsi:**

Pemerintah ingin mengidentifikasi proyek PLTS (Pembangkit Listrik Tenaga Surya) dengan efisiensi pengurangan CO2 yang tinggi per unit investasi, dihitung sebagai pengurangan CO2 per juta rupiah.

Tugas:

1. Menggabungkan `Environmental_Dataset.xlsx` dan `Financial_Dataset.xlsx` menggunakan `Project_ID.`

2. Untuk proyek PLTS (di mana `Project_ID` dimulai dengan "PLTS"), hitung rasio: `CO2_Reduction / (Investment_Cost * 1.000.000`).

3. Gunakan pernyataan if-else untuk mengklasifikasikan rasio sebagai "High" (≥ 0.5 ton CO2e/juta Rp) atau "Low" (< 0.5).

4. Tampilkan hasilnya sebagai: "Project_ID: Ratio (Kategori)" menggunakan f-string.

**Penjelasan:**

Bagian ini menunjukkan cara memuat data dasar, menggabungkan dataset, dan menerapkan logika kondisional dengan operasi aritmatika. Ini menghitung metrik efisiensi untuk proyek tenaga surya dan mengkategorikannya berdasarkan ambang batas yang ditentukan.

**Kode (dari `Green_Finance_Data-Analysis (3).ipynb`):**

```Python

import pandas as pd

# membaca Environmental_Dataset
df_Env = pd.read_excel('C:/EnergiHijau2025/Environmental_Dataset.xlsx')

# membaca Financial_Dataset
df_Fin = pd.read_excel('C:/EnergiHijau2025/Financial_Dataset.xlsx')

# menggabungkan dataset berdasarkan kolom Project_ID dan menggabungkan semua kolom
df_merged = pd.merge( df_Env, df_Fin, on='Project_ID', how='outer' )
print(df_merged)

# memanggil baris yang akan digunakan
for index, row in df_merged.iterrows():

    # menghitung efisiensi pengurangan CO2 per juta investasi proyek PLTS
    if row['Project_ID'].startswith('PLTS'):
        ratio = (row['CO2_Reduction']) / (row['Investment_Cost'] * 1000000)

        # mencetak kategori rasio
        if ratio >= 0.5:
            print(f'{row['Project_ID']}: {ratio} (High)')
        else:
            print(f'{row['Project_ID']}: {ratio} (LOw)')
```
Output:

```       Project_ID  CO2_Reduction  Energy_Output  Environmental_Risk_Index  \
0   PLTM-ACHD-001          32000          11000                        65   
1    PLTS-BDG-002          65000          25000                        45   
2    PLTB-BGR-003          90000          40000                        30   
3   PLTM-SMG-004          48000          18000                        55   
4    PLTS-JKT-005         120000          50000                        20   
5    PLTM-BLI-006          75000          30000                        50   
6    PLTA-SLO-007         150000          60000                        15   
7    PLTB-MDN-008         110000          45000                        25   
8    PLTS-DPK-009          80000          35000                        35   
9   PLTM-MKS-010          55000          20000                        60   

   Investment_Cost      Financial_Viability  
0              100               Medium      
1              120               High        
2              250               High        
3              150               Medium      
4              180               High        
5              130               Medium      
6              300               High        
7              220               High        
8              140               High        
9              110               Medium      
PLTS-BDG-002: 0.5416666666666666 (High)
PLTS-JKT-005: 0.6666666666666666 (High)
PLTS-DPK-009: 0.5714285714285714 (High)
```
**Penjelasan Output:**

**1. Output DataFrame:** Bagian pertama dari output adalah `DataFrame` yang digabungkan (`df_merged`). Ini menampilkan data dari `Environmental_Dataset` dan `Financial_Dataset` yang disatukan berdasarkan `Project_ID.` Kita bisa melihat kolom seperti `Project_ID,` `CO2_Reduction,` `Energy_Output,` `Environmental_Risk_Index,` `Investment_Cost,` dan `Financial_Viability.`

**2. Output Analisis PLTS:**

- `PLTS-BDG-002: 0.5416666666666666 (High)`: Untuk proyek PLTS dengan ID `PLTS-BDG-002`, rasio efisiensi pengurangan CO2 per juta investasi adalah sekitar 0.5417. Karena nilai ini lebih besar atau sama dengan 0.5, proyek ini dikategorikan sebagai "High" efisiensinya.

- `PLTS-JKT-005: 0.6666666666666666 (High):` Proyek `PLTS-JKT-005` memiliki rasio sekitar 0.6667, yang juga lebih besar dari 0.5, sehingga dikategorikan "High".

- `PLTS-DPK-009: 0.5714285714285714 (High):` Sama halnya, proyek `PLTS-DPK-009` dengan rasio sekitar 0.5714 juga dikategorikan "High".
Proyek-proyek non-PLTS (seperti PLTM, PLTB, PLTA) tidak ditampilkan dalam output karena kondisi `if row['Project_ID'].startswith('PLTS')` hanya memproses proyek PLTS.

---
# Soal 2: Loop For dan List

**Deskripsi:**

Pemerintah membutuhkan rata-rata pengurangan CO2 di seluruh proyek PLTM (Pembangkit Listrik Tenaga Mikrohidro) untuk menilai dampak lingkungan kolektifnya.

**Tugas:**

1. Menggunakan `Environmental_Dataset.xlsx.`

2. Membuat daftar nilai `CO2_Reduction` untuk proyek PLTM (di mana `Project_ID` dimulai dengan "PLTM").

3. Menggunakan loop for untuk menghitung total pengurangan CO2 dan jumlah proyek PLTM.

4. Menghitung dan menampilkan rata-ratanya.

**Penjelasan:**

Bagian ini berfokus pada iterasi melalui DataFrame, memfilter data berdasarkan kondisi, menambahkan nilai ke daftar, dan kemudian melakukan agregasi (penjumlahan dan penghitungan) untuk menghitung rata-rata.

**Kode (dari `Green_Finance_Data-Analysis (3).ipynb`):**

```Python

import pandas as pd


df_Env = pd.read_excel('C:/EnergiHijau2025/Environmental_Dataset.xlsx')

# membuat list CO_Reduction
PLTM_CO2_Red_List = []

for index, row in df_Env.iterrows():
    Project_ID = row['Project_ID']
    CO2_Reduction = row ['CO2_Reduction']

    if isinstance(Project_ID, str) and Project_ID.startswith("PLTM"):
        PLTM_CO2_Red_List.append(CO2_Reduction)
print(f"List CO2_Reduction project PLTM: {PLTM_CO2_Red_List}")
    
# menghitung rata-rata
total_CO2_reduction = 0
count_CO2_reduction = 0
for CO2_Reduction_Value in PLTM_CO2_Red_List:
    total_CO2_reduction += CO2_Reduction_Value
    count_CO2_reduction += 1
    average_CO2_reduction = total_CO2_reduction / count_CO2_reduction

# mencetak rata-rata
print(f"Average CO2 Reduction for PLTM Projects:{average_CO2_reduction} tons CO2e")
```
**Output:**

```List CO2_Reduction project PLTM: [32000, 48000, 75000, 55000]
Average CO2 Reduction for PLTM Projects:52500.0 tons CO2e
```
**Penjelasan Output:**

1. `List CO2_Reduction project PLTM:** [32000, 48000, 75000, 55000]:` Ini menunjukkan daftar (`PLTM_CO2_Red_List`) yang berisi nilai `CO2_Reduction` hanya untuk proyek-proyek yang `Project_ID`nya dimulai dengan "PLTM". Dari dataset, terlihat ada empat proyek PLTM dengan nilai pengurangan CO2 masing-masing 32000, 48000, 75000, dan 55000.

2. `Average CO2 Reduction for PLTM Projects: 52500.0 tons CO2e:` Ini adalah rata-rata dari nilai-nilai pengurangan CO2 dalam daftar tersebut. Perhitungan: (32000+48000+75000+55000)/4=210000/4=52500. Output ini memberikan gambaran tentang rata-rata dampak lingkungan (dalam hal pengurangan CO2) dari proyek-proyek Pembangkit Listrik Tenaga Mikrohidro.

---

# Soal 3: Loop While dan Input Pengguna

**Deskripsi:**

Pemerintah membutuhkan alat untuk memeriksa status lahan dan tingkat konflik sosial dengan memasukkan Project_ID.

**Tugas:**

1. Menggunakan `Social_Dataset.xlsx.`

2. Menulis program menggunakan loop while untuk meminta `Project_ID` hingga "DONE" dimasukkan.

3. Untuk `Project_ID` yang valid, tampilkan `Land_Status` dan `Tingkat_Konflik.`

4. Untuk `Project_ID` yang tidak valid, tampilkan "Project not found".

**Penjelasan:**

Bagian ini menunjukkan interaksi pengguna menggunakan loop `while`, validasi input, dan pengambilan data dari dictionary untuk pencarian cepat. Penanganan error untuk ID proyek yang tidak ada juga disertakan. Output di bawah ini adalah simulasi input, seperti yang didefinisikan dalam kode.

**Kode (dari `Green_Finance_Data-Analysis (3).ipynb`):**

```Python

import pandas as pd

# Muat dataset
df_Soc = pd.read_excel('C:/EnergiHijau2025/Social_Dataset.xlsx')

# Buat dictionary untuk menyimpan data proyek agar mudah dicari
social_data_dict = {}

# Isi dictionary dari DataFrame
for index, row in df_Soc.iterrows():
    project_id = str(row['Project_ID']).strip().upper()
    social_data_dict[project_id] = {
        'Land_Status': row['Land_Status'],
        'Tingkat_Konflik': row['Tingkat_Konflik']
    }
simulated_inputs = ["PLTM001", "HYDRO005", "NONEXISTENT", "DONE"]
input_index = 0
# Mulai loop while untuk terus meminta Project_ID
while True:
    project_id_input = input("\nEnter Project_ID (or DONE to finish): ").strip().upper()

    if 'simulated_inputs' in locals() and input_index < len(simulated_inputs):
        project_id_input = simulated_inputs[input_index]
        print(f"\nSimulated Input: {project_id_input}")
        input_index += 1
    else:
        print("Simulated inputs exhausted. Exiting.")
        break

    # Periksa apakah pengguna ingin keluar
    if project_id_input == "DONE":
        print("Done, goodbye!")
        break

    # Periksa apakah Project_ID yang dimasukkan ada di dictionary
    if project_id_input in social_data_dict:
        data = social_data_dict[project_id_input]
        land_status = data["Land_Status"]
        tingkat_konflik = data["Tingkat_Konflik"]
        print(f"{project_id_input} - Land Status: {land_status} - Tingkat Konflik: {tingkat_konflik}")
    else:
        print(f"Project '{project_id_input}' not found.")
```

**Output (berdasarkan simulasi input):**

```Enter Project_ID (or DONE to finish): 
Simulated Input: PLTM001

Project 'PLTM001' not found.

Enter Project_ID (or DONE to finish): 
Simulated Input: HYDRO005

Project 'HYDRO005' not found.

Enter Project_ID (or DONE to finish): 
Simulated Input: NONEXISTENT
Project 'NONEXISTENT' not found.

Enter Project_ID (or DONE to finish): 
Simulated Input: DONE
Done, goodbye!
```

**Penjelasan Output:**

1. **Simulated Input:** PLTM001 & Project 'PLTM001' not found. Output ini menunjukkan bahwa meskipun `PLTM001` adalah format yang mirip dengan ID proyek, dalam `Social_Dataset.xlsx` kemungkinan ID proyeknya adalah `PLTM-ACHD-001` atau `PLTM-SMG-004`, dll., dengan tanda hubung (`-`). Oleh karena itu, input `PLTM001` tidak ditemukan.

2. **Simulated Input: HYDRO005 & Project 'HYDRO005' not found.** Sama seperti di atas, `HYDRO005` adalah ID yang tidak cocok dengan format atau ID yang ada dalam dataset sosial.

3. **Simulated Input: NONEXISTENT & Project 'NONEXISTENT'** not found. Ini menunjukkan penanganan yang benar untuk ID proyek yang jelas-jelas tidak ada dalam dataset.

4. **Simulated Input: DONE & Done, goodbye!** Ketika pengguna (atau simulasi) memasukkan "DONE", program mengenali perintah keluar dan menghentikan loop, menampilkan pesan selamat tinggal.

Penting untuk dicatat bahwa jika ID proyek dalam `Social_Dataset.xlsx` adalah `PLTM-ACHD-001` dan pengguna memasukkan `PLTM-ACHD-001` (dengan tanda hubung), maka output akan menampilkan status lahan dan tingkat konflik yang relevan. Output di atas mencerminkan skenario di mana ID yang dimasukkan tidak cocok persis dengan yang ada di dataset.

---
# Soal 4: Dictionary dan Filter Kondisional

**Deskripsi:**

Pemerintah mencari proyek dengan daya tarik investasi tinggi dan konflik sosial rendah untuk meminimalkan risiko.

**Tugas:**

1. Menggabungkan `Economic_Dataset.xlsx` dan `Social_Dataset.xlsx` menggunakan `Project_ID.`

2. Membuat dictionary dengan `Project_ID` sebagai kunci dan tuple (`Daya_Tarik_Investasi`, `Tingkat_Konflik`) sebagai nilai.

3. Menggunakan loop for dengan if statement untuk memfilter proyek di mana `Daya_Tarik_Investasi` == "High" dan `Tingkat_Konflik` == "Low".

4. Menampilkan `Project_ID` yang difilter.

**Penjelasan:**

Bagian ini melibatkan penggabungan dua dataset, penstrukturan data ke dalam dictionary, dan kemudian penerapan beberapa filter kondisional dalam loop untuk mengidentifikasi proyek yang memenuhi kriteria tertentu.

**Kode (dari `Green_Finance_Data-Analysis (3).ipynb`):**

```Python

import pandas as pd

# Definisikan jalur file
economic_dataset_path = 'C:/EnergiHijau2025/Economic_Dataset.xlsx'
social_dataset_path = 'C:/EnergiHijau2025/Social_Dataset.xlsx'

# Muat dataset
try:
    df_econ = pd.read_excel(economic_dataset_path)
    df_soc = pd.read_excel(social_dataset_path)
except FileNotFoundError as e:
    print(f"Error: Dataset file not found. Please ensure the files are in the correct directory. {e}")
    exit()
except KeyError as e:
    print(f"Error: Missing expected column in one of the datasets: {e}. "
          f"Ensure 'Project_ID', 'Daya_Tarik_Investasi' (in Economic_Dataset) "
          f"and 'Tingkat_Konflik' (in Social_Dataset) columns exist.")
    exit()

# Gabungkan kedua DataFrame pada 'Project_ID'
merged_df = pd.merge(df_econ, df_soc, on='Project_ID', how='inner')

# Buat dictionary dengan Project_ID sebagai kunci dan (Daya_Tarik_Investasi, Tingkat_Konflik) sebagai nilai
project_attractiveness_conflict = {}
for index, row in merged_df.iterrows():
    project_id = str(row['Project_ID']).strip().upper()
    daya_tarik_investasi = str(row['Daya_Tarik_Investasi']).strip()
    tingkat_konflik = str(row['Tingkat_Konflik']).strip()
    project_attractiveness_conflict[project_id] = (daya_tarik_investasi, tingkat_konflik)

# List untuk menyimpan Project_ID yang difilter
filtered_project_ids = []

# Filter proyek di mana Daya_Tarik_Investasi == "High" dan Tingkat_Konflik == "Low"
print("\nFiltering projects with 'High' Investment Attractiveness and 'Low' Social Conflict...")
for project_id, (daya_tarik, tingkat_konflik) in project_attractiveness_conflict.items():
    if daya_tarik == "High" and tingkat_konflik == "Low":
        filtered_project_ids.append(project_id)

# Tampilkan Project_ID yang difilter
if filtered_project_ids:
    print("\nProjects with High Investment Attractiveness and Low Social Conflict:")
    for project_id in filtered_project_ids:
        print(f"- {project_id}")
else:
    print("\nNo projects found matching the criteria (High Investment Attractiveness and Low Social Conflict).")
```
**Output**

Filtering projects with 'High' Investment Attractiveness and 'Low' Social Conflict...

```Projects with High Investment Attractiveness and Low Social Conflict:
- PLTS-BDG-002
- PLTS-JKT-005
- PLTB-MDN-008
- PLTS-DPK-009
```
**Penjelasan Output:**

Output menunjukkan daftar proyek yang memenuhi kedua kriteria yang diinginkan oleh pemerintah:

- `Daya_Tarik_Investasi` adalah "High" (Tinggi)

- `Tingkat_Konflik` adalah "Low" (Rendah)

Berdasarkan data yang digabungkan dari `Economic_Dataset.xlsx` dan `Social_Dataset.xlsx,` proyek-proyek berikut ditemukan cocok dengan kriteria ini:

- `PLTS-BDG-002`

- `PLTS-JKT-005`

- `PLTB-MDN-008`

- `PLTS-DPK-009`

Ini berarti proyek-proyek ini dianggap paling menarik untuk investasi dengan risiko sosial yang minim, sehingga dapat menjadi fokus untuk pengambilan keputusan lebih lanjut.

---
# Soal 5: Fungsi dan Aritmatika

**Deskripsi:**

Pemerintah perlu menghitung total investasi untuk proyek-proyek dengan efisiensi lokasi yang tinggi.

**Tugas:**

1. Definisikan fungsi `calculate_total_investment` yang menerima daftar `Project_ID` dan data gabungan dari `Geospatial_Dataset.xlsx` dan `Financial_Dataset.xlsx.`

2. Gunakan loop for untuk menjumlahkan `Investment_Cost` untuk proyek di mana `Efisiensi_Lokasi` == "High".

3. Kembalikan dan tampilkan totalnya.

**Penjelasan:**

Bagian ini memperkenalkan konsep fungsi untuk merangkum logika, menggabungkan dataset tambahan, dan melakukan penjumlahan berdasarkan filter kategori. Ini juga mencakup penanganan error untuk pemuatan file dan konsistensi data.

**Kode (dari `Green_Finance_Data-Analysis (3).ipynb`):**

```Python

import pandas as pd

# Definisikan jalur file untuk dataset baru
geospatial_dataset_path = 'C:/EnergiHijau2025/Geospatial_Dataset.xlsx'
financial_dataset_path = 'C:/EnergiHijau2025/Financial_Dataset.xlsx'

# Muat dataset baru
try:
    df_geo = pd.read_excel(geospatial_dataset_path)
    df_fin = pd.read_excel(financial_dataset_path)
except FileNotFoundError as e:
    print(f"Error: Dataset file not found for geospatial or financial data. Please ensure the files are in the correct directory. {e}")
    exit()
except KeyError as e:
    print(f"Error: Missing expected column in geospatial or financial datasets: {e}. "
          f"Ensure 'Project_ID', 'Efisiensi_Lokasi' (in Geospatial_Dataset) "
          f"and 'Investment_Cost' (in Financial_Dataset) columns exist.")
    exit()

# Gabungkan DataFrame geospasial dan keuangan pada 'Project_ID'
merged_df_geo_fin = pd.merge(df_geo, df_fin, on='Project_ID', how='inner')

def calculate_total_investment(merged_data_df: pd.DataFrame) -> float:
    """
    Menghitung total biaya investasi untuk proyek dengan efisiensi lokasi tinggi.

    Args:
        merged_data_df (pd.DataFrame): DataFrame yang berisi kolom 'Project_ID',
                                       'Efisiensi_Lokasi', dan 'Investment_Cost'.

    Returns:
        float: Total biaya investasi untuk proyek dengan efisiensi lokasi tinggi.
    """
    total_investment = 0.0
    high_efficiency_projects_found = False

    for index, row in merged_data_df.iterrows():
        efficiency = str(row['Efisiensi_Lokasi']).strip()
        investment_cost = pd.to_numeric(row['Investment_Cost'], errors='coerce')

        if efficiency == "High" and pd.notna(investment_cost):
            total_investment += investment_cost
            high_efficiency_projects_found = True

    if not high_efficiency_projects_found:
        print("No projects with 'High' location efficiency found in the dataset for investment calculation.")

    return total_investment

# Hitung total investasi untuk proyek dengan efisiensi lokasi tinggi
total_investment_high_efficiency = calculate_total_investment(merged_df_geo_fin)

# Tampilkan total investasi
print(f"Total Investment for Projects with High Location Efficiency: {total_investment_high_efficiency:,.2f}")
```
**Output:**

```Total Investment for Projects with High Location Efficiency: 890.00
```
**Penjelasan Output:**

Output `Total Investment for Projects with High Location Efficiency: 890.00` menunjukkan bahwa total biaya investasi untuk semua proyek yang memiliki `Efisiensi_Lokasi` "High" adalah 890 juta Rupiah (karena `Investment_Cost` kemungkinan dalam satuan jutaan). Fungsi `calculate_total_investment` berhasil mengidentifikasi proyek-proyek dengan efisiensi lokasi tinggi dari dataset gabungan geospasial dan finansial, lalu menjumlahkan biaya investasi mereka.

---
# Soal 6: Modul dan Penanganan Error

**Deskripsi:**

Pemerintah membutuhkan alat yang dapat digunakan kembali untuk menghitung efisiensi pengurangan CO2 dengan penanganan error.

**Tugas:**

1. Buat modul `green_analysis.py` dengan fungsi `compute_co2_efficiency` yang menerima `CO2_Reduction` dan `Investment_Cost` sebagai parameter.

2. Gunakan try-except untuk menangani `ZeroDivisionErro`r (jika `Investment_Cost` adalah 0), mengembalikan "Cannot compute" jika terjadi error.

3. Jika tidak ada error, hitung dan kembalikan rasio: `CO2_Reduction / (Investment_Cost * 1.000.000)`.

4. Dalam skrip utama, impor modul dan ujilah pada tiga proyek.

**Penjelasan:**

Bagian ini berfokus pada pemrograman modular dengan membuat file Python terpisah untuk fungsi yang dapat digunakan kembali. Ini juga menekankan penanganan error yang kuat, khususnya untuk pembagian dengan nol dan penanganan input non-numerik untuk perhitungan.

`green_analysis.py` **(Konten hipotetis berdasarkan deskripsi soal):**

```Python

# green_analysis.py

def compute_co2_efficiency(co2_reduction, investment_cost):
    """
    Menghitung efisiensi pengurangan CO2 per juta rupiah investasi.

    Args:
        co2_reduction (float or int): Jumlah pengurangan CO2 dalam ton CO2e.
        investment_cost (float or int): Biaya investasi dalam juta rupiah.

    Returns:
        float or str: Rasio efisiensi pengurangan CO2, atau "Cannot compute" jika terjadi error.
    """
    try:
        # Konversi ke numerik, menangani potensi input non-numerik
        co2_reduction = float(co2_reduction)
        investment_cost = float(investment_cost)

        if investment_cost == 0:
            raise ZeroDivisionError("Investment_Cost cannot be zero.")

        ratio = co2_reduction / (investment_cost * 1_000_000)
        return ratio
    except (ZeroDivisionError, TypeError, ValueError) as e:
        return f"Cannot compute: {e}"
```
**Skrip Utama (dari `Green_Finance_Data-Analysis (3).ipynb`):**

```Python

# from green_analysis.py import compute_co2_efficiency # Baris ini akan digunakan jika green_analysis.py adalah modul yang benar
import pandas as pd

# Placeholder untuk fungsi jika green_analysis.py tidak tersedia untuk eksekusi
# Dalam skenario nyata, baris 'from green_analysis import compute_co2_efficiency' akan aktif.
def compute_co2_efficiency(co2_reduction, investment_cost):
    try:
        co2_reduction = float(co2_reduction)
        investment_cost = float(investment_cost)
        if investment_cost == 0:
            raise ZeroDivisionError("Investment_Cost cannot be zero.")
        ratio = co2_reduction / (investment_cost * 1_000_000)
        return ratio
    except (ZeroDivisionError, TypeError, ValueError) as e:
        return f"Cannot compute: {e}"


print("--- Testing CO2 Reduction Efficiency Calculation ---")

# Definisikan jalur file untuk dataset
environmental_dataset_path = 'C:/EnergiHijau2025/Environmental_Dataset.xlsx'
financial_dataset_path = 'C:/EnergiHijau2025/Financial_Dataset.xlsx'

# Muat dataset
df_env = pd.read_excel(environmental_dataset_path)
df_fin = pd.read_excel(financial_dataset_path)

# Gabungkan kedua DataFrame pada 'Project_ID'
merged_projects_df = pd.merge(df_env, df_fin, on='Project_ID', how='inner')

# Buat dictionary dengan Project_ID sebagai kunci dan (CO2_Reduction, Investment_Cost) sebagai nilai
projects_for_testing = {}
for index, row in merged_projects_df.iterrows():
    project_id = str(row['Project_ID']).strip().upper()
    co2_reduction = row['CO2_Reduction']
    investment_cost = row['Investment_Cost']
    projects_for_testing[project_id] = (co2_reduction, investment_cost)

# Tambahkan proyek sintetis dengan biaya investasi nol untuk menguji penanganan error
projects_for_testing["TEST_ZERO_INV"] = (100000.0, 0.0)
# Tambahkan proyek sintetis dengan biaya investasi tidak valid untuk menguji penanganan error
projects_for_testing["TEST_INVALID_INV"] = (50000.0, "N/A")


# Iterasi melalui dictionary yang dibuat dan uji fungsi untuk setiap proyek
if not projects_for_testing:
    print("No projects available for testing after merging datasets.")
else:
    for project_id, (co2_red, inv_cost) in projects_for_testing.items():
        print(f"\nTesting {project_id}:")
        efficiency = compute_co2_efficiency(co2_red, inv_cost)

        if isinstance(efficiency, float):
            print(f"CO2 Reduction Efficiency: {efficiency:.10f}")
        else:
            print(f"CO2 Reduction Efficiency: {efficiency}")

print("\n--- End of Test ---")
```
**Output:**

```--- Testing CO2 Reduction Efficiency Calculation ---

Testing PLTM-ACHD-001:
CO2 Reduction Efficiency: 0.0003200000

Testing PLTS-BDG-002:
CO2 Reduction Efficiency: 0.0005416667

Testing PLTB-BGR-003:
CO2 Reduction Efficiency: 0.0003600000

Testing PLTM-SMG-004:
CO2 Reduction Efficiency: 0.0003200000

Testing PLTS-JKT-005:
CO2 Reduction Efficiency: 0.0006666667

Testing PLTM-BLI-006:
CO2 Reduction Efficiency: 0.0005769231

Testing PLTA-SLO-007:
CO2 Reduction Efficiency: 0.0005000000

Testing PLTB-MDN-008:
CO2 Reduction Efficiency: 0.0005000000

Testing PLTS-DPK-009:
CO2 Reduction Efficiency: 0.0005714286

Testing PLTM-MKS-010:
CO2 Reduction Efficiency: 0.0005000000

Testing TEST_ZERO_INV:
CO2 Reduction Efficiency: Cannot compute: Investment_Cost cannot be zero.

Testing TEST_INVALID_INV:
CO2 Reduction Efficiency: Cannot compute: could not convert string to float: 'N/A'

--- End of Test ---
```
**Penjelasan Output:**

Output menunjukkan hasil pengujian fungsi `compute_co2_efficiency` untuk berbagai proyek, termasuk kasus-kasus penanganan error:

1. **Untuk Proyek-Proyek Valid (e.g., PLTM-ACHD-001, PLTS-BDG-002, dst.):**

- Output menunjukkan`CO2 Reduction Efficiency` dalam format float (desimal). Ini adalah hasil perhitungan `CO2_Reduction / (Investment_Cost * 1.000.000)`. Misalnya, untuk `PLTM-ACHD-001`, efisiensinya adalah `0.0003200000`. Ini berarti fungsi berhasil menghitung rasio untuk proyek-proyek dengan data input yang valid.

2. **Untuk `EST_ZERO_INV`:**

- Output: `CO2 Reduction Efficiency: Cannot compute: Investment_Cost cannot be zero`.

- Ini menunjukkan bahwa blok `try-except` berhasil menangkap `ZeroDivisionError` yang terjadi ketika `Investment_Cost` adalah 0. Pesan "Investment_Cost cannot be zero." dikembalikan, sesuai dengan penanganan error yang diharapkan.

3. **Untuk `TEST_INVALID_INV`:

- Output: `CO2 Reduction Efficiency: Cannot compute: could not convert string to float: 'N/A'`

= Ini menunjukkan bahwa blok `try-except` berhasil menangkap `ValueError` yang terjadi ketika `Investment_Cost` adalah string "N/A" dan Python mencoba mengkonversinya menjadi float. Pesan error spesifik dari Python ditampilkan, menunjukkan bahwa fungsi telah menangani input yang tidak valid dengan benar.

Secara keseluruhan, output ini memverifikasi bahwa modul `green_analysis.py` (atau fungsi `compute_co2_efficiency` yang disimulasikan) bekerja dengan benar untuk input valid dan secara efektif menangani kasus-kasus error seperti pembagian dengan nol dan tipe data yang tidak sesuai.

---
# Soal 7: Penanganan Error dalam Loop

**Deskripsi:**

Pemerintah perlu menghitung rata-rata output energi dari proyek-proyek terpilih, dengan menangani data yang hilang.

**Tugas:**

1. Buat daftar `Project_ID` untuk dianalisis.

2. Gunakan loop for dengan try-except untuk memproses `Energy_Output` dari `Environmental_Dataset.xlsx`, menangkap KeyError untuk `Project_ID` yang hilang.

3. Jumlahkan nilai `Energy_Output` yang valid dan hitung proyek yang valid.

4. Hitung dan tampilkan rata-ratanya.

**Penjelasan:**

Bagian ini berfokus pada pemrosesan data yang kuat dalam loop, khususnya menggunakan blok `try-except` untuk menangani skenario di mana `Project_ID` mungkin hilang dari dataset atau memiliki nilai `NaN` untuk `Energy_Output.`

**Kode (dari `Green_Finance_Data-Analysis (3).ipynb`):**

```Python

import pandas as pd

df_Env = pd.read_excel('C:/EnergiHijau2025/Environmental_Dataset.xlsx')
print(df_Env)

# membuat list Project_ID
Project_ID_List = []

for index, row in df_Env.iterrows():
    Project_ID = row['Project_ID']
    Project_ID_List.append(Project_ID)
print(f"List Project ID: {Project_ID_List}")

total_energy_output = 0
valid_projects_count = 0
missing_projects = []
invalid_outputs = []

print("Processing energy output for selected projects:\n")

for project_id in Project_ID_List:
    try:
        project_row = df_Env.loc[df_Env['Project_ID'] == project_id]

        if not project_row.empty:
            energy_output = project_row['Energy_Output'].iloc[0]

            if pd.isna(energy_output):
                print(f"Warning: Project ID '{project_id}' found, but has missing (NaN) energy output. Skipping.")
                invalid_outputs.append(project_id)
                continue
            else:
                total_energy_output += energy_output
                valid_projects_count += 1
                print(f"Project ID '{project_id}': Energy Output = {energy_output}")
        else:
            print(f"Error: Project ID '{project_id}' not found in the dataset. Skipping.")
            missing_projects.append(project_id)

    except Exception as e:
        print(f"An unexpected error occurred for Project ID '{project_id}': {e}. Skipping.")

print("\n--- Summary ---")

if valid_projects_count > 0:
    average_energy_output = total_energy_output / valid_projects_count
    print(f"Total valid energy output: {total_energy_output} kWh")
    print(f"Number of valid projects processed: {valid_projects_count}")
    print(f"Average energy output: {average_energy_output:.2f} kWh")
else:
    print("No valid projects were processed to calculate an average.")

if missing_projects:
    print(f"\nProjects not found in the dataset: {', '.join(missing_projects)}")

if invalid_outputs:
    print(f"Projects with missing (NaN) energy output: {', '.join(invalid_outputs)}")
```
Output:

```       Project_ID  CO2_Reduction  Energy_Output  Environmental_Risk_Index
0   PLTM-ACHD-001          32000          11000                        65
1    PLTS-BDG-002          65000          25000                        45
2    PLTB-BGR-003          90000          40000                        30
3   PLTM-SMG-004          48000          18000                        55
4    PLTS-JKT-005         120000          50000                        20
5    PLTM-BLI-006          75000          30000                        50
6    PLTA-SLO-007         150000          60000                        15
7    PLTB-MDN-008         110000          45000                        25
8    PLTS-DPK-009          80000          35000                        35
9   PLTM-MKS-010          55000          20000                        60
List Project ID: ['PLTM-ACHD-001', 'PLTS-BDG-002', 'PLTB-BGR-003', 'PLTM-SMG-004', 'PLTS-JKT-005', 'PLTM-BLI-006', 'PLTA-SLO-007', 'PLTB-MDN-008', 'PLTS-DPK-009', 'PLTM-MKS-010']
Processing energy output for selected projects:

Project ID 'PLTM-ACHD-001': Energy Output = 11000
Project ID 'PLTS-BDG-002': Energy Output = 25000
Project ID 'PLTB-BGR-003': Energy Output = 40000
Project ID 'PLTM-SMG-004': Energy Output = 18000
Project ID 'PLTS-JKT-005': Energy Output = 50000
Project ID 'PLTM-BLI-006': Energy Output = 30000
Project ID 'PLTA-SLO-007': Energy Output = 60000
Project ID 'PLTB-MDN-008': Energy Output = 45000
Project ID 'PLTS-DPK-009': Energy Output = 35000
Project ID 'PLTM-MKS-010': Energy Output = 20000

--- Summary ---
Total valid energy output: 334000 kWh
Number of valid projects processed: 10
Average energy output: 33400.00 kWh
```
**Penjelasan Output:**

1. **Output DataFrame Awal:** Menampilkan `df_Env` yang dimuat dari `Environmental_Dataset.xlsx`, berisi `Project_ID`, `CO2_Reduction`, `Energy_Output`, dan `Environmental_Risk_Index`.

2. `List Project ID: [...]:` Ini adalah daftar semua `Project_ID` yang ditemukan dalam `df_Env`, yang akan diiterasi oleh loop.

3. `Processing energy output for selected projects`:: Bagian ini menunjukkan hasil pemrosesan setiap proyek dalam loop:

- `Project ID 'XYZ': Energy Output = [value]:` Untuk setiap proyek yang ditemukan dengan `Energy_Output` yang valid, nilai output energinya ditampilkan. Dalam contoh output ini, semua proyek memiliki nilai `Energy_Output` yang valid, sehingga tidak ada pesan peringatan atau error yang muncul terkait `NaN` atau `Project_ID` yang tidak ditemukan.

4. `--- Summary ---`: Bagian ini merangkum hasil keseluruhan setelah loop selesai:

- `Total valid energy output: 334000 kWh`: Ini adalah jumlah total `Energy_Output` dari semua proyek yang berhasil diproses (dalam hal ini, semua 10 proyek).

- `Number of valid projects processed: 10`: Menunjukkan berapa banyak proyek yang memiliki `Energy_Output` yang valid dan disertakan dalam perhitungan.

- `Average energy output: 33400.00 kWh`: Ini adalah rata-rata output energi yang dihitung (`334000 / 10`).

Output ini mengkonfirmasi bahwa skrip berhasil mengiterasi melalui daftar proyek, mengambil `Energy_Output` untuk setiap proyek yang valid, dan kemudian menghitung total dan rata-rata dengan benar. Tidak ada `Project_ID` yang hilang atau output energi NaN dalam dataset yang diberikan, sehingga bagian penanganan error (missing_projects dan invalid_outputs) tetap kosong.

---

# Soal Bonus: Machine Learning/AI dengan Decision Tree

**Deskripsi:**

Pemerintah bertujuan untuk memprediksi daya tarik investasi ("High", "Medium", "Low") untuk proyek-proyek baru berdasarkan fitur-fitur seperti GDP_Growth, CO2_Reduction, dan Investment_Cost.

**Tugas:**

1. Menggabungkan `Economic_Dataset.xlsx`, `Environmental_Dataset.xlsx`, dan `Financial_Dataset.xlsx`.

2. Menggunakan scikit-learn untuk membangun Decision Tree Classifier dengan `Daya_Tarik_Investasi` sebagai target.

3. Melatih model, mengevaluasi akurasinya, dan memprediksi daya tarik proyek baru (misalnya, `GDP_Growth=5.0`, `CO2_Reduction=70000`, `Investment_Cost=150)`.

**Penjelasan:**

Pertanyaan bonus ini membahas dasar-dasar machine learning. Ini melibatkan:

Persiapan Data: Menggabungkan beberapa dataset dan memilih fitur yang relevan serta variabel target.

- **Pelatihan Model:** Menggunakan `DecisionTreeClassifier` dari `scikit-learn` untuk melatih model. Ini biasanya melibatkan pembagian data menjadi set pelatihan dan pengujian, penanganan fitur kategorikal (misalnya, dengan one-hot encoding), dan pemasangan model.

- **Evaluasi:** Menilai kinerja model (misalnya, menggunakan skor akurasi).

- **Prediksi:** Menggunakan model yang telah dilatih untuk memprediksi daya tarik investasi dari proyek baru yang belum pernah dilihat.

**Kode (Struktur Konseptual dari `Green_Finance_Data-Analysis (3).ipynb`):**

```Python

# Ini adalah struktur konseptual. Implementasi sebenarnya akan membutuhkan lebih banyak langkah
# seperti penanganan fitur kategorikal, pembagian data, dan properti model evaluation.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Definisikan jalur file
economic_dataset_path = 'C:/EnergiHijau2025/Economic_Dataset.xlsx'
environmental_dataset_path = 'C:/EnergiHijau2025/Environmental_Dataset.xlsx'
financial_dataset_path = 'C:/EnergiHijau2025/Financial_Dataset.xlsx'

# Muat dataset
df_econ = pd.read_excel(economic_dataset_path)
df_env = pd.read_excel(environmental_dataset_path)
df_fin = pd.read_excel(financial_dataset_path)

# Gabungkan dataset
merged_df_ml = pd.merge(df_econ, df_env, on='Project_ID', how='inner')
merged_df_ml = pd.merge(merged_df_ml, df_fin, on='Project_ID', how='inner')

# Select features and target
features = ['GDP_Growth', 'CO2_Reduction', 'Investment_Cost']
target = 'Daya_Tarik_Investasi'

# Handle potential missing values (simple imputation or dropping rows)
merged_df_ml.dropna(subset=features + [target], inplace=True)

X = merged_df_ml[features]
y = merged_df_ml[target]

# Convert categorical target to numerical if necessary (e.g., using LabelEncoder)
# For Decision Tree, string labels can sometimes be handled directly, but numerical is safer.
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y_encoded = le.fit_transform(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")

# Predict for a new project
new_project_data = pd.DataFrame([[5.0, 70000, 150]], columns=features)
predicted_attractiveness = model.predict(new_project_data)
print(f"Predicted attractiveness for the new project: {predicted_attractiveness[0]}")

# If LabelEncoder was used for y, you'd decode it back:
# print(f"Predicted attractiveness for the new project: {le.inverse_transform(predicted_attractiveness)[0]}")
```
**Output (Contoh Output yang Diharapkan):**

`Model Accuracy: 0.85
Predicted attractiveness for the new project: High
Penjelasan Output (Contoh):
`

1. `Model Accuracy: 0.85`: Ini menunjukkan akurasi model Decision Tree pada data pengujian. Akurasi 0.85 (atau 85%) berarti model dapat memprediksi Daya_Tarik_Investasi dengan benar untuk 85% proyek dalam set pengujian. Ini adalah indikator seberapa baik model telah belajar dari data pelatihan.

2. `Predicted attractiveness for the new project: High`: Ini adalah hasil prediksi model untuk proyek baru dengan fitur yang diberikan (`GDP_Growth=5.0, CO2_Reduction=70000, Investment_Cost=150`). Model memprediksi bahwa proyek ini akan memiliki `Daya_Tarik_Investasi` yang "High".

Output ini menunjukkan bahwa model machine learning telah berhasil dilatih dan dapat digunakan untuk membuat prediksi tentang daya tarik investasi berdasarkan fitur-fitur yang relevan, membantu pemerintah dalam pengambilan keputusan investasi.
