# **Link website: **
https://tradcard.adaptable.app/

## Tugas 2
## Cara saya mengimplementasikan _checklist - checklist_ di ketentuan tugas: 
**Membuat Proyek Django Baru:**
django-admin startproject main

**Membuat Aplikasi "main":**
python manage.py startapp main
Routing Proyek:
Buka file namaprojek/urls.py dan tambahkan routing untuk aplikasi "main" di sana. Contoh:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Tambahkan ini untuk routing ke aplikasi "main"
]
**Membuat Model "Item":**
Buka file main/models.py dan definisikan model "Item" seperti yang Anda inginkan:

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    
**Membuat Fungsi di views.py:**
Buka file main/views.py dan buat sebuah fungsi yang akan dikembalikan ke dalam template HTML:

from django.shortcuts import render

def my_view(request):
    nama_aplikasi = "Nama Aplikasi Anda"
    nama_kelas = "Nama Kelas Anda"
    return render(request, 'template.html', {'nama_aplikasi': nama_aplikasi, 'nama_kelas': nama_kelas})
Membuat Template HTML:
Buat template HTML dengan nama template.html dalam direktori main/templates. Anda bisa menggunakan template ini untuk menampilkan nama aplikasi dan nama kelas Anda.

**Routing Aplikasi "main":**
Buat file main/urls.py jika belum ada, dan tambahkan routing untuk fungsi yang telah Anda buat di views.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
]
Mengaplikasikan Migrasi dan Migrasi Database:
Jalankan perintah-perintah berikut untuk membuat migrasi dan menerapkan migrasi ke database:

python manage.py makemigrations
python manage.py migrate

**Deployment ke Adaptable:**
connect dengan github di adaptable dan mencoba deploy app

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

## Tugas 3
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
Struktur dan Tujuan Utama:

XML: XML adalah bahasa markup yang dirancang untuk mengorganisir, menyimpan, dan mentransmisikan data. Ini memiliki struktur hierarkis yang fleksibel dan sering digunakan untuk pertukaran data antara aplikasi yang berbeda atau penyimpanan data terstruktur.
JSON: JSON adalah format pertukaran data ringan yang sering digunakan dalam pengembangan web. Ini digunakan untuk mengirim data antara aplikasi web dan server, serta untuk penyimpanan data yang lebih ringan dan efisien.
HTML: HTML adalah bahasa markup yang digunakan untuk membuat halaman web. Meskipun dapat digunakan untuk menampilkan data, HTML sebagian besar digunakan untuk merancang tampilan dan struktur halaman web.
Sintaksis:

XML: XML menggunakan sintaksis yang ketat dengan tag yang diapit oleh tanda kurung sudut. Ini mendefinisikan struktur data dengan jelas menggunakan elemen dan atribut.
JSON: JSON menggunakan sintaksis yang lebih sederhana dengan pasangan nama-kunci (key-value pairs) yang dipisahkan oleh tanda titik dua (":"). Data dalam JSON dapat berupa objek atau array.
HTML: HTML juga menggunakan tag yang diapit oleh tanda kurung sudut, tetapi strukturnya lebih terbatas dan memiliki tujuan utama dalam merancang tampilan halaman web.
Penggunaan Umum:

XML: Digunakan dalam berbagai konteks, termasuk pertukaran data antara aplikasi yang berbeda, konfigurasi berkas, dan penyimpanan data terstruktur.
JSON: Digunakan secara luas dalam pengembangan web untuk mentransfer data antara server dan browser, serta dalam API web dan penyimpanan data yang lebih fleksibel.
HTML: Digunakan untuk merancang halaman web, menampilkan konten kepada pengguna, dan mengatur tampilan dan struktur halaman.
Ekosistem dan Pustaka:

XML: Memiliki dukungan kuat dalam berbagai bahasa pemrograman dan banyak pustaka untuk pengolahan XML.
JSON: Merupakan format bawaan dalam JavaScript, dan dukungan untuk JSON juga ada dalam sebagian besar bahasa pemrograman modern.
HTML: Khusus digunakan untuk pembuatan halaman web dan memiliki dukungan dalam lingkungan browser web.
Ukuran Data:

