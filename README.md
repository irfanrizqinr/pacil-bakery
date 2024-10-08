[Pertanyaan Tugas-Tugas]

----------------------Tugas 2---------------------------------------
1. tautan menuju PWS : "http://irfan-rizqi31-pacilbakery.pbp.cs.ui.ac.id"

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


-------------------Tugas 3----------------------------
7. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Jawaban: Data delivery (pengiriman data) sangat penting dalam pengimplementasian sebuah platform dengan memastikan informasi atau layanan yang dikeluarkan oleh platform dapat diakses dengan tepat, cepat, dan efisien oleh pengguna. 

8. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Jawaban: JSON dianggap lebih baik dan lebih populer daripada XML karena formatnya yang lebih sederhana, mudah dipahami, dan muah diproses baik oleh mesin maupun manusia. Dengan struktur yang berbasis objek, JSON lebih cocok untuk bahasa pemrograman modern seperti JavaScript, sehingga lebih efisien dalam pertukaran data di web. Meskipun begitu, XML memiliki keunggulan dalam menangani data yang lebih kompleks dengan skema dan validasi, JSON yang lebih ringan dan cepat membuatnya lebih sering digunakan dalam pengembangan web dan API.

9. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Jawaban: Method `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dimasukkan sesuai dengan aturan validasi yang telah ditentukan. Jika valid, method ini mengembalikan `True` dan menghasilkan `cleaned_data` yang dapat diproses lebih lanjut, sementara jika tidak valid, akan mengembalikan `False` dan menyimpan pesan kesalahan di atribut `errors`. Method ini penting untuk memastikan hanya data yang valid yang diproses oleh aplikasi.

10. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Jawaban : `csrf_token` diperlukan dalam form di Django untuk melindungi aplikasi dari Cross-Site Request Forgery (CSRF), yaitu serangan yang mencoba mengeksploitasi sesi pengguna dengan mengirimkan permintaan berbahaya yang terlihat sah. Tanpa `csrf_token`, form dapat menjadi sasaran serangan ini, di mana penyerang bisa menggunakan sesi pengguna untuk melakukan tindakan yang tidak diinginkan, seperti mengubah data atau melaksanakan transaksi tanpa izin. `csrf_token` memastikan bahwa setiap permintaan form berasal dari sumber yang sah dan bukan dari situs lain.

11.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawaban : 
Step 1 : buatlah direktori templates pada direktori utama project dan tambahkan base.html di dalamnya, serta modifikasi BASE_DIRS
Step 2 : modifikasi models.py dan import uuid
Step 3 : migrasi basis data
Step 4 : buatlah forms untuk memasukkan data pada komponen-komponen data yang sudah ditentukan pada models (seperti name, price, description)
Step 5 : buatlah fungsi untuk mengembalikan data dengan format XML
Step 6 : buatlah fungsi untuk mengembalikan data dengan format JSON
Step 7 : buatlah fungsi untuk mengembalikan data XML filtered by id
Step 8 : buatlah fungsi untuk mengembalikan data JSON filtered by id
Step 9 : Modifikasi urls dengan menambahkan path path yang bersesuaian.
Step 10 : Runserver dan lakukan proses git

11. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

![Show XML dari Postman](images/show_xml.png)
![Show JSON dari Postman](images/show_json.png)
![Show XML by ID dari Postman](images/Show_xml_by_id.png)
![Show JSON by ID dari Postman](images/show_json_by_id.png)

sekian terima kasih!

--------------------------Tugas 4-------------------------------

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
Jawaban : 

Pada kode yang digunakan misal logout_user, HttpResponseRedirect() memungkinkan kita untuk membuat objek response dahulu, kemudian melakukan operasi seperti menghapus cookie pada objek response, dan akhirnya mengembalikan respons tersebut. Jika kita menggunakan redirect() secara langsung, kita tidak akan mendapatkan objek response untuk dimodifikasi (seperti menghapus cookie). redirect() adalah shortcut yang langsung mengembalikan respons, tanpa memberikan kita kesempatan untuk memodifikasi objek tersebut.

2. Jelaskan cara kerja penghubungan model Product dengan User!

step 1: ForeignKey digunakan untuk menghubungkan model Product dengan User, dengan tujuan agar produk memiliki pemilik yang jelas.

step 2 : on_delete=models.CASCADE memastikan bahwa ketika pengguna dihapus, produk yang dimiliki oleh pengguna tersebut juga akan dihapus.

step 3 : Saat menyimpan Product, kita menetapkan field owner sebagai User yang sedang login contoh (product_entry.user).

step 4 : Jika kita ingin menampilkan produk yang hanya dimiliki oleh user tertentu, misalnya user yang sedang login, kita bisa melakukannya seperti ini: 

product_entries = Product.objects.filter(user=request.user)

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Jawaban :
Authentication adalah bagaimana suatu web page memverifikasi user yang menggunakan web page tersebut
Authorization adalah bagaimana user dapat mengakses fitur fitur yang sudah diseleksi hanya bagian dari user tersebut.

Django menggunakan konsep login, bisa menggunakan alternatif OAuth, OaAuth2 dll. Django juga menggunakan konsep session dan cookies untuk mengingat user yang sedang login.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Jawaban :
Django menggunakan session framework dan cookies. dengan tahapan tahapan seperti login process, session storage, request object, dan logout process.

Kegunaan lain cookies dari segi keamanaan adalah menyimpan CSRF, token yang menyimpan bahwa permintaan berasal dari sumber yang sah.

Tidak semua Cookies aman untuk digunakan. Penting untuk memastikan bahwa cookies yang digunakan untuk menyimpan informasi sensitif dikonfigurasi dengan aman, menggunakan mekanisme seperti HttpOnly dan secure cookies untuk melindungi dari serangan XSS dan session hijacking.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Step 1 : Membuat fungsi (from django.contrib.auth.forms import UserCreationForm) dan form registrasi (membuat fungsi register)
Step 2 : Membuat template registrasinya (register.html)
Step 3 : URL Routing form registrasi
Step 4 : Import fungsi authentication dan login, serta membuat form login (login_user)
Step 5 : Membuat template loginnya (login.html)
Step 6 : URL Routing form login
Step 7 : Hal yang sama dilakukan dengan tombol logout (membuat fungsi, tambahkan button di main.html, url routing)
Step 8 : Menggunakan Cookies untuk merestriksi user

1. from decorator import login_required
2. pasang di atas fungsi show_main
3. modifikasi fungsi login dengan menambahkan set_cookie setiap form valid
4. menambahkan context last_login untuk ditampilkan di main.html
5. modifikasi fungsi logout dengan menambhakan delete_cookie setiap logout dipencet

Step 9 : Menghubungkan model dengan user
1. import user pada models.py
2. tambahkan field user dengan foreignkey
3. modifikasi create_product pada views.py sehingga product yang ditambahkan sesuai dengan user
4. boleh tambahkan juga data pada context untuk menampilkan user yang sedang login dengan request.user.username
5. migrasi database

Step 8 : Lakukan Git add, commit, Push


------------------------Tugas 5-------------------------------

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Jawaban :
Dalam CSS, prioritas pengambilan selector ditentukan oleh specificity dengan urutan: pertama, inline style memiliki prioritas tertinggi, diikuti oleh ID selector, kemudian class, pseudo-class, dan attribute selector, lalu type selector (tag HTML) dan pseudo-element, serta universal selector memiliki prioritas terendah. Selain itu, aturan yang menggunakan !important akan mengesampingkan semua aturan lain, kecuali ada deklarasi !important lain dengan tingkat specificity lebih tinggi. Jika dua selector memiliki tingkat specificity yang sama, aturan yang dideklarasikan terakhir akan digunakan.


2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Jawaban :

Responsive design penting dalam pengembangan aplikasi web karena memungkinkan tampilan dan fungsionalitas situs menyesuaikan diri secara otomatis dengan berbagai ukuran layar dan perangkat, seperti smartphone, tablet, dan desktop. Hal ini meningkatkan pengalaman pengguna (user experience) dengan memastikan situs tetap mudah diakses dan digunakan, tanpa perlu menggulir atau memperbesar layar secara manual. Contoh aplikasi yang sudah menerapkan responsive design adalah Twitter, yang terlihat rapi di berbagai perangkat, sedangkan aplikasi lama seperti Craigslist cenderung kurang responsif karena tampilannya tetap sama di semua perangkat, sering kali menyulitkan pengguna di layar kecil.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Jawaban :

Margin, border, dan padding adalah tiga properti CSS yang mengatur ruang di sekitar elemen HTML:

Margin adalah ruang kosong di luar elemen yang memisahkan elemen tersebut dari elemen lain. Margin tidak memiliki warna dan tidak termasuk dalam elemen itu sendiri. Border adalah garis di sekitar elemen yang memisahkan elemen dari margin. Border bisa memiliki warna, ketebalan, dan gaya (misalnya solid, dashed). Padding adalah ruang di dalam elemen, antara konten elemen dan border. Padding memberikan jarak antara isi elemen dan tepi border.

Singkatnya, padding berada di dalam border, border di antara padding dan margin, dan margin di luar border.

4.  Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Jawaban :
Flexbox dan Grid Layout adalah dua sistem tata letak di CSS yang memudahkan pengaturan elemen pada halaman web. 

Flexbox adalah tata letak satu dimensi yang mengatur elemen secara horizontal atau vertikal, cocok untuk tata letak sederhana dan responsif seperti navbar atau daftar. Flexbox fleksibel dalam mendistribusikan ruang antar elemen sesuai ukuran kontainer. 

Grid Layout adalah sistem dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom, ideal untuk tata letak yang lebih kompleks seperti halaman dashboard atau majalah. Grid memberikan kontrol lebih detail untuk membuat tata letak yang terstruktur dan fleksibel.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Jawaban :

Step 1 : Menambahkan Tailwind ke Aplikasi
Step 2 : Membuat fitur Edit Mood dan lakukan routing
Step 3 : Membuat fitur Hapus mood dan lakukan routing
Step 4 : Menambahkan Navigation Bar "navbar.html" lalu include ke semua template yang bersesuaian
Step 5 : Melakukan konfigurasi Static files
Step 6 : Menambahkan Global.css sebagai styling utama
Step 7 : Styling tiap halaman yang ada (tiap file pada /templates)
Step 8 : Lakukan Git add, commit dan push ke remote repo.

-------------------------Tugas 6------------------------------

1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

Jawaban :
JavaScript sangat berguna dalam pengembangan aplikasi web karena memungkinkan pembuatan halaman yang lebih interaktif dan responsif. Dengan JavaScript, pengembang dapat memperbarui konten tanpa harus memuat ulang seluruh halaman, memvalidasi input secara langsung, serta menambahkan animasi dan efek yang membuat pengalaman pengguna lebih menarik. Selain itu, JavaScript mendukung komunikasi asinkron melalui AJAX, memungkinkan integrasi API, dan membantu dalam pembuatan aplikasi berbasis single-page (SPA) yang cepat dan efisien.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

Jawaban :
Fungsi await saat digunakan dengan fetch() adalah untuk menunggu hingga permintaan HTTP selesai dan respons diterima sebelum melanjutkan eksekusi kode. Jika await tidak digunakan, kode akan melanjutkan eksekusi tanpa menunggu respons, yang dapat menyebabkan akses data yang belum tersedia, seperti undefined atau Promise yang belum terselesaikan.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Jawaban :
Supaya mengecualikan fungsi tersebut dari pengecekan csrf_token

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Jawaban :
Pembersihan data input di backend tetap diperlukan meskipun sudah dilakukan di frontend karena frontend tidak sepenuhnya dapat diandalkan untuk keamanan. Pengguna yang berpengalaman atau berniat buruk bisa memodifikasi data yang dikirim dari frontend, melewati validasi, atau mengubah kode JavaScript. Dengan melakukan pembersihan dan validasi di backend, server dapat memastikan bahwa data yang diterima tetap aman dan sesuai dengan aturan, mencegah serangan seperti injeksi SQL, skrip lintas situs (XSS), atau data yang tidak valid. Ini memberikan lapisan perlindungan tambahan terhadap potensi eksploitasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Step 1 : Membuat error message pada login_user
Step 2 : membuat fungsi tambah product dengan ajax
Step 3 : url routing fungsi tersebut 
Step 4 : Implementasi fetch pada main.html
Step 5 : Mengedit modal dan menambahkan fungsi fungsi JS pada tag script
Step 6 : Implementasi Strip Tags
Step 7 : Lakukan git commands


