# **Link website: **
https://tradcard.adaptable.app/

## Cara saya mengimplementasikan _checklist - checklist_ di ketentuan tugas: 
 - Membuat sebuah proyek Django baru .
   Disini saya menginstall Django dan membuat virtual environment
 - Membuat aplikasi dengan nama main pada proyek tersebut.
   membuat aplikasi baru (main) dengan cara python manage.py startapp main
 - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
   membuka berkas urls.py pada projek dan tambahkan path untuk aplikasi 'main' ke dalam   
   urlpatterns. Pada urls.py saya juga menambahkan routing untuk ke aplikasi main
- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
  name sebagai nama item dengan tipe CharField.
  amount sebagai jumlah item dengan tipe IntegerField.
  description sebagai deskripsi item dengan tipe TextField.
Pada models.py saya menambahkan context sesuai apa yang diminta yaitu name, amount, dan description

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
**Client:**
Permintaan dimulai ketika pengguna membuka browser dan memasukkan URL aplikasi Django ke dalam alamat browser.

**URL Routing (urls.py):**
Permintaan URL dari client akan diarahkan ke berkas urls.py dalam proyek Django.
Di dalam urls.py, kita menentukan pola URL dan menghubungkannya dengan view tertentu.

**Views (views.py):**
Setelah URL cocok dengan pola yang ditentukan, Django akan memanggil view yang sesuai yang juga didefinisikan dalam berkas views.py.
View adalah bagian dari aplikasi yang berisi logika bisnis untuk menangani permintaan.
View dapat memproses data, berinteraksi dengan model, dan merender berkas HTML atau memberikan respons JSON.

**Models (models.py):**
Dalam view, Anda dapat berinteraksi dengan model yang didefinisikan dalam berkas models.py.
Model digunakan untuk mengakses dan mengelola data dalam basis data.
View dapat mengambil atau menyimpan data ke basis data sesuai dengan kebutuhan.

**Templates (HTML Files):**
Jika view memerlukan tampilan, view akan merender berkas HTML menggunakan Django Template Language (DTL).
DTL memungkinkan Anda menyisipkan data dinamis dari view ke dalam halaman web.
Hal ini menghasilkan tampilan yang akan dikirimkan sebagai respons ke client.

**Server Response:**
Setelah view selesai menjalankan logikanya dan merender tampilan jika diperlukan, Django akan menghasilkan respons HTTP.
Respons ini bisa berupa halaman web lengkap dengan HTML, CSS, dan JavaScript, atau bisa juga data dalam format JSON, tergantung pada tindakan yang diminta oleh client.

**Client Response:**
Respons dari server akan dikirimkan kembali ke browser client.
Browser akan menampilkan tampilan web yang diterima atau akan memproses data JSON sesuai dengan jenis respons yang diterima.

**Interaksi Client:**
Pengguna dapat berinteraksi dengan tampilan web yang diterima, mengisi formulir, mengklik tautan, atau melakukan tindakan lainnya yang akan menghasilkan permintaan tambahan ke server Django.

## Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan dalam pengembangan perangkat lunak Python, termasuk aplikasi web Django, karena:

1. **Isolasi Lingkungan:** Membuat lingkungan kerja terisolasi dari sistem operasi untuk menghindari konflik dan masalah dependensi.

2. **Pengelolaan Dependensi:** Memungkinkan manajemen dependensi yang independen untuk setiap proyek.

3. **Kebersihan dan Keselamatan:** Menghindari pencampuran paket dan dependensi yang dapat merusak proyek.

4. **Reproducibility:** Membuat lingkungan yang dapat direproduksi dengan mudah untuk berbagi proyek dengan orang lain.

5. **Kemudahan Penggunaan:** Memudahkan instalasi, penghapusan, dan manajemen paket Python.

Meskipun memungkinkan untuk tidak menggunakan virtual environment, disarankan untuk meninggalkan praktik ini karena dapat menghemat waktu dan memastikan pengembangan yang lebih terstruktur dan aman.
## Apakah itu MVC, MVT, MVVM dan apa perbedaan dari ketiganya?
MVC (Model-View-Controller):