XML: Biasanya memiliki overhead yang lebih besar dalam hal ukuran data karena sintaksis yang lebih panjang dan atribut yang mendefinisikan struktur.
JSON: Lebih ringan dalam hal ukuran data karena sintaksis yang lebih sederhana dan tidak ada atribut tambahan.
HTML: Ukuran data bergantung pada kompleksitas halaman web, tetapi struktur dasarnya mirip dengan XML.
## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Ringan dan Efisien: JSON memiliki sintaksis yang ringan dan sederhana, yang membuatnya menjadi format yang efisien untuk mentransfer data melalui jaringan. Data dalam JSON direpresentasikan dalam pasangan nama-kunci (key-value pairs), yang membuatnya lebih ringan daripada format yang menggunakan sintaksis yang lebih rumit seperti XML.

Bawaan dalam JavaScript: JSON merupakan format data yang bawaan dalam JavaScript, sehingga memudahkan penggunaannya dalam lingkungan web. Ini berarti data JSON dapat dengan mudah diurai dan dibentuk menggunakan objek JavaScript, yang sangat berguna dalam pengembangan web karena sebagian besar tumpuan web dibangun menggunakan JavaScript.

Mudah dibaca oleh Manusia: JSON menggunakan sintaksis yang mudah dibaca oleh manusia, sehingga memudahkan pengembang dan pengguna dalam memahami struktur data. Ini juga membuat debugging lebih mudah karena struktur data dapat dengan cepat dilihat dan dimengerti.

Bahasa-Agnostik: JSON tidak terbatas pada satu bahasa pemrograman tertentu. Ini berarti Anda dapat menggunakan JSON untuk pertukaran data antara aplikasi yang ditulis dalam bahasa pemrograman yang berbeda. JSON juga memiliki dukungan yang baik dalam sebagian besar bahasa pemrograman, termasuk Python, Java, PHP, dan banyak lainnya.

Dukungan untuk Struktur Data yang Fleksibel: JSON mendukung berbagai struktur data, termasuk objek (objects), array, dan tipe data primitif seperti string, angka, dan boolean. Ini memungkinkan Anda untuk menggambarkan data yang kompleks dan terstruktur dengan mudah.

Pencocokan dengan Model Objek dalam Aplikasi Web: JSON dapat dengan mudah diubah menjadi objek dalam aplikasi web modern, yang memudahkan penggunaan data dalam kode aplikasi. Ini memungkinkan pengembang untuk secara efisien menyimpan, mengambil, dan memproses data yang diterima dari server.

Dukungan untuk API Web: JSON sangat cocok untuk digunakan dalam API web karena kesederhanaan dan dukungannya dalam lingkungan web. Banyak layanan web dan platform, termasuk RESTful API, menggunakan JSON sebagai format data standar untuk berkomunikasi dengan aplikasi klien.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**Membuat input form untuk menambahkan objek model pada app sebelumnya.**
membuat html baru "create_item" dan menambahkan href di main.html serta menambahkan button agar dapat digunakan dan bisa menambahkan item

**Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.**
membuat fungsi untuk kelima format tsb dan menambahkan return sesuai format

**Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**
pada main.urls membuat path yang baru untuk setiap format

