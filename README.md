# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan jaya Maju

## Business Understanding

Perusahaan Jaya Maju adalah perusahaan yang mengalami tingkat pergantian karyawan (attrition) yang cukup tinggi. 
Hal ini menyebabkan ketidakstabilan dalam tim dan peningkatan biaya rekrutmen serta pelatihan. 
Untuk membantu mengurangi attrition dan merancang strategi retensi yang efektif, dibutuhkan sebuah sistem prediksi untuk mengidentifikasi karyawan yang berisiko keluar dari perusahaan.

### Permasalahan Bisnis

- Mencari faktor-faktor utama yang mempengaruhi permasalahan attrition ini.
- Mengidentifikasi karyawan yang berpotensi keluar (attrition).
- Menyediakan dashboard serta alat prediktif yang dapat membantu pengambilan keputusan terkait permasalahan Attrition ini.

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

## Business Dashboard

Dashboard ini dibangun menggunakan Metabase dengan layanan database dari Supabase. Dashboard ini memberikan insight visual kepada tim HR dalam memantau risiko attrition berdasarkan data aktual dan hasil prediksi dari model machine learning.

### Komponen Utama Dashboard

KPI Summary
- Total Karyawan: 1.058
- Employee at Risk (hasil prediksi model): 340 orang
- Total Attrition Aktual: 179 orang

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
