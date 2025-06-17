# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan jaya Maju

## Business Understanding

Perusahaan Jaya Maju merupakan perusahaan multinasional dengan lebih dari 1.000 karyawan yang tersebar di berbagai daerah. Meskipun skalanya sudah besar, perusahaan ini menghadapi tantangan serius berupa tingkat attrition (keluar kerja) karyawan yang tinggi, yaitu lebih dari 10% dari total karyawan. Hal ini berdampak negatif terhadap biaya operasional, produktivitas, serta stabilitas tim.

### Permasalahan Bisnis

- Tingginya tingkat attrition karyawan (>10%).
- Tidak adanya sistem prediktif untuk memantau dan mengantisipasi risiko karyawan keluar.
- Kurangnya insight dari data internal untuk membantu mendeteksi attrition dan melakukan pengambilan keputusan oleh HR.

### Cakupan Proyek

- Eksplorasi data attrition karyawan.
- preprocessing data (encoding, scaling, feature selection, SMOTE).
- Membangun beberapa model machine learning untuk memprediksi attrition.
- Memilih model terbaik berdasarkan metrik AUC.
- Membuat pipeline dan menyimpan model untuk kebutuhan prediksi ke depan.
- Menyusun business dashboard di Metabase.
- Menyediakan skrip prediksi otomatis yang siap dipakai oleh tim HR.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

1. Menjalankan file ipynb
   - Import/Unduh seluruh dependensi, packages, libraries yang dibutuhkan (cek ``requirements.txt``)
   - Jalankan seluruh isi file ```data_science.ipynb```
   
2. Menjalankan Script
   - buka file python ```predict.py```
   - pastikan data ```attrition_cleaned.csv``` telah siap digunakan
   - run file python ```predict.py```
  
3. Menjalankan Dashboard
   - Install Docker
   - Pull docker image untuk metabase
     ```
     docker pull metabase/metabase:v0.46.4
     ```
   - Jalankan Metabase
      ```
       docker run -p 3000:3000 --name metabase metabase/metabase
      ```
   - Login ke Metabase menggunakan username dan password berikut :
     ```
     username: root@mail.com
     password: root123
     ```

## Business Dashboard

Dashboard ini dibangun menggunakan Metabase dengan layanan database dari Supabase. Dashboard ini memberikan insight visual kepada tim HR dalam memantau risiko attrition berdasarkan data aktual dan hasil prediksi dari model machine learning.

### Komponen Utama Dashboard

KPI Summary
- Total Karyawan: 1.058
- Employee at Risk (hasil prediksi model): 340 orang
- Total Attrition Aktual: 179 orang

### Distribusi & Segmentasi Attrition
- Distribusi Departemen: Mayoritas berasal dari R&D dan Sales. Sales memiliki beban risiko tinggi.
- Attrition vs Usia: Usia 30–37.5 tahun mencatat attrition tertinggi.
- Attrition vs Overtime: Karyawan lembur jauh lebih rentan keluar.
- Attrition vs Business Travel: Karyawan Travel_Rarely lebih banyak keluar.
- Attrition vs Marital Status: Status Single memiliki angka keluar tinggi disusul dengan Married.
- Attrition vs YearsWithCurrManager: Tahun-tahun awal (0-2 tahun) menunjukan angka attrition tertinggi.
- Attrition vs Environment Satisfaction: Kepuasan rendah → attrition tinggi.
- Attrition vs JobRole: Sales Representative dan Laboratory Technician memiliki risiko lebih tinggi.

### Trend Risiko Attrition berdasarkan Lama Bekerja di Perusahaan Jaya Jaya Maju
- 5 Tahun pertama (0–5): risiko attrition sangat tinggi (48.12%)
- Setelah itu menurun, lalu naik kembali pada 30–35 tahun

## Conclusion
1. Faktor utama penyebab attrition:
Berikut adalah fitur-fitur paling berpengaruh terhadap prediksi attrition, :
- `OverTime_Yes`: Karyawan yang sering lembur memiliki risiko lebih tinggi keluar akibat kelelahan atau ketidakseimbangan kerja-hidup.
- `YearsWithCurrManager`: Lama bekerja dengan manajer saat ini berpengaruh; hubungan yang baru atau terlalu lama tanpa perkembangan bisa meningkatkan risiko keluar.
- `BusinessTravel_Travel_Frequently`: Bepergian dinas yang terlalu sering dapat menimbulkan kejenuhan dan keinginan untuk mencari pekerjaan yang lebih stabil.
- `MaritalStatus_Single`: Karyawan lajang cenderung lebih mobile dan terbuka terhadap peluang kerja baru.
- `EnvironmentSatisfaction`: Karyawan yang merasa tidak puas dengan lingkungan kerjanya cenderung lebih mudah keluar dari perusahaan.
- `YearsSinceLastPromotion`: Karyawan yang tidak mengalami kenaikan jabatan dalam waktu lama mungkin merasa stagnan dan mencari peluag di luar.
- `JobSatisfaction`: Tingkat kepuasan kerja yang rendah menjadi salah satu indikator utama tingginya risiko attrition. 
  
2. Membangun model prediktif yang akurat
Setelah dilakukan proses data science, model terbaik yang didapatkan adalah Logistic Regression dengan AUC sebesar 0.8393. Model ini mampu mengidentifikasi karyawan yang berisiko keluar dengan cukup baik dan konsisten.

3. Membangun Script prediktif
Script untuk melakukan prediksi terhadap data karyawan sudah disiapkan guna membantu HR dalam mendeteksi dan mengatasi permasalaha attrition ini

### Rekomendasi Action Items 

Berdasarkan hasil analisis fitur dan insight dari model prediktif, berikut beberapa langkah strategis yang dapat diambil oleh tim HR Jaya-Jaya Maju untuk mengurangi tingkat attrition:
1. Evaluasi dan batasi lembur berlebih
   - Terapkan kebijakan kerja yang lebih seimbang untuk karyawan yang sering lembur.
   - Pantau beban kerja dan implementasikan kebijakan fleksibilitas kerja jika memungkinkan.
     
2. Pantau dan dukung karyawan yang sering melakukan perjalanan dinas
   - Berikan dukungan ekstra, seperti insentif, cuti tambahan, atau program kesejahteraan untuk mereka yang Travel_Frequently.

3. Fokus pada karyawan lajang
   - Tawarkan program pengembangan diri, mentoring, atau peluang rotasi kerja untuk meningkatkan engagement pada karyawan dengan status Single.

4. Perkuat hubungan manajer-karyawan di awal masa kerja
   - Buat onboarding yang kuat dan pelatihan bagi manajer untuk membangun koneksi yang efektif dengan anggota tim baru (YearsWithCurrManager rendah).

5. Tingkatkan lingkungan kerja
   - Gunakan hasil survei kepuasan karyawan untuk memperbaiki aspek lingkungan kerja (EnvironmentSatisfaction).

6. Perhatikan peluang promosi
   - Ciptakan jalur karier yang jelas dan seimbang agar tidak ada karyawan yang terlalu lama stagnan (YearsSinceLastPromotion tinggi).

7. Fokus pada peningkatan kepuasan kerja
   - Karyawan dengan JobSatisfaction rendah perlu diprioritaskan dalam program feedback, coaching, atau penyesuaian job-fit.

