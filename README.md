# Green Finance Data Analysis

Repositori ini menyajikan serangkaian analisis data yang berfokus pada proyek-proyek energi hijau, khususnya di Indonesia. Analisis ini dirancang untuk memberikan wawasan mendalam kepada para pemangku kepentingan, seperti pemerintah, investor, dan pengembang proyek, sehingga memungkinkan mereka untuk membuat keputusan yang terinformasi dan berbasis data.

---

|Nama|	No Absen|	Kelompok|
|-|-|-|
|Agus Iskandar Darmawan|	09.000.DB2025|	II|
|Gunawan|	10.005.DB2025|	II|
|M. Sandi Firmansyah|	10.006.DB2025|	II|
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