Model: Mewakili data dan logika bisnis aplikasi. Ini adalah bagian yang bertanggung jawab untuk mengelola dan memanipulasi data.
View: Menampilkan informasi kepada pengguna dan menanggapi input pengguna. Ini adalah bagian yang berhubungan dengan tampilan atau antarmuka pengguna.
Controller: Bertindak sebagai perantara antara Model dan View. Mengatur alur kontrol aplikasi, menerima input dari pengguna, dan mengubah Model atau View sesuai dengan instruksi.
Perbedaan utama: Dalam MVC, Controller adalah komponen yang mengendalikan alur logika aplikasi, sedangkan Model dan View berinteraksi melalui Controller. MVC sering digunakan dalam pengembangan web dan desktop.

MVT (Model-View-Template):

Model: Sama seperti dalam MVC, Model adalah komponen yang mengelola data dan logika bisnis.
View: Ini adalah komponen yang menangani tampilan atau antarmuka pengguna, seperti dalam MVC.
Template: Template mengatur cara data dari Model akan ditampilkan dalam View. Template ini biasanya terkait dengan teknologi server-side rendering seperti dalam framework Django (Python).
Perbedaan utama: MVT adalah variasi dari MVC yang umumnya digunakan dalam konteks aplikasi web yang menggunakan server-side rendering. Perbedaan utama adalah penggunaan Template yang mengatur tampilan.

MVVM (Model-View-ViewModel):

Model: Sama seperti dalam MVC dan MVT, Model mengelola data dan logika bisnis.
View: Ini adalah komponen yang menangani tampilan atau antarmuka pengguna, seperti dalam MVC dan MVT.
ViewModel: ViewModel adalah lapisan tambahan yang berfungsi sebagai perantara antara Model dan View. Ini mengubah data dari Model menjadi format yang dapat ditampilkan di View dan merespons perubahan di View dengan mengupdate Model.
Perbedaan utama: MVVM adalah arsitektur yang umumnya digunakan dalam pengembangan aplikasi berbasis platform seperti Xamarin (untuk pengembangan aplikasi seluler) atau dalam aplikasi berbasis framework seperti AngularJS (untuk pengembangan web). ViewModel adalah komponen unik yang membedakannya dari MVC dan MVT, dan tujuannya adalah memisahkan logika tampilan dari Model dan menghubungkannya dengan View.

## Apa perbedaan antara form POST dan form GET dalam Django?
Perbedaan utama antara penggunaan metode POST dan GET dalam Django adalah sebagai berikut:

**Metode Pengiriman Data:**

- **POST:** Saat Anda menggunakan metode POST dalam formulir, data yang dikirim oleh formulir akan disertakan secara tersembunyi dalam permintaan HTTP, sehingga tidak terlihat di URL. Ini berarti data dikirim sebagai bagian dari badan permintaan, menjadikannya lebih aman untuk mengirim data sensitif seperti kata sandi.

- **GET:** Jika Anda memilih metode GET dalam formulir, data yang dikirim oleh formulir akan ditambahkan ke URL sebagai bagian dari string query. Data ini akan terlihat di URL dan dapat dengan mudah diakses melalui tautan URL. Metode ini cocok untuk mengirim data yang tidak sensitif, tetapi tidak direkomendasikan untuk data yang bersifat rahasia karena dapat terlihat oleh siapa saja.

**Ukuran Data:**

- **POST:** Anda dapat mengirimkan volume data yang lebih besar dengan metode POST karena data dikirim sebagai bagian dari badan permintaan HTTP. Ini cocok untuk mengirim file gambar atau data yang lebih besar.

- **GET:** Metode GET cocok untuk mengirimkan data yang lebih kecil karena data harus dimasukkan ke dalam string query URL. Ini memiliki batasan pada jumlah data yang dapat Anda kirim.

**Keamanan:**

- **POST:** Metode POST lebih aman untuk mengirim data sensitif karena data tidak terlihat di URL. Django juga menyediakan perlindungan terhadap serangan CSRF (Cross-Site Request Forgery) yang dirancang khusus untuk melindungi permintaan POST.

- **GET:** Data yang dikirim melalui metode GET akan terlihat di URL, sehingga lebih rentan terhadap serangan dan potensi pencurian data. Oleh karena itu, sebaiknya tidak digunakan untuk data yang bersifat rahasia.

**Penggunaan Umum:**

- **POST:** Biasanya digunakan ketika Anda perlu mengirim data yang akan mengubah atau memproses sesuatu di server, seperti pengiriman formulir pendaftaran atau komentar.

- **GET:** Biasanya digunakan ketika Anda ingin mengirim data yang hanya akan digunakan untuk mengambil atau menampilkan informasi, seperti melakukan pencarian atau filter pada halaman web.
## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
