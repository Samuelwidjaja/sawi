# **Link website: **
https://tradcard.adaptable.app/

## Cara saya mengimplementasikan _checklist - checklist_ di ketentuan tugas: 
Cara saya mengimplementasikan checklist adalah dengan mengikuti ulang tutorial 0 dan 1 pada web PBP Ganjil. Kemudian saya ubah dikit agar sisa checklist pada tugas juga dapat di checklist.

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
