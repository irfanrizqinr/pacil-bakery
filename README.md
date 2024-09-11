1. tautan menuju PWS : "irfan-rizqi31-pacilbakery.pbp.cs.ui.ac.id"

2. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

jawaban :

step 1 : membuat direktori lokal dahulu
step 2 : menginisiasi dan mengaktifkan virtual environment
step 3 : membuat project
step 4 : membuat app 'main'
step 5 : menambahkan app 'main' pada INSTALLED_APPS pada settings.py yang ada di project
step 6 : membuat class pada models serta atributnya
step 7 : make migrations dan migrate
step 8 : pada direktori app, membuat folder templates yang berisi file html yang akan digunakan pada views.py
step 9 : mengubah views.py = merender file html yang akan dijadikan template 
step 10 : membuat urlrouting (membuat urls.py pada direktori app + meng-include url tersebut pada file urls.py di project)
step 11 : melakukan proses CI git (membuat remote repo, git init, git remote add, git add, git commit, push ke remote repo)
step 12 : deploy ke PWS deh

3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Request
   ↓
Middleware (pre-processing)
   ↓
URL Routing → menentukan/memilah View yang Sesuai dengan request
   ↓
View → menjalankan logika
   ↓
Models ↔ Database (Ambil/Simpan Data)
   ↓
View → mengambil template html untuk ditampilkan,
   ↓
Middleware (post-processing)
   ↓
Response
   ↓
Client

4. Jelaskan fungsi git dalam pengembangan perangkat lunak!

jawaban : git memungkinkan pengembang perangkat lunak untuk berkolaborasi dan mencatat versi dari kode yang dikembangkan (version control system). Dengan git, pengembang dapat meminimalisir konflik yang akan terjadi pada saat real time collaboration pada suatu tim. Git juga memungkinkan pengembang untuk kembali pada kode sebelumnya saat kode tersebut tidak layak untuk diunggah sehingga perbaikan bug dan fixing problem akan lebih efektif.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

jawaban : Salah satu yang paling menonjol dari Django Framework adalah community support. Dengan menggunakan framework Django, kita dapat dengan mudah belajar dari sumber yang tak terbatas di internet karena kepopulerannya yang tinggi. Selain itu, dokumentasi django sangat lengkap sehingga cocok bagi pemula untuk mempelajari lebih dalam terkait fitur, sintaks, serta alur kerja dari komponen-komponen pada django.

6. Mengapa model pada Django disebut sebagai ORM?

jawaban : karena Django menggunakan pendekatan ORM untuk menghubungkan model dengan database relasional. ORM memungkinkan pengembang untuk bekerja dengan data dalam bentuk objek daripada menulis query secara langsung, sehingga memudahkan interaksi dengan basis data tanpa harus memahami atau menulis kode SQL.