**HTML**
![image](https://github.com/Samuelwidjaja/sawi/assets/119392779/40bed75f-a6d7-4665-b4fc-dc7f2a9c2cc1)

**XML**
![image](https://github.com/Samuelwidjaja/sawi/assets/119392779/fe94313a-2ab7-4097-8f86-3a65734038d8)

**JSON**
![image](https://github.com/Samuelwidjaja/sawi/assets/119392779/e20ef149-127e-424b-bb4a-023c82fe1e3f)

**XML by ID**
![image](https://github.com/Samuelwidjaja/sawi/assets/119392779/698b7ee7-59e7-44f6-b0bc-a042fc02e7ca)

**JSON by ID**
![image](https://github.com/Samuelwidjaja/sawi/assets/119392779/9ca1d797-9e73-4073-8fe0-1ab3b4446fed)

## Tugas 4
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah sebuah formulir bawaan (built-in form) yang disediakan oleh Django untuk membantu dalam proses pendaftaran pengguna (user registration) dalam aplikasi web. Formulir ini digunakan untuk membuat pengguna baru dengan mengumpulkan informasi seperti username, password, dan konfirmasi password. Kelebihan dari UserCreationForm adalah bahwa ia memudahkan pengembang untuk mengimplementasikan fitur pendaftaran pengguna dengan cepat dan aman, karena ia secara otomatis melakukan validasi dan enkripsi password. Kelemahan utamanya adalah formulir ini memiliki tampilan standar, sehingga perlu disesuaikan secara ekstensif jika Anda menginginkan tampilan yang berbeda.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
**Autentikasi (Authentication):** Autentikasi adalah proses verifikasi identitas pengguna. Dalam konteks Django, ini mencakup verifikasi apakah pengguna adalah pengguna yang sah dengan memeriksa kombinasi username dan password mereka atau metode otentikasi lainnya seperti OAuth atau token.
**Otorisasi (Authorization):** Otorisasi adalah proses pengendalian akses terhadap sumber daya (seperti halaman web atau data) yang dilakukan setelah autentikasi. Ini memutuskan apa yang diizinkan atau tidak diizinkan oleh pengguna yang sudah diotentikasi. Django memiliki sistem otorisasi yang kuat yang memungkinkan Anda mengendalikan hak akses pengguna ke berbagai bagian dari aplikasi Anda berdasarkan izin.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah data kecil yang disimpan di sisi klien (browser) saat pengguna berinteraksi dengan aplikasi web. Django menggunakan cookies untuk mengelola data sesi pengguna dengan cara yang aman. Saat seorang pengguna masuk ke dalam sesi, Django menyimpan informasi sesi seperti ID pengguna atau preferensi di cookie yang dikirim ke browser pengguna. Data sesi ini dapat digunakan untuk menjaga status masuk pengguna atau menyimpan preferensi pengguna antar permintaan.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web dapat dianggap aman jika dilakukan dengan benar. Namun, ada beberapa risiko potensial yang harus diwaspadai, termasuk:
**Cross-Site Scripting (XSS):** Serangan XSS dapat memanipulasi cookies jika tidak ada langkah-langkah keamanan yang memadai untuk menghindarinya.
**Session Hijacking:** Jika cookie sesi dicuri oleh pihak yang tidak berwenang, penggunaan sesi pengguna dapat disalahgunakan.
**Data Privacy:** Cookies dapat digunakan untuk melacak perilaku pengguna, yang dapat menimbulkan masalah privasi jika tidak diatur dengan benar.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**
Mengimplementasikan fungsi-fungsi dengan cara membuat registrasi.html dan login.html. Kemudian menambahkan button login, logout agar pengguna dapat mengakses aplikasi dengan lancar

**Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**
Pada web yang sudah dibuat registrasi 2 akun pengguna, dan pada akun tsb membuat 3 item sebgaai dummy data

**Menghubungkan model Item dengan User.**
Tahap awal mengimpor
from django.contrib.auth.models import User

Pada model Item yang sudah dibuat, tambahkan potongan kode berikut:
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

kode diatas berfungsi untuk menghubungkan satu produk dengan satu user melalui sebuah relationship, dimana sebuah produk pasti terasosiasikan dengan seorang user. Lebih lanjutnya terkait ForeignKey akan dipelajari pada mata kuliah Basis Data. Penjelasan lebih lanjut terkait ForeignKey pada Django dapat dilihat di sini.

kemudian pada views menambahkan kode pada fungsi create_item
def create_item(request):
 form = ItemForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
Parameter commit=False yang digunakan pada potongan kode diatas berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. Hal tersebut memungkinkan kita untuk memodifikasi terlebih dahulu objek tersebut sebelum disimpan ke database. Pada kasus ini, kita akan mengisi field user dengan objek User dari return value request.user yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.

Lalu ubah fungsi show_main menjadi sebagai berikut.

def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,

Potongan kode diatas berfungsi untuk menampilkan objek Product yang terasosiasikan dengan pengguna yang sedang login. Hal tersebut dilakukan dengan menyaring seluruh objek dengan hanya mengambil Product yang dimana field user terisi dengan objek User yang sama dengan pengguna yang sedang login.
Kode request.user.username berfungsi untuk menampilkan username pengguna yang login pada halaman main.

**Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**
Pada awalnya mengimpor 
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

kemudian menambahkan potongan kode pada fungsi login user
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
untuk context menambahkan
'last_login': request.COOKIES['last_login'],
pada fungsi logout juga ditambahkan
 response.delete_cookie('last_login')
 dan yang terakhir untuk menampilkan last login
 <h5>Sesi terakhir login: {{ last_login }}</h5>

 ## Tugas 5
**Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**
**Manfaat**: Element selector digunakan untuk memilih elemen HTML secara langsung berdasarkan nama elemennya (misalnya, h1, p, div). Ini adalah selektor paling umum dan paling sederhana dalam CSS. Manfaatnya adalah untuk memberikan gaya pada semua elemen yang memiliki nama yang sama tanpa perlu menambahkan kelas atau ID ke setiap elemen.
**Kapan Menggunakan**: Element selector cocok digunakan ketika Anda ingin memberikan gaya yang serupa kepada banyak elemen dengan nama yang sama. Misalnya, jika Anda ingin mengubah semua teks dalam elemen p menjadi warna merah.

**Jelaskan HTML5 Tag yang kamu ketahui.**
Beberapa tag HTML5 yang umumnya digunakan antara lain:
<header>: Untuk bagian atas halaman web yang biasanya berisi judul atau navigasi.
<nav>: Untuk mengelompokkan elemen navigasi.
<section>: Untuk mengelompokkan konten yang memiliki tema atau topik yang sama.
<article>: Untuk konten mandiri yang dapat berdiri sendiri, seperti posting blog atau artikel berita.
<aside>: Untuk konten tambahan yang terkait dengan konten utama, seperti sidebar.
<footer>: Untuk bagian bawah halaman yang biasanya berisi informasi kontak atau hak cipta.

**Jelaskan perbedaan antara margin dan padding.**
**Margin**: Margin adalah ruang di luar batas elemen. Margin digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya. Margin tidak memiliki latar belakang atau warna, hanya mengatur ruang.
**Padding**: Padding adalah ruang di dalam batas elemen. Padding digunakan untuk mengatur jarak antara isi elemen dan batasnya. Padding bisa memiliki latar belakang dan warna yang akan mempengaruhi elemen dan area di sekitarnya.

**Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**
**Bootstrap:**
Framework CSS yang komprehensif dengan komponen UI yang telah dibuat sebelumnya.
Memiliki desain bawaan yang telah ditentukan.
Membutuhkan lebih banyak kelas HTML untuk mengubah tampilan.
Cocok digunakan ketika Anda ingin cepat mengembangkan situs dengan komponen yang telah ada dan gaya desain yang sudah ditentukan.

**Tailwind CSS:**
Framework CSS yang ringan dengan pendekatan utility-first.
Tidak memiliki desain bawaan, Anda harus mendefinisikan gaya Anda sendiri menggunakan kelas.
Memungkinkan fleksibilitas yang tinggi dalam mengatur tampilan.
Cocok digunakan ketika Anda ingin mengendalikan setiap aspek tampilan dengan mudah dan tidak ingin bergantung pada desain yang sudah ada.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
**Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.**
Untuk setiap HTML saya mengkustomisasi satu-satu menggunakan CSS

**Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.**
Membuat class cards baru pada CSS dan di loop untuk setiap item yang ditambahkan

**Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS.**
pada looping item menambahkan        
<div class="card {% if forloop.last %}new-card{% endif %}">
agar untuk setiap loop yang terakhir ditambahkan warna pada background untuk membedakannya

## Tugas 6

**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
**Synchronous Programming (Program Sinkron):**
Pada synchronous programming, tugas-tugas dieksekusi secara berurutan, satu per satu. Artinya, ketika suatu operasi dimulai, program akan menunggu hingga operasi tersebut selesai sebelum melanjutkan ke operasi berikutnya.
Ini seringkali sederhana dan mudah dipahami, tetapi dapat mengakibatkan program menjadi lambat jika ada operasi yang memakan waktu lama. Selama operasi yang memakan waktu lama sedang berlangsung, program akan "terkunci" dan tidak dapat melakukan tugas lain.
Ini adalah model standar dalam pemrograman konvensional, terutama di lingkungan pemrograman seperti bahasa Python, Java, dan C++.

**Asynchronous Programming (Program Asinkron):**
Pada asynchronous programming, tugas-tugas yang memakan waktu lama dapat dijalankan secara paralel atau di latar belakang tanpa menghentikan eksekusi program utama. Program tidak harus menunggu operasi selesai untuk melanjutkan ke tugas berikutnya.
Ini berguna untuk mengatasi operasi yang memerlukan waktu lama, seperti mengunduh data dari internet, membaca atau menulis file, atau berinteraksi dengan perangkat keras.
Asynchronous programming biasanya digunakan dalam lingkungan di mana responsivitas dan efisiensi sangat penting, seperti aplikasi web, jaringan, dan GUI (antarmuka grafis).

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

**Jelaskan penerapan asynchronous programming pada AJAX.**
Pemrograman asinkron pada AJAX adalah cara untuk membuat permintaan HTTP dan memproses respons tanpa menghentikan eksekusi utama aplikasi web. Ini memberikan responsivitas dan efisiensi pada aplikasi. Pemrograman asinkron melibatkan fungsi panggilan balik, Promises, dan async/await dalam JavaScript. Ini meningkatkan pengalaman pengguna dengan menghindari pembekuan halaman dan mengoptimalkan penggunaan sumber daya.

**Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.**

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**










