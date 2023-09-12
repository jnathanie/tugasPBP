# Tugas 2 PBP
link hasil deploy aplikasi: https://catalogjocelyn.adaptable.app/

## Cara implementasi step-by-step
### Membuat sebuah proyek Django baru
Pertama-tama, saya memastikan bahwa Django telah terinstall sebelum memulai. Karena sudah terinstall, langkah selanjutnya yang saya lakukan adalah membuat direktori proyek dengan cara membuka terminal lalu memindahkan direktori di mana saya membuat proyek tugas 2 ini. Lalu, saya membuat direktori proyek ini dengan perintah `mkdir tugas_2`. Setelah itu, saya mengaktifkan virtual environment dengan perintah `env\Scripts\activate.bat`. Terakhir, saya membuat proyek Django bernama tugas_2 dengan perintah `django-admin startproject tugas_2 .`

### Membuat aplikasi dengan nama main pada proyek tersebut
Karena saya telah mengaktifkan virtual environment pada langkah sebelumnya, maka saya dapat langsung menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru. Setelah perintah ini dijalankan, direktori baru dengan nama `main` yang berisi struktur awal aplikasi akan terbentuk. Selanjutnya, saya menambahkan `main` pada variabel `INSTALLED_APPS` yang berada pada berkas `settings.py` dalam direktori proyek `tugas_2` untuk mendaftarkan aplikasi ini ke dalam proyek tugas_2 ini.

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Membuka berkas `urls.py` dalam direktori proyek tugas_2, lalu mengimpor fungsi `include` dari `django.urls`. Setelah itu, routing dilakukan dengan cara menambahkan `path('main/', include('main.urls'))`.

### Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib
Aplikasi `main` menggunakan model bernama `Item` dan memiliki atribut `name` dengan tipe `CharField` , `amount` dengan tipe `IntegerField`, dan `description` dengan tipe `TextField`. Pertama-tama saya membuka berkas `models.py` pada direktori aplikasi `main`, lalu mengisi berkas dengan kode:
```
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
Setelah mendefinisikan model, saya melakukan migrasi dengan perintah `python manage.py makemigrations` dan menerapkan migrasi ke dalam basis data lokal dengan perintah `python manage.py migrate`.

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
Dalam berkas `views.py` pada aplikasi `main`, saya mengimpor fungsi `render` dari modul django.shortcuts dan membuat fungsi view (show_main) dengan parameter request dari user. Setelah itu, main.html akan di-render dan ditambahkan pula context pada pengembalian fungsi render yang dapat dimunculkan pada halaman HTML. Maka dari itu, setelahnya saya membuat berkas `main.html` dalam direktori `templates` di main. Kemudian, untuk memetakan data yang didapatkan ke dalam HTML untuk memetakan data template, saya menggunakan sintaks `{{ name }}` dan `{{ class }}` agar data yang terdapat pada konteks dapat dimapping ke halaman HTML tersebut. 

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
Pada awalnya, saya membuat berkas `urls.py` dalam direktori `main`. Setelah itu, mengimpor `path` dari `django.urls` dan fungsi `show_main` dari berkas `views` pada direktori `main`. Fungsi `show_main` akan digunakan sebagai tampilan yang akan muncul ketika mengakses URL. Lalu, pada variabel `urlpatterns` akan ditambahkan `path('', show_main, name='show_main')` untuk menjadikan tampilan ini sebagai tampilan default.

### Melakukan deployment ke Adaptable
Membuat aplikasi baru dengan klik `new app`, lalu buat aplikasi baru dengan menghubungkan dengan repository yang sudah dibuat sebelumnya. Setelah itu, saya memilih repository github `tugasPBP` dan branch `main` untuk dideploy. Selanjutnya, pilih `Python App Template` sebagai template deployment dan `PostgreSQL` sebagai tipe basis data yang akan digunakan. Kemudian, masukan versi Python sesuai spesifikasi dan masukkan perintah `python manage.py migrate && gunicorn shopping_list.wsgi` pada bagian `Start Command`. Kemudian, saya memasukkan nama `catalogjocelyn` sebagai nama aplikasi sekaligus nama domain situs web aplikasi yang saya buat. Kemudian, centang bagian `HTTP Listener on PORT` dan terakhir, klik `Deploy App` untuk memulai proses deployment.


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
![Alt text](image.png)

Ketika user atau client (web browser) mengirim request ke server melalui URL, Django akan mencocokan URL yang direquest dengan URL yang telah didefinisikan pada berkas `urls.py`. Kemudian, setiap URL akan dipetakan ke fungsi tertentu yang berada pada berkas `views.py` yang akan memanggil fungsi `view` untuk melakukan query terhadap database dengan memanggil objek pada `models.py`sebagai penghubung. Setelah itu,  fungsi view akan mengembalikan respons berupa format HTML, yang merupakan berkas HTML, dan hasil tersebut akan dirender oleh template yang akan menyajikan konten yang akan dilihat oleh user atau client.


## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment adalah sebuah wadah untuk mengisolasi dependensi proyek atau aplikasi sendiri-sendiri dan memastikan tidak ada konflik antara versi library atau package yang berbeda. Kita perlu menggunakan virtual environment untuk menjaga dependensi yang dibutuhkan oleh proyek atau aplikasi yang berbeda. Misalnya, jika proyek A memerlukan versi 1 dari library X dan proyek B memerlukan versi 2 dari library yang sama. Kita harus mengkondisikan environmentnya sesuai dengan proyek yang ingin kita kembangkan, maka virtual environment berperan di sini untuk dapat membuat dua environment terisolasi dengan versi library yang sesuai untuk masing-masing proyek. Intinya, Virtual environment ini juga berguna untuk memastikan kalau versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lain-nya. 

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, sangat disarankan menggunakan virtual environment untuk menghindari kekacauan pada satu proyek jika kita melakukan update library yang sama di proyek yang berbeda. Tetapi, jika aplikasi yang ingin dibuat hanya aplikasi yang ingin dibuat hanya aplikasi kecil yang hanya digunakan oleh diri sendiri dan mungkin untuk hanya untuk sementara, maka kita tidak terlalu membutuhkan penggunaan virtual environment.


## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
### MVC (Model-View-Controller)
MVC adalah pola atau konsep arsitektur yang memisahkan aplikasi dalam 3 komponen utama:
* Model: Model dalam MVC berperan untuk mengelola dan berhubungan langsung dengan database
* View: View dalam MVC berperan untuk menyajikan tampilan informasi kepada pengguna
* Controller: Controller pada MVC berperan untuk menghubungkan model dan view dalam setiap proses request dari user.

### MVT (Model-View-Template)
MVT adalah konsep arsitektur yang digunakan dalam kerangka kerja Django untuk pengembangan web.
* Model: Model dalam MVT bertanggung jawab atas logika bisnis dan mengatur data aplikasi. Ini mencakup definisi struktur data dan berinteraksi dengan database atau sumber data lainnya.
* View: View dalam MVT mengendalikan logika presentasi. Ini bertugas untuk menampilkan data dari Model kepada pengguna. Dalam Django, View juga dapat mengatur alur aplikasi dan mengatur tampilan yang akan digunakan.
* Template: Template adalah komponen unik dalam MVT. Komponen ini memisahkan tampilan HTML dari logika aplikasi. Template digunakan untuk merancang tampilan yang akan digunakan untuk menampilkan data dari Model. Template membuat Django sangat cocok untuk pengembangan web karena memungkinkan desainer web untuk bekerja dengan template HTML tanpa harus berurusan dengan kode Python.

### MVVM (Model-View-ViewModel)
Model-View-ViewModel (MVVM) adalah pola arsitektur perangkat lunak yang banyak digunakan dan dirancang khusus untuk menyederhanakan pemisahan masalah antara antarmuka pengguna (UI) dan logika yang mendasarinya. Pola ini memisahkan aplikasi menjadi tiga komponen utama:
* Model: Model dalam MVVM mengelola data dan logika bisnis, mirip dengan MVC dan MVT.
* View: View dalam MVVM menampilkan data kepada pengguna, seperti dalam MVC dan MVT.
* ViewModel: ViewModel adalah komponen unik dalam MVVM. Ini bertindak sebagai penghubung antara Model dan View. ViewModel menerima input dari View mengenai aktivitas pengguna, melakukan data binding dua arah (2-way data binding) antara Model dan View, dan mengubah format data dari Model agar sesuai dengan tampilan yang diperlukan. ViewModel memungkinkan tampilan yang sangat fleksibel dan dinamis.

### Perbedaan Ketiganya
* Dari Segi Penggunaan Umum
  * MVT umumnya digunakan dalam kerangka kerja web Python seperti Django.
  * MVC adalah pola arsitektur yang lebih umum digunakan dalam pengembangan perangkat lunak, tidak terbatas pada web.
  * MVVM umumnya digunakan dalam pengembangan aplikasi berbasis klien, terutama aplikasi web interaktif dan aplikasi seluler.
* Dari Segi Pemisahan Logika Presentasi
  * MVT memisahkan logika presentasi dari logika aplikasi dengan menggunakan Template.
  * MVC memisahkan logika presentasi dari logika aplikasi dengan menggunakan Controller.
  * MVVM memisahkan logika presentasi dari logika aplikasi dengan menggunakan ViewModel yang memungkinkan manipulasi data sebelum ditampilkan dalam View.
* Dari Segi Ketergantungan Alur Aplikasi
  * MVT dalam Django memiliki pengendalian alur aplikasi yang diatur oleh kerangka kerja secara internal, sedangkan MVC memerlukan Controller untuk mengendalikan alur aplikasi.
  * MVVM memiliki fleksibilitas tinggi dalam mengatur alur aplikasi melalui ViewModel yang dapat menghubungkan View dan Model, tetapi tidak memiliki komponen Controller yang eksplisit.
* Dari Segi Fleksibilitas Tampilan
  * MVVM mencapai tingkat fleksibilitas tampilan yang lebih tinggi melalui penggunaan ViewModel, di mana tampilan dapat dengan mudah diubah tanpa mengganggu Model atau data di baliknya.
  * MVT dan MVC memiliki cara yang lebih terbatas dalam mengelola tampilan.
